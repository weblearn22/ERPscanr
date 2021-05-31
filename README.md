# ERPscanr

`ERPscanr` project repository: automated meta-analysis of the ERP literature.

[![Website](https://img.shields.io/badge/site-erpscanr.github.io-informational.svg)](http://erpscanr.github.io/)

## Overview

Event-related potentials (ERP) are a common signal of analysis in neuroscientific experiments. This project aims to summarize the ERP literature, using automated literature collection and text-mining of published research articles to summarize current findings, and examine patterns in the ERP literature.

## Project Guide

To goal of this project is to map and annotate the existing literature related to the method of ERPs. In order to do so, we first manually curated a dictionary of all known ERP components that we could find. This list of ERP components is available viewable at /notebooks/Intro.ipynb.

For data collection, this project employs main approaches to mining information:
- 'Count': a co-occurence analysis of ERP terms and other pre-defined terms of interest (cognitive and/or disorder-related association terms)
- 'Words': an analysis of all words that appear in the abstract of ERP related papers. From this web-scrape, we also gather and analysis meta-data, such as authors, journals, keywords and date of publication to build profiles of ERPs.

From there, we analyze patterns in the literature and make inferences about ERPs and how they relate based on analyzing this co-occurence data, by analyzing this co-occuring and text data.

The easiest way to examine the outputs of this project is on the
[project website](http://erpscanr.github.io/), which includes
individual profiles for all examined ERP components and group level analyses.

To explore how this project was done, and see the underlying code, you can explore this repository. As a starting point, the `notebooks` describe the approach used in this project. For doing literature analyses in general, see the
[LISC](https://github.com/lisc-tools/lisc) tool.

## Reference

A preprint for this project is upcoming.

This results of this project are hosted project is now hosted online [here](http://erpscanr.github.io/).

## Requirements

This project was written in Python 3 and requires Python >= 3.7 to run.

This project requires standard scientific python libraries, listed in `requirements.txt`, which can be installed with
[Anaconda Distribution](https://www.anaconda.com/distribution/).

Additional requirements include:
- [lisc](https://github.com/lisc-tools/lisc) >= 0.2.0

## Repository Layout

This project repository is set up in the following way:

- `build_site/` contains scripts to create the project website
- `code`/ includes local code used for this project
- `docs/` includes files for the project website
- `notebooks/` is a collection of Jupyter notebooks that step through the project
- `scripts/` contains stand alone scripts that run the data collection and analysis

## Data

The project uses literature data, collected with code that is available in this repository. Due to size, the
collected data files are not hosted on this repository, but are available upon request.
