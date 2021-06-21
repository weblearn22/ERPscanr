---
layout: assoc
title: cognitive
---

# Cognitive Associations

This analyses is a co-occurrence analysis between ERP components, and a curated set of cognition-related terms. The goal of this analysis is the investigate and summarize which ERP components are associated with which cognitive functions, and compare the similarities and differences between different ERP components.

## Cognition Clustermap

The following plot is a clustering of ERP literature and cognition related associations. The colormap represents the normalized association strength between each ERP component and each association term. Similarity between components, measured as cosine similarity is used to re-order the rows and columns, and hierarchical clustering is applied to group ERP components and association terms into groups. Overall, this graph shows the associations between ERP components and cognitive terms, and the similarity between ERP components based on their associations.

![cognitive_clustermap]({{ site.baseurl }}/assets/FIGS/cognitive_clustermap.svg)

This analysis is able to show clusters of ERP components that relate to particular cognitive functions, such as the N400 and P600 that are particularly associated with language and syntax, and the LPP and EPN that are particularly associated with emotional processing. Notably, some of the similarity between components might relate to their timing, with temporally adjacent components clustering together, however, this doesn't explain all the similarities, as some temporally distant components also cluster together, for example the P150 and the P400.

## ERP Timing

Additional analysis was done to examine the most common cognitive association of ERPs across time. This plot is then created by labeling each ERP component with it's typical timing, and the strongest association term from the above co-occurrence analysis. For visualization purposes, this plot only includes a subset of the ERP terms with the highest number of articles (over 250 articles).

![cognitive_time]({{ site.baseurl }}/assets/FIGS/cognitive_time.svg)

This analysis is able to show how different cognitive processes are engaged through time. Notably, earlier ERP components are more broadly related to sensory processing, with later components increasingly relating to more complex cognitive functions.
