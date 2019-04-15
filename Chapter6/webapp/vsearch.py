def search4vowels(phrase: str) -> set:
    """phrase内の母音の集合を返す。"""
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """phrase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
