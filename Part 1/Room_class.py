class Room:
    """
    Room class defining features of the room and their prices.
    """
    roomPrices = {'Single': {'Standard': 40,
                             'Deluxe': 60},
                  'Double': {'Standard': 80,
                             'Deluxe': 100},
                  'Suite': {'Standard': 100,
                            'Deluxe': 120}
                  }

    roomNoCounter = 0

    def __init__(self, roomType, roomFeature, MaxlenghtOfStay):
        """
        Constructor to initialise the Room class object.
        Args:
            roomType (str): Defining the type of room. Possible values are 'Single', 'Double' and 'Suite'
            roomFeature (str): Defining the size of the room on the basis of whether a room has a view or not. Possible values 'Standard' and 'Deluxe'
            MaxlenghtOfStay (int): Defining the maximum number of the day a room can be booked
        """
        self.roomNo = Room.roomNoCounter+1
        self.roomType = roomType   # double, single ,suite
        self.feature = roomFeature  # standard , Deluxe
        Room.roomNoCounter = Room.roomNoCounter+1

        self.lenghtOfStayAllowed = MaxlenghtOfStay
        self.description = roomType+' '+roomFeature+' room' + \
            (' with a view' if roomFeature == 'Deluxe' else ' without a view')

    def get_roomPrice(self, lengthOfStay, guestType):
        """
        Method to get the room price for a particular room on the basis of defined criteria.
        Args:
            lengthOfStay (int): Number of days guest is staying with us.
            guestType (str): This defines the type of guest we have. Whether the guest is VIP or not.
        Returns:
            price (int): Price of the room on the basis of length of stay and guest type.
        """
        # Price of the room on the basis of length of stay.
        price = Room.roomPrices[self.roomType][self.feature]*lengthOfStay

        if guestType == 'VIP':
            price = price*0.9  # 10 % Discount for VIP Guests

        return price
