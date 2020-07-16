def zipcode_to_feature(zipcode, lookup, feature):
    results = lookup.get(zipcode)
    if results is None:
        return None
    else:
        return results[feature]


def zipcode_to_state(zipcode, lookup):
    return zipcode_to_feature(zipcode, lookup, 'state')


def avg_price_by_zipcode(zipcode, lookup):
    return zipcode_to_feature(zipcode, lookup, 'avg_price')
