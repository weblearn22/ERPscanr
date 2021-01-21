---
layout: default
---

# GROUP ANALYSIS

From the data for each ERP component, primarily the co-occurence data, we can analyze across the entire dataset to compare the structure and similarities between different components.

## ERP Timing

The following plot takes the most common ERPs for the typical timing is known, and plots the most common cognitive association.

![cog_mat]({{ site.baseurl }}/assets/GROUP/erp_time.svg)

## Cognition Matrix

In the following matrix, the heatmap relates to the the percent of ERP papers that mention each cognitive term. The matrix is re-ordered based on the cosine similarity between the cognitive associations of ERP components. The dendrogram is a hierachical clustering of ERPs (rows) and cognitive terms (columns).

![cog_mat]({{ site.baseurl }}/assets/GROUP/Cog_Mat.svg)

## Disease Matrix

The following matrix plots the cosine similarity between disease terms (computed across there ERP associations) and the dendrogram shows a hierarchical clustering of disease terms based on their ERP associations.

![cog_mat]({{ site.baseurl }}/assets/GROUP/Dis_Mat.svg)

## ERP Network

Another way to analyze this data is using a network approach. In the following network structure, each node is an ERP component, and the weighted edge between them reflects how often these ERP terms are mentioned in the same papers.

![cog_mat]({{ site.baseurl }}/assets/GROUP/network.svg)
