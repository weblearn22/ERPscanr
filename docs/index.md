---
layout: default
---

# Introduction

ERP-SCANR is an 'automated meta-analysis' of the scientific literature on the topic of event-related potentials (ERPs).

## Motivation

ERPs are a common method of investigation in cognitive neuroscience, so much so that there are now hundreds of thousands of papers investigating cognition, disease states, and the brain using these approaches. The scale of the literature makes it difficult to keep up to date with the field, and explore now ideas about cognitive neuroscience and this method of investigation. This issues can be especially intimidating to newcomers to the field.

Systematic reviews offer one way to gain this kind of information, but involve a large time commitment, typically lag significantly behind the literature, and may not cut across different areas of investigation.

ERP-SCANR serves mostly as a data-driven summarization tool - a way to quickly and efficiently get a quick summary of ERP components that have been characterized in the literature, and the relations between them.

## Methods

ERP-SCANR is based on the PubMed E-Utilities tools, which are used to search through PubMed databases and extract
From there, we use simple text-mining and word co-occurence analysis to derive data-driven summaries for each ERP, as well as to compare across these profiles to work towards summarizing across

A more in-depth overview of the methods is available [here](methods.html).

## Version

The project, codebase, and website are all dynamic and in active development, and this website may change without warning, including changes to the results due to edits to the analysis procedure, changes in the term dictionaries, and the addition of new analyses.

The current scrape is v0.1-PubMed:

Counts Scrape:

    - dbbuild: Build170322-2207m.1
    - lastupdate: 2017/03/23 02:08
    - scraped on: Thursday 23 March

Words  Scrape:

    - dbbuild: Build170322-2207m.2
    - lastupdate: 2017/03/23 07:24
    - scraped on: Thursday 23 March

## Reference

A preprint for this project is upcoming.

A [poster](https://www.dropbox.com/s/sgnz7ecd3qp6tb7/TDonoghue_ERP-SCANR_CNS.pdf?dl=0) for this project was
presented at the Cognitive Neuroscience Society (CNS) conference in 2017.

## Contact

ERP-SCANR was built by [Tom Donoghue](https://tomdonoghue.github.io/).
Please get in touch with any questions, comments, suggestions at tdonoghue.research@gmail.com, or @TomDonoghue on Twitter.

## Acknowledgements

This project is based on the
[BrainSCANR](https://doi.org/10.1016/j.jneumeth.2012.04.019) project, by Jessica & Bradley Voytek, and also
takes inspiration from the [NeuroSynth](http://www.neurosynth.org) project by Tal Yarkoni.

This project is done with the [LISC](https://lisc-tools.github.io/) Python tool, which allows for collecting and analyzing the scientific literature. This tool and project are built upon the PudMed E-Utilities API, and open source tools.
