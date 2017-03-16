"""WordCloud plots for ERP-SCANR."""

import random
from wordcloud import WordCloud

############################################################################################
############################################################################################
############################################################################################

def conv_freqs(freq_dist, n_words):
    """Convert FreqDist into a list of tuple for creating a WordCloud.

    Parameters
    ----------
    freq_dist : nltk FreqDist() object
        Frequency distribution of words from text.
    n_words : int
        Number of words to extract for plotting.

    Returns
    -------
    list of tuple
        All words with their corresponding frequecies.
    """

    # Get most common words, and convert to tuple format
    top_words = freq_dist.most_common(n_words)
    return [(freq[0], freq[1]) for freq in top_words]


def create_wc(words_in):
    """Create WordCloud object.

    Parameters
    ----------
    words_in : list of tuple
        Words to plot, with their corresponding frequencies.

    Returns
    -------
    wc : WordCloud() object
        Wordcloud definition.
    """

    # Create the WordCloud object
    wc = WordCloud(background_color=None,
                   mode='RGBA',
                   width=800,
                   height=400,
                   prefer_horizontal=1,
                   relative_scaling=0.5,
                   min_font_size=25,
                   max_font_size=80).generate_from_frequencies(words_in)

    # Change colour scheme to grey
    wc.recolor(color_func=_grey_color_func, random_state=3)

    return wc

############################################################################################
############################################################################################
############################################################################################

def _grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """Function for custom coloring - use gray pallete.
    From here: https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html
    """

    return "hsl(0, 0%%, %d%%)" % random.randint(25, 50)
