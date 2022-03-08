import os 

def main():
    cmd = input('\n...\n').rstrip()

    if cmd == 'readme':
        with open(os.getcwd() + '/readme.txt') as f:
            txt = f.read()
        print(txt)

    if cmd == 'viewpwsh':
        a = viewpwsh()
        print(a)

    if cmd == 'viewkali':
        a = viewkali()
        print(a)
    
    if cmd.find('setpwsh') > -1:
        cmd2 = cmd.split('setpwsh ')[1]
        themeset = settheme('pwsh', cmd2)
        print('Success!?')

    if cmd.find('setkali') > -1:
        cmd2 = cmd.split('setkali ')[1]
        themset = settheme('kali', cmd2)
        print('success?')
    
    if cmd.find('setall') > -1:
        cmd2 = cmd.split('setall ')[1]
        settheme('pwsh', cmd2)
        settheme('kali', cmd2)
        print('success?!')

    if cmd.find('showthemes') > -1:
        listThemes()

    if cmd == 'quit' or cmd == 'exit':
        quit()

    main()

def listThemes():
    filepath = r'C:\Users\sparky\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json'
    themelist = []
    themez = ''
    with open(filepath) as f:
        themez = f.read()
        themes = themez.split('"name": "')
        for x in themes:
            themelist.append(x.split('"')[0])

    print(themelist)
            
    


def cptheme(name):
    filepath = r'C:\\Users\sparky\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState'
    themedat = ''
    with open(filename + 'settings.json') as f:
        themedat = f.read()
    with open(filename + name, 'w') as f:
        themedat = f.write(themedat)


def settheme(distro, theme):
    strsettings = ''
    with open(r'C:\\Users\\sparky\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json') as f:
        strsettings = f.read()
    settings = strsettings.splitlines()
    ind = 0
    while ind <= len(settings) - 1:
        thepos = settings[ind]
        if distro == 'pwsh':
            if thepos.find('{574e775e-4f2a-5b96-ac1e-a2962a402336}') > -1:
                settings.pop(ind - 1)
                settings.insert(ind - 1, '                "colorScheme": "' + theme + '",')
                
        elif distro == 'kali':
            if thepos.find('{46ca431a-3a87-5fb3-83cd-11ececc031d2}') > -1:
                settings.pop(ind - 1)
                settings.insert(ind - 1, '                "colorScheme": "' + theme + '",')
        ind += 1
    #restring it
    strout = ''
    for line in settings:
        strout += line + '\n'
    
    with open(r'C:\Users\sparky\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json', 'w') as f:
        f.write(strout)
    
    print('Success!')


def viewkali():
    filename = "C:\\Users\\sparky\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"
    filecont = ''
    with open(filename) as f:
        filecont = f.read()

    kalitheme1 = filecont.split('"guid": "{46ca431a-3a87-5fb3-83cd-11ececc031d2}",')[0]
    kalitheme2 = kalitheme1.split('"colorScheme": "')
    kalitheme3 = kalitheme2[len(kalitheme2) - 1]

    kalitheme = kalitheme3.split('"')[0]
    return(kalitheme)

def viewpwsh():
    filename = 'C:\\Users\\sparky\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json'
    filecont = ''
    with open(filename) as f:
        filecont = f.read()
    
    pwshtheme1 = filecont.split('"guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",')[0]
    pwshtheme2 = pwshtheme1.split('"colorScheme": "')
    pwshtheme3 = pwshtheme2[len(pwshtheme2) - 1]

    pwshtheme = pwshtheme3.split('"')[0]

    return(pwshtheme)

if __name__ == "__main__":
    help = "setpwsh (name) - sets the PowerShell theme\n"
    help += "viewpwsh - views the current PowerShell theme\n"
    help += 'setkali (name) - sets the Kali Linux theme\n'
    help += 'viewkali - views the current Kali Linux theme\n'
    help += 'setall (name) - sets both themes to this\n'
    help += 'savetheme (name) - saves current settings as a "theme".json and you can lo=ad this configuration\n'
    help += 'loadtheme (name) - loads a settings file .json from the current folder\n'
    help += 'readme\n'

    help += 'showthemes\n'

    help += 'quit\n'

    print(help)
    main()