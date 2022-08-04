class Room:    
    roomPrices = {'Single' : {'Standard': 40 ,
                               'Deluxe' : 60}, 
                  'Double': {'Standard' : 80,
                             'Deluxe'   : 100}, 
                  'Suite' : {'Standard' : 100,
                             'Deluxe'   : 120}
                  }
    
    roomNoCounter = 0
    #roomsNoPresent = set()
    
    def __init__(self ,roomType , roomFeature, MaxlenghtOfStay):
        self.roomNo =  Room.roomNoCounter+1
        self.roomType = roomType   # double, single ,suite
        self.feature = roomFeature  # standard , Deluxe
        Room.roomNoCounter =  Room.roomNoCounter+1
        #Room.roomsNoPresent.add(Room.roomNoCounter+1)
        self.lenghtOfStayAllowed = MaxlenghtOfStay
        self.description = roomType+' '+roomFeature+' room'+ (' with a view' if roomFeature =='Deluxe' else ' without a view')
        
    def get_roomPrice(self, roomType , roomFeature , lengthOfStay , guestType):
        
        price = Room.roomPrices[roomType][roomFeature]*lengthOfStay
        
        if guestType== 'VIP':
            price = price*0.9 # 10 % Discount for VIP Guests
        
        return price