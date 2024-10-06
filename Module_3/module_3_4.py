def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []

    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Кино', 'Кинематограф', 'Фильм', 'Книга', 'Кинокритик')
result4 = single_root_words('фаза', 'Фазан', 'Синхрофазатрон', 'Ноль', 'фасон')
print(result1)
print(result2)
print(result3)
print(result4)

