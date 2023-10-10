print("~~~~~ Bem-vindo(a) à Calculadora de IPs e Máscaras de Rede ~~~~~\n")

status = False

def solicitation():
    global entry
    print("Insira o IP e o CIDR da máscara no formato IP/CIDR a seguir '121.122.123.124/24'\n")
    entry = input("Insira seu IP: ").replace(" ","").replace(".","")

def InvalidIP():
    print("\nX ERRO | Formato de IP inválido (QUE NEM VOCÊ) X\n")
    solicitation()

def tratamento():
    global ip
    global cidr
    global status
    status = False

    try:
        ip, cidr = entry.split("/")
    except ValueError:
        try:
            ip, cidr = entry.split("\\")
        except ValueError:
            try:
                ip, cidr = entry.split("|")
            except ValueError:
                InvalidIP()
    else:
        status = True

    #if ip.__len__ < 12:
    #    InvalidIP()

def MaskCalc():
    mask = "1" * cidr + "0" * (32 - cidr)
    oct1 = mask[:8]
    oct2 = mask[8:16]
    oct3 = mask[16:24]
    oct4 = mask[24:]

#def NetCalc():

while(status == False):
    solicitation()
    tratamento()