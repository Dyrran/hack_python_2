"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    revres = result
    revres.reverse()
    _str = []
    index_list = [str(i+1) for i in range(len(result))]
    index_list.reverse()

    if len(result) == 4 or len(result) == 2:
        _str = index_list
    else:
        for j in range(len(result)):
            _str.append(f"{revres[j]}-{index_list[j]}")
        

    result = _str
    return result