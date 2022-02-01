#Imports a module that is essential for randomness
import random

#The first and second segment for upgrade names.
x1 = ['Druidic','Heroic','Larger','Long','Glaive','MOAR','MOAB','Druid Of','Heart Of','Faster','Improved','Red Hot','Full','Large','Maim','Cripple','Night Vision','Shrapnel','Bouncing','Supply','Elite','Fast','Even Faster','Semi','Burny','Increased','Hard','Thorn','Pop','Sun','True Sun','Laser','Plasma','Dark','Legend Of The','Robo','Tech','Avatar Of','Spirit Of','Super','Flat Pack','One More','Thicker','Strike Down','Diversion','Mo','Weak','Bonus','Big','Targeted','Triple','Enhanced','Cross','Sharp','Super Monkey','Plasma Monkey','More','Even More Tacks','Grape','Hot','Cannon','Double','Sentry','Oversize','Bloon','Ninja','Sharp','Seeking','Bionic','Rapid','Storm Of','Wall Of','Bio','Syphon Funding','Sword','Sacrifical','Magical','Grape','Spy','Neva-Miss','Centered','Operation: Dart','Sky']
x2 = ['Reach','Velocity','Service Area','Lord','Richocet','Glaives','SHREDR','The Jungle','The Forest','The Storm','Oak','Rangs','Press','Domination','Metal Jacket','Calibre','MOAB','Goggles','Shot','Bullet','Drop','Sniper','Defender','Firing','Automatic','Auto Rifle','Stuff','Accuracy','Swarm','Thorns','Wrath','Lust','Avatar','Temple','God','Knight','Champion','Night','Terror','Storm','Buildings','Spike','Foams','The False','Tactics','Monkey Money','Point','Monkey','Bunch','Pineapples','Eyesight','Bow','Shooter','Fan Club','Tacks','Ship','Gun','Expert','Champion','Nails','Trap','Discipline','Shuriken','Jitsu','Boomerang','Arrows','Trees','Barrage','Hack','Funding','Squeeze','Charge','Hex','Totem','Gold','Plane','Targeting','Path','Storm','Shredder']

#The many possible segments of upgrade descriptions.
y1 = ['Camo Bloons','Purple Bloons','Lead Bloons','Camo and Lead Bloons']
y2 = ['Spiked Ball','Dart','Grape Shot','Glue','Glaive','Boomerang','Bomb','Tack','Blade','Bullet','Hot Grape Shot']
y3 = [f'Shoots further and can detect/pop {random.choice(y1)}']

#Prints upgrade name and description, only description is for enchanced eyesight.
print(f'Upgrade name: {random.choice(x1)} {random.choice(x2)}')
x3 = input(f'Upgrade description: {random.choice(y3)}.')