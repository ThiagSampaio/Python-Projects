
with open(f"Cartas_txt/CT AC.txt", encoding="utf8") as file:
    corpo_message = file.readlines()
    corpo_message_txt = "".join(corpo_message)
print (corpo_message_txt)

'''
import io
f= io.open("Cartas_txt/CT AC.txt", "r", encoding="utf8")
print (type(f))
'''
