"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    result.popitem()
    res_keys = result.keys()
    res_vals = result.values()
    newdict = {}

    # Uppercase the first letter of all keys and values, and delete "k" in values
    res_keys_upper = [i.capitalize() for i in res_keys]
    res_vals_upper = [(i.capitalize()).replace("k", "") for i in res_vals]
    print(res_keys_upper)
    print(res_vals_upper)

    for key in range(len(res_keys_upper)):
        newdict[res_keys_upper[key]] = res_vals_upper[key]

    result = newdict
    return result