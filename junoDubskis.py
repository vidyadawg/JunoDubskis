from keyboard import on_press
from pynput.keyboard import Key, Listener


def dub():
    f = open("stats.txt", "r")
    stat = f.readline()
    statSplit = stat.split('-')
    statSplitDub = int(statSplit[0])
    statSplitL = int(statSplit[1])
    f.close()

    f = open("stats.txt", "w")
    statSplitDub = statSplitDub + 1
    f.write(str(statSplitDub) + '-' + str(statSplitL))
    f.close()


def loss():
    f = open("stats.txt", "r")
    stat = f.readline()
    statSplit = stat.split('-')
    statSplitDub = int(statSplit[0])
    statSplitL = int(statSplit[1])
    f.close()

    f = open("stats.txt", "w")
    statSplitL = statSplitL + 1
    f.write(str(statSplitDub) + '-' + str(statSplitL))
    f.close()


def show(key):
    keyData = str(key)
    print(keyData)
    if keyData == "\'+\'":
        dub()

    if keyData == "\'-\'":
        loss()

    if key == Key.delete:
        return False


with Listener(on_press=show) as listener:
    listener.join()
