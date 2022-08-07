# Importing all the required classes
from Room_class import Room
from Guest_class import Guest
from Guest_class import VIP


class Hotel:
    """
    Hotel class containing all the details on guest and rooms. Also, responsible for check in and check out of guests
    """

    def __init__(self, hotelName='', hotelAddress=''):
        """
       Constructor to initialise the Hotel class fields.
       Args:
           hotelName (str, optional): Defaults to ''. Name of the hotel
           hotelAddress (str, optional): Defaults to ''. Address of the hotel
       """
        self.hotelName = hotelName
        self.hotelAddress = hotelAddress
        self.rooms = {}
        self.roomNoAndGuest = {}
        self.roomAvailability = {'Available': [],
                                 'UnAvailable': []}

    def add_Room(self, room: Room):
        """
        Method to add individual room to the list of available rooms
        Args:
            room (Room): room to add to the list
        Returns:
            None
        """
        self.rooms[room.roomNo] = room
        self.roomAvailability['Available'].append(room.roomNo)

    def add_Rooms(self, roomType, roomFeature, maxLenghtofStay, noOfRoomsToAdd):
        """
        Method to iteratively add multiple rooms with the defined set of properties.
        Args:
            roomType (str): Defining the type of room for eg. 'Single', 'Double' and so on.
            roomFeature (str): Feature describing the size of the room. Possible values 'Standard' and 'Deluxe'
            maxLenghtofStay (int): Defining the maximum days a room can be booked
            noOfRoomsToAdd (int): Number of the rooms to add. This will be used for iteration.
        Returns:
            None
        """

        for i in range(noOfRoomsToAdd):
            room = Room(roomType, roomFeature, maxLenghtofStay)
            self.add_Room(room)

    def process_checkin(self, guest: Guest, roomNo, enteredNumberOfDays):
        """
        Method facilitate room check in process for a guest.
        Args:
            guest (Guest): guest that is checking in
            roomNo (int): Room allocated to the guest
            enteredNumberOfDays (int): Number of days guest is staying in
        Returns:
            None
        """
        guest.check_in(roomNo, enteredNumberOfDays)
        self.roomNoAndGuest[roomNo] = guest
        self.roomAvailability['Available'].remove(roomNo)
        self.roomAvailability['UnAvailable'].append(roomNo)

    def process_checkout(self, roomNo):
        """
        Method facilitate room check out process for a guest.
        Args:

            roomNo (int): Room allocated to the guest

        Returns:
            None
        """
        self.roomNoAndGuest.pop(roomNo, None)
        self.roomAvailability['UnAvailable'].remove(roomNo)
        self.roomAvailability['Available'].append(roomNo)

    def issue_invoices(self, roomNo, bookingdays):
        """
        Generating invoices after the guest check out of the room
        Args:
            roomNo (int): Room allocated to the guest.

            bookingdays (int): length of the stay

        Returns:
            None
        """
        room = self.rooms[roomNo]
        guest = self.roomNoAndGuest[roomNo]
        vipType=''
        if isinstance(roomNo, VIP):
            vipType = guest.vip
                
        room_charge = room.get_roomPrice(bookingdays, vipType) 
        
        print(" Thank Your for staying at {}".format(self.hotelName))
        print("\n ****** Your Invoice ******\n")
        print("Name                  : {}\n".format(guest.name))
        print("Number                : {}\n".format(guest.phoneNumber))
        print("Room Type/Feature     : {}\n".format(room.description))
        print("Number of Days of stay: {}\n".format(bookingdays))
        if vipType=='VIP':
            print("10% Discount Applied for VIP customer")
        print("Total price          :£{}".format(room_charge))
       
       
       
       
    def display_rooms(self, numberOfPeople =None, lengthOfStay = None, withView = 'n'  ):
        """
        Generating and printing list of rooms on the basis of search criteria
        Args:
            numberOfPeople (int, optional): Defaults to None.
                Filter to search for the rooms which can have certain number of people.
            lengthOfStay (int, optional): Defaults to None. Filtering room by length of stay
            withView (str, optional): Defaults to 'n' or No. Filtering room on the basis of whether a room has a
                view or not.
        Returns:
            None
        """
        print("Available rooms as per your search criteria are as follows :")
        
        print("Room Number" , "       Room Description", sep=("\t"))
        
        roomType = 'Single' if numberOfPeople ==1 else 'Double' if numberOfPeople ==2 else 'Suite' if numberOfPeople >2 and numberOfPeople <5 else ''
        roomFeature = 'Deluxe' if withView == 'y' else 'Standard'
        
        for i in range(len(self.roomAvailability['Available'])):
            room = self.rooms[self.roomAvailability['Available'][i]]
            
            # print(room.roomType , room.feature)
                       
            if room.roomType == roomType and room.feature ==  roomFeature and  lengthOfStay <= room.lenghtOfStayAllowed :
                
                print(room.roomNo ,'              ',  room.description , sep=("\t") )
            
    def search_guest(self,DOB,name):
        """
        Look for the guest. Basically, search if the guest has already checked in.
        Args:
            DOB (datetime.date): Date of birth of the user, considered for uniquely identifying a guest
            name (str): Name of the guest
        Returns:
            Whether a guest is already checked in or not (bool)
        """
        # getting only the values of the dictionary, for getting the guest details
        for guest in self.roomNoAndGuest.values():   
            # strip is used to remove whitespaces and making search easier we use lower to convert it into lowercase         
            if guest.DOB == DOB and guest.name.strip().lower() == name.strip().lower() : # IF true then guest already checked in 
                return True
        
        return False  
   
    def retrieve_guest(self,roomNo, name , DOB ):
        # for guest in self.roomNoAndGuest.values():  
        guest = self.roomNoAndGuest[roomNo]
        if guest is not None and guest.DOB == DOB and guest.name.strip().lower() == name.strip().lower() : # IF true then guest already checked in 
            return (True,guest)
        
        return (False,None)
    
    
    def verify_room(self):
        pass        