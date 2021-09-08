# ERPscanr

`ERPscanr` project repository: automated meta-analysis of the ERP literature.

[![Website](https://img.shields.io/badge/site-erpscanr.github.io-informational.svg)](http://erpscanr.github.io/)

## Overview

Event-related potentials (ERP) are a common signal of analysis in neuroscience experiments, with a large existing literature of ERP-related work. This project uses automated literature collection and text-mining of published research articles in order to help summarize the ERP literature, examining patterns and associations within and between ERP components.

This results of this project are hosted online on the [project website](http://erpscanr.github.io/).

## Project Guide

To goal of this project is explore and summarize the existing ERP-related literature. In order to do so, we first manually curated a dictionary of all known ERP components that we could find. This list of ERP components and labels is viewable in the `SearchTerms` notebook.

For data collection, this project employs main approaches for collecting literature data:
- The 'Words' approach collects text and metadata, such as authors, journals, keywords and date of publication, from all articles that are found based on the search terms. This data is primarily used to characterize and build profiles of ERP components.
- The 'Count' approach collects data on co-occurence of ERP terms and other pre-defined terms of interest, including cognitive and/or disorder-related association terms of interest. This data is primarily used to examine patterns and similarities across ERP components, based on their associated topics.

Overall, the goal is to analyze patterns in the literature and make inferences about ERPs, by analyzing the collected data.

The easiest way to examine the outputs of this project is on the
[project website](http://erpscanr.github.io/), which includes
individual profiles for all examined ERP components and group level analyses.

To explore how this project was done, and see the underlying code, you can explore this repository. As a starting point, the `notebooks` describe the approach used in this project. For doing literature analyses in general, see the
[LISC](https://github.com/lisc-tools/lisc) tool.

## Reference

This project is described in the following preprint:

    Donoghue T & Voytek B (2021). Automated meta-analysis of the event-related
    potential (ERP) literature. PsyArXiv. DOI: 10.31234/osf.io/7ezmh

Direct link: https://doi.org/10.31234/osf.io/7ezmh

## Requirements

This project was written in Python 3 and requires Python >= 3.7 to run.

This project requires standard scientific python libraries, listed in `requirements.txt`, which can be installed with
[Anaconda Distribution](https://www.anaconda.com/distribution/).

Additional requirements include:
- [lisc](https://github.com/lisc-tools/lisc) >= 0.2.0

## Repository Layout

This project repository is organized in the following way:

- `build_site/` contains scripts to create the project website
- `code`/ contains code written and used for this project
- `docs/` contains files that create and define the project website
- `notebooks/` contains a collection of Jupyter notebooks that step through the project
- `scripts/` contains stand alone scripts that run the data collection and analysis
- `terms/` contains all the search terms used for the literature collection

## Data

The project uses literature data, collected using code that is available in this repository.

Data files from the current collection are available on
[OSF](https://osf.io/g2ruj/).
