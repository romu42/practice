# https://codechalleng.es/bites/4/

import os
import re
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    words = re.findall(r'<category>(\w+)</category>', content)
    return Counter(words).most_common(n)


if __name__ == '__main__':
    get_pybites_top_tags()