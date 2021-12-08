---
layout: default
---

# Introduction

ERPscanr is a semi-automated meta-analysis of scientific literature on the topic of event-related potentials (ERPs).

## Motivation

ERPs are a common method of investigation in neuroscience, with tens of thousands of existing articles using ERPs to investigate
both cognitive and clinical questions, with thousands more published each year.
The scale of this literature can make it difficult to keep up with the research, motivating the need for synthesis of the existing literature.

Systematic reviews offer one way to examine the literature, however, they require a significant time commitment,
and are often focused on specific topics. As a complement to systematic reviews, here we use literature analysis
to collect and analyze the ERP literature at scale, in a semi-automated way.
After manual curation of search terms of interest, automated processes are used to collect and analyze literature data.
In doing so, this project serves as a data-driven summarization tool - a way to quickly and efficiently get a summary of
ERP components that have been characterized in the literature, what they are used to investigate, and the relations between them.

## Methods & Data

ERPscanr uses the [LISC](https://lisc-tools.github.io/) Python tool to collect and analyze scientific literature. The data is collected from
[Pubmed](https://pubmed.ncbi.nlm.nih.gov/), a database of biomedical literature.
From there, we use text-mining and word co-occurrence analysis to derive data-driven summaries for each ERP,
as well as to compare across these profiles to summarize patterns across the literature.

The code for this project is openly available in the [project repository](https://github.com/ERPscanr/ERPscanr).
This includes the curated set of search terms for ERP components and potential associations, which is available in the
[terms](https://github.com/ERPscanr/ERPscanr/tree/main/terms) sub-folder.

The literature data collected and analyzed in this project is also openly available, in this
[OSF repository](https://osf.io/g2ruj/).

A more in-depth overview of the methods is available on the [methods page](methods.html).

## Version

The current collection and analysis is v0.2:

    - database: Pubmed
	- collected on: 14th June, 2021
	- db-build: Build210612-2212m.2
	- db-lastupdate: 2021/06/13 07:12

Note that this project may update periodically, including updates to the terms lists, collected dataset, and analyses presented.
Any major updates to the project are logged on the
[releases](https://github.com/ERPscanr/ERPscanr/releases) page.

## Reference

This project is described in the following preprint:

    Donoghue T & Voytek B (2021). Automated meta-analysis of the event-related
    potential (ERP) literature. PsyArXiv. DOI: 10.31234/osf.io/7ezmh

Direct link: [https://doi.org/10.31234/osf.io/7ezmh](https://doi.org/10.31234/osf.io/7ezmh)

## Contact

The ERPscanr project was led and is maintained by
[Tom Donoghue](https://tomdonoghue.github.io/),
and was done in the
[Voytek lab](https://voyteklab.com/).

You can get in touch with questions, comments, or suggestions by email at `tdonoghue.research@gmail.com`, or on
[Twitter](https://twitter.com/Tomdonoghue).

## Acknowledgments

This project is based on the
[BrainSCANR](https://doi.org/10.1016/j.jneumeth.2012.04.019) project, by Jessica & Bradley Voytek, and also
takes inspiration from the [NeuroSynth](http://www.neurosynth.org) project by Tal Yarkoni.

This project is done with the [LISC](https://lisc-tools.github.io/) Python tool,
which allows for collecting and analyzing the scientific literature.
