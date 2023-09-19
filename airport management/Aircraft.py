from re import findall


class Aircraft:
    def __init__(self, make, code, typ, flight_range) -> None:
        self.make = make
        self.code = code
        self.type = typ
        flight_range += ".0"
        m = findall(r'\d+\.\d+', flight_range)


        self.flight_range = flight_range = float(m[0])

    def get_make(self):
        return self.make

    def get_flight_range(self):
        return self.flight_range

    def __repr__(self) -> str:
        return f"Aircraft make: {self.make} code: {self.code} type: {self.type} range: {self.flight_range}"


# range = Aircraft("airbus", 124, "plane", "1342.0")

# print(range.get_flight_range())
