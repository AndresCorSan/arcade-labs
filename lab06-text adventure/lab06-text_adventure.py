class Room:
    """
    Class for rooms
    """
    def __init__(self, description, north, east, south, west):
        """ This is a method that sets up the variables in the object. """
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    room0 = Room("Estas en el inicio, puedes ir al este o al oeste.", None, 2, None, 1)
    room_list.append(room0)
    room1 = Room("Sala llave", None, 0, None, None)
    room_list.append(room1)
    room2 = Room("Pasillo1", None, 3, None, 0)
    room_list.append(room2)
    room3 = Room("Habitación con enemigo", 4, None, None, 2)
    room_list.append(room3)
    room4 = Room("Pasillo2", 6, None, 3, 5)
    room_list.append(room4)
    room5 = Room("Cofre del tesoro", None, 4, None, None)
    room_list.append(room5)
    room6 = Room("Balcon", 4, None, None, None)
    room_list.append(room6)

    while not done:
        print()
        print(room_list[current_room].description)
        respuesta = input("Where do you want to move next? ---> ")

        if respuesta.lower() == "salir": done = True

        if respuesta.lower() == "north" or respuesta.lower() == "n":
            next_room = room_list[current_room].north
        elif respuesta.lower() == "east" or respuesta.lower() == "e":
            next_room = room_list[current_room].east
        elif respuesta.lower() == "south" or respuesta.lower() == "s":
            next_room = room_list[current_room].south
        elif respuesta.lower() == "west" or respuesta.lower() == "w":
            next_room = room_list[current_room].west

        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    print("You finished the game.")


main()
