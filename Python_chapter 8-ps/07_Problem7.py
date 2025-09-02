def rem(lst, word):
    n = []
    for item in lst:
        if item != word:                     # skip exact matches
            n.append(item.replace(word, "")) # remove substring "word"
    return n

names = ['caks', 'Jnni', 'Tuan', 'Aditi', 'Kajal']

print(rem(names, "an"))
