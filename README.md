
 Laser Pong

 by Sam Neurohack (Team Laser /tmp/lab)

 Based on Laser Hexagon by pclf.



BE SMART ! LASERS ARE DANGEROUS. AVOID DIRECT AND NON DIRECT EYES EXPOSURE AT ANY COST.
Lasers are Universe Class Boss that cannot be defeated. Your eyes will be killed instantly. Yes,... seriously !!

You must comply to your local laws.



Features :

+ Dead Simple Pong : first to eleven wins.
+ It's playable without laser or controller devices.
+ It's meant to be used with an awesome network ether-dream ILDA controller and RGB laser
+ Easy parameters modifications : see globalVars.py 
+ Some calibration code appeared since Laser Hexagon to center and zoom the play area easily within ether dream/laser space. Play with your keyboard keys. 
+ Cross platform.
+ To play : Left player use A Q, right player use UP and DOWN.
+ A few line to draw, you don't need a 30 kpps device. We tried on many 25 and 30 kpps lasers.
+ Logo screen
+ Self explanatory code.
 

Launch :

python main.py


Requirements :

- pygame. Tested with 1.9 version. We've seen some pygame bugs with a 32 bits linux. On OS X : try brew install pygame.



Todo :
 
- Make alignement/calibration persistent.
- More code cleaning. 
- Make original rotary pads.
- Optimize points generation to make nice lines.
- Add sound. This code is basically the same than Laser Hexagon, so you get there the sound code.  



Good to know :

+ Most of the code runs depending of the game state "gstt.fs" (logo, actual game, waiting for start)
+ Some laser has Y and X directions not easily changeable : in renderer.py see the line 

return (x, y, ((c >> 16) & 0xFF) << 8, ((c >> 8) & 0xFF) << 8, (c & 0xFF) << 8)

You can change x and y to -x or -y to suit your needs.

+ If you need speed you can remove some lines like all with "filet" that draws the middle line.
+ In the simulator display on your computer screen, there is extra blue lines that helps you to see the invisible lines between objects. You can reorder them to improve laser speed.
+ ILDA cables are crazy too expensive. Because of the beauty of ether dream, buy/make a small ILDA between laser and the controller, then use network cable. 
+ Keep this dedicated network simple. For public shows and for each laser, we use one computer, one network cable and one ether dream. No wifi, no router. Put an autoplay.txt inside the ether dream with a fixed IP. 



Sorry :
- Variables, functions,... are English but source comments are mainly in french :(
- This is certainly not the best python programming ever. It's not our goal.




Laser safety :

- Most important things to understand are basic optics in different materials, laser class, Maximum Permissible Exposure aka MPE and NOHD. http://www.research.northwestern.edu/ors/forms/laser-safety-handbook.pdf
- Of course "there is some apps for that". Search MPE.
- Educate yourself, there is nice online classes. Your eyes worth the fee (i.e lia.org)
