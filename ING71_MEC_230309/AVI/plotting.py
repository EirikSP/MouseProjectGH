import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
import plot_utils


def plot_area(proc, show=True, save=False, filename='area'):
    file = proc['filenames'][0][0]
    file = file.split('/')[-1]

    plt.plot(proc['pupil'][0]['area'])
    plt.xlabel('frames')
    plt.title('Area ' + file)
    if save:
        plt.savefig('./figures/' + filename + '.pdf')
    if show:
        plt.show()


def plot_com(proc, show=True, save=False, filename='com'):
    plt.plot(proc['pupil'][0]['com'])
    plt.xlabel('frames')
    plt.title('Center of mass')
    if save:
        plt.savefig('./figures/' + filename + '.pdf')
    if show:
        plt.show()


def plot_blink_and_area(proc, proc_blink=None, show=True, save=False, filename='blink_and_area'):
    if proc_blink is None:
        plt.plot(minmax_scale((proc['blink'][0])))
    else:
        plt.plot(minmax_scale((proc_blink['blink'][0])))
    plt.plot(minmax_scale(proc['pupil'][0]['area']), alpha=0.5)
    plt.xlabel('frames')
    plt.title('Area and blinking')
    if save:
        plt.savefig('./figures/' + filename + '.pdf')
    if show:
        plt.show()