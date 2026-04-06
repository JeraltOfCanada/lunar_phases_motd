import time 
import math
# Calculating where in a 29.53 day lunar phase todays date is
# Defining function 'lunar_phase' and passing 'phase_calculation' into function
def lunar_phase():
    # Converting time since unix epoch to days, assigning variable 'jd'
    jd = time.time() / 86400 + 2440587.5 
    """
    Subtracting Julian date of last new moon from current JD
    Last new moon was 2461118.3097222 (2026-03-18 19:26:00). 
    Calculating remainder of time since new moon and 29.53 
    """
    phase_calculation = (jd - 2461118.3097222) % 29.53
    return phase_calculation

# Defining lunar phases dictionary for lunar phase ASCII
phases_dict = {
"NEW MOON" : 
"""
       _..._     
     .'     `.    
    :         :    
    :         :  
    `.       .'  
jgs   `-...-'  
""", 
"WAXING CRESCENT" : 
"""
       _..._     
     .'   `::.    
    :       :::    
    :       :::  
    `.     .::'  
jgs   `-..:'' 
""", 
"FIRST QUARTER" : 
"""
       _..._     
     .'  ::::.    
    :    ::::::    
    :    ::::::  
    `.   :::::'  
jgs   `-.::''   
""", 
"WAXING GIBBOUS" : 
""" 
       _..._     
     .' .::::.    
    :  ::::::::    
    :  ::::::::  
    `. '::::::'  
jgs   `-.::''  
""", 
"FULL MOON" : 
"""    
       _..._     
     .:::::::.    
    :::::::::::   
    ::::::::::: 
    `:::::::::'  
jgs   `':::'' 
""", 
"WANING GIBBOUS" : 
""" 
       _..._     
     .::::. `.    
    :::::::.  :    
    ::::::::  :  
    `::::::' .'  
jgs   `'::'-'
 """, 
 "THIRD QUARTER" : 
 """
       _..._     
     .::::  `.    
    ::::::    :    
    ::::::    :  
    `:::::   .'  
jgs   `'::.-'   
""", 
"WANING CRESCENT" : 
"""  
       _..._     
     .::'   `.    
    :::       :    
    :::       :  
    `::.     .'  
jgs   `':..-'
"""
}
# Starting at full moon just reverse string

# boundary points for lunar phase
"""
Waxing crescent: 0-6.375
First quarter: 6.375-7.375
Waxing gibbous: 7.375-13.75
Full moon: 13.75-14.75
Waning Gibbous: 14.75 - 21.125
Last quarter: 21.125-22.125
Waning crescent: 22.125-28.5
New moon: 28.5-29.5
"""

# Assining output of lunar_phase() function to variable 'phase'
phase = lunar_phase()
# Calculating days to next full/new moon and assigning variable 'cntdwn' & 'cntdwn2'
cntdwn = math.floor(14.75 - phase)
cntdwn2 = math.floor(29.5 - phase)
# make lunar halfpoints a constant
# Assigning variable 'day' for propper grammar
day = "day" if cntdwn == 1 else "days"
day2 = "day" if cntdwn2 == 1 else "days"
# ^create plural function

# Remove the # if you want to print the output of the function above
# Commented out by default because it's unnecessary
# print(phase)

# Assigning a physical phase to the calculated date 
# printing ASCII, phase name, and countdown to next new/full moon
if 0 < phase <= 6.375 :
    print(phases_dict["WAXING CRESCENT"])
    print("Today the moon is a WAXING CRESCENT")
    print(f"{cntdwn} {day} until next Full Moon")
elif 6.375 < phase <= 7.375 :
    print(phases_dict["FIRST QUARTER"])
    print("Today the moon is starting its FIRST QUARTER")
    print(f"{cntdwn} {day} until next Full Moon")
elif 7.375 < phase <= 13.75 :
    print(phases_dict["WAXING GIBBOUS"])
    print("Today the moon is a WAXING GIBBOUS")
    print(f"{cntdwn} {day} until next Full Moon")
elif 13.75 < phase <= 14.75 :
    print(phases_dict["FULL MOON"])
    print("Today is the FULL MOON!")
elif 14.75 < phase <= 21.125 :
    print(phases_dict["WANING GIBBOUS"])
    print("Today the moon is a WANING GIBBOUS")
    print(f"{cntdwn2} {day2} until next New Moon")
elif 21.125 < phase <= 22.125 :
    print(phases_dict["LAST QUARTER"])
    print("Today the moon is starting its LAST QUARTER")
    print(f"{cntdwn2} {day2} until next New Moon")
elif 22.125 < phase <= 28.5 :
    print(phases_dict["WANING CRESCENT"])
    print("Today the moon is a WANING CRESCENT")
    print(f"{cntdwn2} {day2} until next New Moon")
else:
    print(phases_dict["NEW MOON"])
    print("Today is the NEW MOON!")

# Add a timer that times from beginning of code to end of code and prints the time
# for comparison of future versions
# Write all future versions separatelt to show changes in the code.     
# Move full/new moon logic to bottom
# write binary search/bisection for fun
# variable scoping
