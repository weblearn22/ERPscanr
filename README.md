# ERP_SCANR

This is the code based for the Event-Related Potential (ERP) Scanner project, and a text-mining project aiming to use automated web scraping and text analysis of published research articles to summarize current findings about ERPs, and also to generate novel hypotheses. 

It uses two main approaches to mining information:
- 'Count': a co-occurence analysis of ERP terms and other pre-defined terms of interest (cognitive and/or disease terms)
- 'Words': an analysis of all words that appear in the abstract of ERP related papers. From this web-scrape, we also gather and analysis meta-data, such as authors, journals, keywords and date of publication to build profiles of ERPs. 

The current list of terms is in erpsc/terms/ or viewable at /notebooks/Intro.ipynb.

This project is heavily inspired by the BRAIN SCANR project by Voytek & Voytek, viewable here: http://www.brainscanr.com
The BRAIN SCANR project is described in detail here: http://www.sciencedirect.com/science/article/pii/S0165027012001513
