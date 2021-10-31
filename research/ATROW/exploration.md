# Possibilities

## Requirement

 We need a tool that can provide reports on :

 1. Space economy
 2. Performance Issues visible
 3. UX experience of a particular issue
 4. Security level checks
 5. Competitive leaks

### From the facts we've gathered what are actual possibilities currently?

Implementable items:

1. Space economy analysis, based on component boundary analysis on different viewports using Selenium and Python
2. Performance analysis based on 'tracert' or 'ping' analysis of packet propagation, for CDNs and page delivery networks
3. Security level checks for CSRF, Certificate Authority checks, SQL Injection testing, Path traversal testing, DDoS testing
4. Scraping checks by making use of various bot prevention and detection methods.
5. SEO ranking

There are certain aspects that require continuous analysis, such as :

1. Normal traffic analysis
2. Eavesdropping and packet modifications detection, through network performance analysis
3. DB infiltration detection, through normalized privileged access analysis

These cannot be made a part of a one-time report.

### What are expected to be possible, but unclear, on implementations?

1. Regression learning for automated A/B test predictions(UI/UX acceptance is a classification problem)
2. Active Bot traffic rejection(this is usually cost effective in an extremely high request-per-second scenario)
3. Identifying data seepage through periodic analysis of embedded tools, such as Twitter Analytics, Google Analytics, Facebook Analytics, Hotjar, etc.

## Difficulty of implementations of implementable items

### Easy

1. Performance analysis based on 'tracert' or 'ping' analysis of packet propagation, for CDNs and page delivery networks
2. Security level checks for CSRF, Certificate Authority checks, SQL Injection testing, Path traversal testing, DDoS testing
3. SEO ranking(Google, Bing, Yahoo and Baidu account for 95% of the Search engines market)

The stated points are purely technological, with known methods and complexities.

Packet route tracing and Security level checks is a problem of P type complexity, i.e. they have optimized algorithmic approaches of finding them.
Whereas SEO ranking is a NP problem, i.e. can be solved in polynomial time, but it is not constant, due to the changing nature of the Search Engine Algorithms.

### Moderate

Scraping checks by making use of various bot prevention and detection methods.

This is an NP-complete type of problem, i.e. this requires brute forcing for automating if a page can be scraped.

### Hard

Space economy analysis.

This deals with rendering the page for viewports under analysis, and analyzing the computed dimensions, for evaluating a space economy, algorithmically. This is a NP-complete problem, but not NP-hard. It can be brute forced, but it isn't unsolvable.
