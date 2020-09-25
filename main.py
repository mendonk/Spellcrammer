# SPELLCRAMMER
# BY MENDON K
# 9/24/2020

# This program is a quick reference for spell caster classes in D&D 3.5.

# TO DO
# Logic control
# Webscrape d20SRD
# Test

# PACKAGES
# from bs4 import BeautifulSoup

# WEBSCRAPING PARAMETERS
pageExamples = [
    "https://www.d20srd.org/srd/spellLists/bardSpells.htm",
    "https://www.d20srd.org/srd/spellLists/clericSpells.htm",
    "https://www.d20srd.org/srd/spellLists/druidSpells.htm",
    "https://www.d20srd.org/srd/spellLists/paladinSpells.htm",
    "https://www.d20srd.org/srd/spellLists/rangerSpells.htm",
    "https://www.d20srd.org/srd/spellLists/sorcererWizardSpells.htm",
]
exampleSymbol = "YYZ"

# CLASSES
playerClass = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Wizard"]

# GREETING AND playerClass CHOICE

print(
    'Welcome to SPELLCRAMMER, a quick reference for your D&D 3.5 caster class. Please choose your class from the list below: ')

print(*playerClass, sep="\n")

playerClass = input()

playerLevel = int(input('Thank you. Please enter your current level (1 - 20): '))

#CHECK playerLevel INPUT
while (playerLevel)>20:
    playerLevel = int(input('Sorry, we don\'t have epic levels yet. Please enter your current level (1 - 20): '))
    continue

while (playerLevel)<1:
    playerLevel = int(input('Sorry, we don\'t have negative levels yet. Please enter your current level (1 - 20): '))
    continue

spellsPerDay = '5';
spellsKnown = '5';

# FLOW CONTROL WITH playerClass and playerLevel

if playerClass == "Bard":
    print('You are a melodious Level' , playerLevel, 'Bard! ')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Cleric":
    print('You are a devoted Level' , playerLevel,'Cleric!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Druid":
    print('You are a mystical Level' , playerLevel, 'Druid!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Paladin":
    print('You are a steadfast Level' , playerLevel, 'Paladin!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Ranger":
    print('You are a rugged Level' , playerLevel, 'Ranger!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Sorcerer":
    print('You are a mysterious Level' , playerLevel, 'Sorcerer!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')

elif playerClass == "Wizard":
    print('You are a studious Level' , playerLevel, 'Wizard!')
    print('You can cast' , spellsPerDay, 'spells per day. ')
    print('You know' , spellsKnown, 'spells. Here are the spells you can choose from: ')


