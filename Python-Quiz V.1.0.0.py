import time
import os
qlist = []
alist = []
rfile = []
choice = "x"
qbar = 1
readcount = 1

def choose():
    print "Welcome to Obsid's Python Quiz"
    global choice
    choice = raw_input("Choose (a)dmin for making a quiz, (i)mport to load a question set or (p)lay to play the quiz: ")
    game()

def exportqs():
    chosenloc = raw_input("Enter the full path of your destination here: ")
    outfile = open(chosenloc, "w")
    writecount = 0
    while writecount < qbar - 1:
        outfile.writelines(qlist[writecount])
        outfile.writelines(os.linesep)
        outfile.writelines(alist[writecount])
        outfile.writelines(os.linesep)
        writecount = writecount + 1
    outfile.close()
    print "Done!"

def importqs():
    importloc = raw_input("Enter the full path of your import file here: ")
    intext = open(importloc, 'r').read().splitlines()
    for i in range(len(intext)):
        rfile.append(intext[i].split('\n'))
    newrfile = [i[0] for i in rfile]
    qamount = len(newrfile[:])
    global qbar
    qbar = len(newrfile[:])
    qbar = qbar/2
    qbar = qbar + 1
    print qamount, "lines loaded."
    global readcount
    readcount = 0
    while readcount < qamount:
        if readcount%2==0:
            qlist.append(newrfile[readcount])
        else:
            alist.append(newrfile[readcount])
        global readcount
        readcount = readcount + 1
    print "Done!"
    
def game():
    if choice == "a":
        del alist[:]
        del qlist[:]
        c = int(raw_input("Enter the number of questions you want: "))
        global qbar
        qbar = c
        qbar = qbar + 1
        while c > 0:
            question = raw_input("Enter Your Question: ")
            qlist.append(question)
            answer = raw_input("Enter The Answer (Warning: It is case sensitive): ")
            alist.append(answer)
            c = c - 1
        export = raw_input("Do you want to export your question set to a file (y/n)?: ")
        if export == "y":
            exportqs()
        else:
            pass
        print "Ok, Finished. Returning to Home Screen..."
        time.sleep(1)
    elif choice == "p":
        dashcount = 0
        while dashcount < 100:
            print "--------------------------------------------------"
            dashcount = dashcount + 1
        score = 0
        qnum = 1
        while qnum < qbar:
            print qnum,".",qlist[qnum-1],": "
            givenanswer = raw_input("Enter your answer: ")
            if givenanswer == alist[qnum-1]:
                print "Correct"
                score = score + 1
            else:
                print "Wrong"
            qnum = qnum + 1
        print "You got ", score, "/", qbar - 1
    elif choice == "i":
        importqs()
    choose()

choose()