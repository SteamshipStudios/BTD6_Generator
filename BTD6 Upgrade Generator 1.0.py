import random
x1 = ['Druidic','Heroic','Larger','Long','Glaive','MOAR','MOAB','Druid Of','Heart Of','Faster','Improved','Red Hot','Full','Large','Maim','Cripple','Night Vision','Shrapnel','Bouncing','Supply','Elite','Fast','Even Faster','Semi','Burny','Increased','Hard','Thorn','Pop','Sun','True Sun','Laser','Plasma','Dark','Legend Of The','Robo','Tech','Avatar Of','Spirit Of','Super','Flat Pack','One More','Thicker','Strike Down','Diversion','Mo','Weak','Bonus','Big','Targeted','Triple','Enhanced','Cross','Sharp','Super Monkey','Plasma Monkey','More','Even More Tacks','Grape','Hot','Cannon','Double','Sentry','Oversize','Bloon','Ninja','Sharp','Seeking','Bionic','Rapid','Storm Of','Wall Of','Bio','Syphon Funding','Sword','Sacrifical','Magical','Grape']
x2 = ['Reach','Velocity','Service Area','Lord','Richocet','Glaives','SHREDR','The Jungle','The Forest','The Storm','Oak','Rangs','Press','Domination','Metal Jacket','Calibre','MOAB','Goggles','Shot','Bullet','Drop','Sniper','Defender','Firing','Automatic','Auto Rifle','Stuff','Accuracy','Swarm','Thorns','Wrath','Lust','Avatar','Temple','God','Knight','Champion','Night','Terror','Storm','Buildings','Spike','Foams','The False','Tactics','Monkey Money','Point','Monkey','Bunch','Pineapples','Eyesight','Bow','Shooter','Fan Club','Tacks','Ship','Gun','Expert','Champion','Nails','Trap','Discipline','Shuriken','Jitsu','Boomerang','Arrows','Trees','Barrage','Hack','Funding','Squeeze','Charge','Hex','Totem','Gold']
y1 = ['the druid','the engineer monkey','the sun avatar','Gwendolin','Pat Fusty','the sniper monkey','the dart monkey','the monkey sub','the monkey buccaner','the wizard monkey']
y2 = ['boomerangs','shurikens','grape shot','darts','nails','thorns']
y4 = ['richocet','pop lead and frozen bloons','shred MOABs']
y3 = [f'shoots {random.randint(2,5)}x as fast',f'shoots out firey {random.choice(y2)}','pops lead and frozen bloons','detects camo',f'shoots {random.randint(2,5)} {random.choice(y2)} at once',f'shoots {random.choice(y2)} that {random.choice(y4)}']
print(f'Upgrade name: {random.choice(x1)} {random.choice(x2)}')
x3 = input(f'Upgrade description: {random.choice(y1)} now {random.choice(y3)}.')