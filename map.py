from items import *
from people import *

room_corridor = {
    "name": "Corridor",

    "description":
    """You are standing at the end of the corridor. You have two options now, either go north to go to the Guard's Office, or go south to go to the Infirmary.""",

    "exits": {"north": "Office", "south": "Infirmary", "east": "Cell"},

    "items": []
}




room_cell = {
    "name": "Cell",

    "description":
    """You are in your cell. You can either go east to go to the Cafeteria, or you can go west to go to the end of the Corridor.""",

    "exits": {"east": "Food", "west": "Corridor"},

    "items": []
}

room_food = {
    "name": "Cafeteria",

    "description":
    """You are in the Cafeteria. You can either go north to go to the Yard, or you can go west to go back to your cell.""",

    "exits":  {"north": "Yard", "west": "Cell"},

    "items": [],

    "people": [people_sisters]
}

room_office = {
    "name": "Guard's Office",

    "description":
    """You are in the Guard's Office. You can go south to go back to the end of the Corridor.""",

    "exits": {"south": "Corridor"},

    "items": [],

    "people": [people_guard]
}

room_infirmary = {
    "name": "Infirmary",

    "description":
    """You are in the Infirmary. You can go north to go back to the end of the Corridor.""",

    "exits": {"north": "Corridor"},

    "items": []
}

room_yard = {
    "name": "Yard",

    "description":
    """You are in the Yard. You can go south to go back to the Cafeteria.""",

    "exits": {"south": "Food"},

    "items": [],

    "people": [people_red]
}



rooms = {
    "Corridor": room_corridor,
    "Cell": room_cell,
    "Food": room_food,
    "Office": room_office,
    "Infirmary": room_infirmary,
    "Yard": room_yard
}
