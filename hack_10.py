"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    keys = []
    values = []
    newdl = []
    dict_item = {}

    i = 0
    k = 1
    while i < len(result):
        keys.append(str(k))
        values.append(str(k+1))
        i += 1
        k += 2

    for j in range(len(keys)):
        newdl.append({keys[j]: values[j]})

    result = newdl
    return result