"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    vowels = ["a", "e", "i", "o", "u"]
    altervowels = ["@", "3", "¡", "0", "v"]
    _str = []
    
    for index in range(len(result)):
        content = ""

        if result[index] in vowels:
            for vw in range(len(vowels)):
                if vowels[vw] == result[index]:
                    content = altervowels[vw]
        else:
            if index == 0:
                content = result[index].upper()
            elif index == len(result)-1:
                content = result[index].upper()
            else:
                content = result[index]
        
        _str.append(content)

    result = "".join(_str)
    return result

print(fn_hack_3("fooziman"))