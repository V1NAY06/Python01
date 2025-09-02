letter = '''Dear <|Name|>,
 you are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Vinay").replace("<|Date|", "02 October 2032"))