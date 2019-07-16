#!/bin/python3
"""Function for pretty printing JSON from string or dict."""

import json


def pp_json(json_thing, sort=True, indents=4):
    """Pretty print JSON."""
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None
