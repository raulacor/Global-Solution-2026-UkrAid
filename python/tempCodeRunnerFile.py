from pyfiglet import figlet_format



#Func de apoio:
def println(str_):
    print(str_, "\n")

def separador():
    print("═" * 60 + "\n")

def pause():
    input("\nPressione Enter para voltar ao menu...")


def main():
    separador()
    print(figlet_format("OrbitGuard"))
    separador()

if __name__=="__main__":
    main()