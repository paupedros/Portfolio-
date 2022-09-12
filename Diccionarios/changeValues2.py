def convert(s):
    result = ""
    for c in s:
        result += "(" + str(ord(c)) + ")"
    return result

def changeValues2(d):
    result = {}
    elements = d.items()
    for item in elements:
        key = item[0]
        value = item[1]
        result[key] = convert(value)
    return result

print(changeValues2({"hello": "bye"}))

# Transforma los valores por su equivalente en código Ascii