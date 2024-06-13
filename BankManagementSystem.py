import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="1234",database="bank")

def OpenAcc():
    n = input("Enter Name :")
    if len(n) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID NAME   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    for x in n:
        if x != " " :
            if not x.isalpha():
                for i in range (2):
                    print("\n")
                    print("                            INVALID NAME   ")
                    for i in range (2):
                        print("\n")
                    print(" "*20,"-"*20,"X","-"*20,sep="")
                    main()
    ac = input("Enter Account No :")
    if ac == None :
        for i in range (2):
            print("\n")
        print("                            INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    elif not ac.isdigit() or len(ac)>9:
        for i in range (2):
            print("\n")
        print("                            INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    db = input("Enter D.O.B(FORMAT: DD-MM-YYYY) : ")
    if len(db) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID D.O.B   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    elif db.isalnum():
        for i in range (2):
            print("\n")
        print("                            INVALID D.O.B FORMAT   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    elif db[2]!="-" or db[5]!="-" or len(db)>10:
        for i in range (2):
            print("\n")
        print("                            INVALID D.O.B FORMAT   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    else :
        l = db.split("-")
        if int(l[2]) > 2004 :
            for i in range (2):
                print("\n")
            print("                            AGE MUST BE GREATER THAN 18 YEARS   ")
            for i in range (2):
                print("\n")
            print(" "*20,"-"*20,"X","-"*20,sep="")
            main()
        elif int(l[1]) > 12:
            for i in range (2):
                print("\n")
            print("                            D.O.B INVALID   ")
            for i in range (2):
                print("\n")
            print(" "*20,"-"*20,"X","-"*20,sep="")
            main()
        elif int(l[0]) > 31:
            for i in range (2):
                print("\n")
            print("                            D.O.B INVALID   ")
            for i in range (2):
                print("\n")
            print(" "*20,"-"*20,"X","-"*20,sep="")
            main()
        elif int(l[0]) > 30 and int(l[1]) in [2,4,6,9,11] :
            for i in range (2):
                print("\n")
            print("                            D.O.B INVALID   ")
            for i in range (2):
                print("\n")
            print(" "*20,"-"*20,"X","-"*20,sep="")
            main()
        elif  int(l[1]) == 2:
            if int(l[2])%100 != 0:
                if int(l[2])%4 == 0:
                    if int(l[0]) > 29:
                        for i in range (2):
                            print("\n")
                        print("                            D.O.B INVALID   ")
                        for i in range (2):
                            print("\n")
                        print(" "*20,"-"*20,"X","-"*20,sep="")
                        main()
                else:
                    if int(l[0]) > 28:
                        for i in range (2):
                            print("\n")
                        print("                            D.O.B INVALID   ")
                        for i in range (2):
                            print("\n")
                        print(" "*20,"-"*20,"X","-"*20,sep="")
                        main()
            else:
                if int(l[2])%400 == 0:
                    if int(l[0]) > 29:
                        for i in range (2):
                            print("\n")
                        print("                            D.O.B INVALID   ")
                        for i in range (2):
                            print("\n")
                        print(" "*20,"-"*20,"X","-"*20,sep="")
                        main()
                else:
                    if int(l[0]) > 28:
                        for i in range (2):
                            print("\n")
                        print("                            D.O.B INVALID   ")
                        for i in range (2):
                            print("\n")
                        print(" "*20,"-"*20,"X","-"*20,sep="")
                        main()                  
    p = input("Enter Phone :")
    if len(p) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID PHONE NUMBER   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    elif not p.isdigit() or len(p)!=10:
        for i in range (2):
            print("\n")
        print("                            INVALID PHONE NUMBER   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    ad = input("Enter Address :")
    if len(ad) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID ADDRESS   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    Bal = input("Enter Opening Balance")
    if len(Bal) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID BALANCE AMOUNT   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    elif int(Bal) < 500 :
        for i in range (2):
            print("\n")
        print("                            OPENING BALANCE MUST BE AT LEAST 500!!!")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
    D = (n,ac,db,ad,p,Bal)
    Q = "insert into account values(%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(Q,D)
    con.commit()
    for i in range (2):
        print("\n")
    s = '''                       DATA ENTERED SUCCESSFULLY
                              THANKYOU!!!'''
    print(s)
    for i in range (2):
        print("\n")
    print(" "*20,"-"*20,"X","-"*20,sep="")
    main()

def DepAmnt():
    amnt = int(input("Enter Amount :"))
    acc = input("Enter Account no :")
    Q = "select bal from account where accno = %s"
    D = (acc,)
    c = con.cursor()
    c.execute(Q,D)
    result = c.fetchone()
    if result != None :
        total = result[0] + amnt
        Q = "update account set Bal = %s where accno = %s"
        D1 = (total,acc)
        c.execute(Q,D1)
        con.commit()
        for i in range (2):
            print("\n")
        print("                         ENTERED AMOUNT HAS BEEN DEPOSITED ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
    else:
        for i in range (2):
            print("\n")
        print("                          INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
    main()

def WiDrawAmnt():
    amnt = int(input("Enter Amount :"))
    acc = input("Enter Account no :")
    Q = "select bal from account where accno = %s"
    D = (acc,)
    c = con.cursor()
    c.execute(Q,D)
    result = c.fetchone()
    if result== None:
        for i in range (2):
            print("\n")
        print("                       INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    total = result[0] - amnt
    if total < 0:
        for i in range (2):
            print("\n")
        print("                       ENTERED AMOUNT GREATER THAN AVAILABLE AMOUNT   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    Q1 = "update account set Bal = %s where accno = %s"
    D1 = (total,acc)
    c.execute(Q1,D1)
    con.commit()
    for i in range (2):
        print("\n")
    print("                          AMOUNT WITHDRAWN SUCCESSFULLY   ")
    for i in range (2):
        print("\n")
    print(" "*20,"-"*20,"X","-"*20,sep="")
    main()

def Balance():
    acc = input("Enter Account No. :")
    Q = "select Bal from account where accno = %s"
    D = (acc,)
    c = con.cursor()
    c.execute(Q,D)
    result = c.fetchone()
    if result == None:
        for i in range (2):
            print("\n")
        print("                       INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    else:
        print("Balance for Account No.",acc,"is Rs.",result[0])
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()

def DispAcc():
    acc = input("Enter Account No :")
    Q = "select * from account where accno = %s"
    D = (acc,)
    c = con.cursor()
    c.execute(Q,D)
    result = c.fetchone()
    if result != None:
        print("NAME    ","ACC_NO","DOB","ADD.    "," ","PHN","","BAL",sep=" "*7)
        for i in result:
            print(i,"|",end=" ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
    else :
        for i in range (2):
            print("\n")
        print("                            INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
    main()

def CloseAcc():
    acc = input("Enter Account No :")
    if len(acc) == 0 :
        for i in range (2):
            print("\n")
        print("                            INVALID ACCOUNT NO.   ")
        for i in range (2):
            print("\n")
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()
    Q = "delete from account where accno = %s"
    D = (acc,)
    c = con.cursor()
    c.execute(Q,D)
    con.commit()
    print("ACCOUNT HAS BEEN CLOSED")
    for i in range (2):
        print("\n")
    print(" "*20,"-"*20,"X","-"*20,sep="")
    main()
    
def main():
    for i in range (2):
            print("\n")
    print("                          WELCOME TO MUTUAL COOPERATION BANK!!!   ")
    for i in range (2):
            print("\n")
    print('''
    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT
    ''')

    choice = input("Enter Task No :")

    if choice == "1":
        OpenAcc()
    elif choice == "2":
        DepAmnt()
    elif choice == "3":
        WiDrawAmnt()
    elif choice == "4":
        Balance()
    elif choice == "5":
        DispAcc()
    elif choice == "6":
        CloseAcc()
    else:
        print('''
        ...WRONG CHOICE...
        ...PLEASE ENTER AGAIN...
        ''')
        print(" "*20,"-"*20,"X","-"*20,sep="")
        main()

main()
    
