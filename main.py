import random
from colorama import Fore
import numpy
import json

def genMultipliers(numRange, numFactors):
    multipliers = []

    counter = 0
    while len(multipliers) < 10:
        # Slumpar fram faktorer för varje multiplikation
        factors = 2 if len(numFactors) == 1 else random.randint(numFactors[0], numFactors[1])
        newMults = [random.randint(*numRange) for i in range(0, factors)]  

        is_unique = True
        # Sorterar genom alla redan tillagda multipliers och checkar om det är unikt
        for mult in multipliers:
            if sorted(newMults) == sorted(mult):
                is_unique = False
                counter += 1
                break
        # Om det är unikt, läggs den till i multipliers arrayen
        if is_unique:
            multipliers.append(newMults)
            counter = 0
        
        # Om counter blir 10 finns det inte tillräckligt mycket variation för att få tillräckligt många unika sets av faktorer
        if counter == 10: return False

    return multipliers

def questioning(multipliers):
    wrongAnswers = []

    for mult in multipliers:
        while True:
            # Hämtar fram spanska fraser
            with open("./spanishPhrases.json", "r") as f:
                phrases = json.load(f)
                # Slumpar fram en fras
                currentPhrase = phrases[random.randint(0, len(phrases) - 1)]

            while True:
                try:
                    # Ber användaren om ett svar för multiplikationen, lägger till x mellan talen om inte sista faktorn
                    newLine = ""
                    userInput = input(f"{newLine.join(f"{m}{" x " if i != len(mult) - 1 else ""}" for i, m in enumerate(mult))} = ")
                    
                    if userInput == "help":
                        break

                    # Checkar så det är ett tal
                    if int(userInput) % 1 == 0:
                        userInput = int(userInput)
                        break
                except Exception as e:

                    print(Fore.RED, "Me no stupido", Fore.RESET)

            answer = numpy.prod((mult))

            if userInput == answer:
                print(f"{Fore.GREEN}{currentPhrase.get("spanish")}{Fore.RESET} (write 'help' to get translation)")
                break
            elif userInput == "help":
                print(currentPhrase.get("english"))
            else:
                print(f"{Fore.RED}NO TENGO SI SEÑOR VERY VERY BAD{Fore.RESET}")
                wrongAnswers.append(mult)
                break

    # Om man svarat fel på någon hanterar vi nedan svar på frågan om dem vill försöka igen
    if len(wrongAnswers) > 0:
        print(f"{Fore.YELLOW}Sho bre säg wallah om vill du försöka igen yani {Fore.RESET}")

        while True:
            userInput = input(f"{Fore.YELLOW}wallah/nej: {Fore.RESET}")

            if userInput == "wallah":
                questioning(wrongAnswers)
                break
            elif userInput == "nej":
                print(f"{Fore.YELLOW}nejhopp{Fore.RESET}")
                break
            elif userInput == "help":
                print(currentPhrase.get("english"))
            else:
                print(f"{Fore.YELLOW}YALLA BRAM JAG KOMMER SKICKA MINA GRABBAR PÅ DIG OM DU TESTAR DET DÄR EN GÅNG TILL{Fore.RESET}")
    elif len(wrongAnswers) == 0:
        print(f"{Fore.GREEN}\n\nTack för idag bre{Fore.RESET}")
        
def main(difficulty):
    # Konfigurerar värdena baserat på den valda svårhetsgraden
    match difficulty:
        case 1:
            numRange = [1, 5]
            numFactors = [2]
        case 2:
            numRange = [1, 10]
            numFactors = [2, 3]
        case 3:
            numRange = [1, 20]
            numFactors = [2]
        case "egna":
            while True:
                # Hämtar värdena från användaren
                numRange = [int(input("Minsta faktorn: ")), int(input("Största faktorn: "))]
                numFactors = [2, int(input("Ange max antal faktorer: "))]

                # Sorterar dem
                if numRange[0] > numRange[1]: 
                    numRange[0], numRange[1] = numRange[1], numRange[0]

                if genMultipliers(numRange, numFactors) == False: 
                    print("De givna talen gav inte en tillräcklig unika multiplikationer")
                else: break
        case _:
            print("Värdet är inte ett giltigt svårighetsgrad")

    # print("Generear faktorer")
    multipliers = genMultipliers(numRange, numFactors)
    if multipliers == False: "very weird try again please"
    # print(f"Faktorerna är: {multipliers}")
    # print(f"Faktorerna är: {multipliers}")
    questioning(multipliers)


def init():
    # Konfiguera programmet
    difficulty = input("Välj en svårhetsgrad mellan 1-3, om du vill göra en custom skriv 'egna': ")
    
    # Checkar så input är ett tal
    try:
        difficulty = int(difficulty) 
    except Exception as e:
        pass
    main(difficulty)

if __name__ == "__main__":
    init()