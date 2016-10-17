from items import *

room_corridor = {
    "name": "Corridor",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"north": "Office", "south": "Corridor"},

    "items": []
}




room_cell = {
    "name": "cell",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Admins", "east": "Food", "west": "Corridor"},

    "items": [item_biscuits, item_handbook]
}

room_food = {
    "name": "Cafeteria",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": []
}

room_office = {
    "name": "Guard's Office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": []
}

room_infirmory = {
    "name": "Infirmory",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_yard = {
    "name": "Yard",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen]
}



rooms = {
    "Corridor": room_corridor,
    "Cell": room_cell,
    "Food": room_food,
    "Office": room_office,
    "Infirmory": room_infirmory,
    "Yard": room_yard
}
