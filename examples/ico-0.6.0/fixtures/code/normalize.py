def normalize(values):
    if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
        raise ValueError('list of strings required')
    return [v.strip() for v in values]
