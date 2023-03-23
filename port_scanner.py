import os
import re
import art
import socket
from time import sleep

well_known_ports = {
    20: 'FTP (Data)',
    21: 'FTP (Control)',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    194: 'IRC',
    443: 'HTTPS',
    465: 'SMTPS',
    587: 'SMTP (Message Submission)',
    993: 'IMAPS',
    995: 'POP3S'
}

protocols = {
    1: 'tcp',
    2: 'udp'
}

def display_banner():
    print(f'\033[35m{art.text2art("Port Scanner")}\033[0m')
    sleep(1.5)

def is_well_known(port):
    return port in well_known_ports

os.system('cls' if os.name == 'nt' else 'clear')

display_banner()

host = input(f"\033[34m💻 Digite o host ou endereço IP que deseja escanear: \033[0m")
regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
while not re.match(regex, host):
    print(f"\033[91mEndereço IP inválido!\033[0m")
    sleep(1)
    host = input(f"\033[34m💻 Digite o host ou endereço IP que deseja escanear: \033[0m")
sleep(1)
start = input(f"\033[34m🏁 Digite a porta de início do intervalo \033[91m(ENTER para 0): \033[0m")
while not start.isdigit() and start != '':
    print(f"\033[91mPorta inválida!\033[0m")
    sleep(1)
    start = input(f"\033[34m🏁 Digite a porta de início do intervalo \033[91m(ENTER para 0): \033[0m")
sleep(1)
end = input(f"\033[34m🔚 Digite a porta final do intervalo \033[91m(ENTER para 0)ENTER para 65536): \033[0m")
while not end.isdigit() and end != '':
    print(f"\033[91mPorta inválida!\033[0m")
    sleep(1)
    start = input(f"\033[34m🏁 Digite a porta de início do intervalo \033[91m(ENTER para 0): \033[0m")
print("\n")
sleep(1)

if start == '':
    start = 0
else:
    start = int(start)

if end == '':
    end = 65536
else:
    end = int(end)

print(f"\033[33mPORT | SERVICE | WELL-KNOWN PORT SERVICE\033[0m")
print("\n")

for porta in range(start, end+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.001)
    try:
        s.connect((host, porta))
        servico = socket.getservbyport(porta)
        if is_well_known(porta):
            print(f"\033[92m{porta}/{protocols[s.type]} is open | {servico} | {well_known_ports[porta]}\033[0m")
            sleep(0.5)
        else:
            print(f"\033[92m{porta}/{protocols[s.type]} is open | {servico}\033[0m")
            sleep(0.5)
        print(f"\033[31m----------------------------------------\033[0m")
    except:
        pass
    s.close()
