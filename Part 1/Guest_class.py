class Guest:
    GuestUniqueID_counter = 0
    #guestPresent = set()
    def __init__ (self ,name , DOB , phoneNumber  ):
        self.booking = None
        self.name=  name
        self.DOB = DOB
        self.phoneNumber = phoneNumber
        self.ID = Guest.GuestUniqueID_counter+1
        Guest.GuestUniqueID_counter  = Guest.GuestUniqueID_counter+1
        #Guest.guestPresent.add(self.ID)
        
    
    def set_guest_details(self,name , DOB , phoneNumber ):
        self.name=  name
        self.DOB = DOB
        self.phoneNumber = phoneNumber
    
    
    def check_in(self,roomNo, bookingdays):
        self.booking = roomNo
        self.bookingdays= bookingdays
        
        
    
    def enquire_Room(self, hotel,  numberOfPeople =None, lengthOfStay = None, withView = 'n'  ):        
        hotel.display_rooms(numberOfPeople,lengthOfStay,withView)
     
    def check_out(self,roomNo):        
        # free room in hotel        
        self.booking = 0
    
    def get_invoice():
        pass        
        
    def print_name_DOB(self):        
        print(f'hello {self.name} with dob {self.DOB}')
        print(self.booking)
        print(self.id)


class VIP(Guest): 
   # guestType= 'VIP'
   def __init__ (self ,name , DOB , phoneNumber,vip  ):
       super().__init__(name, DOB, phoneNumber)
       self.vip = vip
      

    
                
        
        
if __name__ == '__main__':
    guest1 =  VIP('name', '21/02/1991','45454445', 'y')
   # guest1.print_name_DOB()  
   
    print(guest1.phoneNumber)