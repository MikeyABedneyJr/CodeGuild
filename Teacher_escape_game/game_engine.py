# This file holds all of the functions that run the game. Attacking, winning/losing individual fights, displaying
# a menu for the users, and winning or losing the entire game are stored here.

import random
import os

# Simple text to show what choices the user can make when fighting battles.
def battle_menu(hero):
  print '''BATTLE MENU:
  1 = Run away
  2 = Use patience
  3 = Make up an excuse to leave'''
  print '-'*75  

# The entire battle sequence is in this block. It throws to other functions for specific conditions.
def battle(hero, challenge):
  print "How do you plan to bypass this {}?\n".format(challenge.name)
  battle_menu(hero)
  battle_choice = raw_input("What will you do?:  "  )
  
  try:
    # Player tries to run
    if battle_choice == "1":    
      player_roll = random.randint(0,100)
      if player_roll <= challenge.energy:   
        hero.energy -= 1
        if hero.energy <= 0:
          return(hero)
        battle_success(hero)
      if challenge.energy <= player_roll:
        hero.energy -= 2
        if hero.energy <= 0:
          return(hero)
        battle_failure(hero, challenge)
    
    # Player uses patience
    if battle_choice == "2":    
      player_roll = random.randint(0,100)
      if player_roll <= challenge.patience:
        hero.patience -= 1
        if hero.patience <= 0:
          return(hero)
        battle_success(hero)
      if challenge.patience <= player_roll:
        hero.patience -= 2
        if hero.patience <= 0:
          return(hero)
        battle_failure(hero, challenge)

    # Player tries to make up an excuse
    if battle_choice == "3":    
      player_roll = random.randint(0,100)
      if player_roll <= challenge.excuse_detection:
        hero.excuses -= 1
        if hero.excuses <= 0:
          return(hero)
        battle_success(hero)
      if challenge.excuse_detection <= player_roll:
        hero.excuses -= 1
        if hero.excuses <= 0:
          return(hero)
        battle_failure(hero, challenge)

 # Player doesn't type a 1, 2, or 3
  except:
    print "Please enter a number 1, 2, or 3"
    pause = raw_input("Press any key to continue...")
    os.system('cls')
    battle(hero, challenge)

# Called when user wins the fight
def battle_failure(hero, challenge):
  print "Oh nooo!! It didn't work!!"
  pause = raw_input("Press any key to continue...")
  os.system('cls')
  current_stats(hero)
  battle(hero, challenge)

# Called when user loses the fight
def battle_success(hero):
  print"YOU HAVE BEATEN YOUR OPPONENT!!!!"
  hero.opponents_beaten += 1
  pause = raw_input("Press any key to continue...")
  os.system('cls')
  current_stats(hero)


# Called when needing to display current teacher status
def current_stats(hero):  
  print '''
Here are the current stats for %s:
  Energy: %d 
  Patience: %d
  Excuses: %d

And you have beaten %d opponents''' % (hero.name, hero.energy, hero.patience, hero.excuses, hero.opponents_beaten)

# Called when any one of the player attributes reaches zero
def defeat():
  print '''
  You have tried your best but cannot go further without rest.
  After going into the fetal position for a few moments, you 
  accidently fall asleep and wake up several hours later. There
  is no use trying to get out, the doors were locked long
  ago. Picking yourself up slowly, you head back to your 
  classroom to sleep under your desk.

  GAME OVER'''
  print '-'*75
  print '-'*75
  print '-'*75

# Called after each encounter with an opponent
def hallway_update(hero): 
    print '-'*75
    print "HALLWAY  {}".format(str(hero.opponents_beaten  + 1))
    print '-'*75

# Called when player has beaten 10 opponents and every attribute is more than zero
def player_wins():
    print '-'*75
    print '''
    YOU'VE ESCAPED! 
    Go out and live your life!
    The game starts over in a few short days....

    GAME OVER'''
    print '-'*75
    print '-'*75
    print '-'*75


