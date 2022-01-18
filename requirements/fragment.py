import re
from typing import cast, Dict, List, Optional, Tuple

# Copied from pip
# https://github.com/pypa/pip/blob/281eb61b09d87765d7c2b92f6982b3fe76ccb0af/pip/index.py#L947
HASH_ALGORITHMS = set(['sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'])

extras_require_search = re.compile(r'(?P<name>.+)\[(?P<extras>[^\]]+)\]')


def parse_fragment(fragment_string: str) -> Dict[str, str]:
    """Takes a fragment string nd returns a dict of the components"""
    fragment_string = fragment_string.lstrip('#')

    try:
        return dict(cast(Tuple[str, str], tuple(key_value_string.split('='))) for key_value_string in
                    fragment_string.split('&'))
    except ValueError:
        raise ValueError(f'Invalid fragment string {fragment_string}')


def get_hash_info(d: Dict[str, str]) -> Tuple[Optional[str], Optional[str]]:
    """Returns the first matching hashlib name and value from a dict"""
    for key in d.keys():
        if key.lower() in HASH_ALGORITHMS:
            return key, d[key]

    return None, None


def parse_extras_require(egg: Optional[str]) -> Tuple[Optional[str], List[str]]:
    if egg is not None:
        match = extras_require_search.search(egg)
        if match is not None:
            name = match.group('name')
            extras = match.group('extras')
            return name, [extra.strip() for extra in extras.split(',')]
    return egg, []
