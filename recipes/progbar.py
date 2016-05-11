#!/bin/python3
"""Example usage of the tqdm and progressbar2 modules."""

import sys
from time import sleep

from progressbar import (ETA, AbsoluteETA, AdaptiveETA, AdaptiveTransferSpeed,
                         AnimatedMarker, Bar, BouncingBar, Counter,
                         FileTransferSpeed, FormatLabel, Percentage,
                         ProgressBar, ReverseBar, RotatingMarker,
                         SimpleProgress, Timer)
from tqdm import tqdm

examples = []


def example(fn):
    """Display progess bars."""
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')

    examples.append(wrapped)
    return wrapped


@example
def example99():
    """
    Display progess bar using tqdm.

    >>> example99()
    True
    """
    for i in tqdm(range(100)):
        sleep(0.01)
    return True


@example
def example0():
    """
    Display progess bar using tqdm.

    >>> example0()
    True
    """
    pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=100).start()
    for i in range(100):
        sleep(0.02)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def with_example0():
    """
    Display progess bar using tqdm.

    >>> with_example0()
    True
    """
    with ProgressBar(max_value=100) as progress:
        for i in range(100):
            sleep(0.02)
            progress.update(i)
    return True


@example
def example1():
    """
    Display progess bar using tqdm.

    >>> example1()
    True
    """
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        sleep(0.05)
        pbar.update(10 * i + 1)
    pbar.finish()
    return True


@example
def with_example1():
    """
    Display progess bar using tqdm.

    >>> with_example1()
    True
    """
    with ProgressBar(max_value=100, redirect_stdout=True) as p:
        for i in range(100):
            sleep(0.05)
            p.update(i)
    return True


@example
def example2():
    """
    Display progess bar using tqdm.

    >>> example2()
    True
    """
    class CrazyFileTransferSpeed(FileTransferSpeed):
        """
        Display progess bar using tqdm.

        It's bigger between 45 and 80 percent.
        """

        def update(self, pbar):
            """
            Display progess bar using tqdm.

            >>> update()
            True
            """
            if 45 < pbar.percentage() < 80:
                return 'Bigger Now ' + FileTransferSpeed.update(self, pbar)
            else:
                return FileTransferSpeed.update(self, pbar)

    widgets = [CrazyFileTransferSpeed(), ' <<<', Bar(), '>>> ',
               Percentage(), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, max_value=1000)
    # maybe do something
    pbar.start()
    for i in range(200):
        sleep(0.01)
        pbar.update(5 * i + 1)
    pbar.finish()
    return True


@example
def example3():
    """
    Display progess bar using tqdm.

    >>> example3()
    True
    """
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        sleep(0.01)
        pbar.update(10 * i + 1)
    pbar.finish()
    return True


@example
def example4():
    """
    Display progess bar using tqdm.

    >>> example4()
    True
    """
    widgets = ['Test: ', Percentage(), ' ',
               Bar(marker='0', left='[', right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(100, 500 + 1, 50):
        sleep(0.2)
        pbar.update(i)
    pbar.finish()
    return True


@example
def example5():
    """
    Display progess bar using tqdm.

    >>> example5()
    True
    """
    pbar = ProgressBar(widgets=[SimpleProgress()], max_value=17).start()
    for i in range(17):
        sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example6():
    """
    Display progess bar using tqdm.

    >>> example6()
    True
    """
    pbar = ProgressBar().start()
    for i in range(10):
        sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example7():
    """
    Display progess bar using tqdm.

    >>> example7()
    True
    """
    pbar = ProgressBar()  # Progressbar can guess max_value automatically.
    for i in pbar(range(8)):
        sleep(0.2)
    return True


@example
def example8():
    """
    Display progess bar using tqdm.

    >>> example8()
    True
    """
    pbar = ProgressBar(max_value=8)  # Progressbar can't guess max_value.
    for i in pbar((i for i in range(8))):
        sleep(0.2)
    return True


@example
def example9():
    """
    Display progess bar using tqdm.

    >>> example9()
    True
    """
    pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])
    for i in pbar((i for i in range(24))):
        sleep(0.2)
    return True


@example
def example10():
    """
    Display progess bar using tqdm.

    >>> example10()
    True
    """
    widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(15))):
        sleep(0.2)
    return True


@example
def example11():
    """
    Display progess bar using tqdm.

    >>> example11()
    True
    """
    widgets = [FormatLabel('Processed: %(value)d lines (in: %(elapsed)s)')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(15))):
        sleep(0.2)
    return True


@example
def example12():
    """
    Display progess bar using tqdm.

    >>> example12()
    True
    """
    widgets = ['Balloon: ', AnimatedMarker(markers='.oO@* ')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(24))):
        sleep(0.1)
    return True


@example
def example13():
    """
    Display progess bar using tqdm.

    >>> example13()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='←↖↑↗→↘↓↙')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
    return True


@example
def example14():
    """
    Display progess bar using tqdm.

    >>> example14()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='◢◣◤◥')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
    return True


@example
def example15():
    """
    Display progess bar using tqdm.

    >>> example15()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Wheels: ', AnimatedMarker(markers='◐◓◑◒')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
    return True


@example
def example16():
    """
    Display progess bar using tqdm.

    >>> example16()
    True
    """
    widgets = [FormatLabel('Bouncer: value %(value)d - '), BouncingBar()]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(25))):
        sleep(0.2)
    return True


@example
def example17():
    """
    Display progess bar using tqdm.

    >>> example17()
    True
    """
    widgets = [FormatLabel('Animated Bouncer: value %(value)d - '),
               BouncingBar(marker=RotatingMarker())]

    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(25))):
        sleep(0.2)
    return True


# @example
# def with_example18():
#     """Display progess bar using tqdm."""
#     with ProgressBar(max_value=10, term_width=20, left_justify=False) as \
#             progress:
#         assert progress._env_size() is not None
#         for i in range(10):
#             progress.update(i)


@example
def with_example19():
    """
    Display progess bar using tqdm.

    >>> example19()
    True
    """
    with ProgressBar(max_value=1) as progress:
        try:
            progress.update(2)
        except ValueError:
            pass
    return True


@example
def with_example20():
    """
    Display progess bar using tqdm.

    >>> example20()
    True
    """
    progress = ProgressBar(max_value=1)
    try:
        progress.update(1)
    except RuntimeError:
        pass
    return True


@example
def with_example21a():
    """
    Display progess bar using tqdm.

    >>> example21a()
    True
    """
    with ProgressBar(max_value=1, redirect_stdout=True) as progress:
        print('', sys.stdout)
        progress.update(0)
    return True


@example
def with_example21b():
    """
    Display progess bar using tqdm.

    >>> example21b()
    True
    """
    with ProgressBar(max_value=1, redirect_stderr=True) as progress:
        print('', sys.stderr)
        progress.update(0)
    return True


@example
def with_example22():
    """
    Display progess bar using tqdm.

    >>> example22()
    True
    """
    try:
        with ProgressBar(max_value=-1) as progress:
            progress.start()
    except ValueError:
        pass
    return True


@example
def example23():
    """
    Display progess bar using tqdm.

    >>> example23()
    True
    """
    widgets = [BouncingBar(marker=RotatingMarker())]
    with ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)

    widgets = [BouncingBar(marker=RotatingMarker(), fill_left=False)]
    with ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)
    return True


@example
def example24():
    """
    Display progess bar using tqdm.

    >>> example24()
    True
    """
    pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=10).start()
    for i in range(10):
        # do something
        sleep(0.1)
        pbar += 1
    pbar.finish()
    return True


@example
def example25():
    """
    Display progess bar using tqdm.

    >>> example25()
    True
    """
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=1000,
                       redirect_stdout=True).start()
    for i in range(100):
        # do something
        pbar += 10
    pbar.finish()
    return True


@example
def example26():
    """
    Display progess bar using tqdm.

    >>> example26()
    True
    """
    widgets = [
        Percentage(),
        ' ', Bar(),
        ' ', ETA(),
        ' ', AdaptiveETA(),
        ' ', AdaptiveTransferSpeed(),
    ]
    pbar = ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(500):
        sleep(0.01 + (i < 100) * 0.0001 + (i > 400) * 0.009)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example27():
    """
    Display progess bar using tqdm.

    >>> example27()
    True
    """
    # Testing AdaptiveETA when the value doesn't actually change
    pbar = ProgressBar(widgets=[AdaptiveETA(), AdaptiveTransferSpeed()],
                       max_value=2, poll=0.0001)
    pbar.start()
    pbar.update(1)
    sleep(0.01)
    pbar.update(1)
    pbar.finish()
    return True


@example
def example28():
    """
    Display progess bar using tqdm.

    >>> example28()
    True
    """
    # Testing using progressbar as an iterator with a max value
    pbar = ProgressBar()

    for n in pbar(iter(range(100)), 100):
        # iter range is a way to get an iterator in both python 2 and 3
        pass
    return True


@example
def example29():
    """
    Display progess bar using tqdm.

    >>> example29()
    True
    """
    widgets = ['Test: ', Percentage(), ' | ', ETA(), ' | ', AbsoluteETA()]
    pbar = ProgressBar(widgets=widgets, maxval=500).start()
    for i in range(500):
        sleep(0.01)
        pbar.update(i+1)
    pbar.finish()
    return True


def run():
    """Display progess bar examples."""
    for example in examples:
        example()
    return True


def test():
    """Run tests."""
    assert run() is True


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')
