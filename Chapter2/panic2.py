phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# リストスライスを使ってphraseから"on tap"を取り出す
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
