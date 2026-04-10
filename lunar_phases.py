import time 
import math

SECONDS_IN_DAY = 86400
JULIAN_DATE_UNIX_EPOCH = 2440587.5
JULIAN_DATE_MARCH_NEW_MOON = 2461118.3097222
LUNAR_PHASE_LENGTH = 29.53
LUNAR_PHASE_HALFPOINT = 14.765
NEW_MOON_HIGH = 29.53
NEW_MOON_LOW = 28.53
FULL_MOON_HIGH = 14.765
FULL_MOON_LOW = 13.765
FIRST_QUARTER_HIGH = 7.3825
FIRST_QUARTER_LOW = 6.3825
THIRD_QUARTER_HIGH = 22.1475
THIRD_QUARTER_LOW = 21.1475

def lunar_phase():
    """Function calculates where today falls inside a lunar phase."""
    current_julian_date = time.time() / SECONDS_IN_DAY + JULIAN_DATE_UNIX_EPOCH 
    phase_calculation = (current_julian_date - JULIAN_DATE_MARCH_NEW_MOON) % LUNAR_PHASE_LENGTH
    return phase_calculation

class LunarPhase:
    """Class LunarPhase for holding the phase information for each phase and a
    check at the end if the phase_calculation falls within that class."""
    def __init__(self, low, high, name, art):
       self.low = low
       self.high = high
       self.name = name
       self.art = art
    def is_active(self, phase):
      return self.low < phase <= self.high

new_moon = LunarPhase(NEW_MOON_LOW, NEW_MOON_HIGH, "NEW MOON", 
"""
       _..._     
     .'     `.    
    :         :    
    :         :  
    `.       .'  
jgs   `-...-'  
""")

waxing_crescent = LunarPhase(NEW_MOON_HIGH, FIRST_QUARTER_LOW, "WAXING CRESCENT", 
"""
       _..._     
     .'   `::.    
    :       :::    
    :       :::  
    `.     .::'  
jgs   `-..:'' 
""")

first_quarter = LunarPhase(FIRST_QUARTER_LOW, FIRST_QUARTER_HIGH, "FIRST QUARTER", """
       _..._     
     .'  ::::.    
    :    ::::::    
    :    ::::::  
    `.   :::::'  
jgs   `-.::''   
""")

waxing_gibbous = LunarPhase(FIRST_QUARTER_HIGH, FULL_MOON_LOW, "WAXING GIBBOUS", 
""" 
       _..._     
     .' .::::.    
    :  ::::::::    
    :  ::::::::  
    `. '::::::'  
jgs   `-.::''  
""")

full_moon = LunarPhase(FULL_MOON_LOW, FULL_MOON_HIGH, "FULL MOON", 
"""    
       _..._     
     .:::::::.    
    :::::::::::   
    ::::::::::: 
    `:::::::::'  
jgs   `':::'' 
""")

waning_gibbous = LunarPhase(FULL_MOON_HIGH, THIRD_QUARTER_LOW, "WANING GIBBOUS", 
""" 
       _..._     
     .::::. `.    
    :::::::.  :    
    ::::::::  :  
    `::::::' .'  
jgs   `'::'-'
 """)

third_quarter = LunarPhase(THIRD_QUARTER_LOW, THIRD_QUARTER_HIGH, "THIRD QUARTER", 
"""
       _..._     
     .::::  `.    
    ::::::    :    
    ::::::    :  
    `:::::   .'  
jgs   `'::.-'   
""")

waning_crescent = LunarPhase(THIRD_QUARTER_HIGH, NEW_MOON_LOW, "WANING CRESCENT", 
"""  
       _..._     
     .::'   `.    
    :::       :    
    :::       :  
    `::.     .'  
jgs   `':..-'
""")



phases = [new_moon, waxing_crescent, first_quarter, waxing_gibbous, full_moon, 
waning_gibbous, third_quarter, waning_crescent]

# Remove the # if you want to print the output of the lunar_phase() function
# print(phase)

if __name__ == "__main__":

    phase = lunar_phase()
   
    for current_phase in phases:
        if current_phase.is_active(phase):
            print(current_phase.art)
            print(current_phase.name)

# Calculating days to next full/new moon
    cntdwn = math.floor(LUNAR_PHASE_HALFPOINT - phase)
    cntdwn2 = math.floor(LUNAR_PHASE_LENGTH - phase)

# Assigning variable 'day' for propper grammar
    day = "day" if cntdwn == 1 else "days"
    day2 = "day" if cntdwn2 == 1 else "days"

    if phase < LUNAR_PHASE_HALFPOINT:
        print(f"{cntdwn} {day} until next Full Moon")
    else:
        print(f"{cntdwn2} {day2} until next New Moon")