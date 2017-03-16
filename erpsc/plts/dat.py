import matplotlib.pyplot as plt

##
##

def plot_years(year_counts, savefig=False):
    """   """

    f, ax = plt.subplots(figsize=(12, 4))

    yrs = set(range(1990, 2018))

    # Extract x & y data to plot
    x_dat = [y[0] for y in year_counts]
    y_dat = [y[1] for y in year_counts]

    # Add line and points to plot
    plt.plot(x_dat, y_dat)
    plt.plot(x_dat, y_dat, '.', markersize=14)

    #
    plt.xlim([min(yrs), max(yrs)])
    plt.ylim([0, max(y_dat)+5])

    #
    plt.title('Publication History')
    plt.xlabel('Year')
    plt.ylabel('# Pubs')

    if savefig:
        plt.savefig('hist.png', transparent=True)