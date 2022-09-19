import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(RED+"WELCOME TO THE REAL TRIVIA"+RESET)
puntaje=random.randint(15,30)
nombre=input(CYAN+"\nPlease tell us your name: \n")

print(CYAN+"\nIt's nice to have you here,",nombre +". We will test your intelligence. Don't get nervous, just have fun. To answer a question, write the letter next to the alternative you consider to be the one.\n")
print(YELLOW+"You are starting with",puntaje,"points.\n"
      "Wrong answer:     -1 point\n"
      "Correct answer:   +2 points\n"
      "Tricky answer:   +10 points\n"
      "Any other answer: -2 points\n")
comenzar=input("Are you ready to start? Yes or no?: ").lower()
if comenzar not in ("yes","Yes", "Si", "Sí", "y", "Y"):
  print("LOL! It doesn't matter, we will start anyways. kkkkkkk \n"+RESET)
else:  
  print("\nLet's start then! :)\n"+RESET)
#input("\nPress start to continue: ")
print(YELLOW+"We'll start in:")
for i in range (0,6,1):
  print(i)
  time.sleep(1)

iniciar=True
intentos=0
########################################################
########################################################
while iniciar==True:
  print(RED+"This is the",intentos,"th try")
  print(RESET+"\n1. In which country did the Carlist Wars take place during the 19th century?\n")
  lista1=("        a) France","        b) Spain|||","        c) Italy","        d) Germany")
  for alternativa in lista1:
    print(alternativa)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "abracadabra"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "abracadabra"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "b":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="abracadabra":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("a", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ########################################################
  time.sleep(2)
  print("2. Which war was fought between the Bristish houses of Lancaster and York for the throne of England?\n")	
  lista2=("        a) The Wars of the Roses|||","        b) The Medical war","        c) Star wars", "        d) WWII")
  for alternativa in lista2:
    print(alternativa)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "eres"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "eres"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "a":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="eres":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("b", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ######################################################## 
  time.sleep(2) 
  print("3. Which astronomer proposed the heliocentric theory in the 16th century?")
  print("""
        a) Nicolaus Copernicus|||
        b) Galileo Galilei
        c) Issac Newton
        d) Stephen Hawking
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "el"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "el"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "a":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="el":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("b", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ########################################################
  time.sleep(2)
  print("4. Which gas makes up more than 90% of Mars' atmosphere?")	
  print("""
        a) Nitrogen
        b) Oxigen
        c) Carbon oxide|||
        d) Carbon dioxide
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "mejor"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "mejor"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "c":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="mejor":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("a", "b", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ######################################################## 
  time.sleep(2) 
  print("5. In which city is Denmark's statue of The Little Mermaid located?")	
  print("""
        a) Copenhagen|||
        b) Vejle
        c) Odensen
        d) Toronto
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "regalo"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "regalo"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "a":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="regalo":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("b", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ########################################################
  time.sleep(2) 
  print("6. What is China's earliest known book of military strategy?")	
  print("""
        a) Sun Tzu's \'The Cards of Art\'
        b) Sun Tzu's \'The Art of Cards\'
        c) Sun Tzu's \'The Art of War\'|||
        d) Sun Tzu's \'The War of Art\'
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "que"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "que"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "d":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="que":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("a", "c", "b"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ######################################################## 
  time.sleep(2) 
  print("7. What is the conversion ratio of amperes (A) to milliamperes (mA)?")	
  print("""
        a) 1/1
        b) 1/10
        c) 1/100
        d) 1/1000|||
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "dios"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "dios"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "d":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="dios":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("a", "c", "b"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ########################################################
  time.sleep(2)  
  print("8. Who first implemented the Julian Calendar in Rome?")	
  print("""
        a) Julius Caesar|||
        b) Marcus Aurelius
        c) Maximus
        d) Lucius Verus
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "te"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "te"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again. \nNow you have",puntaje,"points\n\n"+RESET)
    
  if respuesta_1 == "a":
    puntaje+=2
    print(GREEN+"Nice! Now you have",puntaje,"points.\n\n"+RESET)
  elif respuesta_1=="te":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer. Now you have",puntaje,"points. Shhh!\n\n"+RESET)  
  elif respuesta_1 in ("b", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try. Now you have",puntaje,"points.\n\n"+RESET)
  ########################################################
  ######################################################## 
  time.sleep(2) 
  print("9. Which European country's king funded Christopher Columbus' famous expedition?")	
  print("""
        a) Portugal
        b) Spain|||
        c) Great Britain
        d) Turkey
        """)
  respuesta_1 = input(BLUE+"Your answer: ").lower()
  if respuesta_1 not in ("a", "b", "c", "d", "dio"):
    puntaje-=2
    print(RED+"Ups! You have to answer with: a, b, c or d lower-case. \nNow you have",puntaje,"points\n"+RESET)
    respuesta_1 = input(BLUE+"One more chance: ")
  if respuesta_1 not in ("a", "b", "c", "d", "dio"):
    puntaje-=2
    print(RED+"Sorry mate, wrong again.\n\n"+RESET)
    
  if respuesta_1 == "b":
    puntaje+=2
    print(GREEN+"Nice!\n\n"+RESET)
  elif respuesta_1=="dio":
    puntaje+=10
    print(YELLOW+"Easy tiger! You just activated the Wingardium Leviosa answer.\n\n"+RESET)  
  elif respuesta_1 in ("a", "c", "d"):
    puntaje-=1
    print(RED+"¡¡¡Mehh!!! Wrong, but nice try.\n\n"+RESET)
  
  time.sleep(2)
  print(YELLOW+"Now we are going to show you the final results in:")
  for i in range(10,0,-1):
    print(i)
    time.sleep(1)
  print(GREEN+"Congratulations",nombre+"!, you scored",puntaje,"points.\n"+RESET)
  
  repetir=input(RED+"Would you like to try the trivia again? Yes or no?: ").lower()
  if repetir not in ("yes","Yes", "Si", "Sí", "y", "Y"):
    intentos+=1
    iniciar=False
    print(YELLOW+"We hope you had fun. Take care",nombre,"See you soon"+RESET)
  else:  
    print(YELLOW+"Let's start again then!!!"+RESET)