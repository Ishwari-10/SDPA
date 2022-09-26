# importing all the required classes
from  Room_class import Room
from Hotel_class import Hotel
from Guest_class import Guest
from Guest_class import VIP
# importing the required package
import datetime


# initialising the required variables
hotelName='Hotel Regency'
hotelAddress = 'Britol City Center'
# initialising the number of rooms
singleStandard= 5
singleDeluxe = 5

doubleStandard = 4
doubleDeluxe = 4

suiteStandard = 2
suiteDeluxe = 2


maxLengthOfStay = {'Single' : {'Standard': 3 ,
                               'Deluxe' : 5}, 
                  'Double': {'Standard' : 5,
                             'Deluxe'   : 10}, 
                  'Suite' : {'Standard' : 15,
                             'Deluxe'   : 20}
                  }



if __name__ == '__main__':    

    print('Initializing Hotel')
    # instantiating Hotel object
    hotelRegency = Hotel(hotelName=hotelName, hotelAddress= hotelAddress)
    
    
    print('adding Rooms')
    # Adding single rooms
    hotelRegency.add_Rooms('Single', 'Standard', maxLengthOfStay['Single']['Standard'], singleStandard)
    hotelRegency.add_Rooms('Single', 'Deluxe', maxLengthOfStay['Single']['Deluxe'], singleStandard)
    # Adding double rooms
    hotelRegency.add_Rooms('Double', 'Standard', maxLengthOfStay['Double']['Standard'], doubleStandard)
    hotelRegency.add_Rooms('Double', 'Deluxe', maxLengthOfStay['Double']['Deluxe'], doubleDeluxe)
    # Adding suite rooms
    hotelRegency.add_Rooms('Suite', 'Standard', maxLengthOfStay['Suite']['Standard'], suiteStandard)
    hotelRegency.add_Rooms('Suite', 'Deluxe', maxLengthOfStay['Suite']['Deluxe'], suiteDeluxe)
   
    
    
    
    print(hotelRegency.hotelName, ' is open for Guests')
    # creating an infinite loop to get the user input until the conditions are met
    while True:
        print("\n")
        # No need to  save guest if guest doesn't checkin
        guest = Guest(None, None, None) # Initializing a blank guest as we dont know if the guest is new or old 
        
        print("We have {} rooms available".format(len(hotelRegency.roomAvailability['Available'])))
        print("\n")
        print("Please select Available Options")
        
        
        option1 =None
         # printing the menu to user and defining options users can enter to interact with the hotel management system
        while option1 is None:
            print("1. Search Available Rooms",
                  "2. Check in",
                  "3. Check Out ",sep=("\n"))
            try:
                # typecasting
                value =  int(input())
                if value in [1,2,3]:
                    option1 = value
                else:
                    # error handling scenario
                    # check whether the entered number is correct or not
                    print("Please enter correct option")
            except ValueError:
                # checking if user is entering int values and not garbage value.
                print("Please enter a number from the options")
        
       
        if option1==1:
            print("Please Enter Search Criteria. \n")
            
            numberOfPeople = None
            
            while numberOfPeople is None:
                print("1. Please enter number of People")
                try:
                    enteredNumberOfPeople =  int(input())
                    
                    if enteredNumberOfPeople > 0:
                        numberOfPeople = enteredNumberOfPeople
                    else:
                        # validation handling scenario
                        print("Entered value cannot be less than 0")                    
                    
                except ValueError:
                    # error handling scenario
                    print("Please enter a number")
             
             
            
            
            
            lengthOfStay = None
            
            while lengthOfStay is None:
                print("2. Please enter Length of stay.\n")
                try:
                    enteredLengthOfStay =  int(input())
                    
                    if enteredLengthOfStay >0:
                        lengthOfStay = enteredLengthOfStay
                    else:
                        print("Entered value cannot be less than 0")
                    
                    
                except ValueError:
                    print("Please enter a number")
            
                      
            
            
            
            withView = None
            
            while withView is None:
                print("3. Would you like a Room with View (May have extra charges)")
                try:
                    value4 =  str(input("y for yes or n for no \n"))
                    if value4 in ['y','n']:
                        withView = value4
                    else:
                        print("Please enter correct option")
                    
                except ValueError:
                    print("Please enter y for yes  or n for no")    
            
           # hotelRegency.display_rooms(numberOfPeople,lengthOfStay,withView)
            guest.enquire_Room(hotelRegency,numberOfPeople,lengthOfStay,withView)
            
            print("\nPlease select the room number that you want to checkin into")
        
        elif option1 ==2:  ## Checkin Option 
        
            roomNo =None
            
            while roomNo is None:
                print(" Please Enter the room Number you would like to checkin. (Enter 0 To exit)",sep=("\n"))
                try:
                    enteredRoomNo =  int(input())
                    
                    if enteredRoomNo == 0 :
                        roomNo =0
                        break
                    
                    if enteredRoomNo in hotelRegency.roomAvailability['Available']:
                        roomNo = enteredRoomNo
                    else:
                        print("Room not available. Please enter correct room number ")
                except ValueError:
                    print("Please enter a valid room number")

            if roomNo ==0: # Restart loop if 0 entered
                continue            
            # Guest Date of Birth  
            

            DOB= None
            while DOB is None:
                print(" Please Enter your DOB in DD/MM/YYY format. (Enter 0 to Exit) ",sep=("\n"))
                try:
                    enteredDOB =  str(input())
                    if enteredDOB == '0' :
                        DOB ='0'
                        break                    
                    
                    enteredDOB = datetime.datetime.strptime(enteredDOB, '%d/%m/%Y')  # Code Reference  :  https://www.codegrepper.com/code-examples/python/how+to+verify+date+dd%2Fmm%2Fyyyy+python
                    if enteredDOB is not None:
                        DOB = enteredDOB
                    
                except ValueError:
                    print("Please enter date in correct format")
                    
            if DOB =='0': # Restart loop if 0 entered
                continue                     
                    
                    
            name = None
            while name is None:
                print("Please Enter your Full Name ",sep=("\n"))
                try:
                    enteredName =  str(input()).strip()
                    
                    if enteredName is not None and len(enteredName)>0 and enteredName.replace(" ","").isalpha():
                        name = enteredName
                    else:
                        print("Incorrect value entered")
                    
                except ValueError:
                    print("Incorrect value entered")                    
            
                        
            
            # Guest Phone Number 
            phoneNumber = None        
            while phoneNumber is None:
                print(" Please enter your 10 digit Phone Number",sep=("\n"))
                try:
                    enteredPhoneNo =  input()
                    if int(enteredPhoneNo) >0 and len(enteredPhoneNo) == 10:
                        phoneNumber = int(enteredPhoneNo)
                    else:
                        print("Please enter correct phone number")
                except ValueError:
                    print("Please enter correct phone number")  
            
            if hotelRegency.search_guest(DOB, name):
               print("User has already Checked in. Cannot book more than 1 Room \n")
               input("Press Enter to restart")
               continue
            else:
                guest.set_guest_details(name, DOB, phoneNumber)
                        
           
            # Number of Days
            
            numberOfDays = None        
            while numberOfDays is None:
                print(" Please enter number of days for the stay",sep=("\n"))
                try:
                    enteredNumberOfDays =  int(input())
                    if enteredNumberOfDays >0 and enteredNumberOfDays <= hotelRegency.rooms[roomNo].lenghtOfStayAllowed :
                        numberOfDays = enteredNumberOfDays
                    else:
                        print("Please enter correct value less than ", hotelRegency.rooms[roomNo].lenghtOfStayAllowed, " days and greater than 0 ")
                except ValueError:
                    print("Please enter correct value")
            
            # Number of People staying        
            numberOfPeople = None        
            while numberOfPeople is None:
                print(" Please enter number of People staying ",sep=("\n"))
                try:
                    enterednumberOfPeople =  int(input())
                    
                    if enterednumberOfPeople >0 :
                        numberOfPeople = enterednumberOfPeople
                    else:
                        print("Please enter greater than 0 ")
                except ValueError:
                    print("Please enter correct value")  
                    
            roomTypeAllowed =  'Single' if numberOfPeople ==1 else 'Double' if numberOfPeople ==2 else 'Suite' if numberOfPeople >2 and numberOfPeople <5 else ''   
            
            if roomTypeAllowed != hotelRegency.rooms[roomNo].roomType:
                print("The selected Room doesnt allow the number of People entered for staying.\n")
                print("Please search for correct Room as per your requirements\n")
                input('Press Enter to restart')
                continue 
                
 
            # Guest Type
            
            guestTypeVIP = None        
            while guestTypeVIP is None:
                print("Would you like to avail VIP previleges (y for yes or  n for no)",sep=("\n"))
                try:
                    enteredGuestTypeVIP =  str(input()).strip().lower()
                    if enteredGuestTypeVIP in ['y','n']:
                        guestTypeVIP = 'VIP'
                    else:
                        print("Incorrect value entered")
                except ValueError:
                    print("Incorrect value entered")            
            
            
            if hotelRegency.search_guest(DOB, name):
               print("User has already Checked in. Cannot book more than 1 Room \n")
               input("Press any Key to restart")
               continue
            else:
                if guestTypeVIP == 'VIP':
                    guest = VIP(name, DOB, phoneNumber, guestTypeVIP)  
                else:   
                    guest.set_guest_details(name, DOB, phoneNumber)        
                
                # Perform check in
                hotelRegency.process_checkin(guest, roomNo, numberOfDays)
                roomFeature = hotelRegency.rooms[roomNo].feature
                price = hotelRegency.rooms[roomNo].get_roomPrice( numberOfDays , guestTypeVIP)
                print("You have booked a room for {} guests, room type: {}/features {} for {} days, total cost is {}".format(numberOfPeople ,roomTypeAllowed , roomFeature,numberOfDays , price ))
                
                print('\n Press Enter to continue')
                
                input()
                continue
                    
        
        elif option1 ==3:
            
            
            print("Please Enter below details to process checkout.\n")
            
            roomNo =None
            
            while roomNo is None:
                print("Please Enter the room Number you are staying in (Enter 0 to Exit)",sep=("\n"))
                try:
                    enteredRoomNo =  int(input())
                    
                    if enteredRoomNo == 0 :
                        roomNo =0
                        break
                    
                    if enteredRoomNo in hotelRegency.roomAvailability['UnAvailable']:
                        roomNo = enteredRoomNo
                    else:
                        print("Incorrect Room number entered")
                except ValueError:
                    print("Please enter a valid room number")
                    
            if roomNo ==0: # Restart loop if 0 entered
                continue                      
            
            # Guest Date of Birth  
            

            DOB= None
            while DOB is None:
                print(" Please Enter your DOB in DD/MM/YYY format.(Enter 0 to exit)",sep=("\n"))
                try:
                    enteredDOB =  str(input())
                    
                    if enteredDOB == '0' :
                        DOB =0
                        break
                    
                    enteredDOB = datetime.datetime.strptime(enteredDOB, '%d/%m/%Y')  # Code Reference  :  https://www.codegrepper.com/code-examples/python/how+to+verify+date+dd%2Fmm%2Fyyyy+python
                    if enteredDOB is not None:
                        DOB = enteredDOB
                    
                except ValueError:
                    print("Please enter date in correct format.")
            
            if DOB ==0: # Restart loop if 0 entered
                continue                      
                    
                    
            name = None
            while name is None:
                print("Please Enter your Full Name.  (Enter 0 to exit)",sep=("\n"))
                try:
                    enteredName =  str(input()).strip()
                    
                    if enteredName == '0' :
                        name = 0
                        break                    
                    
                    if enteredName is not None and len(enteredName)>0 and enteredName.replace(" ","").isalpha():
                        name = enteredName
                    else:
                        print("Incorrect value entered")
                    
                except ValueError:
                    print("Incorrect value entered")                    

            if name ==0: # Restart loop if 0 entered
                continue             
                        
            
          
            
            guestFound , guest = hotelRegency.retrieve_guest(roomNo, name, DOB)
            
            if not(guestFound) :
                print("Guest not found, please enter valid details.\n")
                input("Press enter to restart.\n")
                continue
            else:
                if guest is not None:                    
                    guest.get_invoice(hotelRegency)
                    guest.check_out(hotelRegency)
                    print("\n\n*********** Checkout Complete ***********")
                    input("Press enter to Exit to main menue \n")
                    guest =None
                
            
                
                        
                        
                
            

    
    
    

