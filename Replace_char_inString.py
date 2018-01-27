
#Method 1

text = 'abcdefg'
new = list(text)
new[6] = 'W'
''.join(new)

#Method 2
text = "naveen"
# Below line will replace teh char at index-1 with 'W'
text[:1] + 'W' + text[2:]
