print("~~~~~ Bem-vindo(a) à Calculadora de IPs e Máscaras de Rede ~~~~~\n")

#status = False

def Solicitation():
    global entry
    global error_message

    print("Insira o IP e o CIDR da máscara no formato IP/CIDR a seguir '121.122.123.124/24'\n")
    entry = input("> Insira IP e CIDR: ")\
        .replace(" ","").replace(".","").replace("\\","/").replace("|","/")
    
    if "/" not in entry:
        error_message = "'/' não encontrada"
        InvalidIP()
    
    Treating()

def InvalidIP():
    global error_message

    print(f"\nX  ERRO | Formato de IP ou CIDR inválido ({error_message}) X\n")
    Solicitation()

def Treating():
    #global status
    global ip
    global cidr
    global entry
    global error_message

    ip, cidr = entry.split("/")

    try:
        cidr = int(cidr)
    except ValueError:
        error_message = "CIDR não é um valor numérico"
        InvalidIP()

    if cidr > 30:
        error_message = "CIDR excede o valor máximo de 30"
        InvalidIP()

    if len(ip) != 12:
        error_message = "IP deve ter exatos 12 números"
        InvalidIP()
    
    print(f"\nSeu IP é: {ip}")
    print(f"Seu CIDR é: {cidr}")
    
    x = input("\nDigite Enter")

    #status = True

    MaskCalc()

def MaskCalc():
    mask = "1" * cidr + "0" * (32 - cidr)
    mask_oct1 = '0b' + mask[:8]
    mask_oct2 = '0b' + mask[8:16]
    mask_oct3 = '0b' + mask[16:24]
    mask_oct4 = '0b' + mask[24:]

    print("\nMáscara Calculada!")
    x = input("\nDigite Enter")

#def NetCalc():

#while(status == False):
Solicitation()

#MaskCalc()