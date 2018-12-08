name = input("What's your name?: ")
last_name = input("What's your last name?: ")
first_letter_name = name[:1].upper()
third_letter_last_name = last_name[2:3].lower()
if first_letter_name == "A":
    name1 = "Darth"
elif first_letter_name == "B":
    name1 = "Padame"
elif first_letter_name == "C":
    name1 = "Jar Jar"
elif first_letter_name == "D":
    name1 = "Obi-Wan"
elif first_letter_name == "E":
    name1 = "Emperor"
elif first_letter_name == "F":
    name1 = "Han"
elif first_letter_name == "G":
    name1 = "Greedo"
elif first_letter_name == "H":
    name1 = "Anakin"
elif first_letter_name == "I":
    name1 = "Count"
elif first_letter_name == "J":
    name1 = "Starlacc"
elif first_letter_name == "K":
    name1 = "Jabba"
elif first_letter_name == "L":
    name1 = "Sergeant"
elif first_letter_name == "M":
    name1 = "Boba"
elif first_letter_name == "N":
    name1 = "Wicket W."
elif first_letter_name == "O":
    name1 = "Wampa"
elif first_letter_name == "P":
    name1 = "Senator"
elif first_letter_name == "Q":
    name1 = "Queen"
elif first_letter_name == "R":
    name1 = "Padawan"
elif first_letter_name == "S":
    name1 = "Imperial"
elif first_letter_name == "T":
    name1 = "General"
elif first_letter_name == "U":
    name1 = "Storm"
elif first_letter_name == "V":
    name1 = "R2"
elif first_letter_name == "W":
    name1 = "Luke"
elif first_letter_name == "X":
    name1 = "C3"
elif first_letter_name == "Y":
    name1 = "Mace"
elif first_letter_name == "Z":
    name1 = "Princess"
    
if third_letter_last_name == "a":
    last_name1 = "Bane"
elif third_letter_last_name == "b":
    last_name1 = "Sidious"
elif third_letter_last_name == "c":
    last_name1 = "Skywalker"
elif third_letter_last_name == "d":
    last_name1 = "Chewbacca"
elif third_letter_last_name == "e":
    last_name1 = "Fett"
elif third_letter_last_name == "f":
    last_name1 = "Trooper"
elif third_letter_last_name == "g":
    last_name1 = "PO"
elif third_letter_last_name == "h":
    last_name1 = "Speeder"
elif third_letter_last_name == "i":
    last_name1 = "Dooku"
elif third_letter_last_name == "j":
    last_name1 = "Pit"
elif third_letter_last_name == "k":
    last_name1 = "Vader"
elif third_letter_last_name == "l":
    last_name1 = "D2"
elif third_letter_last_name == "m":
    last_name1 = "Palpatine"
elif third_letter_last_name == "n":
    last_name1 = "Grievous"
elif third_letter_last_name == "o":
    last_name1 = "Binks"
elif third_letter_last_name == "p":
    last_name1 = "Soldier"
elif third_letter_last_name == "q":
    last_name1 = "Kenobi"
elif third_letter_last_name == "r":
    last_name1 = "Solo"
elif third_letter_last_name == "s":
    last_name1 = "The Hutt"
elif third_letter_last_name == "t":
    last_name1 = "Maul"
elif third_letter_last_name == "u":
    last_name1 = "Windu"
elif third_letter_last_name == "v":
    last_name1 = "Queen"
elif third_letter_last_name == "w":
    last_name1 = "Leia"
elif third_letter_last_name == "x":
    last_name1 = "Monster"
elif third_letter_last_name == "y":
    last_name1 = "Yoda"
elif third_letter_last_name == "z":
    last_name1 = "Warrick"

result = "Your Star Wars name is {} {}.".format(name1,last_name1)
print(result)
       
