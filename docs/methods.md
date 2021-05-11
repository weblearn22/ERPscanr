---
layout: default
---

# Methods

In order to collect the literature data, search terms for ERP components and associated terms were curated, and then used to identify relevant papers in the literature, and collect information from ERP-related papers in the literature and about how terms of interest co-occur in the literature.

The main methods for this project are briefly summarized in the following graphic:

![methods]({{ site.baseurl }}/assets/FIGS/methods.png)

Code for this project is written in Python, and primarily uses the
[LISC](https://github.com/lisc-tools/lisc) module for data collection and analysis.
All the code to run this project is openly available in the
[project repository](https://github.com/ERPscanr/ERPscanr).

## Literature Search & Collection

To collect information on ERP-related papers, lists of search terms were manually curated. These lists include ERP terms, as well as potential associations, including cognitive and disease terms.

In order to ensure the searches found papers reporting on ERPs, rather than potential homophones, each search was manually checked and ERP-specific exclusion words were curated to tune the search results. These exclusion terms restrict search results to the relevant literature, (for example, for some components, we use an exclusion word of 'protein' to avoid papers examining proteins that happen to have the same label as an ERP component).

Using these terms, the PubMed E-Utilities were used to search for term co-occurrences and to return data on relevant articles. Specifically, E-Search was used to identify IDs for relevant papers, and to extract the number of relevant papers, and E-Fetch was used to retrieve data regarding these articles.

Data collection was done in two ways: in the co-occurrence analysis we collected data on the number of articles returned by a combination of search terms (for example, counting the number of IDs returned by the search for "N400 AND language"). For the "words" collection, search terms were used to collect available meta-data for all articles mentioning a particular ERP, including title, journal, author, publication date, keywords, and abstract text.

## Data-Driven Profiles

For each ERP, we create a data-driven profile, based on the collected text, using simple text analyses to find the most common words that are used to describe each component, as well as some historical context regarding when, where, and by whom this component has been investigated in the literature.

## Group Analysis

We also examined similarities between different ERP components, computing similarity and clustering metrics on both the collected data.

## Limitations

Note that this project is explicitly a summary of the literature, and will share any limitations of the underlying literature. Limitations of this kind of literature analysis includes that papers are identified by terms of interest, which can include primary research and review articles, and no weighting is done for sample size, experiment design, or research quality. We also note that this analysis only reflects a subset of the literature, in particular papers that reference terms of interest in their titles and/or abstracts.

In the co-occurence analyses, we note that the while co-occurence can be useful to identify which topics are discussed together (or at least nearby), this approach does not reflect if or how such terms actually associated. In the text analyses, we only access limited information including only words which occur in the title, keywords and abstract, as well as certain meta-data such as journal, authors, and publication date. The current collection and analysis does not include full-text analysis, and so is only getting a limited insight into the collected papers.

Due to these limitations, this project should perhaps best be thought of as a high-level summary of the literature, rather than a detailed summary of the topics under question. This analysis will share the biases of the literature, including being susceptible to trends and popularity in research, as well as publication bias. While this kind of "birds eye view" may be useful to identify general patterns in the literature, we note that detailed conclusions should be further explored for verification.
