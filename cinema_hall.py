
class Star_Cinema:
    hall_list = []

    def entry_hall(self, obj):
        self.hall_list.append(vars(obj))


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__id = id
        self.__movie_name = movie_name
        self.__time = time
        self.show_list.append((self.__id, self.__movie_name, self.__time))
        self.list = [["Empty"]*self._cols for _ in range(self._rows)]
        self.seats[id] = self.list

    def book_seats(self, customer_name, phone_number, show_id, seat_list):
        self.__customer_name = customer_name
        self.__phone_number = phone_number
        if show_id not in self.seats.keys():
            print("\nId didn't match with any show!\n")
            return
        self.show_id = show_id
        self.seat_list = seat_list
        for seat in self.seat_list:
            if len(seat) > 2:
                print("\nInvalid Seat number. Try again!!\n")
                return

        for (a, b) in seat_list:
            if a >= self._rows or b >= self._cols:
                print("\nSeat out of range!! Try again\n")
                return
            if self.seats[show_id][a][b] == "Booked":
                print(f"\nSeat {a}{b} already booked. Try again!\n")
                return

        for (a, b) in seat_list:
            if self.seats[show_id][a][b] == "Empty":
                self.seats[show_id][a][b] = "Booked"
        print("\n\n")
        print("-"*10, "TICKET BOOKED SUCCESSFULLY!!", "-"*11)
        print("NAME:", self.__customer_name)
        print("PHONE NUMBER:", self.__phone_number)
        self.temp_movie = ''
        self.temp_time = ''
        for lst in self.show_list:
            if lst[0] == show_id:
                self.temp_movie = lst[1]
                self.temp_time = lst[2]
        print(
            f"MOVIE NAME: { self.temp_movie}\tMOVIE TIME: { self.temp_time}")
        print("YOUR SEATS: ", end="")
        for idx, item in enumerate(self.seat_list):
            for i, j in enumerate(item):
                print(item[i], end="")
            print(end=" ")
        print("\nHall:", self._hall_no)
        print('-'*51)
        print("\n\n")

    def view_show_list(self):
        print("-"*25, "Show List", "-"*25, "\n")
        for lst in self.show_list:
            print("SHOW ID:", lst[0], '\tMOVIE NAME:',
                  lst[1], "\tTIME:", lst[2])
        print()
        print("-"*61, '\n')

    def view_available_seats(self, show_id):
        # print(self.seats[str(show_id)])
        if show_id in self.seats.keys():
            print()
            print("-"*16, "Available Seats", "-"*17)
            self.temp_movie = ''
            self.temp_time = ''
            for lst in self.show_list:
                if lst[0] == show_id:
                    self.temp_movie = lst[1]
                    self.temp_time = lst[2]
            print(
                f"MOVIE NAME: { self.temp_movie}\tMOVIE TIME: { self.temp_time}")
            # print("*True for already booked seats\n")

            # for lst in self.seats[str(show_id)]:
            print()
            for row in range(self._rows):
                for col in range(self._cols):
                    print(
                        f"{row}{col}:({self.seats[show_id][row][col]})\t", end="")
                print()

            print("-"*50, '\n')
        else:
            print("Id didn't match with any show!")


hall = Hall(3, 5, 1)


# print(hall.hall_list)
hall.entry_show("12", "Tarzan", "Nov 2 2022 9pm")
hall.entry_show("13", "Spider Man", "Nov 2 2022 5pm")
# hall.book_seats("mominur", "0258", "12", [(0, 1), (0, 0)])
# print()
# print(hall.seats)
# print(hall.show_list)
# hall.view_show_list()
# hall.view_available_seats("12")

if __name__ == "__main__":
    while True:
        print("1. VIEW ALL SHOWS TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        choice = int(input("ENTER OPTION: "))
        if choice == 1:
            hall.view_show_list()
        elif choice == 2:
            show_id = input("ENTER SHOW ID: ")
            hall.view_available_seats(show_id)
        elif choice == 3:
            name = input("ENTER CUSTOMER NAME: ")
            number = input("ENTER CUSTOMER PHONE NUMBER: ")
            show_id = input("ENTER SHOW ID: ")
            num_of_ticket = int(input("ENTER NUMBER OF TICKETS: "))
            seat_list = []
            for num in range(num_of_ticket):
                seat_no = input(f"ENTER SEAT NO.{num+1}: ")
                seat_no = list(seat_no)
                # if len(seat_no) > 2:

                for idx, val in enumerate(seat_no):
                    seat_no[idx] = int(val)
                seat_no = tuple(seat_no)
                seat_list.append(seat_no)
            hall.book_seats(name, number, show_id, seat_list)
        print("Game end!!!")
