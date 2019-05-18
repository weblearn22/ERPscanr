"""Run analysis on scraped words data."""

from erpsc.core.io import load_pickle_obj
from erpsc.erp_data_all import ERPDataAll
from erpsc.plts.wc import make_wc
from erpsc.plts.single import plot_years

###################################################################################################
###################################################################################################

F_NAME = 'BaseScrape_words'

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING WORDS DATA \n\n')

    words = load_pickle_obj(F_NAME)

    for erp in words.result_keys:

        print('Analyzing ', erp, 'data.')

        # Check if raw data loaded - load if not
        if not words[erp].n_articles:
            words[erp].load()

        # Turn into ERPDataAll object
        erp_dat = ERPDataAll(words[erp])

        # Create and save summary
        erp_dat.create_summary()
        erp_dat.save_summary()

        # Create and save wordcloud figure
        make_wc(erp_dat.word_freqs, 20, erp_dat.label,
                disp_fig=False, save_fig=True)

        # Create and save years figure
        plot_years(erp_dat.year_counts, erp_dat.label,
                   disp_fig=False, save_fig=True)

    print('\n\n ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
