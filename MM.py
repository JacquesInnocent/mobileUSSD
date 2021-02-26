import time

#user
print ("Welcome to MTN MoMo Services\n")
# phone_number = input("Enter Receiver's number\n")
# senderNumner = input("")
# receiverNumber = input("")

print ("1. Send Money")
print ("2. Request Money")
print ("3. Save Money")
print ("4. Buy Bundles")

userChoice = input("Choose your service\n")

def requester():
    print ("Please enter the sender's number\n")
    senderNumner = input("")
    if (senderNumner == "123"):
        print("Sorry. You can't transact with a reserved number")
    else:   
        print (senderNumner,  "is unavailable to send you Money right now\n")

def sender():
    print ("1. Send Money")
    print ("2. Request Money")
    print ("3. Save Money")
    print ("4. Buy Bundles")

userChoice = input("Choose your service\n")

# First Step
if (userChoice == "1"):
    print ("1. MTN")
    print ("2. Other Network\n")

elif (userChoice == "2"):
    sec = input("How many seconds to get the number?\n")
    print (sec, "seconds only")
    time.sleep(int(sec))
    # time.sleep(2)
    print ("Please enter the sender's number\n")
    senderNumner = input("")
    if (senderNumner == "123"):
        print("Sorry. You can't transact with a reserved number")
        requester()
    else:   
        print (senderNumner,  "is unavailable to send you Money right now\n")    
    

elif (userChoice == "3"):
    time.sleep(2)
    print ("Service currently unavailable\n")
    exit()

elif (userChoice == "4"):
    time.sleep(2)
    print ("Budles currently unavailable\n")
    exit()
else:
    time.sleep(2)
    print ("Wrong input. Please try again later!\n")
    exit()


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

#F2295B

    #F2295B
