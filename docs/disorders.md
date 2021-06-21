---
layout: assoc
title: disorders
---

# Disorder-Related Associations

This analyses is a co-occurence analysis between ERP components, and a curated set of disorder-related terms. The goal of this analysis is the investigate and summarize which ERP components are associated with which clinical disorders, and compare the similarities and differences between different ERP components.

## Disorder Clustermap

The following plot is a clustering of ERP literature and disorder related associations. The colormap represents the normalized association strength between each ERP component and each association term. Similarity between components, measured as cosine similarity is used to re-order the rows and columns, and hierchichal clustering is applied to group ERP components and association terms into groups. Overall, this graph shows the associations between ERP components and disorder-related terms, and the similarity between ERP components based on their associations.

![disorders_clustermap]({{ site.baseurl }}/assets/FIGS/disorders_clustermap.svg)

This analysis is able to show clusters of ERP components that relate to particular cognitive functions, such as how error related ERPs such as the ERN relate to anxiety, and perceptual processing related ERPs such as the N100 and MMN relate to schizophrenia.
