# Lunar Phases MOTD
## Goal/Introduction
The primary goal of this program is to show ASCII art of the current lunar phase in my ubuntu server MOTD. It will also show the name of the phase below, and a countdown to when the next new/full moon is. Eventually I also want it to pull ISS location data from an API and country name/coordinate data from a different API to display which country ISS is currently above, and countdown to when it will be above Edmonton.
~~Also maybe Voyager 1/2 distances from earth.~~ Not as interesting for scope of project. Could find some way to include voyager data in future  
### Major functions/loops in the code
Function to calculate remainder using modulo variable. The remainder would be compared to todays current date, and print the countdowns, and the ASCII image.  
## Research
### Questions
**Lunar phase is 29.53 days, what's a fixed historical date when a new moon occurred that I can always measure forward from**
Julian new moon epoch: J2000.0 Epoch - January 6 2000 at 12 noon (approximately 18:14UTC) use the current Julian date minus the Julian new moon epoch, take the remainder of this output divided by 29.5 using the modulo variable. x= (j-e) % 29.5. Theres 8 lunar phases, new, waxing crescent, first quarter, waxing gibbous, full moon, waning gibbous, last quarter, waning crescent. 3.7 days for every lunar phase.If x = 0, new moon, if x = 14.75, full moon. Ect. 
Store Lunar phase ASCII art as key:value pairs in a 'lunar_phases' dictionary
So I have a dictionary at the start of the code that I assign the ASII images to. 
Then I have a function that calculates the remainder of todays julian date and the julian epoch, and assign it to the variable of whatever(something to do with lunar phase, don't want x)
Then I have 8 different if then statements, each one checking if the lunar phase variable is in range of which lunar phase, i asign the phase name, and then print the lunar phase

**ISS Location and next pass over Edmonton?**
https://open-notify-api.readthedocs.io/en/latest/iss_pass.html
https://openweathermap.org/api/geocoding-api?collection=other
**Can voyager 1/2 information be a calculation, or does it need to pull from API?**
Distance of voyagers can be calculated, but its too complicated for the scope of this project. Pulling from API is better
 
### Potential improvements once core program is complete
Include calculations to show countdowns as to when favourite planets are at optimal viewing positions, major lunar events, comets, solar/lunar eclipses. Show countdowns to upcoming major astronomical events, such as major space missions by pulling from an API
