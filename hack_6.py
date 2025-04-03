"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    _lst = []

    if len(result) > 0:
        for index in range(len(result)):
            if (index+1) % 2 != 0:
                _lst.append(str(index+1))
            else:
                _lst.append("-")
    else:
        _lst.append("0")

    result = _lst
    return result
