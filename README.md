# ERP_SCANR

### Overview

This repository is for the Event-Related Potential (ERP) Scanner project, and a text-mining project aiming to use automated web scraping and text analysis of published research articles to summarize current findings, and generate novel hypotheses about ERP research. This project is now hosted on a website, [here](http://tomdonoghue.github.io/ERP_SCANR/).

### Automated Literature Analysis

This project is heavily inspired by the [BRAIN SCANR](http://www.sciencedirect.com/science/article/pii/S0165027012001513) project by Voytek & Voytek, an automated analysis of the neuroscientific literature. 

If you are interested in performing automated literature analyses, we provide an open-source tool to do so [here](https://github.com/TomDonoghue/lisc). This package, 'LISC', for 'Literature Scanner' is basically a generalized version of the code used for this project, and as such is an extended and re-implemented version of the original brain scanr project. 

### Project Details

In order to do this project, we manually curated a dictionary of all known ERP components that we could find. This list of ERP components is available in erpsc/terms/ or viewable at /notebooks/Intro.ipynb.

In terms of data collection, this project employs main approaches to mining information:
- 'Count': a co-occurence analysis of ERP terms and other pre-defined terms of interest (cognitive and/or disease terms)
- 'Words': an analysis of all words that appear in the abstract of ERP related papers. From this web-scrape, we also gather and analysis meta-data, such as authors, journals, keywords and date of publication to build profiles of ERPs.

The full results, including individual profiles for all examined ERP components, and group level analysis, are hosted [here](http://tomdonoghue.github.io/ERP_SCANR/).
