dict = {}
with open('ass2.txt', encoding='utf-8') as t:
    txt = t.read()
for symbol in txt:
    count = txt.count(symbol)
    if count >= 1:
        dict[symbol] = round(count/len(txt), 4)
print(txt)
for key, value in sorted(dict.items()):
    print(key, ' - ', value)
