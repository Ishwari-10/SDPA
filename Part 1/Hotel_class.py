class Hotel:
    
    def __init__(self, hotelName = '', hotelAddress = '', ):
        self.hotelName = hotelName
        self.hotelAddress = hotelAddress
        
    def process_checkin():
        pass
    
    def process_checkout():
        pass
    
    def issue_invoices():
        pass
    
    def display_rooms():
        pass
    
    def verify_availability():
        pass
    
    

class Room:
    
    roomPrices = {'Single' : {'Standard': 40 ,
                               'Deluxe' : 60}, 
                  'Double': {'Standard' : 80,
                             'Deluxe'   : 100}, 
                  'Suite' : {'Standard' : 100,
                             'Deluxe'   : 120}
                  }
    
    def __init__(self , roomNO , roomType , roomFeature):
        self.roomNo = roomNO
        self.roomType = roomType   # double, single ,suite
        self.feature = roomFeature  # standard , Deluxe
                
        
if __name__ == '__main__':
    guest1 =  Guest(1234,'name', '10/09/1999', 25864789)
    guest1.print_name_DOB()  
    vip1 = VIP(123, 'name', 'asd', 123467)
    print(vip1.guestType)