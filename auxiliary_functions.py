import random as rd
import matplotlib.cm as cm
import matplotlib.colors as mcolors


def generate_random_colors(n):
    '''
    Generates a list of `n` random colors in hexadecimal format.

    The function creates `n` unique colors by generating random 
    hexadecimal color codes. These color codes are formatted as 
    strings in the format "#RRGGBB", where RR, GG, and BB are 
    two-digit hexadecimal numbers representing the red, green, 
    and blue color channels, respectively.

    Parameters:
    -----------
    n : int
        The number of random colors to generate.

    Returns:
    --------
    colors : list of str
        A list of `n` strings, each representing a random color 
        in hexadecimal format.

    Example:
    --------
    >>> generate_random_colors(5)
    ['#1a2b3c', '#4d5e6f', '#7a8b9c', '#c1d2e3', '#e4f5a6']
    
    Notes:
    ------
    The colors are generated randomly, so each call to this 
    function will produce a different set of colors.
    '''
    colors = []
    for i in range(n):
        color = "#%06x" % rd.randint(0, 0xFFFFFF)
        colors.append(color)
    return colors


def generate_viridis_colors(n, cmap_name='viridis'):
    '''
    Generates a list of `n` equally spaced colors from a given matplotlib colormap.
    The output colors are in hexadecimal format.

    Parameters
    ----------
    n : int
        Number of colors to generate.
    cmap_name : str, optional
        Name of the matplotlib colormap (default is 'viridis').

    Returns
    -------
    colors : list of str
        List of `n` colors in hexadecimal format.

    Example
    -------
    >>> generate_colormap_colors(5, cmap_name='viridis')
    ['#440154', '#31688e', '#35b779', '#fde725']
    '''
    cmap = cm.get_cmap(cmap_name, n)  # Get colormap with n discrete steps
    colors = [mcolors.to_hex(cmap(i)) for i in range(n)]
    return colors