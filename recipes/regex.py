#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regex snippets."""

import re

# http and web links in text
TEXT = re.compile(r"(?:https?:|\/img\/)\S*\w/?")

# <a> and <img> links in HTML
HTML = re.compile(r"(?:<a href=\"|<img.*src=\")(\S*\w/?)\"")

text = """## A heading [example link](http://example.com)

Here is a [example link](https://docs.mongodb.com/manual/tutorial/getting-started/) and another [cool link](https://docs.mongodb.com/manual/core/schema-validation/)

Here is a [broken link](http://example.com/).

Here `is a [broken link](http://example.com/noanadsfadsfadsfasfads)`.

A jira link: [TSWRITING-577](https://jira.mongodb.org/browse/TSWRITING-577 "Sync test article")

![an image](/img/TSWRITING-921_1.png "an image")
![a missing image](/img/TSWRITING-921_2.png)

```
Here is a [example link](http://example.com/afadsfasdfads) in a code block.
Here is a [broken link](http://exampasdfasd3343333f.com) in a code block.
http://example.com
```"""  # noqa: E501

html = """<h2>A heading <a href="http://example.com">example link</a></h2>
<p>Here is a <a href="https://docs.mongodb.com/manual/tutorial/getting-started/">example link</a> and another <a href="https://docs.mongodb.com/manual/core/schema-validation/">cool link</a></p>
<p>Here is a <a href="http://example.com/">broken link</a>.</p>
<p>Here <code>is a [broken link](http://example.com/noanadsfadsfadsfasfads)</code>.</p>
<p>A jira link: <a href="https://jira.mongodb.org/browse/TSWRITING-577" title="Sync test article">TSWRITING-577</a></p>
<p><img alt="an image" src="/img/TSWRITING-921_1.png" title="an image" />
<img alt="a missing image" src="/img/TSWRITING-921_2.png" /></p>
<p><code>Here is a [example link](http://example.com/afadsfasdfads) in a code block.
Here is a [broken link](http://exampasdfasd3343333f.com) in a code block.
http://example.com</code></p>"""  # noqa: E501

textlinks = re.findall(TEXT, text)
htmllinks = re.findall(HTML, html)

print(textlinks)
print(htmllinks)
