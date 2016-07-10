def parse_fragment(fragment_string):
    """Takes a fragment string nd returns a dict of the components"""
    fragment_string = fragment_string.lstrip('#')

    try:
        return dict(
            key_value_string.split('=')
            for key_value_string in fragment_string.split('&')
        )
    except ValueError:
        raise ValueError(
            'Invalid fragment string {fragment_string}'.format(
                fragment_string=fragment_string
            )
        )
