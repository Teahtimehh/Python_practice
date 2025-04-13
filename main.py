import re


def analyze_text(text):
    text = text.lower()

    words = re.findall(r'\b\w+\b', text)

    word_count = len(words)

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    longest_word = max(words, key=len)

    vowels = 'аеёиоуыэюя'
    vowel_count = sum(word.count(vowel) for word in words for vowel in vowels)

    return {
        'word_count': word_count,
        'longest_word': longest_word,
        'vowel_count': vowel_count,
        'word_frequency': word_frequency
    }


if __name__ == "__main__":
    user_input = input("Введите текст для анализа: ")
    result = analyze_text(user_input)

    print(f'Количество слов: {result["word_count"]}')
    print(f'Самое длинное слово: {result["longest_word"]}')
    print(f'Количество гласных букв: {result["vowel_count"]}')
    print('Частота встречаемости слов:')
    for word, frequency in result['word_frequency'].items():
        print(f'{word}: {frequency}')