import os
import sys
from termcolor import colored
alphabet = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

def singleChar():
    os.system("cls")
    print("\n\n","*"*10,"Welcome to Ascii ART","*"*10,end="\n\n")
    
    text = input("Enter single Character -- ").upper()
    if len(text)!= 1:
        print("\n\n Please Enter Only One Letter🙏 -- \n\n")
        singleChar()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27 * 6 if text == "@" else 28 * 6 if text == "_" else 29 * 6 if text == "-" else 30 * 6 if text == "." else ((ord(text) - 64)-1)*6
        for i in alphabet:
            for j in range(n , n + 6):
                print(i[j],end="")
            print()

def alphaNumWords():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"Welcome to Ascii ART","*"*10,end="\n\n")
  
    text = input("Enter String (Only <= 15 Character) -- ").upper()
    color = input("Enter color name--")
    color_ascii =colored(text,color)
    
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        alphaNumWords()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        for i in alphabet:
            for x in text:
                n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else 26*6 if x ==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else ((ord(x) - 64)-1)*6 
                for j in range(n , n + 6):
                    print(i[j],end="")
            print()


def Alphabet():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"Welcome to Ascii ART","*"*10,end="\n\n")
 
    text = input("Enter only alphabet 0-15 -- ").upper()
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
       
        Alphabet()
    else:
        if text.isalpha() == False:
            print("\n\nPlease Enter Only Alphabets -- \n\n")
            Alphabet()
        else:
            print("\n\nYou Entered -- {0}\n\n".format(text))
            for i in alphabet:
                for x in text:
                    n =((ord(x) - 64)-1)*6 
                    for j in range(n , n + 6):
                        print(i[j],end="")
                print()

def Number():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"Welcome to Ascii ART","*"*10,end="\n\n")

    text = input("Enter String (Only <= 15 Character) -- ").upper()
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
      
        Number()
    else:
        if text.isnumeric() == False:
            print("\n\nPlease Enter Only Numbers -- \n\n")
            Number()
        else:
            print("\n\nYou Entered -- {0}\n\n".format(text))
            for i in alphabet:
                for x in text:
                    n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else ((ord(x) - 64)-1)*6 
                    for j in range(n , n + 6):
                        print(i[j],end="")
                print()


def mainUI():
    os.system("cls")
    print("\n\n","*"*10,"Priyanshu sharma","*"*10,end="")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("OPTIONS -- \n\n")
    print("1. single Character")
    print("2. Words (Maximum 15 Letters)")
    print("3. Only Alphabets")
    print("4. Only Numbers")
    print("5. Exit")
    print("\n\nEnter Your Choice -- ",end="")
    choise =input("Enter your number (1-5)")
    new_func(choise)
    
    yes = input("\n\nDo you want to continue Project.. Press y else any key...")
   
    if yes == "r" or yes == "r":
        mainUI()

def new_func(choise):
    if choise == "1":
        singleChar()
    elif choise == "2":
        alphaNumWords()
    elif choise == "3":
        Alphabet()
    elif choise == "4":
        Number()
    elif choise == "5":
        pass

mainUI()
