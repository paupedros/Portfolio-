def convert(s):
    result = 0
    for c in s:
        result += ord(c)
    return result

def estimateTotal2(d):
    result = {}
    elements = d.items()
    for item in elements:
        key = item[0]
        value = item[1]
        result[convert(key)] = convert(value)
    values = result.values()
    keys = result.keys()
    return sum(result.keys())

print(estimateTotal2({"hola": "adeu", "hello": "bye"}))

# Devuelve el valor de las claves del diccionario en código Ascii