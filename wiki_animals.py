import wikipediaapi


def get_animals_count(all_animals, letter):
        animals = []
        for animal in all_animals.values():
            if animal.title[:1] == letter:
                animals.append(animal.title)
        return len(animals)        


if __name__ == "__main__":
    wiki = wikipediaapi.Wikipedia('ru')
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    cat = wiki.page("Категория:Животные_по_алфавиту")
    all_animals = cat.categorymembers
    animals_count = {}
    for letter in alphabet:
        animals_count[letter] = get_animals_count(all_animals, letter)
    for i in animals_count:
        print(i, animals_count[i])