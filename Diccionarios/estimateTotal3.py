def convert(s):
    result = 0
    for c in s:
        result += ord(c)
    return result

def estimateTotal3(d):
    result = {}
    elements = d.items()
    for item in elements:
        key = item[0]
        value = item[1]
        result[convert(key)] = convert(value)
    values = result.values()
    keys = result.keys()
    return sum((result.values() + result.keys()))

print(estimateTotal3({"hola": "adeu", "hello": "bye"}))

# Devuelve el valor total del diccionario en código Ascii