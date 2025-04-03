"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    _lst = []

    if len(result) > 1:
        for index in range(len(result)):
            if (index+1) % 2 != 0:
                _lst.append(str(index+1))
            else:
                _lst.append(index+1)
    else:
        _lst = result

    result = _lst
    return result
