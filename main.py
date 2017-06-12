from os import listdir
from os.path import isfile, join

def getCMD():
    cmds = dict(enumerate([f for f in listdir('cmd') if isfile(join('cmd', f))]))
    print('Choose cmd:')
    for key in cmds.keys():
        print(key, cmds[key])
    cmd = open(join('cmd', cmds[int(input('>>> '))])).read()
    return cmd

def getExploit():
    xplts = dict(enumerate([f for f in listdir('ducky') if isfile(join('ducky', f))]))
    print('Choose Exploit:')
    print('0 Custom')
    for key in xplts.keys():
        print(key+1, xplts[key])
    key = int(input('>>> '))
    if key == 0:
        print('Type EXIT to stop accepting input')
        xplt = ''
        while(True):
            inp = input('> ')
            if inp.lower().find('exit') == 0: break
            xplt+=inp+'\n'
    else: xplt = open(join('ducky', xplts[key-1])).read()
    return xplt

def scanExploit(content):
    posn=[]
    n=0
    while content.find('>>>', n) != -1:
        loc = content.find('>>>', n)
        n = content.find('<<<', loc) + 3
        posn.append((loc, n))
    vals=[]
    for pos in posn:
        vals.append(content[pos[0]:pos[1]])
    return vals

def matchExploit(content, found, preset = {'>>>CMD<<<': getCMD}):
    for key in preset.keys():
        if key in found:
            content = content.replace(key, preset[key]())
            while key in found: found.remove(key)
    while found != []:
        key = found[0]
        content = content.replace(key, input(key[3:-3] + ': '))
        while key in found: found.remove(key)
    return content

def exploit():
    xplt=getExploit()
    found = scanExploit(xplt)
    return matchExploit(xplt, found)

out = '\n\nDELAY 5000\n'
out += exploit()
while input("Add another exploit? (Y/n)").lower() == 'y':
    out += exploit()
print(out)
input()
