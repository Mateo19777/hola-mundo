meme_dict = {"XD":  "una expresion para cuando algo da risa",
             "CRINGE": "algo que es raro",
             "BASADO": "alguien que hizo algo bueno"}

            
word = input("Escribe una palabra nueva que no entiendas").upper()


if word in meme_dict.keys():
 print(meme_dict[word])
else:
 print("esta palabra no esta")
