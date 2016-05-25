#!/bin/python3
"""
Conversion options for working with Markdown in Python.

Demonstrates the markdown module, a GitHub flavoured Python port,
and the pypandoc module.
"""

import re

import pypandoc
from markdown import markdown, markdownFromFile

try:
    from hashlib import md5 as md5_func
except ImportError:
    from md5 import new as md5_func


def mkdown(mdtext):
    """Convert MD to HTML using the markdown module and tables extension."""
    html = markdown(mdtext, extensions=['markdown.extensions.tables'])
    return html


def directmkdown(mdfile):
    """Convert MD file to HTML using markdown module and tables extension."""
    html = markdownFromFile(mdfile, extensions=['markdown.extensions.tables'])
    return html


def gfmkdown(mkstring):
    """
    Convert MD to HTML using the markdown module and tables extension.

    Preprocesses the markdown string to include some GitHub flavouring.
    """
    htmltext = markdown(gfm(mkstring),
                        extensions=['markdown.extensions.tables'])
    return htmltext


def pandoc(mkstring):
    """Convert MD to RST using the pypandoc module."""
    output = pypandoc.convert(mkstring, 'rst', format='md')
    return output


def source(mdfile):
    """Open a file containing example MD text."""
    with open(mdfile, 'r') as f:
        result = f.read()
    return result


def output(htmlfile, html):
    """Write html to file."""
    with open(htmlfile, 'w') as f:
        f.write(html)
    return True


def gfm(text):
    """
    Github flavoured markdown.

    Ported from http://github.github.com/github-flavored-markdown/

    Usage:

        html_text = markdown(gfm(markdown_text))

    (ie, this filter should be run on the markdown-formatted string BEFORE the
    markdown filter itself.)
    """
    # Extract pre blocks
    extractions = {}

    def pre_extraction_callback(matchobj):
        hash = md5_func(matchobj.group(0)).hexdigest()
        extractions[hash] = matchobj.group(0)
        return "{gfm-extraction-%s}" % hash
    pre_extraction_regex = re.compile(
        r'{gfm-extraction-338ad5080d68c18b4dbaf41f5e3e3e08}',
        re.MULTILINE | re.DOTALL)
    text = re.sub(pre_extraction_regex, pre_extraction_callback, text)

    # prevent foo_bar_baz from ending up with an italic word in the middle
    def italic_callback(matchobj):
        if len(re.sub(r'[^_]', '', matchobj.group(1))) > 1:
            return matchobj.group(1).replace('_', '\_')
        else:
            return matchobj.group(1)
    text = re.sub(r'(^(?! {4}|\t)\w+_\w+_\w[\w_]*)', italic_callback, text)

    # in very clear cases, let newlines become <br /> tags
    def newline_callback(matchobj):
        if len(matchobj.group(1)) == 1:
            return matchobj.group(0).rstrip() + '  \n'
        else:
            return matchobj.group(0)
    text = re.sub(r'^[\w\<][^\n]*(\n+)', newline_callback, text)

    # Insert pre block extractions
    def pre_insert_callback(matchobj):
        return extractions[matchobj.group(1)]
    text = re.sub(r'{gfm-extraction-([0-9a-f]{40})\}',
                  pre_insert_callback, text)

    return text

if __name__ == '__main__':
    green = '\033[92m'
    end = '\033[0m'
    mdfile = "example.md"
    mdtext = source(mdfile)
    print("\n" + green + "Standard Markdown:" + end)
    print(mkdown(mdtext) + "\n")
    print(green + "Standard Markdown direct from file:" + end)
    print(directmkdown(mdfile))
    print("\n" + green + "GitHub flavoured Markdown:" + end)
    print(gfmkdown(mdtext) + "\n")
    print(green + "MD converted to RST using pypandoc:" + end)
    print(pandoc(mdtext))
