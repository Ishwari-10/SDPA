
class Guest:
    """
    Guest class which contains definition related to a guest. The methods are also defnied which allows interaction
    with the class members.
    """
    # global incrementor
    GuestUniqueID_counter = 0
    #guestPresent = set()

    def __init__(self, name, DOB, phoneNumber):
        self.booking = None
        self.name = name
        self.DOB = DOB
        self.phoneNumber = phoneNumber
        self.ID = Guest.GuestUniqueID_counter+1
        Guest.GuestUniqueID_counter = Guest.GuestUniqueID_counter+1

    def set_guest_details(self, name, DOB, phoneNumber):
        """
        Method to set the guest details
        Args:
            name (str): Full Name of the guest making a booking
            DOB (datetime.date): Date of birth of the guest making a booking
            phoneNumber (int): Phone number of the guest making a booking
        Returns:
            None
        """
        self.name = name
        self.DOB = DOB
        self.phoneNumber = phoneNumber

    def check_in(self, roomNo, bookingdays):
        """
        Processing the check in of a guest to the selected room
        Args:
            roomNo (int): Room in which user is going to stay
            bookingdays (int): The number of days user is going to stay with us
        Returns:
            None
        """
        self.booking = roomNo
        self.bookingdays = bookingdays

    def enquire_Room(self, hotel,  numberOfPeople=None, lengthOfStay=None, withView='n'):
        """
        Enquiring Hotel class for available rooms on the basis of search criteria
        Args:
            hotel (Hotel): Hotel class containing details related to hotel
            numberOfPeople (int, optional): Defaults to None.
                Filter to search for the rooms which can have certain number of people.
            lengthOfStay (int, optional): Defaults to None. Filtering room by length of stay
            withView (str, optional): Defaults to 'n' or No. Filtering room on the basis of whether a room has a
                view or not.
        Returns:
            None
        """
        hotel.display_rooms(numberOfPeople, lengthOfStay, withView)

    def check_out(self, hotel):
        # free room in hotel
        hotel.process_checkout(self.booking)

        self.booking = 0

    def get_invoice(self, hotel):
        hotel.issue_invoices(self.booking, self.bookingdays)

    def print_name_DOB(self):
        """
        A method to print the name and date of birth of the user
        Returns:
            None
        """
        print(f'hello {self.name} with dob {self.DOB}')
        print(self.booking)
        print(self.id)


class VIP(Guest):
    """
    Args:
    name(str):
    DOB:
    phoneNumber:
    vip:

    """
   # guestType= 'VIP'

    def __init__(self, name, DOB, phoneNumber, vip):
        super().__init__(name, DOB, phoneNumber)
        self.vip = vip
