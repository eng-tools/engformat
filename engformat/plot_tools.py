__author__ = 'maximmillen'


import numpy as np

from bwplot import cbox


def remove_chartjunk(ax, grid=None, ticklabels=None, show_ticks=False):
    '''
    Removes "chartjunk", such as extra lines of axes and tick marks.

    If grid="y" or "x", will add a white grid at the "y" or "x" axes,
    respectively

    If ticklabels="y" or "x", or ['x', 'y'] will remove ticklabels from that
    axis
    '''
    all_spines = ['top', 'bottom', 'right', 'left', 'polar']
    ax.tick_params(color=cbox('dark grey'))
    for spine in all_spines:
        # The try/except is for polar coordinates, which only have a 'polar'
        # spine and none of the others
        try:
            # ax.spines[spine].set_visible(False)
            ax.spines[spine].set_color(cbox('dark grey'))
            ax.spines[spine].set_linewidth(0.5)
#             ax.spines[spine].set_tick_color(0.5)

        except KeyError:
            pass
    ax.yaxis.label.set_color('0.1')
    ax.xaxis.label.set_color('0.1')
    # For the remaining spines, make their line thinner and a slightly
    # off-black dark grey
    for spine in all_spines:
        if spine not in all_spines:
            # The try/except is for polar coordinates, which only have a 'polar'
            # spine and none of the others
            try:
                ax.spines[spine].set_linewidth(0.5)
            except KeyError:
                pass
                # ax.spines[spine].set_color(almost_black)
                #            ax.spines[spine].set_tick_params(color=almost_black)
                # Check that the axes are not log-scale. If they are, leave the ticks
                # because otherwise people assume a linear scale.
    x_pos = set(['top', 'bottom'])
    y_pos = set(['left', 'right'])
    xy_pos = [x_pos, y_pos]
    xy_ax_names = ['xaxis', 'yaxis']

    ax.tick_params(axis='y', colors='blue', width=0, which='top')

    if grid is not None:
        for g in grid:
            assert g in ('x', 'y')
            ax.grid(axis=grid, color='white', linestyle='-', linewidth=0.3)

    if ticklabels is not None:
        if type(ticklabels) is str:
            assert ticklabels in {('x', 'y')}
            if ticklabels == 'x':
                ax.set_xticklabels([])
            if ticklabels == 'y':
                ax.set_yticklabels([])
        else:
            assert set(ticklabels) | {('x', 'y')} > 0
            if 'x' in ticklabels:
                ax.set_xticklabels([])
            elif 'y' in ticklabels:
                ax.set_yticklabels([])


def trim_ticks(sub_fig, **kwargs):
    balance = kwargs.get('balance', False)
    xlims = sub_fig.get_xlim()
    xticks = list(sub_fig.get_xticks())
    pts = len(xticks)
    for i in range(pts - 1, 0, -1):
        if xticks[i] < xlims[0] or xticks[i] > xlims[1]:
            xticks.pop(i)
    sub_fig.set_xticks(xticks)

    ylims = sub_fig.get_ylim()
    yticks = list(sub_fig.get_yticks())
    pts = len(yticks)
    for i in range(pts - 1, 0, -1):
        if yticks[i] < ylims[0] or yticks[i] > ylims[1]:
            yticks.pop(i)
    if balance and (yticks[0] / -yticks[-1]) - 1.0 > 0.001:
        max_end = np.max([abs(yticks[0]), abs(yticks[-1])])
        tick_delta = abs(yticks[1] - yticks[0])
        yticks = np.arange(-max_end, max_end + tick_delta, tick_delta)
    sub_fig.set_yticks(yticks)


def revamp_legend(sub_fig, ncol=1, **kwargs):
    legloc = kwargs.get('legloc', 'upper right')
    single = kwargs.get('single', True)
    bbox_to_anchor = kwargs.get('bbox_to_anchor', False)
    prop = kwargs.get('prop', None)

    if single:
        handles, labels = sub_fig.get_legend_handles_labels()
        labs = []
        hands = []
        for qq in range(len(labels)):
            if labels[qq] not in labs:
                labs.append(labels[qq])
                hands.append(handles[qq])
        sub_fig.legend(hands, labs, numpoints=1, handlelength=1, handletextpad=0.5, labelspacing=0.3, scatterpoints=1, loc=legloc, ncol=ncol, prop=prop)
    else:
        sub_fig.legend(numpoints=1, handlelength=1, handletextpad=0.5, labelspacing=0.3, scatterpoints=1, loc=legloc, ncol=ncol, prop=prop)
    if bbox_to_anchor != False:
        sub_fig.legend(numpoints=1, handlelength=1, handletextpad=0.5, labelspacing=0.3, scatterpoints=1, loc=legloc, ncol=ncol, bbox_to_anchor=bbox_to_anchor, prop=prop)
    # borderpad    the fractional whitespace inside the legend border
    # shadow    if True, draw a shadow behind legend
    # framealpha    If not None, alpha channel for the frame.
    # ncol    number of columns
    # labelspacing    the vertical space between the legend entries
    # handlelength    the length of the legend handles
    # handletextpad    the pad between the legend handle and text
    leg = sub_fig.get_legend()


    try:  # check if plot has a legend
        frame = leg.get_frame()
    except AttributeError:
        return

    # leg.set_fancybox(True)
    ltext = leg.get_texts()  # all the text.Text instance in the legend
    # llines = leg.get_lines()  # all the lines.Line2D instance in the legend
    frame.set_lw(0.5)
    frame.set_facecolor('0.99')
    frame.set_edgecolor('0.3')
    frame.set_alpha(kwargs.get('alpha', 1.0))
    for tt in ltext:
        tt.set_color('0.1')
        # tt.set_size(7)


def restyle_lines(sub_fig, style="bw", **kwargs):
    """
    Change the color and line style based on the bw_plot style.
    """

    if style == "bw":
        from bwplot.colours import cbox as cs
    elif style == "spectra":
        from bwplot.colours import spectra as cs

    lines = sub_fig.lines
    labs = {}
    cc_box = 0
    for i in range(len(lines)):
        label = lines[i].get_label()
        if "_line" == label[:5]:
            continue  # Don't recolor unlabelled lines

        if label not in labs:  # unique color for each label
            labs[label] = cc_box
            cc_box += 1
        lines[i].set_color(cs(labs[label]))
