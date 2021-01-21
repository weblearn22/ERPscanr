---
layout: default
---

# Methods

The codebase to run collect this data and analyze the results was all written in Python, including calls the PubMed E-Utilities API. All code written and used for this project will be made freely available (coming soon).

![methods]({{ site.baseurl }}/assets/FIGS/methods.png)

## Literature Searchs & Web Scraping

Dictionaries of terms were manually compiled to serve as serve terms on PubMed. These include separate dictionaries for ERP terms, cognitive terms, and disease terms. In addition, we collected a dictionary of exclusion words, per ERP, that were also manually curated to restrict search results to the relevant literature, and exclude homophones (for example, for P50, we use an exclusion word of 'protein' to avoid papers examining the P50 protein).

Using these terms, PubMed E-Utilities tools were used to find search for term co-occurrences and to return data on relevant articles. In particles, E-Search was used to identify IDs for relevant papers, and to extract the number of relevant papers, and E-Fetch was used to retrieve data regarding these articles.

Specifically, data scraping was done in two ways: in the co-occurrence analysis we collected data on the number of articles returned by a combination of search terms (for example, counting the number of IDs returned by the search for "N400 AND language"). In addition, in the scraped-text analysis, we scraped available meta-data for all articles mentioning a particular ERP, including title, journal, author, publication date, keywords, and abstract text.

## Data-Driven Profiles

For each ERP, we create a data-driven, based on the scraped text, using rudimentary text analysis to find the most common words that are used to descripe each component, as well as some historical context regarding when, where and by whom this component is published on.

## Group Analysis

We also examined similarities between different ERP components, computing similarity and clustering metrics on both the counts and words data.

## Limitations

- This project should best be thought of as a summary of the literature, rather than a direct summary of the topics under question. This analysis will share the biases of the literature, including being susceptible to trends and popularity in research, as well as publication bias.
- Much of this analysis is based on word co-occurrence, which does not necessarily imply these terms are actually associated, merely that the words sometimes occur near each other.
- All studies and publication types listed on PubMed are included in this analysis, and each is given equal weight. There is no weighting for quality or sample size, as would typically be done in a systematic review.
- Only limited portions of included articles actually get included in this analysis, in particular, only words which occur in the title, keywords and abstract, as well as certain meta-data such as journal, authors, and publication date. The current data does not include full-text analysis.
- We can not guarantee we are finding all relevant literature, notably we may miss papers using unknown (to us) synonyms for ERP terms, and/or older papers describing components before the current naming conventions were set.
