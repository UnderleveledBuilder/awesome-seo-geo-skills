### What is GEO, and how is it different from SEO?

SEO (search engine optimization) gets your pages ranked by search engines such as Google and Bing. GEO (generative engine optimization, also called AEO) gets you mentioned and cited in AI answers from ChatGPT, Perplexity, Google AI Overviews and others. They overlap: AI search usually starts from search engine results, so good SEO is the base of GEO. But AI answers care more about passages they can quote directly, clear sources, and how often other sites mention you. GEO-focused projects are under [GEO: get cited in AI answers](#group-geo) ({{group:geo}}).

### What are the best agent skills for SEO?

This list has {{count}} hand-checked SEO and GEO skill projects (data updated {{updated}}). For one system that covers most of the work, start with [All-in-one](#group-pipeline) ({{group:pipeline}}); the most-starred are {{top:group:pipeline}}. For a single step, go to the keywords and ranking data, content, technical audit or backlinks sections.

### Do these skills need paid SEO data?

It depends. Skills that rely only on the model and page fetching don't. Those that look up search volume, backlinks or rankings usually need Search Console (free) or a paid API such as Ahrefs, Semrush or DataForSEO; each entry says what it needs.

### What about Chinese AI assistants and Baidu?

Projects built for them are under [Chinese AI search](#group-cn-ai) ({{group:cn-ai}}); some in other sections also cover Doubao or Kimi, and {{facet:engines:doubao}} in total explicitly target Doubao. Chinese assistants crawl differently from English AI search: GitHub's robots.txt blocks ByteDance's crawler (Bytespider), for example, so Doubao can hardly read GitHub pages directly and relies on off-site content such as WeChat articles, Zhihu and Toutiao. See [By search engine and AI platform](#by-engines).

### Are these projects safe to install?

Every repo was checked by hand (README, folders and files) and scanned by a script for binaries and archives, install hooks, remote code execution and reads of sensitive files. {{count}} skill projects and {{platforms}} tools made the list. Repos that were reviewed and turned down are recorded with the reason in [data/ignore.toml](data/ignore.toml) (in Chinese; {{ignored}} so far). A clean scan does not prove a skill is safe, so read its `SKILL.md` and scripts before installing.

### How often is the list updated?

Every Monday, stars, last-updated dates and licenses refresh automatically and new repos are searched; new repos are added only after a manual check. See [New this week](#new).
