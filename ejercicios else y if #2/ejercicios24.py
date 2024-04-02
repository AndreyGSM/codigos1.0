def es_vocal(letra):
    return letra.lower() in ['a', 'e', 'i', 'o', 'u']

letra = input('Introduce una letra por favor: ')
if es_vocal(letra):
    print('Es vocal!')
else:
    print('No es vocal!')
