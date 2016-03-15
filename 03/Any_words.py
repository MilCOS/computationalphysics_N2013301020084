words = {   
        'A': "\   #        ##      # #      #  #     ####    #    #  ###  ### ",
        'B': "\######    #    #   ######   #     #  #     #  #     # #######  ",
        'C': "\   ####    #    #  #        #        #         #    #    ####  ",
        'D': "\######    #    #   #     #  #     #  #     #  #    #  ######   ",
        'E': "\######    #    #   #        ####     #        #    #  ######   ",
        'F': "\ #######   #        #   #    #####    #   #    #       ###     ",
        'G': "\   ####    #   #   #        #        #   ##   #    #    #####  ",
        'H': "\###  ###  #    #   #    #   ######   #    #   #    #  ###  ### ",
        'I': "\ #####      #        #        #        #        #      #####   ",
        'J': "\  #####      #        #        #        #    #   #     ###     ",
        'K': "\##  ##    #  #     # #      ##       # #      #  #    ##  ##   ",
        'L': "\###       #        #        #        #        #    #  #######  ",
        'M': "\ ## ##   #######  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  ",
        'N': "\##   ###  ##   #   # #  #   #  # #   #   ##   #    #  ###   #  ",
        'O': "\  ###     #   #   #     #  #     #  #     #   #   #     ###    ",
        'P': "\######    #    #   #    #   #####    #        #       ###      ",
        'Q': "\  ###     #   #   #     #  #     #  #   # #   #   #     ### ## ",
        'R': "\######    #    #   #    #   #####    ###      #  #    ###  ##  ",
        'S': "\  #####   #    #   ##         ##         ##   #    #   #####   ",
        'T': "\#######     #        #        #        #        #       ###    ",
        'U': "\###  ###  #    #   #    #   #    #   #    #   #    #    ####   ",
        'V': "\###  ###  #    #   #    #   ##  #     #  #     #  #      ##    ",
        'W': "\## # ##   # # #    # # #    # # #    # # #     ###      # #    ",
        'X': "\###  ###  #    #    #  #      ##       ##      #  #   ##    ## ",
        'Y': "\### ###   #   #    #   #     # #       #        #       ###    ",
        'Z': "\ ######  #    #       #       #       #       #    #  ######   ",
        ' ': "\                                                               "
    }

def change_mode():
    try:
        mode = raw_input("Enter the run_mode(0,1,2,3): ")[0]
    except:
        pass
    if mode == '0':
        mode0()
    elif mode == '1':
        mode1()
    elif mode == '2':
        mode2()
    elif mode == '3':
        mode3()
    else:
        print('Try again!')
        change_mode()

def mode0():
    print('Welcome!')
    print('You are in mode_0 now')
    print('run_mode2 is "about the words"')
    print('run_mode3 is purely for the decoration.')
    change_mode()

def mode1():
    print('###  ###     ###  ### \n #    #       #    #  \n  #  #        #    #  \n   ##         ######  \
\n   ##         #    #  \n  #  #        #    #  \n##    ##     ###  ### ')
    change_mode()

def mode2():
    ini = raw_input('Any letters but seperated with "space"(an example: a b c): ').upper()
    ini = str(ini)
    adj = ini.split()
    adj.reverse()
    l = len(adj)
    x = 1
    ss = {}
    while x <= l:
        letter = adj.pop()
        word = words[letter]
        ss[x] = word
        x += 1
    temp = {}
    k = 0
    link = ''
    while k <= 7:
        y = 1
        final = []
        while y <= l:
            temp = ss[y]
            d_start = k*9+1
            d_end = (k+1)*9
            fn = temp[d_start:d_end]
            final.append(fn)
            fn = []
            y += 1
        k += 1      
        print(link.join(final))
        final = []
    change_mode()

def mode3():
    import math
    import MiniGUI
    print("Still working on it. = = . This part will be based on Wentao Liu's MiniGUI")
    change_mode()

mode0()
