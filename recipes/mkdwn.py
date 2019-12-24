#!/bin/python3
"""
Conversion options for working with Markdown in Python.

Demonstrates the markdown module and the pypandoc module.
"""

import sys
from io import StringIO

import pypandoc
import pytest
from markdown import markdown, markdownFromFile

mdfile = "recipes/example.md"
htmlfile = "recipes/example.html"
samplemd = """# Heading 1
This is some text

## Heading 2
This is some more text.
This is an *emphasized* word.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

```
What about code blocks?
```
"""

samplehtml = """<h1>Heading 1</h1>
<p>This is some text</p>
<h2>Heading 2</h2>
<p>This is some more text.
This is an <em>emphasized</em> word.</p>
<table>
<thead>
<tr>
<th>Tables</th>
<th align="center">Are</th>
<th align="right">Cool</th>
</tr>
</thead>
<tbody>
<tr>
<td>col 3 is</td>
<td align="center">right-aligned</td>
<td align="right">$1600</td>
</tr>
<tr>
<td>col 2 is</td>
<td align="center">centered</td>
<td align="right">$12</td>
</tr>
<tr>
<td>zebra stripes</td>
<td align="center">are neat</td>
<td align="right">$1</td>
</tr>
</tbody>
</table>
<p><code>What about code blocks?</code></p>"""

samplerst = """Heading 1
=========

This is some text

Heading 2
---------

This is some more text. This is an *emphasized* word.

+---------------+---------------+-------+
| Tables        | Are           | Cool  |
+===============+===============+=======+
| col 3 is      | right-aligned | $1600 |
+---------------+---------------+-------+
| col 2 is      | centered      | $12   |
+---------------+---------------+-------+
| zebra stripes | are neat      | $1    |
+---------------+---------------+-------+

::

    What about code blocks?
"""


def mkdown(mdtext):
    """Convert MD to HTML using the markdown module and tables extension."""
    html = markdown(mdtext, extensions=["markdown.extensions.tables"])
    return html


def test_mkdown():
    """Test mkdown."""
    assert mkdown(samplemd) == samplehtml


def directmkdown(mdfile):
    """Convert MD file to HTML using markdown module and tables extension."""
    html = markdownFromFile(mdfile, extensions=["markdown.extensions.tables"])
    return html


@pytest.mark.xfail(raises=TypeError, reason="TypeError in markdownFromFile.")
def test_directmkdown():
    """Test directmkdown."""
    old_stdout = sys.stdout
    capturer = StringIO()
    sys.stdout = capturer
    # call functions
    directmkdown(mdfile)
    # end functions
    sys.stdout = old_stdout
    output = capturer.getvalue()
    assert output == samplehtml


def mkpandoc(mkstring):
    """Convert MD to RST using the pypandoc module."""
    output = pypandoc.convert_text(mkstring, "rst", format="md")
    return output


@pytest.mark.xfail(reason="Different pandoc versions locally and in CI.")
def test_mkpandoc():
    """Test pandoc."""
    assert mkpandoc(samplemd) == samplerst


def source(mdfile):
    """Open a file containing example MD text."""
    with open(mdfile, "r") as f:
        result = f.read()
    return result


def test_source():
    """Test source."""
    assert source(mdfile) == samplemd


def output(htmlfile, html):
    """Write html to file."""
    with open(htmlfile, "w") as f:
        f.write(html)
    return True


def test_output():
    """Test output."""
    assert output(htmlfile, "</p>") is True


if __name__ == "__main__":
    green = "\033[92m"
    end = "\033[0m"
    mdfile = "example.md"
    mdtext = source(mdfile)
    print("\n" + green + "Standard Markdown:" + end)
    print(mkdown(mdtext) + "\n")
    print(green + "Standard Markdown direct from file:" + end)
    print(directmkdown(mdfile))
    print(green + "MD converted to RST using pypandoc:" + end)
    print(mkpandoc(mdtext))
