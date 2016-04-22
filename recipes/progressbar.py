#!/bin/python3
"""Example usage of the progressbar module."""

import sys
import time

from progressbar import (ETA, AnimatedMarker, Bar, BouncingBar, Counter,
                         FileTransferSpeed, FormatLabel, Percentage,
                         ProgressBar, ReverseBar, RotatingMarker,
                         SimpleProgress, Timer)

examples = []


def example(fn):
    """Base example function."""
    try:
        name = 'Example %d' % int(fn.__name__[7:])
    except:
        name = fn.__name__

    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % name)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')

    examples.append(wrapped)
    return wrapped


@example
def example0():
    """Display percentage progress bar."""
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start()
    for i in range(300):
        time.sleep(0.01)
        pbar.update(i+1)
    pbar.finish()


@example
def example1():
    """Display ."""
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()


@example
def example2():
    """Display ."""
    class CrazyFileTransferSpeed(FileTransferSpeed):
        """It's bigger between 45 and 80 percent."""

        def update(self, pbar):
            if 45 < pbar.percentage() < 80:
                return 'Bigger Now ' + FileTransferSpeed.update(self, pbar)
            else:
                return FileTransferSpeed.update(self, pbar)

    widgets = [CrazyFileTransferSpeed(), ' <<<', Bar(), '>>> ',
               Percentage(), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000)
    # maybe do something
    pbar.start()
    for i in range(2000000):
        # do something
        pbar.update(5*i+1)
    pbar.finish()


@example
def example3():
    """Display ."""
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()


@example
def example4():
    """Display ."""
    widgets = ['Test: ', Percentage(), ' ',
               Bar(marker='0', left='[', right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=500)
    pbar.start()
    for i in range(100, 500+1, 50):
        time.sleep(0.2)
        pbar.update(i)
    pbar.finish()


@example
def example5():
    """Display ."""
    pbar = ProgressBar(widgets=[SimpleProgress()], maxval=17).start()
    for i in range(17):
        time.sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()


@example
def example6():
    """Display ."""
    pbar = ProgressBar().start()
    for i in range(100):
        time.sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()


@example
def example7():
    """Display ."""
    pbar = ProgressBar()  # Progressbar can guess maxval automatically.
    for i in pbar(range(80)):
        time.sleep(0.01)


@example
def example8():
    """Display ."""
    pbar = ProgressBar(maxval=80)  # Progressbar can't guess maxval.
    for i in pbar((i for i in range(80))):
        time.sleep(0.01)


@example
def example9():
    """Display ."""
    pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])
    for i in pbar((i for i in range(50))):
        time.sleep(.08)


@example
def example10():
    """Display ."""
    widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(150))):
        time.sleep(0.1)


@example
def example11():
    """Display ."""
    widgets = [FormatLabel('Processed: %(value)d lines (in: %(elapsed)s)')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(150))):
        time.sleep(0.1)


@example
def example12():
    """Display ."""
    widgets = ['Balloon: ', AnimatedMarker(markers='.oO@* ')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(24))):
        time.sleep(0.3)


@example
def example13():
    """Display ."""
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='????????')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def example14():
    """Display ."""
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='????')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def example15():
    """Display ."""
    try:
        widgets = ['Wheels: ', AnimatedMarker(markers='????')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def example16():
    """Display ."""
    widgets = [FormatLabel('Bouncer: value %(value)d - '), BouncingBar()]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(180))):
        time.sleep(0.05)


@example
def example17():
    """Display ."""
    widgets = [FormatLabel('Animated Bouncer: value %(value)d - '),
               BouncingBar(marker=RotatingMarker())]

    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(180))):
        time.sleep(0.05)

# @example
# def example18():
#     """Display ."""
#     widgets = [Percentage(),
#                ' ', Bar(),
#                ' ', ETA(),
#                ' ', AdaptiveETA()]
#     pbar = ProgressBar(widgets=widgets, maxval=500)
#     pbar.start()
#     for i in range(500):
#         time.sleep(0.01 + (i < 100) * 0.01 + (i > 400) * 0.9)
#         pbar.update(i + 1)
#     pbar.finish()

# @example
# def example19():
#     """Display ."""
#     pbar = ProgressBar()
#     for i in pbar([]):
#         pass
#     pbar.finish()

if __name__ == '__main__':
    try:
        for example in examples:
            example()
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')
