#Imports:
from pyfiglet import figlet_format



#Func de apoio:
def println(str_):
    print(str_, "\n")

def separador():
    print("═" * 53 + "\n")

def pause():
    input("\nPressione Enter para voltar ao menu...")

#Main func:
def main():
        separador()
        print(figlet_format("OrbitGuard"))

        while True:
          separador()
          print("""
          [1] About this system
          [2] Troop Movement tracker
          [3] Air raid alert monitor
          [4] Safe route calculator
          [5] Refugee resource locator
          [0] Exit
          """ + "\n")

          usr_choice = input("Insert choice: ")
          match usr_choice:
               case "1":
                    println("case 1")
               case "2":
                    println("case 2")
               case "3":
                    println("case 3")
               case "4":
                    println("case 4")
               case "5":
                    println("case 5")
               case "0":
                    break
               case _:
                    println("Wrong input type.")
                

if __name__=="__main__":
    main()