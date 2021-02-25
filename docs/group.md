---
layout: default
---

# GROUP ANALYSIS

In the 'group' analyses, analyses across the entire dataset are done to compare the similarities and differences between different ERP components. These analyses are primarily done using the co-occurence data, and so can generally be interpreted in terms of examining

## ERP Timing

The following figure plots the most common cognitive association of ERPs across time.

![erp_timing]({{ site.baseurl }}/assets/GROUP/erp_time.svg)

This plot is created by by labelling each ERP component with it's typical timing, and then labelling them with their strongest association term. For visualization purposes, this plot only includes a subset of the ERP terms with the highest number of articles.

## Cognition Matrix

The following plot is a clustering of ERP literature and cognitive associations.

![cognition_matrix]({{ site.baseurl }}/assets/GROUP/Cog_Mat.svg)

The heatmap reflects the percent of ERP papers that mention each cognitive term. The matrix is re-ordered based on the cosine similarity, with the dendrogram is a hierachical clustering of ERPs (rows) and cognitive terms (columns). This graph shows the similarity and differences of ERP components based on their putative cognitive associations.

## Disease Matrix

The following plot is a clustering of ERP literature and cognitive associations.

![disease_matrix]({{ site.baseurl }}/assets/GROUP/Dis_Mat.svg)

The following matrix plots the cosine similarity between disease terms (computed across there ERP associations) and the dendrogram shows a hierarchical clustering of disease terms based on their ERP associations.

## ERP Network

Another way to analyze this data is using a network approach. In the following network structure, each node is an ERP component, and the weighted edge between them reflects how often these ERP terms are mentioned in the same papers.

![erp_network]({{ site.baseurl }}/assets/GROUP/network.svg)
