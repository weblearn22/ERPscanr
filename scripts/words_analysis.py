"""Run analysis on collected words data."""

from lisc.data import ArticlesAll
from lisc.utils import load_object
from lisc.plts.words import plot_years, plot_wordcloud

###################################################################################################
###################################################################################################

# Settings
F_NAME = 'BaseScrape_words'

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING WORDS DATA \n\n')

    words = load_object(F_NAME)

    for erp in words.labels:

        print('Analyzing ', erp, 'data.')

        # Check if raw data loaded, and load if not
        if not words[erp].n_articles:
            words[erp].load()

        # Aggregate data together across all articles
        erp_data = ArticlesAll(words[erp])

        # Create and save summary
        erp_data.create_summary()
        erp_data.save_summary()

        # Create and save wordcloud figure
        plot_wordcloud(erp_data.words, 20)
        # TODO: turn off display & save

        # Create and save years figure
        plot_years(erp_data.years)
        # TODO: turn off display & save

    print('\n\n ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
