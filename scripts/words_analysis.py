"""Run analysis on collected words data."""

from lisc.data import ArticlesAll
from lisc.utils import load_object

from lisc.utils import SCDB

from lisc.plts.words import plot_years, plot_wordcloud

###################################################################################################
###################################################################################################

# Set words object to load
F_NAME = 'words_erps'

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING WORDS DATA \n\n')

    db = SCDB('../data')

    words = load_object(F_NAME, db)

    for erp in words.labels:

        print('Analyzing ', erp, 'data.')

        # Load data for the current term
        words[erp].load(directory=db)

        # Aggregate data together across all articles
        erp_data = ArticlesAll(words[erp])

        # Create and save summary
        erp_data.create_summary()
        erp_data.save_summary(directory=db)

        # Create and save wordcloud figure
        plot_wordcloud(erp_data.words, 20, save_fig=True, f_name='wc/' + erp, directory=db)

        # Create and save years figure
        plot_years(erp_data.years, save_fig=True, f_name='years/' + erp, directory=db)

        # Clear the loaded data for the current term
        words[erp].clear()

    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
