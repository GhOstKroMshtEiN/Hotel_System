class Room:
    def __init__(self, number_room, type_room, status='свободен'):
        self.number_room = number_room
        self.type_room = type_room
        self.status = status

    def change_status(self, new_status):
        self.status = new_status

    def information(self):
        return f'Номер комнаты: {self.number_room}, тип комнаты: {self.type_room}, статус: {self.status}'


class Guest:
    def __init__(self, name, check_in_date, check_out_date):
        self.name = name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def information_user(self):
        return f'Гость: {self.name}, дата заезда: {self.check_in_date}, дата выезда: {self.check_out_date}'


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def book_room(self, room_number, guest):
        for room in self.rooms:
            if room.number_room == room_number and room.status == 'свободен':
                room.change_status('занят')
                self.add_guest(guest)
                print(f'Номер {room_number} забронирован гостем {guest.name}')
                return
        print(f'Номер {room_number} не может быть забронирован')

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number_room == room_number and room.status == 'занят':
                room.change_status('свободен')
                print(f'Номер {room_number} освобожден')
                return
        print(f'Номер {room_number} не может быть освобожден')

    def show_all_rooms(self):
        for room in self.rooms:
            print(room.information())

    def show_available_rooms(self):
        for room in self.rooms:
            if room.status == 'свободен':
                print(room.information())
