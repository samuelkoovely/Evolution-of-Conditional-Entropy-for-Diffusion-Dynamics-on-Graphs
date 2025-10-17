import random as rd
import matplotlib.cm as cm
import matplotlib.colors as mcolors

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