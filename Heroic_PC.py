#Heroic NPC Generation

from bisect import bisect_left
import numpy as np
import random


class OptionsWeightsLengthMismatchException(BaseException):
    """Raises when the number of elements in the options list doesn't match the
    number of elements in the weight list."""
    pass


# Using an class
class RollTable:

    def __init__(self, options: list, weights: np.array) -> "RollTable":
        self.options = options
        self.weights = weights
        self._validate_inputs()
        pdf = weights/np.sum(weights)
        self.cdf = np.cumsum(pdf)

    def _validate_inputs(self) -> None:
        if len(self.options) != self.weights.size:
            raise OptionsWeightsLengthMismatchException(f"options and weights must have the same number of elements.")
        if max(self.weights.shape) != np.prod(self.weights.shape): # i.e. make sure it's 1D
            raise ValueError("Weights must be 1D, i.e. only one non-singular dimension.")

    def get_item(self):
        roll = np.random.random()
        idx = bisect_left(self.cdf, roll)
        return self.options[idx]

class PC:
    def __init__(self):
        self.age = random.randint(18,65)
        self.attributes = {
                "Strength":0,
                "Dexterity":0,
                "Constitution":0,
                "Intelligence":0,
                "Wisdom":0,
                "Charisma":0,
                }
        self.background = "Unknown"
        self.skills = []
        self.wealth = "Middle Class"
        self.social = "Middle Class"
        self.gen_new()

    def gen_new(self):
        #Roll Stats
        for k, v in self.attributes.items():
            self.attributes[k] = stat_roll.get_item()
        
        #Background
        self.background = random.choice(["Barbarian", "Clergy", "Courtesan", "Criminal", "Dilettante", "Entertainer", "Merchant", "Noble", "Official", "Peasant", "Physician", "Pilot", "Politician", "Scholar", "Soldier", "Spacer", "Technician", "Thug", "Vagabond", "Worker"])
        
        #Skills
        if self.background == "Barbarian":
            self.skills = ["Survive", random.choice(["+1 Any Stat", "+2 Physical", "+2 Physical", "+2 Mental", "Exert", "Any Skill"]), random.choice(["Any Combat", "Connect", "Exert", "Lead", "Notice", "Punch", "Sneak", "Survive"]), random.choice(["Any Combat", "Connect", "Exert", "Lead", "Notice", "Punch", "Sneak", "Survive"])]
        
        if "Clergy" in self.background:
            self.skills = ["Talk", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Connect", "Know", "Lead", "Notice", "Perform", "Talk", "Talk"]), random.choice(["Administer", "Connect", "Know", "Lead", "Notice", "Perform", "Talk", "Talk"])] 
            
        if "Courtesan" in self.background:
            self.skills = ["Perform", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Perform", "Survive", "Talk", "Trade"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Perform", "Survive", "Talk", "Trade"])]
            
        if "Criminal" in self.background:
            self.skills = ["Sneak", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Any Combat", "Connect", "Program", "Notice", "Sneak", "Talk", "Trade"]), random.choice(["Administer", "Any Combat", "Connect", "Program", "Notice", "Sneak", "Talk", "Trade"])] 
            
        if "Dilettante" in self.background:
            self.skills = ["Connect", random.choice(["+1 Any Stat", "+1 Any Stat", "+1 Any Stat", "+1 Any Stat", "Connect", "Any Skill"]), random.choice(["Any Skill", "Any Skill", "Connect", "Know", "Perform", "Pilot", "Talk", "Trade"]), random.choice(["Any Skill", "Any Skill", "Connect", "Know", "Perform", "Pilot", "Talk", "Trade"])] 
            
        if "Entertainer" in self.background:
            self.skills =  ["Perform", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Perform", "Perform", "Talk", "Sneak"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Perform", "Perform", "Talk", "Sneak"])] 
            
        if "Merchant" in self.background:
            self.skills =  ["Trade", random.choice(["+1 Any Stat", "+2 Mental", "+2 Mental", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Any Combat", "Connect", "Fix", "Notice", "Know", "Talk", "Trade"]), random.choice(["Administer", "Any Combat", "Connect", "Fix", "Notice", "Know", "Talk", "Trade"])]
            
        if "Noble" in self.background:
            self.skills =  ["Lead", random.choice(["+1 Any Stat", "+2 Mental", "+2 Mental", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Any Combat", "Connect", "Lead", "Notice", "Know", "Talk", "Pilot"]), random.choice(["Administer", "Any Combat", "Connect", "Lead", "Notice", "Know", "Talk", "Pilot"])] 
            
        if "Official" in self.background:
            self.skills =  ["Administer", random.choice(["+1 Any Stat", "+2 Mental", "+2 Mental", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Any Skill", "Connect", "Lead", "Notice", "Know", "Talk", "Trade"]), random.choice(["Administer", "Any Skill", "Connect", "Lead", "Notice", "Know", "Talk", "Trade"])] 
            
        if "Peasant" in self.background:
            self.skills =  ["Exert", random.choice(["+1 Any Stat", "+2 Physical", "+2 Physical", "+2 Physical", "Exert", "Any Skill"]), random.choice(["Connect", "Exert", "Fix", "Notice", "Sneak", "Survive", "Trade", "Work"]), random.choice(["Connect", "Exert", "Fix", "Notice", "Sneak", "Survive", "Trade", "Work"])] 
            
        if "Physician" in self.background:
            self.skills =  ["Heal", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Fix", "Connect", "Heal", "Notice", "Know", "Talk", "Trade"]), random.choice(["Administer", "Fix", "Connect", "Heal", "Notice", "Know", "Talk", "Trade"])] 
            
        if "Pilot" in self.background:
            self.skills =  ["Pilot", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Physical", "Connect", "Any Skill"]), random.choice(["Exert", "Fix", "Connect", "Pilot", "Notice", "Pilot", "Shoot", "Trade"]), random.choice(["Exert", "Fix", "Connect", "Pilot", "Notice", "Pilot", "Shoot", "Trade"])] 
            
        if "Politician" in self.background:
            self.skills =  ["Talk", random.choice(["+1 Any Stat", "+2 Mental", "+2 Mental", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Connect", "Connect", "Lead", "Notice", "Perform", "Talk", "Talk"]), random.choice(["Administer", "Connect", "Connect", "Lead", "Notice", "Perform", "Talk", "Talk"])] 
            
        if "Scholar" in self.background:  
            self.skills =  ["Know", random.choice(["+1 Any Stat", "+2 Mental", "+2 Mental", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Connect", "Fix", "Know", "Notice", "Perform", "Program", "Talk"]), random.choice(["Administer", "Connect", "Fix", "Know", "Notice", "Perform", "Program", "Talk"])] 
            
        if "Soldier" in self.background:
            self.skills =  ["Any Combat", random.choice(["+1 Any Stat", "+2 Physical", "+2 Physical", "+2 Physical", "Exert", "Any Skill"]), random.choice(["Administer", "Any Combat", "Exert", "Fix", "Notice", "Lead", "Sneak", "Survive"]), random.choice(["Administer", "Any Combat", "Exert", "Fix", "Notice", "Lead", "Sneak", "Survive"])]
            
        if "Spacer" in self.background:
            self.skills =  ["Fix", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Physical", "Exert", "Any Skill"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Know", "Pilot", "Program", "Talk"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Know", "Pilot", "Program", "Talk"])] 
            
        if "Technician" in self.background:
            self.skills =  ["Fix", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Mental", "Connect", "Any Skill"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Know", "Fix", "Notice", "Pilot"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Know", "Fix", "Notice", "Pilot"])] 
            
        if "Thug" in self.background:
            self.skills =  ["Any Combat", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Physical", "Connect", "Any Skill"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Sneak", "Stab or Shoot", "Survive", "Talk"]), random.choice(["Any Combat", "Connect", "Exert", "Notice", "Sneak", "Stab or Shoot", "Survive", "Talk"])]
            
        if "Vagabond" in self.background:
            self.skills =  ["Survive", random.choice(["+1 Any Stat", "+2 Mental", "+2 Physical", "+2 Physical", "Exert", "Any Skill"]), random.choice(["Any Combat", "Connect", "Perform", "Notice", "Sneak", "Pilot", "Survive", "Work"]), random.choice(["Any Combat", "Connect", "Perform", "Notice", "Sneak", "Pilot", "Survive", "Work"])] 
            
        if "Worker" in self.background:
            self.skills =  ["Work", random.choice(["+1 Any Stat", "+1 Any Stat", "+1 Any Stat", "+1 Any Stat", "Exert", "Any Skill"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Any Skill", "Work", "Program", "Pilot"]), random.choice(["Administer", "Connect", "Exert", "Fix", "Any Skill", "Work", "Program", "Pilot"])] 
            
        #Wealth background
        self.wealth = wealth_status_roll.get_item() + " class wealth"
        
        #Social Status background
        self.status = wealth_status_roll.get_item() + " class status"

    def get_summary(self):
        print('\n', "----Statistics----")
        for k, v in self.attributes.items():
            print (k, ' -- ', v, ' -- ', round((v-10)/4))
        print('\n', "----Character Development----")
        print("Background: ", self.background)
        print("Family Wealth: ", self.wealth)
        print("Family Social Status: ", self.status)
        print("Skills:", self.skills)
        
        print("\nReminder: Raise any stat of choice to 18.\nNo skills can start above Level-1, if the sheet suggests more, choose any other skill.")

#%%
#### Roll Tables ####
stat_roll = RollTable([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], np.array([0.0771604938272,0.308641975309,0.771604938272,1.62037037037,2.93209876543,4.78395061728,7.02160493827,9.41358024691,11.4197530864,12.8858024691,13.2716049383,12.3456790123,10.1080246914,7.25308641975,4.16666666667,1.62037037037]))

wealth_status_roll = RollTable(["Low", "Medium", "High"], np.array([0.165, 0.67, 0.165]))

#%% Test area
test = PC()
test.get_summary()
