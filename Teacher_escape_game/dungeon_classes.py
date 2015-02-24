# This file only holds enough information to create an instance of the hero (Player class), a method to choose what
# subject they want to teach (changes their attributes a little), and another class to make instances of opponents.

# This builds your teacher stats to be modified throughout the game
class Player(object):
  def __init__(self, name, energy, patience, excuses, opponents_beaten, alive=True):
    self.name = name
    self.energy = energy
    self.patience = patience
    self.excuses = excuses
    self.opponents_beaten = opponents_beaten
    self.alive = alive

  def description(self):
    print '''
You are Teacher %s and here are your stats:
  Energy: %d 
  Patience: %d
  Excuses: %d''' % (self.name, self.energy, self.patience, self.excuses)
    print '-'*75
    print '-'*75

  # User chooses teacher subject
  def begin(self, hero):  
    print '''What kind of teacher do you want to be?
    1 = Math (++energy, -excuses)
    2 = English (++patience, -excuses)
    3 = Theater (+energy, +excuses)'''
    print '-'*75
    print '-'*75
    class_choice = raw_input("Which subject will you chose?: ")
    if class_choice == "1":
      math(hero)
    elif class_choice == "2":
      english(hero)
    elif class_choice == "3":
      theater(hero)
    else:
      print '-'*75
      print "I didn't understand your choice. Try again"
      print '-'*75
      begin()

# Adding/removing stats for choice of what type of teacher
def math(hero):
  hero.energy += 4
  hero.excuses -= 2
  print "You've chosen to be a math teacher..."
def english(hero):
  hero.patience += 4
  hero.excuses -= 2
  print "You've chosen to be an english teacher..."
def theater(hero):
  hero.energy += 2
  hero.excuses += 2
  print "You've chosen to be a theater teacher..."

# Class to build opponents
class Opponent(object):
  def __init__(self, name, energy, patience, excuse_detection):
    self.name = name
    self.energy = energy
    self.patience = patience
    self.excuse_detection = excuse_detection
