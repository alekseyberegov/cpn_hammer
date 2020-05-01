
def make_query_string(params):
    qs = []
    for k, v in params.items():
        qs.append(str(k) + '=' + str(v))
    return '&'.join(qs)


def make_url(base_url, *res, **params):
    url = base_url
    for r in res:
        url = '{}/{}'.format(url, r)
    if params:
        url = '{}?{}'.format(url, make_query_string(params))
    return url
