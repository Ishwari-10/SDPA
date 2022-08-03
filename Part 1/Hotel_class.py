from Room_class import Room
class Hotel:
    
    
    def __init__(self, hotelName = '', hotelAddress = ''  ):
        self.hotelName = hotelName
        self.hotelAddress = hotelAddress
        self.rooms = {}  
        self.roomNoAndGuest = {}
        self.roomAvailability = {'Available':[],
                                 'UnAvailable' :[]}
    

    def addRoom(self, room :Room):
        self.rooms[room.roomNo] = room
        self.roomAvailability['Available'].append(room.roomNo)
        
    def addRooms(self, roomType, roomFeature, maxLenghtofStay, noOfRoomsToAdd):
        
        for i in range(noOfRoomsToAdd):
            room = Room(roomType, roomFeature, maxLenghtofStay)
            self.addRoom(room)             
        
        
    def process_checkin(self):
        pass
    
    def process_checkout(self):
        pass
    
    def issue_invoices(self):
        pass
    
    def display_rooms(self, numberOfPeople =None, lengthOfStay = None, withView = 'no'  ):
        pass
    
    def verify_availability(self):
        pass