#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/23/

import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r"<category>([^<]+)</category>")
TEMPFILE = os.path.join("/tmp", "feed")
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/tags.xml", TEMPFILE)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # for tag1, tag2 in itertools.combinations(tags, 2):
    #     if IDENTICAL > SequenceMatcher(None, tag1, tag2).ratio() > SIMILAR:
    #         yield (tag1, tag2)
    return [
        (tag1, tag2)
        for tag1, tag2 in itertools.combinations(tags, 2)
        if IDENTICAL > SequenceMatcher(None, tag1, tag2).ratio() > SIMILAR
    ]


if __name__ == "__main__":
    get_similarities()