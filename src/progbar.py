#!/bin/python3
"""Example usage of the tqdm and progressbar2 modules."""

import contextlib
import sys
from time import sleep

import progressbar
from pytest import mark
from tqdm import tqdm

examples = []

# Testing the progbars is a bit slow, so we'll skip them.
# Comment the following line if testing of progbar.py is required.
pytestmark = mark.skip(reason="Testing progbars takes a long time")


def example(fn):
    """Display progress bars."""

    def wrapped() -> None:
        try:
            sys.stdout.write("Running: %s\n" % fn.__name__)
            fn()
            sys.stdout.write("\n")
        except KeyboardInterrupt:
            sys.stdout.write("\nSkipping example.\n\n")

    examples.append(wrapped)
    return wrapped


@example
def example99() -> bool:
    """Display progress bar using tqdm.

    >>> example99()
    True
    """
    for _i in tqdm(range(100)):
        sleep(0.01)
    return True


@example
def example0() -> bool:
    """Display progress bar using tqdm.

    >>> example0()
    True
    """
    pbar = progressbar.ProgressBar(
        widgets=[progressbar.Percentage(), progressbar.Bar()], max_value=100
    ).start()
    for i in range(100):
        sleep(0.02)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def with_example0() -> bool:
    """Display progress bar using tqdm.

    >>> with_example0()
    True
    """
    with progressbar.ProgressBar(max_value=100) as progress:
        for i in range(100):
            sleep(0.02)
            progress.update(i)
    return True


@example
def example1() -> bool:
    """Display progress bar using tqdm.

    >>> example1()
    True
    """
    widgets = [
        "Test: ",
        progressbar.Percentage(),
        " ",
        progressbar.Bar(marker=progressbar.RotatingMarker()),
        " ",
        progressbar.ETA(),
        " ",
        progressbar.FileTransferSpeed(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        sleep(0.05)
        pbar.update(10 * i + 1)
    pbar.finish()
    return True


@example
def with_example1() -> bool:
    """Display progress bar using tqdm.

    >>> with_example1()
    True
    """
    with progressbar.ProgressBar(max_value=100, redirect_stdout=True) as p:
        for i in range(100):
            sleep(0.05)
            p.update(i)
    return True


@example
def example2() -> bool:
    """Display progress bar using tqdm.

    >>> example2()
    True
    """

    class CrazyFileTransferSpeed(progressbar.FileTransferSpeed):
        """Display progress bar using tqdm.

        It's bigger between 45 and 80 percent.
        """

        def update(self, pbar):
            """Display progress bar using tqdm.

            >>> update()
            True
            """
            if 45 < pbar.percentage() < 80:
                return "Bigger Now " + progressbar.FileTransferSpeed.update(self, pbar)
            return progressbar.FileTransferSpeed.update(self, pbar)

    widgets = [
        CrazyFileTransferSpeed(),
        " <<<",
        progressbar.Bar(),
        ">>> ",
        progressbar.Percentage(),
        " ",
        progressbar.ETA(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=1000)
    # maybe do something
    pbar.start()
    for i in range(200):
        sleep(0.01)
        pbar.update(5 * i + 1)
    pbar.finish()
    return True


@example
def example3() -> bool:
    """Display progress bar using tqdm.

    >>> example3()
    True
    """
    widgets = [
        progressbar.Bar(">"),
        " ",
        progressbar.ETA(),
        " ",
        progressbar.ReverseBar("<"),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        sleep(0.01)
        pbar.update(10 * i + 1)
    pbar.finish()
    return True


@example
def example4() -> bool:
    """Display progress bar using tqdm.

    >>> example4()
    True
    """
    widgets = [
        "Test: ",
        progressbar.Percentage(),
        " ",
        progressbar.Bar(marker="0", left="[", right="]"),
        " ",
        progressbar.ETA(),
        " ",
        progressbar.FileTransferSpeed(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(100, 500 + 1, 50):
        sleep(0.2)
        pbar.update(i)
    pbar.finish()
    return True


@example
def example5() -> bool:
    """Display progress bar using tqdm.

    >>> example5()
    True
    """
    pbar = progressbar.ProgressBar(widgets=[progressbar.SimpleProgress()], max_value=17).start()
    for i in range(17):
        sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example6() -> bool:
    """Display progress bar using tqdm.

    >>> example6()
    True
    """
    pbar = progressbar.ProgressBar().start()
    for i in range(10):
        sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example7() -> bool:
    """Display progress bar using tqdm.

    >>> example7()
    True
    """
    pbar = progressbar.ProgressBar()  # Progressbar can guess max_value automatically.
    for _i in pbar(range(8)):
        sleep(0.2)
    return True


@example
def example8() -> bool:
    """Display progress bar using tqdm.

    >>> example8()
    True
    """
    pbar = progressbar.ProgressBar(max_value=8)  # Progressbar can't guess max_value.
    for _i in pbar(i for i in range(8)):
        sleep(0.2)
    return True


@example
def example9() -> bool:
    """Display progress bar using tqdm.

    >>> example9()
    True
    """
    pbar = progressbar.ProgressBar(widgets=["Working: ", progressbar.AnimatedMarker()])
    for _i in pbar(i for i in range(24)):
        sleep(0.2)
    return True


@example
def example10() -> bool:
    """Display progress bar using tqdm.

    >>> example10()
    True
    """
    widgets = [
        "Processed: ",
        progressbar.Counter(),
        " lines (",
        progressbar.Timer(),
        ")",
    ]
    pbar = progressbar.ProgressBar(widgets=widgets)
    for _i in pbar(i for i in range(15)):
        sleep(0.2)
    return True


@example
def example11() -> bool:
    """Display progress bar using tqdm.

    >>> example11()
    True
    """
    widgets = [progressbar.FormatLabel("Processed: %(value)d lines (in: %(elapsed)s)")]
    pbar = progressbar.ProgressBar(widgets=widgets)
    for _i in pbar(i for i in range(15)):
        sleep(0.2)
    return True


@example
def example12() -> bool:
    """Display progress bar using tqdm.

    >>> example12()
    True
    """
    widgets = ["Balloon: ", progressbar.AnimatedMarker(markers=".oO@* ")]
    pbar = progressbar.ProgressBar(widgets=widgets)
    for _i in pbar(i for i in range(24)):
        sleep(0.1)
    return True


@example
def example13() -> bool:
    """Display progress bar using tqdm.

    >>> example13()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ["Arrows: ", progressbar.AnimatedMarker(markers="←↖↑↗→↘↓↙")]
        pbar = progressbar.ProgressBar(widgets=widgets)
        for _i in pbar(i for i in range(24)):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write("Unicode error: skipping example")
    return True


@example
def example14() -> bool:
    """Display progress bar using tqdm.

    >>> example14()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ["Arrows: ", progressbar.AnimatedMarker(markers="◢◣◤◥")]
        pbar = progressbar.ProgressBar(widgets=widgets)
        for _i in pbar(i for i in range(24)):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write("Unicode error: skipping example")
    return True


@example
def example15() -> bool:
    """Display progress bar using tqdm.

    >>> example15()
    True
    """
    # You may need python 3.x to see this correctly
    try:
        widgets = ["Wheels: ", progressbar.AnimatedMarker(markers="◐◓◑◒")]
        pbar = progressbar.ProgressBar(widgets=widgets)
        for _i in pbar(i for i in range(24)):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write("Unicode error: skipping example")
    return True


@example
def example16() -> bool:
    """Display progress bar using tqdm.

    >>> example16()
    True
    """
    widgets = [
        progressbar.FormatLabel("Bouncer: value %(value)d - "),
        progressbar.BouncingBar(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets)
    for _i in pbar(i for i in range(25)):
        sleep(0.2)
    return True


@example
def example17() -> bool:
    """Display progress bar using tqdm.

    >>> example17()
    True
    """
    widgets = [
        progressbar.FormatLabel("Animated Bouncer: value %(value)d - "),
        progressbar.BouncingBar(marker=progressbar.RotatingMarker()),
    ]

    pbar = progressbar.ProgressBar(widgets=widgets)
    for _i in pbar(i for i in range(25)):
        sleep(0.2)
    return True


# @example
# def with_example18():
#     """Display progress bar using tqdm."""
#     with progressbar.ProgressBar(max_value=10, term_width=20, left_justify=False) as \
#             progress:
#         assert progress._env_size() is not None
#         for i in range(10):
#             progress.update(i)


@example
def with_example19() -> bool:
    """Display progress bar using tqdm.

    >>> example19()
    True
    """
    with progressbar.ProgressBar(max_value=1) as progress, contextlib.suppress(ValueError):
        progress.update(2)
    return True


@example
def with_example20() -> bool:
    """Display progress bar using tqdm.

    >>> example20()
    True
    """
    progress = progressbar.ProgressBar(max_value=1)
    with contextlib.suppress(RuntimeError):
        progress.update(1)
    return True


@example
def with_example21a() -> bool:
    """Display progress bar using tqdm.

    >>> example21a()
    True
    """
    with progressbar.ProgressBar(max_value=1, redirect_stdout=True) as progress:
        progress.update(0)
    return True


@example
def with_example21b() -> bool:
    """Display progress bar using tqdm.

    >>> example21b()
    True
    """
    with progressbar.ProgressBar(max_value=1, redirect_stderr=True) as progress:
        progress.update(0)
    return True


@example
def with_example22() -> bool:
    """Display progress bar using tqdm.

    >>> example22()
    True
    """
    try:
        with progressbar.ProgressBar(max_value=-1) as progress:
            progress.start()
    except ValueError:
        pass
    return True


@example
def example23() -> bool:
    """Display progress bar using tqdm.

    >>> example23()
    True
    """
    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker())]
    with progressbar.ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)

    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker(), fill_left=False)]
    with progressbar.ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)
    return True


@example
def example24() -> bool:
    """Display progress bar using tqdm.

    >>> example24()
    True
    """
    pbar = progressbar.ProgressBar(
        widgets=[progressbar.Percentage(), progressbar.Bar()], max_value=10
    ).start()
    for _i in range(10):
        # do something
        sleep(0.1)
        pbar += 1
    pbar.finish()
    return True


@example
def example25() -> bool:
    """Display progress bar using tqdm.

    >>> example25()
    True
    """
    widgets = [
        "Test: ",
        progressbar.Percentage(),
        " ",
        progressbar.Bar(marker=progressbar.RotatingMarker()),
        " ",
        progressbar.ETA(),
        " ",
        progressbar.FileTransferSpeed(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=1000, redirect_stdout=True).start()
    for _i in range(100):
        # do something
        pbar += 10
    pbar.finish()
    return True


@example
def example26() -> bool:
    """Display progress bar using tqdm.

    >>> example26()
    True
    """
    widgets = [
        progressbar.Percentage(),
        " ",
        progressbar.Bar(),
        " ",
        progressbar.ETA(),
        " ",
        progressbar.AdaptiveETA(),
        " ",
        progressbar.AdaptiveTransferSpeed(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(500):
        sleep(0.01 + (i < 100) * 0.0001 + (i > 400) * 0.009)
        pbar.update(i + 1)
    pbar.finish()
    return True


@example
def example27() -> bool:
    """Display progress bar using tqdm.

    >>> example27()
    True
    """
    # Testing AdaptiveETA when the value doesn't actually change
    pbar = progressbar.ProgressBar(
        widgets=[progressbar.AdaptiveETA(), progressbar.AdaptiveTransferSpeed()],
        max_value=2,
        poll=0.0001,
    )
    pbar.start()
    pbar.update(1)
    sleep(0.01)
    pbar.update(1)
    pbar.finish()
    return True


@example
def example28() -> bool:
    """Display progress bar using tqdm.

    >>> example28()
    True
    """
    # Testing using progressbar as an iterator with a max value
    pbar = progressbar.ProgressBar()

    for _n in pbar(iter(range(100)), 100):
        # iter range is a way to get an iterator in both python 2 and 3
        pass
    return True


@example
def example29() -> bool:
    """Display progress bar using tqdm.

    >>> example29()
    True
    """
    widgets = [
        "Test: ",
        progressbar.Percentage(),
        " | ",
        progressbar.ETA(),
        " | ",
        progressbar.AbsoluteETA(),
    ]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=500).start()
    for i in range(500):
        sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()
    return True


def run() -> bool:
    """Display progress bar examples."""
    for example in examples:
        example()
    return True


def test() -> None:
    """Run tests."""
    assert run() is True


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.stdout("\nQuitting examples.\n")
