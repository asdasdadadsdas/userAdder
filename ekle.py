'''
============= CODERMAN =====================
BU YAZILIM CANPOLAT GÖKKAYA TARAFINDAN KODLANDI.
************************************************
'''

# kitaplıkları içe aktar
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
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
        print(f'{random.choice(colors)}{char}{rs}')
    #print('============= CODED BY CANPOLATGKKY ==============')
    print(f'{lg}   Versiyon: {w}31.0{lg} | Telegram: {w}androedit{rs}\n')


# ekranı temizleme işlevi
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('hesaplar.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# oturumlar oluşturma (varsa) ve yasaklanmış hesapları kontrol etme
# YAPILACAKLAR: Kod girişini kaldırma (sadece bir hesabın yasaklanıp yasaklanmadığını kontrol etmek için)
print('\n' + info + lg + ' Engellenen hesaplar kontrol ediliyor...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} kontrol ediliyor {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 8088717, '7d1e0295ee1c2628f1933e9ffd2d8b78')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('TAMAM')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}yasaklandı!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' Yasaklanan hesap kaldırıldı [ manager.py kullanarak kalıcı olarak kaldırın ]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Oturumlar oluşturuldu!')
clr()
banner()
# tarama ayrıntılarını günlüğe kaydetmek
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} oturum şurada saklanır{w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} Çıkmak İçin Enter Basın...')
    clr()
    banner()
    sys.exit()

# kullanıcı ayrıntılarını okuma
try:
    # eklemeye devam etme isteği
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} Üyeleri Buradan Bulmaya Devam Et: {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} Hedef Grup Genel/Özel Grup Bağlantısını Gir: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} Hedefin Genel/Özel Grup Bağlantısı: {r}')
    index = 0
# load all the accounts(phonenumbers)
accounts = []
f = open('hesaplar.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} Toplam hesaplar: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} Kullanılacak hesap sayısını girin: {r}'))
print(f'{info}{cy} Bir seçenek belirleyin{lg}')
print(f'{cy}[0]{lg} Herkese açık gruba ekle')
print(f'{cy}[1]{lg} Özel gruba ekle')
choice = int(input(f'{INPUT}{cy} Seçimi girin: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} Herkese Açık Grup Bağlantınızı Girin: {r}'))
else:
    target = str(input(f'{INPUT}{cy} Özel grup bağlantısını girin: {r}'))
print(f'{grey}_'*50)
#status_choice = str(input(f'{INPUT}{cy} Aktif üyeler eklemek istiyor musunuz?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('hesaplar.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Kaç Saniyede Bir Üye Eklemek İstiyorsun{w}[{lg}0 yok demektir.{w}]: {r}'))
#print(f'{info}{lg} gruba katılacak {w}{number_of_accs} hesaplar...')
#print(f'{grey}-'*50)
print(f'{success}{lg} ---- Başlıyor Kullanılan Hesap {w}{len(to_use)}{lg} (s) ----')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
    print(f'{plus}{grey} Kullanıcı: {cy}{acc[0]}{lg} -- {cy}Oturum başlatılıyor... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Taramak için gruba katıldı')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Taramak için gruba katıldı')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Eklemek için gruba katıldı')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Eklemek için gruba katıldı')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} Kullanıcı: {cy}{acc_name}{lg} -- Gruba katılamadı')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {cy}Kişiler Bulunuyor...')
    #c.get_dialogs()
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, limit = 5500)
    except Exception as e:
        print(f'{error}{r} Üyeler silinemedi')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} Eklenecek üye yok!')
        continue
    print(f'{info}{lg} Başlat: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} Çok fazla Flood Hatası! Oturum Kapatıldı...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Uyku 1 saniye')
            adding_status += 1
            print(f'{info}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Uyku {w}{sleep_time} {lg} Saniye(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Hata Kullanıcı Gizliliği Kısıtlı')
            continue
        except PeerFloodError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Flood Hatası.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} Gruba eklenemiyor. Üye eklemeyi etkinleştirmek için grup yöneticisiyle iletişime geçin')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Gruplarda yazma Kısıtlandı')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Eklemek için Sohbet Yöneticisi Olman Gerekli')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Kullanıcı zaten Eklendi')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} Kişi Hatası')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Ekleme Sonlandırılmıştır Telegram: androedit ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} Ekleme oturumu sona erdi. Telegram: androedit")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()