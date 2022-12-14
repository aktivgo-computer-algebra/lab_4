frequency_russian = {
    '_': 0.175, 'о': 0.090, 'е': 0.072, 'а': 0.062, 'и': 0.062, 'т': 0.053, 'н': 0.053, 'с': 0.045,
    'р': 0.040, 'в': 0.038, 'л': 0.035, 'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021,
    'я': 0.018, 'ы': 0.016, 'з': 0.016, 'ь': 0.014, 'ъ': 0.014, 'б': 0.014, 'г': 0.013, 'ч': 0.012, 'й': 0.010,
    'х': 0.009, 'ж': 0.007, 'ю': 0.006, 'ш': 0.006, 'ц': 0.004, 'щ': 0.003, 'э': 0.003, 'ф': 0.002,
}


def get_word_frequency(text: str) -> dict:
    result = {}

    for key in frequency_russian.keys():
        result[key] = 0

    length = len(text)

    print(length)

    for s in text:
        result[s] = result[s] + 1

    for key in result.keys():
        result[key] = round(float(result[key]) / float(length), 3)

    return result


if __name__ == '__main__':
    text = input("input text: ").lower()

    print(get_word_frequency(text))
