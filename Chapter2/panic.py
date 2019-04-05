phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# ここにリストを追加するコードを追加。"on tap"に変更する
for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
