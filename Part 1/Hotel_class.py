from Room_class import Room
from Guest_class import Guest
class Hotel:
    
    
    def __init__(self, hotelName = '', hotelAddress = ''  ):
        self.hotelName = hotelName
        self.hotelAddress = hotelAddress
        self.rooms = {}  
        self.roomNoAndGuest = {}
        self.roomAvailability = {'Available':[],
                                 'UnAvailable' :[]}
    

    def add_Room(self, room :Room):
        self.rooms[room.roomNo] = room
        self.roomAvailability['Available'].append(room.roomNo)
        
    def add_Rooms(self, roomType, roomFeature, maxLenghtofStay, noOfRoomsToAdd):
        
        for i in range(noOfRoomsToAdd):
            room = Room(roomType, roomFeature, maxLenghtofStay)
            self.add_Room(room)             
        
        
    def process_checkin(self, guest : Guest ,roomNo, enteredNumberOfDays):
        guest.check_in(roomNo, enteredNumberOfDays)
        self.roomNoAndGuest[roomNo] = guest
        self.roomAvailability['Available'].remove(roomNo)
        self.roomAvailability['UnAvailable'].append(roomNo)
         
        
    
    def process_checkout(self):
        pass
    
    def issue_invoices(self):
        pass
    
    def display_rooms(self, numberOfPeople =None, lengthOfStay = None, withView = 'n'  ):
        print("Available rooms as per your search criteria are as follows :")
        
        print("Room Number" , "       Room Description", sep=("\t"))
        
        roomType = 'Single' if numberOfPeople ==1 else 'Double' if numberOfPeople ==2 else 'Suite' if numberOfPeople >2 and numberOfPeople <5 else ''
        roomFeature = 'Deluxe' if withView == 'y' else 'Standard'
        
        for i in range(len(self.roomAvailability['Available'])):
            room = self.rooms[self.roomAvailability['Available'][i]]
            
            #print(room.roomType , room.feature)
                       
            if room.roomType == roomType and room.feature ==  roomFeature and  lengthOfStay <= room.lenghtOfStayAllowed :
                
                print(room.roomNo ,'              ',  room.description , sep=("\t") )
            
    def search_guest(self,DOB,name):
        
        for guest in self.roomNoAndGuest.values():            
            if guest.DOB == DOB and guest.name.strip().lower() == name.strip().lower() : # IF true then guest already checked in 
                return True
        
        return False  
         
    def verify_room(self):
        pass        
    
    #def verify_availability(self):
     #   pass