from datetime import date, timedelta
from moneydb import Database

today = date.today()
db = Database("moneydb.db")
d1 = today.strftime("%d")
global finalbal
global finbal

class BankBalance:
    def __init__(self):
        self.bal = 0

b1 = BankBalance()

def getMonthlySavings():
    if d1 == '21':
        b1.bal = b1.bal + 5000

getMonthlySavings()

def manualEntry():
    incamt = int(input ("Amount:"))
    incdate = today.strftime("%d-%m-%y")
    increm = input ("Remarks:")
    finalbal = incamt
    for row in db.fetch():
        finalbal = row[4] + incamt
    db.insert(incamt, increm, incdate, finalbal)

def manualExpense():
    expamt = int(input ("Expense:"))
    expdate = today.strftime("%d-%m-%y")
    exprem = input ("Remarks:")
    for row in db.fetch():
        finalbal = row[4] - expamt
    db.insert(-abs(expamt), exprem, expdate, finalbal)

def balEnquiry():
    for row in db.fetch():
        finBal = row[4]
        print(finBal)
    print ("Your final Balance is:", finBal, "Rs.")

def sort():
    sort1 = str(input ("Enter the date from which you want the record to be searched: "))
    sort = sort1 + '%'
    for row in db.fetch():
        if sort1 == row[3]:
            db.search(sort)
            for row in db.search(sort):
                print("Id = ", row[0], )
                print("Balance = ", row[1])
                print("Remarks = ", row[2])
                print("Date = ", row[3])
                print("Final Balance  = ", row[4], "\n")
                break
        else:
            print("No records were found for that day.")
            break

def rangSort():
    #make a way to search using date range
    print ("This feature has not been added. Please wait for another update.")
    # fdate1 = input ("Enter the first range from which you want the record to be searched: ")
    # fdate = fdate1 + '%'
    # ldate1 = input ("Enter the second range from which you want the record to be searched: ")
    # ldate = ldate1 + '%'
    # db.rangSearch(fdate, ldate)
    # for row in db.rangSearch(fdate, ldate):
    #     print("Id = ", row[0], )
    #     print("Balance = ", row[1])
    #     print("Remarks = ", row[2])
    #     print("Date = ", row[3])
    #     print("Final Balance  = ", row[4], "\n")

def viewStatement():
    for row in db.fetch():
        print("Id = ", row[0], )
        print("Balance = ", row[1])
        print("Remarks = ", row[2])
        print("Date = ", row[3])
        print("Final Balance  = ", row[4], "\n")

def delAll():
    db.delete()

def main():
    choice = input("1) Income\n2) Expense\n3) Balance Enquiry\n4) Specific date\n5) Date Range\n6) View Statement\n7) Clear all data\n8) Exit\n")
    if choice == '1':
        manualEntry()
        input("")
        main()
    elif choice == '2':
        manualExpense()
        input("")
        main()
    elif choice == '3':
        balEnquiry()
        input("")
        main()
    elif choice == '4':
        sort()
        input("")
        main()
    elif choice == '5':
        rangSort()
        main()
    elif choice == '6':
        viewStatement()
        input("")
        main()
    elif choice == '7':
        delAll()
        print("All records have been deleted successfully...")
        input("")
        exit
    elif choice == '8':
        exit
    else:
        print ("Input a valid choice.")
        input("")
        main()

main()
