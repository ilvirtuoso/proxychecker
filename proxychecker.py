import asyncio
import httpx
import time
import multiprocessing
from math import ceil
from collections import deque

# Config
TEST_URL = 'http://icanhazip.com'  
TIMEOUT = 2.0 
MAX_CONCURRENT = 2000  
BATCH_SIZE = 500  
WORKER_COUNT = 300  # threads

# Shared progress counter
processed = 0
total_proxies = 0
print_lock = asyncio.Lock()

async def check_proxy(proxy):
    global processed
    proxy_url = f"http://{proxy}"
    
    try:
        async with httpx.AsyncClient(
            proxy=proxy_url,
            timeout=httpx.Timeout(TIMEOUT),
            transport=httpx.AsyncHTTPTransport(retries=0)
        ) as client:
            
            start = time.monotonic()
            resp = await client.get(TEST_URL, headers={'Connection': 'close'})
            latency = int((time.monotonic() - start) * 1000)
            
            if resp.status_code == 200:
                async with print_lock:
                    processed += 1
                    return proxy, latency
    except Exception:
        pass
    
    async with print_lock:
        processed += 1
    return None

async def worker(proxy_queue, results):
    while True:
        try:
            proxy = proxy_queue.popleft()
        except IndexError:
            return
        result = await check_proxy(proxy)
        if result:
            results.append(result)

async def main():
    global total_proxies
    
    # Proxy listesini yükle
    with open('proxies.txt', 'r') as f:
        proxy_list = deque(line.strip() for line in f if line.strip())
    
    total_proxies = len(proxy_list)
    print(f"⚡ started proxychecker")
    print(f"🔍 allof {total_proxies} proxy | {MAX_CONCURRENT} request live")
    
    start_time = time.monotonic()
    results = []
    workers = []
    
    # Worker'ları başlat
    for _ in range(WORKER_COUNT):
        workers.append(asyncio.create_task(worker(proxy_list, results)))
    
    # Progress bar
    while processed < total_proxies:
        percent = ceil((processed / total_proxies) * 100)
        print(f"\r🚀 ok: {percent}% | {processed}/{total_proxies}", end="", flush=True)
        await asyncio.sleep(0.1)
    
    await asyncio.gather(*workers)
    
    # Sonuçlar
    duration = time.monotonic() - start_time
    print(f"\n\n✅ {len(results)} found proxy live")
    print(f"⏱️ time: {duration:.2f}s | Proxy/s: {total_proxies/duration:.1f}")
    
    with open('working_proxies.txt', 'w') as f:
        for proxy, latency in results:
            f.write(f"{proxy} | {latency}ms\n")

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # Windows optimizasyonu
    asyncio.run(main())
