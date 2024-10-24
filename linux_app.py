#!/usr/bin/python3

from class_linux import Linux
from class_topics import Topics
import linuxdict

while True:
    topics = Topics()
    topics.main_menu()
    response = input('> ')
    if response == '1':
        #  topics.mod1_menu()  Create this
        #  response = input('> ')
        mod1 = Linux()
        mod1.flash_cards(linuxdict.sbj_mod1td, linuxdict.dict_mod1td)
    elif response == '2':
        mod2 = Linux()
        mod2.flash_cards(linuxdict.sbj_mod2td, linuxdict.dict_mod2td)
    elif response == '3':
        mod3 = Linux()
        mod3.flash_cards(linuxdict.sbj_mod3td, linuxdict.dict_mod3td)
    elif response == '4':
        mod4 = Linux()
        mod4.flash_cards(linuxdict.sbj_core, linuxdict.dict_core)
    elif response == '5':
        mod5 = Linux()
        mod5.flash_cards(linuxdict.sbj_mod5td, linuxdict.dict_mod5td)
    elif response == '6':
        mod6 = Linux()
        mod6.flash_cards(linuxdict.sbj_mod6td, linuxdict.dict_mod6td)
    elif response == '7':
        mod7 = Linux()
        mod7.flash_cards(linuxdict.sbj_mod7td, linuxdict.dict_mod7td)
    elif response == '8':
        mod8 = Linux()
        mod8.flash_cards(linuxdict.sbj_mod8td, linuxdict.dict_mod8td)
    elif response == '9':
        mod9 = Linux()
        mod9.flash_cards(linuxdict.sbj_mod9td, linuxdict.dict_mod9td)
    elif response == '10':
        mod10 = Linux()
        mod10.flash_cards(linuxdict.sbj_mod10td, linuxdict.dict_mod10td)
    elif response == '11':
        mod11 = Linux()
        mod11.flash_cards(linuxdict.sbj_mod11td, linuxdict.dict_mod11td)
    elif response == '12':
        mod12 = Linux()
        mod12.flash_cards(linuxdict.sbj_mod12td, linuxdict.dict_mod12td)
    elif response == '13':
        mod13 = Linux()
        mod13.flash_cards(linuxdict.sbj_mod13td, linuxdict.dict_mod13td)
    elif response == '14':
        mod14 = Linux()
        mod14.flash_cards(linuxdict.sbj_mod14td, linuxdict.dict_mod14td)
    else:
        print("Do It Again Tomorrow!!")
        break
