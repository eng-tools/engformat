import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from bwplot import cbox

import engformat.plot as esfp


@image_comparison(baseline_images=['basic_xy'], extensions=['png'])
def test_basic_xy():
    x = np.linspace(0, 10, 50)
    y = x ** 2
    big_fig = plt.figure()
    sf = big_fig.add_subplot(111)
    sf.plot(x, y, label="test", c=cbox(2))
    esfp.xy(sf)


@image_comparison(baseline_images=['pb_time_series'], extensions=['png'])
def test_pb_time_series():
    x = np.linspace(0, 10, 50)
    y = x ** 2
    big_fig = plt.figure()
    sf = big_fig.add_subplot(111)
    sf.plot(x, y, label="test")
    esfp.time_series(sf)


@image_comparison(baseline_images=['pb_transfer_function'], extensions=['png'])
def test_pb_transfer_function():
    x = np.linspace(0, 10, 50)
    y = x ** 1.2
    big_fig = plt.figure()
    sp = big_fig.add_subplot(111)
    sp.plot(x, y, label="test")
    esfp.transfer_function(sp, ratio=True)
    lines = sp.get_lines()
    assert len(lines) == 2
    assert lines[0].get_zorder() == 102
    assert lines[1].get_zorder() == 50  # ratio line
    xlim = sp.get_xlim()
    ylim = sp.get_ylim()
    assert xlim[0] == 0.0
    assert xlim[1] == 10.0
    assert ylim[0] == 0.0


@image_comparison(baseline_images=['spines_axes_positions'],
                  extensions=['png'])
def test_spines_axes_positions():
    # SF bug 2852168
    fig = plt.figure()
    x = np.linspace(0, 2 * np.pi, 100)
    y = 2 * np.sin(x)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('centered spines')
    ax.plot(x, y)
    ax.spines['right'].set_position(('axes', 0.1))
    ax.yaxis.set_ticks_position('right')
    ax.spines['top'].set_position(('axes', 0.25))
    ax.xaxis.set_ticks_position('top')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')

