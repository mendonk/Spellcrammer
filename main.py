# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# SPELLCRAMMER
# BY MENDON
# 9/24/2020

# This program is a quick reference for spell caster classes in D&D 3.5.

# PACKAGES
from bs4 import BeautifulSoup

# WEBSCRAPING PARAMETERS
pageExamples = [
    "https://seekingalpha.com/symbol/AAPL/overview",
    "https://seekingalpha.com/symbol/AAPL/momentum/performance",
    "https://www.aistockcharts.com/correlation-report.pl?s=AAPL",
]
exampleSymbol = "AAPL"
waitAvg, waitVar, waitDefault = 60.0, 0.1, 10.0

# CLASSES
playerClass = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Wizard"]

# GREETING AND playerClass CHOICE

print(
    'Welcome to SPELLCRAMMER, a quick reference for your D&D 3.5 caster class. Please choose your class from the list below: ')

print(*playerClass, sep="\n")

playerClass = input()

print('Thank you. Please enter your current level (1 - 20): ')
playerLevel = input()

# FLOW CONTROL WITH playerClass and playerLevel

if playerClass == "Bard":
    print('You are a melodious Level ' + playerLevel, ' Bard!' 
    'You can cast ' + spellsPerDay, ' spells per day.' 
    'You know ' + spellsKnown, ' spells. Here are the spells you can choose from: ')

elif playerClass == "Cleric":
    print('You are a steadfast Level' + playerLevel,
    ' Cleric!' 
    'You can cast ' + spellsPerDay,
    ' spells per day.' 
    'You know ' + spellsKnown,
    ' spells. Here are the spells you can choose from: ')

elif playerClass == "Druid":
    print('You are a mystical Level' + playerLevel, ' Druid!' 
    'You can cast ' + spellsPerDay,
    ' spells per day.' 
    'You know ' + spellsKnown,
    ' spells. Here are the spells you can choose from: ')

elif playerClass == "Sorcerer":
    print('You are a mysterious Level ' + playerLevel,
    ' Sorcerer!' 
    'You can cast ' + spellsPerDay,
    ' spells per day.' 
    'You know ' + spellsKnown,
    ' spells. Here are the spells you can choose from: ')

elif playerClass == "Wizard":
    print('You are a studious Level ' + playerLevel,
    ' Wizard!'
    'You can cast ' + spellsPerDay,
    ' spells per day.'
    'You know ' + spellsKnown,
    ' spells. Here are the spells you can choose from: ')


