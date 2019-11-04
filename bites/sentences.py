import re

def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""

    matched = re.sub('([\.|\?|\!]\s)(\w+)', title_match, text.capitalize())
    return matched

def title_match(matchobj):
    return matchobj[0].title()