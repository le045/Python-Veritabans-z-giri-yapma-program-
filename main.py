import time
from colorama import Fore, Back, Style, init
init(autoreset=True)



print(Fore.LIGHTBLUE_EX + """
 | |                                                      | |           | |
 | |     ___  ___    _   _ ___  ___ _ __    ___ ___  _ __ | |_ _ __ ___ | |
 | |    / _ \/ _ \  | | | / __|/ _ \ '__|  / __/ _ \| '_ \| __| '__/ _ \| |
 | |___|  __/ (_) | | |_| \__ \  __/ |    | (_| (_) | | | | |_| | | (_) | |
 |______\___|\___/   \__,_|___/\___|_|     \___\___/|_| |_|\__|_|  \___/|_|
""")


tr_ch = "şüğöçıİ"

time.sleep(1)

def quitprogress():
    print(Fore.BLUE + "[+]Programdan çıkış yapılıyor....")
    time.sleep(1)
    quit()
    return

while True:
    print(Fore.LIGHTCYAN_EX + "[+] Programa Daha Önce giriş yapmadığınız görülüyor...")
    user_cont = str(input(Fore.BLUE + "[*]Yeni hesap oluşturmak istiyorsanız [Y]\n[*]Çıkış yapma istiyorsanız[Q]\n[?]İşleminiz :  "))
    time.sleep(1)
    if user_cont.lower() == "q":
        quitprogress()
    elif user_cont.lower() == "y":
        new_user_id = str(input(Fore.BLUE + "[+]Yeni Kullanıcı Adınızı Giriniz..... : "))
        for kontrol in tr_ch:
            if kontrol in new_user_id:
                print(Fore.LIGHTRED_EX + "[!]Kullanıcı Adında Türkçe Karakter kullanılamaz..")
                break
            else:
                print(Fore.BLUE + "[+] Yeni Şifrenizi Belirleyin: ",end="")
                new_user_pass = int(input())
                print(Fore.BLUE + "[+] Yeni Şifrenizi Tekrar Yazın: ",end="")
                new_user_pass_control = int(input())
                if new_user_pass != new_user_pass_control:
                    print(Fore.LIGHTRED_EX + "[!] Hata. Şifreleriniz aynı değil....")
                    break
                else:
                    print(Fore.LIGHTGREEN_EX + "[+] Hesabınız Oluşturuldu...")

                    user_pass = new_user_pass
                    user_id = new_user_id
                    while True:

                        open_cont = str(input(Fore.BLUE + "[?]Programa Giriş Yapmak İstiyor musunuz ? E/H: "))
                        if open_cont.lower() == "e":
                            print(Fore.CYAN + "[+] Giriş Ekranına Yönlendiriliyorsunuz.....")
                            time.sleep(2)
                            print(Fore.BLUE + "[+]Kullanıcı adınızı giriniz : ",end="")
                            user_id2 = str(input())
                            print(Fore.BLUE + "[+]Şifrenizi giriniz : ",end="")
                            user_pass2 = int(input())
                            if user_id2 != user_id and user_pass2 != user_pass:
                                print(Fore.LIGHTRED_EX + "[!]Şifre Ve Kullanıcı Adı Yanlış.")
                                time.sleep(1)
                                continue
                            elif user_id2 == user_id and user_pass2 != new_user_pass:
                                print(Fore.LIGHTRED_EX + "[!]Şifre Yanlış.")
                                time.sleep(1)
                                continue
                            elif user_pass2 == user_pass and user_id2 != user_id:
                                print(Fore.LIGHTRED_EX + "[!]Kullanıcı Adı Yanlış.")
                                time.sleep(1)
                                continue
                            elif user_pass2 == user_pass and user_id2 == user_id:
                                print(Fore.LIGHTGREEN_EX + "[+]Giriş Sağlandı Programa Yönlendiriliyorsunuz....")
                                time.sleep(1)
                                print(Fore.LIGHTCYAN_EX + "[+]Kullanıcı Adınız: {}\n[+]Şifreniz: {}".format(user_id,user_pass))
                                time.sleep(1)
                                print(Fore.LIGHTBLACK_EX + """
                                Leo | 
                                """)
                                time.sleep(60)
                                break

                        elif open_cont.lower() == "h":
                            print(Fore.CYAN + "[+]Program Kapatılıyor..")
                            quitprogress()
                        else:
                            print(Fore.LIGHTCYAN_EX + "Lütfen size tanımlanan işlemleri tuşlayın")
                            continue

    else:
        print(Fore.LIGHTCYAN_EX + "Lütfen size tanımlanan işlemleri tuşlayın")
        continue
