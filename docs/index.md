---
layout: default
---

# Introduction

ERPscanr is a semi-automated meta-analysis of scientific literature on the topic of event-related potentials (ERPs).

## Motivation

ERPs are a common method of investigation in cognitive neuroscience, having been examined in thousands of articles investigating various aspects of cognition and disease. The scale of this literature can make it difficult to keep up, as well as to examine patterns across to literature.

Systematic reviews offer one way to examine the literature. However, they require a significant time commitment, and are often focues on specific topics. As a complement to systematic reviews, here we use literature analysis to collect and analyze the ERP literature at scale, in a semi-automated way.In doing so, this project serves mostly as a data-driven summarization tool - a way to quickly and efficiently get a quick summary of ERP components that have been characterized in the literature, what they are used to investigate, and the relations between them.

## Methods

ERPscanr uses the [LISC](https://lisc-tools.github.io/) Python tool to collect and analyze scientific literature. The data is collected primarily from [Pubmed](https://pubmed.ncbi.nlm.nih.gov/), a database of biomedical literature. From there, we use simple text-mining and word co-occurence analysis to derive data-driven summaries for each ERP, as well as to compare across these profiles to summarize patterns across the literature.

A more in-depth overview of the methods is available [here](methods.html). The code for this analysis is openly available in the [project repository](https://github.com/ERPscanr/ERPscanr).

## Version

The current collection and analysis is v0.2:

	- collected on: 23 March, 2017
	- dbbuild: Build170322-2207m.1
	- lastupdate: 2017/03/23 02:08

Note that this website may update periodicially, as

The project, codebase, and website are all dynamic and in active development, and this website may change without warning, including changes to the results due to edits to the analysis procedure, changes in the term dictionaries, and the addition of new analyses.

## Reference

A preprint for this project is upcoming.

## Contact

ERP-SCANR was built and is maintained by [Tom Donoghue](https://tomdonoghue.github.io/).

You can get in touch with questions, comments, or suggestions by email at `tdonoghue.research@gmail.com`, or on [Twitter](https://twitter.com/Tomdonoghue).

## Acknowledgements

This project is based on the
[BrainSCANR](https://doi.org/10.1016/j.jneumeth.2012.04.019) project, by Jessica & Bradley Voytek, and also
takes inspiration from the [NeuroSynth](http://www.neurosynth.org) project by Tal Yarkoni.

This project is done with the [LISC](https://lisc-tools.github.io/) Python tool, which allows for collecting and analyzing the scientific literature. This tool and project are built upon the PudMed E-Utilities API, and open source tools.
