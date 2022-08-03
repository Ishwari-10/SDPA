from  Room_class import Room
from Hotel_class import Hotel
from Guest_class import Guest


hotelName='Hotel Regency'
hotelAddress = 'Britol City Center'
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
    
    hotelRegency = Hotel(hotelName=hotelName, hotelAddress= hotelAddress)
    
    
    print('adding Rooms')
    # single standard
    hotelRegency.addRooms('Single', 'Standard', maxLengthOfStay['Single']['Standard'], singleStandard)
    hotelRegency.addRooms('Single', 'Deluxe', maxLengthOfStay['Single']['Deluxe'], singleStandard)
    
    hotelRegency.addRooms('Double', 'Standard', maxLengthOfStay['Double']['Standard'], doubleStandard)
    hotelRegency.addRooms('Double', 'Deluxe', maxLengthOfStay['Double']['Deluxe'], doubleDeluxe)
    
    hotelRegency.addRooms('Suite', 'Standard', maxLengthOfStay['Suite']['Standard'], suiteStandard)
    hotelRegency.addRooms('Suite', 'Deluxe', maxLengthOfStay['Suite']['Deluxe'], suiteDeluxe)
   
    print(hotelRegency.roomAvailability)
    
    #print(hotelRegency.rooms)
    
    
    print(hotelRegency.hotelName, ' is open for Guests')

    while True:
        print("\n")
        print("We have {} rooms available".format(len(hotelRegency.rooms)))
        print("\n")
        print("Please select Available Options")
        
        option1 =None
        
        while option1 is None:
            print("1. Search Available Rooms",
                  "2. Check in",
                  "3. Check Out " ,sep=("\n"))
            try:
                value =  int(input())
                if value in [1,2,3]:
                    option1 = value
                else:
                    print("Please enter correct option")
            except ValueError:
                print("Please enter a number from the options")
        
        
        if option1==1:
            print("Please select Search Criteria")
            
            option2 = None
            
            while option2 is None:
                print("1. Search Available Rooms",
                  "2. Check in",
                  "3. Check Out " ,sep=("\n"))
            try:
                value =  int(input())
                if value in [1,2,3]:
                    option1 = value
                else:
                    print("Please enter correct option")
            except ValueError:
                print("Please enter a number from the options")
        
        
        
        
        elif option1 ==2:
        
            pass
        
        
        
        
        
        
        elif option1 ==3:
            
            pass