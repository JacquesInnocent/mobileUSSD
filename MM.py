import time

# user
print("Welcome to MTN MoMo Services\n")
# phone_number = input("Enter Receiver's number\n")
# senderNumber = input("")
# receiverNumber = input("")

print("1. Send Money")
print("2. Request Money")
print("3. Save Money")
print("4. Buy Bundles")
print("0. Back")

userChoice = input("Choose your service\n")


def requester():
    print("Please enter the sender's number\n")
    senderNumber = input("")
    if (senderNumber == "123"):
        print("Sorry. You can't transact with a reserved number")
    else:
        print(senderNumber, "is unavailable to send you Money right now\n")


def sender():
    print("1. Send Money")
    print("2. Request Money")
    print("3. Save Money")
    print("4. Buy Bundles")
    print("0. Back")


# userChoice = input("Choose your service\n")
# print ("1. MTN")
# print ("2. Other Network\n")

# First Step
if (userChoice == "1"):
    print("1. MTN")
    print("2. Other Network\n")

# Step 2
elif (userChoice == "2"):
    sec = input("How many seconds to get the number?\n")
    print(sec, "seconds only")
    time.sleep(int(sec))

    # time.sleep(2)
    print("Please enter the sender's number\n")
    senderNumber = input("")
    if (senderNumber == "123"):
        print("Sorry. You can't transact with a reserved number")
        requester()
    else:
        print(senderNumber, "is unavailable to send you Money right now\n")
        sender()

    # Step 3
elif (userChoice == "3"):
    time.sleep(2)
    print("1. MoCash")
    print("2. Local Bank")
    print("3. Other")

    savingChoice = input("")

    if (savingChoice == "1"):
        print("1. Savings")
        print("2. Loans")
        print("3. Loan Limit")

    elif (savingChoice == "2"):
        print("1. Standard Chatered")
        print("2. Equity")
        print("3. DTB")
        print("4. ABSA")
        print("5. Centenary")
        print("0. Back")

    bankLoan = input("")

    if (bankLoan == "0"):
        time.sleep(2)
        print("Make a choice again")
        time.sleep(2)
        print(sender())
        time.sleep(1)
        print("Serve you better next time")
        time.sleep(5)

    elif (savingChoice == "3"):
        otherBank = input("Please enter the Bank's name\n")

        time.sleep(2)
        print(otherBank, "is not yet available under our services")
        time.sleep(2)
        sender()

# Step 4
elif (userChoice == "4"):
    time.sleep(2)
    print("Bundles currently unavailable\n")
    sender()

else:
    time.sleep(5)

# if (networkChoice == "1"):
#         print ("Enter Receiver's Number\n")
#         print (receiverNumber)
#     elif (networkChoice == "2"):
#         print ("Please choose a network\n")
#         print ("1. Airtel")
#         print ("2. Africell")
#         print ("3. Lycamobile")
#     else:
#         print ("Invalid input. Please try again\n")

