
class Purchase:
    def __init__(self,
                 street,
                 city,
                 baths,
                 beds,
                 state,
                 home_type,
                 longitude,
                 latitude,
                 price,
                 sq__ft,
                 zipcode,
                 sale_date
                 ):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip = zipcode
        self.street = street
        self.city = city

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            int(lookup['baths']),
            int(lookup['beds']),
            lookup['state'],
            lookup['type'],
            float(lookup['longitude']),
            float(lookup['latitude']),
            float(lookup['price']),
            int(lookup['sq__ft']),
            lookup['zip'],
            lookup['sale_date'])
