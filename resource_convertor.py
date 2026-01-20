from dataclasses import dataclass

@dataclass
class ResourceConvertor:

    #Basic Resources
    energy : float = 0 #Upkeep costs
    minerals : float = 0 #Nemesis crisis costs, lithoids too I think
    food : float = 0 #Living ship costs, upkeep, behemoths
    trade : float = 0 #Probably useless
    alloys : float = 0 #Normal ship costs and upkeep
    consumer_goods : float = 0 #Probably useless

    #Strategic Resources
    exotic_gases : float = 0
    rare_crystals : float = 0
    volatile_motes : float = 0

    #Rare Resources
    zro : float = 0
    dark_matter : float = 0
    living_metal : float = 0
    nanites : float = 0

    #From wiki, engy, min, food = 1 price
    #con_good = 2, alloy = 4
    #strat_resource = 10
    #rare_resource = 20
    cost_values = {
        "energy" : 1, "minerals" : 1, "food" : 1,
        "consumer_goods" : 2, "alloys" : 4,
        "exotic_gases" : 10, "rare_crystals" : 10, "volatile_motes" : 10,
        "zro" : 20, "dark_matter" : 20, "living_metal" : 20, "nanites" : 20,
    }

    def calculate_total_cost(self):
        total=0.0
        #Method to convert costs of all types of resources into one centralized cost
        pass

    def get_total_cost(self):
        return self.calculate_total_cost()


