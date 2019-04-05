# 2章 vowels3.pyを集合で扱うようにする

# vowels = ['a', 'e', 'i', 'o', 'u']
vowels = set('aeiou')
word = input("単語を入力してください。母音を探します。")

# 任意の文字列内の母音を特定する、という課題を1行のコードで解決する
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)

# intersectionは共通点を示す set関数は集合を作成する
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
