import numpy as np
import matplotlib
matplotlib.use('agg')
from eqsig import AccSignal
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from bwplot import cbox

from engformat import plot_acc_signal

from tests.conftest import TEST_DATA_DIR


@image_comparison(baseline_images=['plot_acc_sig_as_response_spectrum'], extensions=['png'])
def test_plot_acc_sig_as_response_spectrum():
    record_path = TEST_DATA_DIR
    record_filename = 'test_motion_dt0p01.txt'
    motion_step = 0.01
    rec = np.loadtxt(record_path + record_filename)
    acc_sig = AccSignal(rec, motion_step)
    plot_acc_signal.plot_acc_sig_as_response_spectrum(acc_sig)


@image_comparison(baseline_images=['plot_acc_sig_as_time_series'], extensions=['png'])
def test_plot_acc_sig_as_time_series():
    record_path = TEST_DATA_DIR
    record_filename = 'test_motion_dt0p01.txt'
    motion_step = 0.01
    rec = np.loadtxt(record_path + record_filename)
    acc_sig = AccSignal(rec, motion_step)
    plot_acc_signal.plot_acc_sig_as_time_series(acc_sig)


@image_comparison(baseline_images=['plot_acc_sig_as_fa_spectrum'], extensions=['png'])
def test_plot_acc_sig_as_fa_spectrum():
    record_path = TEST_DATA_DIR
    record_filename = 'test_motion_dt0p01.txt'
    motion_step = 0.01
    rec = np.loadtxt(record_path + record_filename)
    acc_sig = AccSignal(rec, motion_step)
    plot_acc_signal.plot_acc_sig_as_fa_spectrum(acc_sig)


@image_comparison(baseline_images=['plot_acc_sig_as_avd'], extensions=['png'])
def test_plot_acc_sig_as_avd():
    record_path = TEST_DATA_DIR
    record_filename = 'test_motion_dt0p01.txt'
    motion_step = 0.01
    rec = np.loadtxt(record_path + record_filename)
    acc_sig = AccSignal(rec, motion_step)
    plot_acc_signal.plot_acc_sig_as_avd(acc_sig)


@image_comparison(baseline_images=['plot_acc_sig_as_transfer_function'], extensions=['png'])
def test_plot_acc_sig_as_transfer_function():
    record_path = TEST_DATA_DIR
    record_filename = 'test_motion_dt0p01.txt'
    motion_step = 0.01
    rec = np.loadtxt(record_path + record_filename)
    acc_sig = AccSignal(rec, motion_step)
    plot_acc_signal.plot_acc_sig_as_transfer_function(acc_sig, [acc_sig])


if __name__ == '__main__':
    test_plot_acc_sig_as_response_spectrum()