import mido
import keyboard
from threading import Thread
import music21

file='Asleep.mid'

mid = mido.MidiFile(file)
score = music21.converter.parse(file)
key = score.analyze('key')

Allkeys=["y","u","i","o","p","h","j","k","l",";","n","m",",",".","/"]
def keyset(Key,Har):
    if Har=="major":
        if Key=="C": return 12
        if Key=="D-": return 13
        if Key=="D": return 14
        if Key=="E-": return 15
        if Key=="E": return 16
        if Key=="F": return 17
        if Key=="F#": return 18
        if Key=="G": return 19
        if Key=="A-": return 20
        if Key=="A": return 21
        if Key=="B-": return 22
        if Key=="B": return 23
    if Har=="minor":
        if Key=="C": return 15
        if Key=="D-": return 16
        if Key=="D": return 17
        if Key=="E-": return 18
        if Key=="E": return 19
        if Key=="F": return 20
        if Key=="F#": return 21
        if Key=="G": return 22
        if Key=="A-": return 23
        if Key=="A": return 12
        if Key=="B-": return 13
        if Key=="B": return 14
def play(note,mode):
    for k in range(0,9):
        if currentnote == i and currentstate == "note_on":
            keyboard.press("y")#C
            continue
        if currentnote == i+12*k and currentstate == "note_off":
            keyboard.release("y")
            continue
        if currentnote == i+12*k+2 and currentstate == "note_on":
            keyboard.press("u")#D
            continue
        if currentnote == i+12*k+2 and currentstate == "note_off":
            keyboard.release("u")
            continue
        if currentnote == i+12*k+4 and currentstate == "note_on":
            keyboard.press("i")#E
            continue
        if currentnote == i+12*k+4 and currentstate == "note_off":
            keyboard.release("i")
            continue
        if currentnote == i+12*k+5 and currentstate == "note_on":
            keyboard.press("o")#F
            continue
        if currentnote == i+12*k+5 and currentstate == "note_off":
            keyboard.release("o")
            continue
        if currentnote == i+12*k+7 and currentstate == "note_on":
            keyboard.press("p")#G
            continue
        if currentnote == i+12*k+7 and currentstate == "note_off":
            keyboard.release("p")
            continue
        if currentnote == i+12*k+9 and currentstate == "note_on":
            keyboard.press("h")#A
            continue
        if currentnote == i+12*k+9 and currentstate == "note_off":
            keyboard.release("h")
            continue
        if currentnote == i+12*k+11 and currentstate == "note_on":
            keyboard.press("j")#B
            continue
        if currentnote == i+12*k+11 and currentstate == "note_off":
            keyboard.release("j")
            continue
        if currentnote == i+12*k+12 and currentstate == "note_on":
            keyboard.press("k")#C
            continue
        if currentnote == i+12*k+12 and currentstate == "note_off":
            keyboard.release("k")
            continue
        if currentnote == i+12*k+12+2 and currentstate == "note_on":
            keyboard.press("l")#D
            continue
        if currentnote == i+12*k+12+2 and currentstate == "note_off":
            keyboard.release("l")
            continue
        if currentnote == i+12*k+12+4 and currentstate == "note_on":
            keyboard.press(";")#E
            continue
        if currentnote == i+12*k+12+4 and currentstate == "note_off":
            keyboard.release(";")
            continue
        if currentnote == i+12*k+12+5 and currentstate == "note_on":
            keyboard.press("n")#F
            continue
        if currentnote == i+12*k+12+5 and currentstate == "note_off":
            keyboard.release("n")
            continue
        if currentnote == i+12*k+12+7 and currentstate == "note_on":
            keyboard.press("m")#G
            continue
        if currentnote == i+12*k+12+7 and currentstate == "note_off":
            keyboard.release("m")
            continue
        if currentnote == i+12*k+12+9 and currentstate == "note_on":
            keyboard.press(",")#A
            continue
        if currentnote == i+12*k+12+9 and currentstate == "note_off":
            keyboard.release(",")
            continue
        if currentnote == i+12*k+12+11 and currentstate == "note_on":
            keyboard.press(".")#B
            continue
        if currentnote == i+12*k+12+11 and currentstate == "note_off":
            keyboard.release(".")
            continue
        if currentnote == i+12*k+12*2 and currentstate == "note_on":
            keyboard.press("/")#C
            continue
        if currentnote == i+12*k+12*2 and currentstate == "note_off":
            keyboard.release("/")
            continue
i = keyset(key.tonic.name,key.mode)
print(i,key.tonic.name,key.mode)

for x in Allkeys:   
    keyboard.release(x)
keyboard.release("ins")
keyboard.wait("ins")
for msg in mid.play():
        currentstate=msg.type
        if currentstate=="note_on" or currentstate=="note_off":
                currentnote=msg.note
        else:
            currentnote=0
        play(currentnote,currentstate)