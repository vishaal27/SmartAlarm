import random
import time
from espeak import espeak

jokes_list=[
'0,"Yo mama so fat, I took a picture of her last Christmas and its still printing."',
'1,"What do you get when you cross a lawyer with the Godfather? An offer you cant understand."',
'2,"Yo mama so poor your family ate cereal with a fork to save milk."',
'3,"Why Does Ariel wear seashells? Because she cant fit into D-shells"',
'4,"If I could have dinner with anyone, dead or alive......I would choose alive."',
'5,"Two guys walk into a bar. The third guy ducks."',
'6,"Why cant Barbie get pregnant? Because Ken comes in a different box."',
'7,"Why was the musician arrested? He got in treble."',
'8,"Did you hear about the guy who blew his entire lottery winnings on a limousine? He had nothing left to chauffeur it."',
'9,"What do you do if a bird shits on your car? Dont ask her out again."',
'10,"He was a real gentlemen and always opened the fridge door for me"',
'11,"Telling my daugthers date that she has lice and its very contagious the closer you get to her. *Correct way to parent."',
'12,"What should you do before criticizing Pac-Man? WAKA WAKA WAKA mile in his shoes"',
'13,"Whats the difference between an illegal Mexican and an autonomous robot...? Nothing... they were both made to steal American jobs."',
'14,"What do you call a barbarian you cant see? an Invisigoth."',
'15,"How do you spell Canda? C,eh,N,eh,D,eh"',
'16,"You ever notice that the most dangerous thing about marijuana is getting caught with it?"',
'17,"What did Arnold Schwarzenegger say at the abortion clinic? Hasta last vista, baby."',
'18,"My wife is in a bad mood. I think her boyfriend forgot their anniversary. Way to go, dude. Now we all suffer..."',
'19,"My speech today will be like a mini-skirt. Long enough to cover the essentials but short enough to hold your attention!"',
'20," What does Miley Cyrus eat for Thanksgiving? Twerky! Just kidding... Drugs. She eats drugs."',
'21,"Why do you never see elephants hiding in trees? Cause they are freaking good at it"',
'22,"How did the blonde die raking leaves? She fell out of the tree."',
'23,"That guy is such a douche-bag! Is he single? Maybe I can fix him!  women"',
'24,"My son just got a tattoo of a heart, a spade, a club, and a diamond, all without my permission. I guess Ill deal with him later."',
'25,"What do you call a potato in space? Spudnik"']

ch=random.randint(0,25)
chosen=jokes_list[ch]
if(chosen[1]=='0' or chosen[1]=='1' or chosen[1]=='2' or chosen[1]=='3' or chosen[1]=='4' or chosen[1]=='5' or chosen[1]=='6' or chosen[1]=='7' or chosen[1]=='8' or chosen[1]=='9'):
    speak=chosen[4:]
else:
    speak=chosen[3:]
print(speak)
espeak.synth(speak)
time.sleep(7)
espeak.synth('Haha')
time.sleep(3)