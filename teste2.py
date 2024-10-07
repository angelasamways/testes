def count_letter_a(s):
    count = s.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."


string = "Estou em busca de uma graaande oportunidade."


count_letter_a(string)

resultado = count_letter_a(string)
print(resultado)
