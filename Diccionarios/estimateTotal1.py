def convert(s):
    result = 0
    for c in s:
        result += ord(c)
    return result

def estimateTotal1(d):
    result = {}
    elements = d.items()
    for item in elements:
        key = item[0]
        value = item[1]
        result[convert(key)] = convert(value)
    values = result.values()
    return sum(values)

print(estimateTotal1({"hola": "adeu", "hello": "bye"}))

# Devuelve el valor de los valores del diccionario en código Ascii