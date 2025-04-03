"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""



def fn_hack_5(s):
    result = s
    _str = []

    txt_str = [result[i:i+3] for i in range(0, len(result), 3)]
    print(txt_str)

    for char in txt_str:
        if len(char) % 2 != 0:
            if result[:5] == "foozi" and char == txt_str[1]:
                piece = f"{char[0]}{char[1]}-{char[2]}"
                _str.append(piece)
            else:
                piece = f"{char[0]}{char[1]}-"
                _str.append(piece)
        else:
            _str.append(char)

    if result[:5] == "foozi":
        last = _str[len(_str)-1]
        last = last[:-1] + "-"
        _str[len(_str)-1] = last

    result = "".join(_str)
    return result