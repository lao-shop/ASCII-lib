import cowsay
import random
import os
import time
import colorama
from colorama import init, Fore, Back, Style
import pywhatkit

def exx():
    print('0. Back                 99. Exit')
    decide = int(input(Fore.BLUE + '[+]Enter number of function: '))

    if decide == 99:
        print(Fore.RED + '[+]Program finished')
        exit()
    elif decide == 0:
        os.system('cls')
        main(decide)

decide = 0

def main(decide):
    init(autoreset=True)
    print(Fore.RED + '            /\ \n'
'/vvvvvvvvvvvv \--------------------------------------,\n'
'`^^^^^^^^^^^^ /====================================="\n'
            '            \/\n')
    print(Fore.RED + '===============================================================\n'
          '               made by https://t.me/lao_takanava\n'
          '===============================================================\n'
          '\n'
          '1. Matrix               2. Ghostbusters banner\n'
          '3. Tiger banner         4. Turkey banner\n'
          '5. Linux penguin banner 6. Author\n'
          '7. +REP                 8. -REP\n'
          '9. Convert image to ASCII-art\n'
          '99. Exit\n')

    decide = int(input(Fore.BLUE + '[+]Enter number of function: '))

    if decide == 1:
        while decide == 1:
            for i in range(100):
                x = random.randint(0, 1)
                print(Fore.GREEN + str(x), end='')
            print('')
            time.sleep(1)


    elif decide == 2:
        cowsay.ghostbusters('Ghostbusters!')
        exx()


    elif decide == 3:
        cowsay.meow('Meow')
        exx()


    elif decide == 4:
        cowsay.turkey('AAAAAAAAAAAAAAAA')
        exx()


    elif decide == 5:
        cowsay.tux('Hello world!')
        exx()


    elif decide == 6:
        print(Fore.MAGENTA + "I'm Lao Takanava. I'm starter python programmer. \n"
            "If you want you can subscribe my tg channels:\n"
            "https://t.me/c_lao_tg\n"
            "https://t.me/lao_shop")
        exx()


    elif decide == 7:
        print(Fore.GREEN +   '░░░░░░░██████╗░███████╗██████╗░░\n'
                '░░██╗░░██╔══██╗██╔════╝██╔══██╗░\n'
                '██████╗██████╔╝█████╗░░██████╔╝░\n'
                '╚═██╔═╝██╔══██╗██╔══╝░░██╔═══╝░░\n'
                '░░╚═╝░░██║░░██║███████╗██║░░░░░░\n'
                '░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░\n')
        exx()


    elif decide == 8:
        print(Fore.RED +   '░░░░░░░██████╗░███████╗██████╗░░\n'
                '░░░░░░░██╔══██╗██╔════╝██╔══██╗░\n'
                '██████╗██████╔╝█████╗░░██████╔╝░\n'
                '╚═════╝██╔══██╗██╔══╝░░██╔═══╝░░\n'
                '░░░░░░░██║░░██║███████╗██║░░░░░░\n'
                '░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░\n')
        exx()


    elif decide == 9:
        image_path = input(Fore.BLUE + '[+]Enter path to image, that you want to convert into ASCII-art: ')
        output_file = 'ascii-art.txt'
        pywhatkit.image_to_ascii_art(image_path, output_file)
        print(f'[+]ASCII-art saved to {output_file}')
        exx()


    elif decide == 99:
        print(Fore.RED + '[+]Program finished')
        exit()


    else:
        print(Fore.RED + '[-]Wrong command, program finished')
        exit()

main(decide)
