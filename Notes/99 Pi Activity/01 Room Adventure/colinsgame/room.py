

class Room:
    
    def __init__(self, name: str):
        self.name = name
        self.exit_directions = [] # north, south, east, west.
        self.exit_destinations = [] # the rooms
        self.items = []
        self.item_descriptions = []
        self.grabbables = []
    
    # getters/setters
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def exit_directions(self):
        return self._exit_directions
    
    @exit_directions.setter
    def exit_directions(self, value):
        self._exit_directions = value
    
    @property
    def exit_destinations(self):
        return self._exit_destinations 
    
    @exit_destinations.setter
    def exit_destinations(self, value):
        self._exit_destinations = value
    
    @property
    def items(self):
        return self._items 
    
    @items.setter
    def items(self, value):
        self._items = value
    
    @property
    def item_descriptions(self):
        return self._item_descriptions 
    
    @item_descriptions.setter
    def item_descriptions(self, value):
        self._item_descriptions = value
    
    @property
    def grabbables(self):
        return self._grabbables 
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    
    def add_exit(self, exit_direction, exit_destination):
        self.exit_directions.append(exit_direction)
        self.exit_destinations.append(exit_destination)
    
    def add_item(self, item_name, item_description):
        self.items.append(item_name)
        self.item_descriptions.append(item_description)
        
    def add_grabbable(self, new_grabbable):
        self.grabbables.append(new_grabbable)
        
    def delete_grabbable(self, existing_grabbable):
        if existing_grabbable in self.grabbables:
            self.grabbables.remove(existing_grabbable)

    def delete_item(self, existing_item):
        if existing_item in self.items:
            self.items.remove(existing_item)

    
    # __str__ func
    def __str__(self):
        result = ''
        
        # room name
        result += f"Current location: {self.name}\n"
    
        # items in room
        if len(self.items) != 0:
            result += "I see: "
            for item in self.items:
                result += f"{item} "
            result += "\n"
        
        # exits
        if len(self.exit_directions) != 0:
            result += "Exits: "
            for direction in self.exit_directions:
                result += f"{direction} "
        
        return result