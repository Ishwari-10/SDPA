class Guest:
   # GuestUniqueID = 0
    def __init__ (self , ID , name , DOB , phoneNumber  ):
        self.id = ID
        self.booking = 0
        self.name=  name
        self.DOB = DOB
        #self.guestUniqueID = Guest.GuestUniqueID+1
        #Guest.GuestUniqueID

        
    def check_in(self,roomNo):
        self.booking = roomNo
    
    def enquireRoom(self, hotel):
        pass     
     
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
    guestType= 'VIP'
      

    
                
        
        
if __name__ == '__main__':
    guest1 =  Guest(1234,'name', '10/09/1999', 25864789)
    guest1.print_name_DOB()  
    vip1 = VIP(123, 'name', 'asd', 123467)
    print(vip1.guestType)