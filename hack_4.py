"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    lastpos = (len(result)-1)
        
    if len(result) > 3:
        result = result[1:lastpos]

    return result
