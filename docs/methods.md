---
layout: default
---

# Methods

The main methods for this project are briefly summarized in the following graphic: search terms for ERP components and associated terms were collected, after which we collected information on how these words co-occur in the literature, as well as collecting meta-data from all identified ERP-related papers.

![methods]({{ site.baseurl }}/assets/FIGS/methods.png)

Code for this project is written in Python, and primarily uses the [LISC](https://github.com/lisc-tools/lisc) module for data collection and analysis. All the code to run this project is openly availabe in the [project repository](https://github.com/ERPscanr/ERPscanr).

## Literature Search & Collection

To collect information on ERP-related paper, lists of search terms were manually curated. These lists include ERP terms, as well as potential associations, including cognitive and disease terms.

In order to ensure the searches found papers reporting on ERPs, rather than potential homophones, each search was manually checked and ERP-specific exclusion words were curated to tune the search results. These exclusion terms restrict search results to the relevant literature, (for example, for some components, we use an exclusion word of 'protein' to avoid papers examining protein).

Using these terms, PubMed E-Utilities tools were used to find search for term co-occurrences and to return data on relevant articles. In particles, E-Search was used to identify IDs for relevant papers, and to extract the number of relevant papers, and E-Fetch was used to retrieve data regarding these articles.

Specifically, data scraping was done in two ways: in the co-occurrence analysis we collected data on the number of articles returned by a combination of search terms (for example, counting the number of IDs returned by the search for "N400 AND language"). In addition, in the scraped-text analysis, we scraped available meta-data for all articles mentioning a particular ERP, including title, journal, author, publication date, keywords, and abstract text.

## Data-Driven Profiles

For each ERP, we create a data-driven profile, based on the scraped text, using rudimentary text analysis to find the most common words that are used to descripe each component, as well as some historical context regarding when, where and by whom this component is published on.

## Group Analysis

We also examined similarities between different ERP components, computing similarity and clustering metrics on both the counts and words data.

## Limitations


Note that this project is explicitly a summary of the literature, and will share any limitations of the underlying literature, for example, publication bias. Literature analysis has limitations, including that papers are identified by terms of interest, which can include primary research and review articles, and no weighting is done for sample size, experiment design, or research quality.


- This project should best be thought of as a summary of the literature, rather than a direct summary of the topics under question. This analysis will share the biases of the literature, including being susceptible to trends and popularity in research, as well as publication bias.
- Much of this analysis is based on word co-occurrence, which does not necessarily imply these terms are actually associated, merely that the words sometimes occur near each other.
- All studies and publication types listed on PubMed are included in this analysis, and each is given equal weight. There is no weighting for quality or sample size, as would typically be done in a systematic review.
- Only limited portions of included articles actually get included in this analysis, in particular, only words which occur in the title, keywords and abstract, as well as certain meta-data such as journal, authors, and publication date. The current data does not include full-text analysis.
- We can not guarantee we are finding all relevant literature, notably we may miss papers using unknown (to us) synonyms for ERP terms, and/or older papers describing components before the current naming conventions were set.
