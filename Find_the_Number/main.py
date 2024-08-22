import random 
from ascii_art import get_ascii_art
import time

def main():
    ascii_art = get_ascii_art()
    print(ascii_art)

if __name__ == "__main__":
    main()

numero_secreto = random.randrange(1,101)
pontos = 1000
print("--------------> SELECIONE A DIFICULDADE: <----------------\n")
print("1- EASY         |20 Tentativas|")
print("2- MEDIUM       |10 Tentativas|")
print("3- HARD         |5  Tentativas|")
print(" ")
dif=int(input("Digite uma dificuldade: "))
print(" ")
tentativas = 0
match dif:#switch case do python
    case 1:
        tentativas = 20
    case 2:
        tentativas = 10
    case 3:
        tentativas = 5   

chute=int(input("-> Digite o chute: "))
while tentativas>0:
    
    print("Loading...")
    time.sleep(1)
    
    if chute > numero_secreto:
        print("\nEsse numero que você digitou é maior que o numero secreto.")
    elif chute < numero_secreto:
        print("\nEsse numero que você digitou é menor que o numero secreto.")
    else:
        break
    pontos -= abs(chute-numero_secreto)
    tentativas -= 1
    print(f" -> Total de pontos: {pontos}")
    print(f"\nRestam {tentativas} Tentativas")
    chute=int(input("-> Digite o chute novamente: "))

if tentativas==0:
   print("\nOPS... As tentativas acabaram, Você Perdeu! =( ")

if chute==numero_secreto:
    print("========================================")
    print("     ___________  ")
    print("   '._==_==_=_.' ")
    print("   .-\\:      /-. ")
    print("  | (|:.     |) |")
    print("   '-|:.     |-' ")
    print("     \\::.    /   ")
    print("      '::. .'    ")
    print("        ) (      ")
    print("      _.' '._    ")
    print("     `\"\"\"\"\"`")
    print(f"Acertou o numero correto era {numero_secreto}!")
    print(f"Você acumulou {pontos} pontos!")
    print("=========================================")