# This is the main storyline of a game where your character is a teacher of a subject that you decide upon early
#  in the game.  It is a Friday and you are trying to make your way through 10 hallways to escape the building. 
#  Every hallway has a randomly generated opponent---student, parent, coworker, or administrator (main boss).
#  The player has the option to run, listen patiently, or create an excuse to leave. Every opponent has varying
#  percentages that each method will/won't work.  If any one of your three stats reaches 0, you lose and have to 
#  sleep under your desk because the doors to the school have been locked.

import os

import game_engine as ge
import dungeon_classes as dc

# TODO: Test os.system('clear') command when needing to wipe screen. This will mean the displays may be off
#           While loop below continues game till you've beaten 10 opponents EVEN AS DEFEAT MSG IS DISPLAYED

# os.system('clear')

os.system('cls')

# Beginning script of the game
print '-'*75
print '''
You are a teacher at the end of a looong week.
Your goal is to escape the building with ANY amount 
of energy, patience & excuses. You must reach the
exit before running out of any of these attributes
or else the doors will lock and you will have to 
sleep under your desk...which is what they think you 
do anyway...
'''
print '-'*75

# User choses name and a player instance is created. 
hero_name = raw_input("What is your teacher/player's name?: ")
hero = dc.Player(hero_name, 7, 7, 7, 0)
os.system('cls')
hero.description()

# Run function to choose teacher subject to modify attribute values
hero.begin(hero)

# Generate 4 types of opponents.  Stats are ordered as: energy, patience, excuse_detection
# The number is the percentage of success. So you have a 40% chance of success running
# from a student and a 20% chance of success using an excuse on an admin
studentOpp = dc.Opponent("student", 40, 90, 80)
parentOpp = dc.Opponent("parent", 20, 80, 60)
coworkerOpp = dc.Opponent("coworker", 90, 50, 50)
adminOpp = dc.Opponent("administrator", 30, 30, 20)


# User has chosen subject, this displays latest skills before the first part of the game begins
ge.current_stats(hero)

# Name and subject are chosen---the beginning of the adventure begins here!
os.system('cls')
print '''The bell has run, classes have been dismissed, and
you are ready for this week to be over. You eagerly
open the door and take your first steps toward the exit...'''
print '-'*75
print '-'*75
pause = raw_input("Press any button to continue...")
os.system('cls')
ge.current_stats(hero)
def main():
		# Check if the hero is alive or dead
	def is_alive(hero):
	  # This looks at hero instance as dictionary, attr looks at attribute, val looks at values associated
	  # with it.  We only focus on checking val since it contains the integers for each attribute.
	  for attr, val in hero.__dict__.iteritems():
	    if val <= 0:
		ge.defeat()
		return False
	  if hero.opponents_beaten >= 10:
	    ge.player_wins()
	    return False

	while True:
		
		ge.hallway_update(hero)
		chance_encounter = ge.random.randint(1,100)
		if 1 <= chance_encounter <= 50:
			print 'Teacher {}! I have a quick question for you...'.format(hero_name)
			ge.battle(hero, studentOpp)
		if 51 <= chance_encounter <=70:
			print 'Excuse me, teacher {}? I need to talk to you about my child...'.format(hero_name)
			ge.battle(hero, parentOpp)
		if 71 <= chance_encounter <=90:
			print 'Hey {}. Do you have a second?...'.format(hero_name)
			ge.battle(hero, coworkerOpp)
		if 91 <= chance_encounter <=100:
			print "I've been looking for you {}. I need you to...".format(hero_name)
			ge.battle(hero, adminOpp)
		if is_alive(hero) == False:
			break
		
main()