
class Cinema:

    cinemas = []

    def __init__(self, address, seats):
        self.id = len(Cinema.cinemas)
        self.address = address
        self.seats = seats
        Cinema.cinemas.append(self)

    @classmethod
    def get_cinema_by_id(cls, id):
        for cinema in cls.cinemas:
            if cinema.id == id:
                return cinema
        return "Not found"


