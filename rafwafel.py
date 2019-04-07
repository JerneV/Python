## Jerne Vingerhoets
# 7/04/2019
# Rafwafel is een Soyboy

import sys
legalChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "@"]

def checkEmail(mail):
    if(mail == "STOP"):
	    sys.exit() #Stopt het programma.
	#Eerst kijken we na of de mail enkel legale karakters bevat. 
    for x in mail:
        if x not in legalChars:
            print("Not valid, contains illegal characters")
            sys.exit()
	#Nu splitsen we de mail in de eerste twee delen: PREFIX en DOMEIN
	#PREFIX zou automatisch aan de voorwaarden moeten voldoen. Er zijn strengere voorwaarden voor DOMEIN. 
    prefix, domain = mail.split("@")
	
    #We kijken voorwaarden na voor DOMEIN
    try:
        dom1, dom2 = domain.split(".")
        if len(dom1) < 2 or len(dom2) < 2:
            print("Domain was too short.")
            sys.exit()
        else:
            print("%s was a valid mail!" % mail)
    
    except:
        print("No '.' found in domain")
        sys.exit()
	
	
if __name__ == '__main__':
	checkEmail(input("Geef mail, danku. "))

