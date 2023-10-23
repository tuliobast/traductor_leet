"""
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

texto = input("Introduce el texto que quieras traducir a lengueje 'leet'/'1337': ").lower()

def traductor(text):
   
    abc = {"a":"4","b":"8","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":"_|","k":">|","l":"7","m":"JVI","n":"^/","o":"0","p":"|*","q":"9","r":"|2","s":"5","t":"7","u":"(_)","v":"|/","w":"'//","x":"><","y":"`/","z":"2"}
    traduccion=""

    for i in range(len(text)):
        if text[i] in abc.keys():
            letra=text[i]
            text2=letra.replace(letra, abc[letra])
            traduccion+=text2
        else:
            traduccion+=text[i]
    return traduccion
 
print(traductor(texto))

