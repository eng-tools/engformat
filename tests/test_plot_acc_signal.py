import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from eqsig import AccSignal

from engformat import plot_acc_signal
from tests.conftest import TEST_DATA_DIR

matplotlib.use("agg")


def _load_acc_signal():
    rec = np.loadtxt(TEST_DATA_DIR + "test_motion_dt0p01.txt")
    return AccSignal(rec, 0.01)


def test_plot_acc_sig_as_response_spectrum():
    acc_sig = _load_acc_signal()
    fig, ax = plt.subplots()
    returned = plot_acc_signal.plot_acc_sig_as_response_spectrum(acc_sig, sub_plot=ax)
    assert returned is ax
    assert len(ax.lines) == 1


def test_plot_acc_sig_as_time_series():
    acc_sig = _load_acc_signal()
    fig, ax = plt.subplots()
    returned = plot_acc_signal.plot_acc_sig_as_time_series(acc_sig, sub_plot=ax)
    assert returned is ax
    assert ax.get_xlabel() == "Time [s]"
    assert len(ax.lines) == 2  # signal + zero axis line


def test_plot_acc_sig_as_fa_spectrum():
    acc_sig = _load_acc_signal()
    fig, ax = plt.subplots()
    returned = plot_acc_signal.plot_acc_sig_as_fa_spectrum(acc_sig, sub_plot=ax)
    assert returned is ax
    assert ax.get_xscale() == "log"
    assert ax.get_yscale() == "log"


def test_plot_acc_sig_as_avd():
    acc_sig = _load_acc_signal()
    sub_plots = plot_acc_signal.plot_acc_sig_as_avd(acc_sig)
    assert len(sub_plots) == 3
    assert len(sub_plots[0].lines) >= 1


def test_plot_acc_sig_as_transfer_function():
    acc_sig = _load_acc_signal()
    fig, ax = plt.subplots()
    returned = plot_acc_signal.plot_acc_sig_as_transfer_function(acc_sig, [acc_sig], sub_plot=ax)
    assert returned is ax
    assert ax.get_xscale() == "log"
    assert ax.get_yscale() == "log"
