# Lunar Phases MOTD
This is just a simple program to remind me to get outside and look up at the sky every once and a while, and giving me a cool program to learn python with.

## Goal/Introduction
The primary goal of this program is to show ASCII art of the current lunar phase in my ubuntu server MOTD. It will also show the name of the phase below, and a countdown to when the next new/full moon is. Eventually I also want it to pull International Space Station (ISS) location data from an API and country name/coordinate data from a different API to display which country ISS is above, and countdown to when it will be above Edmonton. 
### Side Note
Though the original intent of this program is to display in my server MOTD, I'm curious to see what other people can do with it and if anyone else has any different use cases!
## Getting started
### Dependencies
- As of now, just requires python3 installed on whatever device you are running the program.
- As an MOTD, ensure the shebang in line 1, explained in 'Executing Program' section
### Installing 
Just click the green code button above and clone with your preferred method.
### Executing Program
- For the regular version, just run: `python3 lunar_phases_motd.py` in your terminal and it will output the correct ASCII.
- If using as an MOTD:
  1. Ensure the shebang `#!/usr/bin/env python3` in line 1
  2. Move the script to a directory on your server, I used `scp lunar_phases_motd.py user@ip:/path/to/folder` to copy from my laptop to my server
  3. Create a symlink into the MOTD directory and assign execute order: `sudo ln -s /path/to/lunar_phases_motd.py /etc/update-motd.d/20-lunar-phases`
  4. Ensure original script(not symlink) is an executable `sudo chmod +x ~/path/to/lunar_phases_motd.py`
 
## Help
As of now it's pretty simple and I haven't experienced any problems. This is my first script and it works without issue for me. If you have any problems, create an issue and let me know! 

## Authors
[JeraltOfRivia](https://github.com/JeraltOfCanada)

## Version History
- 0.1
  - Initial release
 
## License
This project is licensed under the MIT License - See LICENSE.md file for details.

## Acknowledgements
Basically, I looked up 'first python projects' a few months ago. I saw a reddit post where someone did something using ASCII showing the lunar phases, but I basically saw a screenshot of their ASCII and the general idea and then I closed the tab. Then when I decided to write this script I just used the general memory of what that person on reddit had done as inspiration. 
- [README template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
- [Lunar Phase ASCII](https://www.asciiart.eu/art/43240015b2f2240a) This person only included their signature on one of the phases, I copied it to each phase image so it's always visible when the ASCII is printed.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
> I'd love to see what you build with this — if you use it in a project, let me know!
