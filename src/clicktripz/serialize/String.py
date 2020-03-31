

def String(value, encoding='utf-8', errors='ignore'):
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode(encoding=encoding, errors=errors)
    return str(value)
