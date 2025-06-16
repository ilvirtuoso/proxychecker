<div class="lg:col-span-8 space-y-6"><div class="bg-white rounded-lg shadow-sm p-4"><div dir="ltr" data-orientation="horizontal" class="mt-4"><div role="tablist" aria-orientation="horizontal" class="h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground grid w-full grid-cols-2" tabindex="0" data-orientation="horizontal" style="outline: none;"><button type="button" role="tab" aria-selected="true" aria-controls="radix-:r15:-content-preview" data-state="active" id="radix-:r15:-trigger-preview" class="inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">Preview</button><button type="button" role="tab" aria-selected="false" aria-controls="radix-:r15:-content-edit" data-state="inactive" id="radix-:r15:-trigger-edit" class="inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">Edit</button></div><div data-state="active" data-orientation="horizontal" role="tabpanel" aria-labelledby="radix-:r15:-trigger-preview" id="radix-:r15:-content-preview" tabindex="0" class="mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2" style=""><div class="border border-border rounded-lg bg-background p-6 shadow-sm"><div class="prose prose-sm md:prose-base lg:prose-lg max-w-none prose-headings:font-bold prose-a:text-blue-600" style="user-select: none;"><div id="top" class="">

<div align="center" class="text-center">
<h1>PROXYCHECKER</h1>
<p><em>Empower Your Network with Instant Proxy Validation</em></p>

<img alt="last-commit" src="https://img.shields.io/github/last-commit/ilvirtuoso/proxychecker?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/ilvirtuoso/proxychecker?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/ilvirtuoso/proxychecker?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Built with the tools and technologies:</em></p>
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&amp;logo=Python&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
</div>
<br>
<hr>
<h2>Table of Contents</h2>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#overview">Overview</a></li>
<li class="my-0"><a href="#getting-started">Getting Started</a>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#prerequisites">Prerequisites</a></li>
<li class="my-0"><a href="#installation">Installation</a></li>
<li class="my-0"><a href="#usage">Usage</a></li>
<li class="my-0"><a href="#testing">Testing</a></li>
</ul>
</li>
</ul>
<hr>
<h2>Overview</h2>
<p>proxychecker is a high-performance tool designed to efficiently validate and monitor proxy servers through asynchronous testing. It leverages multi-threaded processing to quickly identify live proxies, measure response times, and provide real-time progress updates.</p>
<p><strong>Why proxychecker?</strong></p>
<p>This project aims to streamline proxy validation and management. The core features include:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><strong>🧵🧵</strong> <strong>Multi-threaded Validation:</strong> Accelerates proxy testing by processing multiple proxies concurrently.</li>
<li class="my-0"><strong>⚡️⚡️</strong> <strong>Asynchronous Operations:</strong> Ensures non-blocking, fast execution even with large proxy lists.</li>
<li class="my-0"><strong>🔄🔄</strong> <strong>Real-time Progress Updates:</strong> Keeps you informed during lengthy validation processes.</li>
<li class="my-0"><strong>📊📊</strong> <strong>Latency Recording:</strong> Measures and logs response times for optimal proxy selection.</li>
<li class="my-0"><strong>📝📝</strong> <strong>Up-to-date Proxy List:</strong> Maintains a current, reliable set of functional proxies for your applications.</li>
</ul>
<hr>
<h2>Getting Started</h2>
<h3>Prerequisites</h3>
<p>This project requires the following dependencies:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><strong>Programming Language:</strong> Python</li>
<li class="my-0"><strong>Package Manager:</strong> Conda</li>
</ul>
<h3>Installation</h3>
<p>Build proxychecker from the source and install dependencies:</p>
<ol>
<li class="my-0">
<p><strong>Clone the repository:</strong></p>
<pre><code class="language-sh">❯ git clone https://github.com/ilvirtuoso/proxychecker
</code></pre>
</li>
<li class="my-0">
<p><strong>Navigate to the project directory:</strong></p>
<pre><code class="language-sh">❯ cd proxychecker
</code></pre>
</li>
<li class="my-0">
<p><strong>Install the dependencies:</strong></p>
</li>
</ol>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">❯ conda env create -f conda.yml
</code></pre>
<h3>Usage</h3>
<p>Run the project with:</p>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">conda activate {venv}
python {entrypoint}
</code></pre>
<h3>Testing</h3>
<p>Proxychecker uses the {<strong>test_framework</strong>} test framework. Run the test suite with:</p>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">conda activate {venv}
pytest
</code></pre>
<hr>
<div align="left" class=""><a href="#top">⬆ Return</a></div>
<hr></div></div></div></div><div data-state="inactive" data-orientation="horizontal" role="tabpanel" aria-labelledby="radix-:r15:-trigger-edit" hidden="" id="radix-:r15:-content-edit" tabindex="0" class="mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"></div></div></div></div>
