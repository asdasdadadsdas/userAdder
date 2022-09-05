from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Modüller Yükleniyor...{n}')
    os.system('pip install requests')

def banner():
    import random
    # logo
    b = [
    

  ' ██████╗ ██████╗  ██████╗ ',
  ' ██╔══██╗██╔══██╗██╔═══██╗ ',
  ' ██████╔╝██████╔╝██║   ██║',
  ' ██╔═══╝ ██╔══██╗██║   ██║',
  ' ██║     ██║  ██║╚██████╔╝',
  ' ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('============= CODED BY CANPOLATGKKY ==============')
    print(f'   Versiyon: 31.0 | KODLAYAN: CANPOLAT GÖKKAYA{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni Hesap Ekle'+n)
    print(lg+'[2] Tüm Yasaklı Hesapları Filtrele'+n)
    print(lg+'[3] Belirli hesapları sil'+n)
    print(lg+'[4] Çıkış'+n)
    a = int(input('\nSeçimini gir: '))
    if a == 1:
        new_accs = []
        with open('hesaplar.txt', 'ab') as g:
            number_to_add = int(input(f'\n{gr} [~] Eklenecek hesap sayısını girin: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{ye} [~] Telefon Numarasını Girin: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{cy} [i] Tüm hesaplar şuraya kayıt edildi: hesaplar.txt')
            clr()
            print(f'\n{gr} [*] Yeni Hesaplardan Oturum Açılıyor..\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                c.start(number)
                print(f'{ye}[+] Giriş Başarılı :)')
                c.disconnect()
            input(f'\n Ana menüye gitmek için enter bas...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesap Yok! Lütfen Hesap Ekleyin Ve Tekrar Deneyin')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Kodu Girin: '))
                        print(f'{lg}[+] {phone} Yasaklı Değil{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Yasaklı !!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Tebrikler! Yasaklanmış hesap yok')
                input('\nAna menüye gitmek için enter bas...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('hesaplar.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Engellenen tüm hesaplar kaldırıldı'+n)
                input('\nAna menüye gitmek için enter bas...')

    elif a == 3:
        accs = []
        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{ye}[i] Silmek için bir hesap seçin\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Bir Seçim Girin: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('hesaplar.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesap Silindi :({n}')
        input(f'\nAna menüye gitmek için enter bas...')
        f.close()
    elif a == 4:
        clr()
        banner()
        exit()