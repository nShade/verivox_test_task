from deepdiff import DeepDiff


def assert_json(template, json, message: str, ignore_order=False):
    """
    Advanced assertion for JSON objects. Assertion fail message improved in comparison with default pytest one.

    :param template: expected JSON value
    :param json: actual JSON value
    :param str message: Assertion fail message
    """
    diff = DeepDiff(template, json, ignore_order=ignore_order)

    if diff == {}:
        return

    result = ["Comparing JSON to a template:"]
    dict_keys_added = diff.get('dictionary_item_added', None)

    if dict_keys_added:
        result.append("    Keys are found in the JSON, but are not expected:")

        for item in dict_keys_added:
            result.append(f'        {item}')

    dict_keys_removed = diff.get('dictionary_item_removed', None)

    if dict_keys_removed:
        result.append("    Keys are expected in the JSON, but not found:")

        for item in dict_keys_removed:
            result.append(f'        {item}')

    list_items_added = diff.get('iterable_item_added', None)

    if list_items_added:
        result.append("    Values found in the JSON lists, but are not expected:")

        for item, value in list_items_added.items():
            result.append(f'        {item}: {value}')

    list_items_removed = diff.get('iterable_item_removed', None)

    if list_items_removed:
        result.append("Values not found in the JSON lists, but are expected:")

        for item, value in list_items_removed.items():
            result.append(f'        {item}: {value}')

    values_changed = diff.get('values_changed', None)

    if values_changed:
        result.append("    Values not as expected:")

        for item, values in values_changed.items():
            result.append(f'        {item} expected: {values["new_value"]} actual: {values["old_value"]}')

    raise AssertionError(message + '\n\n' + '\n'.join(result))
