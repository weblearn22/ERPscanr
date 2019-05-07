# ERP_SCANR

An automated meta-analysis of the ERP literature.

### Overview

This repository is for the Event-Related Potential (ERP) Scanner project, and a text-mining project aiming to use automated web scraping and text analysis of published research articles to summarize current findings, and generate novel hypotheses about ERP research. This project is now hosted on a website, [here](http://tomdonoghue.github.io/ERP_SCANR/).

### Requirements

If you want to run the code in this repository, you will need Python 3, with the scipy-stack, which are easiest to collect together using the [Anaconda Distribution](https://www.anaconda.com/distribution/). To make the WordCloud plots, you will need [wordcloud](https://pypi.org/project/wordcloud/).

If you are looking to run your own literature scrapes, use [LISC](https://github.com/lisc-tools/lisc), as briefly described below.

### Automated Literature Analysis

This project is heavily inspired by the [BrainSCANR](http://www.sciencedirect.com/science/article/pii/S0165027012001513) project by Voytek & Voytek, an automated analysis of the neuroscientific literature.

If you are interested in performing automated literature analyses, we provide an open-source tool to do so [here](https://github.com/lisc-tools/lisc). This package, 'LISC', for 'Literature Scanner' is basically a generalized version of the code used for this project, and as such is an extended and re-implemented version of the original BrainSCANR project.

### Project Details

To goal of this project is to map and annotate the existing literature related to the method of event-related potentials (ERPs). In order to do so, we first manually curated a dictionary of all known ERP components that we could find. This list of ERP components is available in erpsc/terms/ or viewable at /notebooks/Intro.ipynb.

In terms of data collection, this project employs main approaches to mining information:
- 'Count': a co-occurence analysis of ERP terms and other pre-defined terms of interest (cognitive and/or disease terms)
- 'Words': an analysis of all words that appear in the abstract of ERP related papers. From this web-scrape, we also gather and analysis meta-data, such as authors, journals, keywords and date of publication to build profiles of ERPs.

From there, we analyze patterns in the literature and make inferences about ERPs and how they relate based on analyzing this co-occurence data, by analyzing this co-occuring and text data.

The full results, including individual profiles for all examined ERP components, and group level analysis, are available [here](http://tomdonoghue.github.io/ERP_SCANR/).
