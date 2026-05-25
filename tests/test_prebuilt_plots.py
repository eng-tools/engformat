import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from bwplot import cbox

import engformat.plot as esfp

matplotlib.use("agg")


def test_basic_xy():
    x = np.linspace(0, 10, 50)
    y = x**2
    fig, ax = plt.subplots()
    ax.plot(x, y, label="test", c=cbox(2))
    esfp.xy(ax)
    assert len(ax.lines) == 1
    assert ax.get_xlim()[1] >= 10


def test_pb_time_series():
    x = np.linspace(0, 10, 50)
    y = x**2
    fig, ax = plt.subplots()
    ax.plot(x, y, label="test")
    esfp.time_series(ax)
    assert len(ax.lines) == 2  # signal + zero axis line
    assert ax.get_ylim()[0] <= 0


def test_pb_transfer_function():
    x = np.linspace(0, 10, 50)
    y = x**1.2
    fig, ax = plt.subplots()
    ax.plot(x, y, label="test")
    esfp.transfer_function(ax, ratio=True)
    lines = ax.get_lines()
    assert len(lines) == 2
    assert lines[0].get_zorder() == 102
    assert lines[1].get_zorder() == 50  # ratio line
    assert ax.get_xlim()[0] == 0.0
    assert ax.get_ylim()[0] == 0.0


def test_spines_axes_positions():
    fig = plt.figure()
    x = np.linspace(0, 2 * np.pi, 100)
    y = 2 * np.sin(x)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("centered spines")
    ax.plot(x, y)
    ax.spines["right"].set_position(("axes", 0.1))
    ax.yaxis.set_ticks_position("right")
    ax.spines["top"].set_position(("axes", 0.25))
    ax.xaxis.set_ticks_position("top")
    ax.spines["left"].set_color("none")
    ax.spines["bottom"].set_color("none")
    assert len(ax.lines) == 1


def test_new_time_series_plots_supports_single_row():
    # Regression: matplotlib returns a single Axes instance for nrows=1,
    # so this helper must normalize to a sequence.
    sub_plots = esfp.new_time_series_plots(nrows=1)
    assert len(sub_plots) == 1
    assert hasattr(sub_plots[0], "plot")
