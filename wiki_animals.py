import wikipediaapi


def get_animals_count(all_animals, letter):
        animals = []
        for c in all_animals.values():
            if c.title[:1] == letter:
                animals.append(c.title)
        return len(animals)        


if __name__ == "__main__":
    wiki = wikipediaapi.Wikipedia('ru')
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    cat = wiki.page("Категория:Животные_по_алфавиту")
    all_animals = cat.categorymembers
    animals_count = {}
    for letter in alphabet:
        animals_count[letter] = get_animals_count(all_animals, letter)
    print(animals_count)