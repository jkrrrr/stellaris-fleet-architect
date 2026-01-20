from dataclasses import dataclass
from resource_convertor import ResourceConvertor

@dataclass(frozen=True) #Might want to keep frozen
class Ship:
    ship_id: str
    base_hull: float
    base_armour: float
    base_shields: float #Think this is always 0?
    base_evasion: float
    base_speed: float
    size: int
    disengage_chance : float #If we want to account for this, probably not
    base_alloy_cost: float 

    weapon_slots : None #Use a dictionary to store available components?
    defensive_slots : None
    utility_slots : None

    ship_sections : None #Use stored data to find available section types for a given ship

    def take_damage(self, amount):
        #Need to account for damage bonsuses + pen
        #shield_dmg = amount * shield_bonus
        #shields -= shield_dmg
        #amount -= shield_dmg + amount * shield_pen? Something like this
        #armour -= amount * armour_bonus
        pass

    @property
    def total_cost(self):
        #Calculate a way to find total alloy costs
        return self.base_alloy_cost
    
#Something like this to create a ship design?
corvette = Ship(
    ship_id="corvette",
    base_hull=100,
    base_armour=0,
    base_shields=0,
    base_evasion=0,
    base_speed=0,
    size=1,
    disengage_chance=0,
    base_alloy_cost=0,
    weapon_slots=None,
    defensive_slots=None,
    utility_slots=None,
    ship_sections=None
    )
