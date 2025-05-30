class Property:
    def __init__(self, area, neighborhood, bedrooms, living_rooms, bathrooms, parking_spaces, property_type, price, source):
        self.area = area
        self.neighborhood = neighborhood
        self.bedrooms = bedrooms
        self.living_rooms = living_rooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.property_type = property_type
        self.price = price
        self.source =  source

    def toDictionary(self):
        return {
            "area": self.area,
            "neighborhood": self.neighborhood,
            "bedrooms": self.bedrooms,
            "living_rooms": self.living_rooms,
            "bathrooms": self.bathrooms,
            "parking_spaces": self.parking_spaces,
            "property_type": self.property_type,
            "price": self.price,
            "source": self.source
        }