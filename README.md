# Character Generator

## Description
This tool is designed to assist in basic character conceptualization. By providing countless combinations, users can create a unique character every time. This may be especially helpful to concept artists, designers and storytellers who are looking to create multi-dimentionl characters and escape stereotypes.

![ScreenShot](examples/CharactrGenerator.JPG?raw=true "Character Generator Example")

## Current State
The Character Generator tool is still in development, and is built with Python and the tkinter library.

The tool is in a functional state, however some combinations may be nonsensicle; such as a human 2 year old, who is a wizard and works as a carpenter. This will remain in the tool to provide the user with full control over how they interpret the information. For example, a story writer may interpret the information creatively; the human 2 year old is predisposed to wizardry but will start out as a carpentery apprentice before realizing their full magical potential. Or, the user can choose to re-roll specific areas in search of a more appropriate option.

Some sections currently have limited potential outputs, and they will be expanded over time. Users can easily add their own optins as well, by following the correct format in each of the 'data' documents.

## Features

#### Name
A male or female name can be generated, depending on which box is checked by the user. If both boxes are checked, there is a 50% chance of recieving a male name, and a 50% chance of a female name. If neither boxes are checked, no name will be supplied.

#### Race
A random humanoid race is supplied.

#### Traits
A positive, neutral and negative personality trait is supplied. This single function was the original heart of this tool!

#### Quirk
A random quirk is supplied; things that are compulsively done, or are a particularly unique feature can be found here.

#### Age
A random age is supplied, depending on the boxe(s) checked by the user. The boxes indicate basic life stages from infancy to senior. If a race has already been generated, the age will be multiplied to generally accepted equivalant ages for creatures of that race. In the default human years, the age ranges are as follows:

- Infant (0 - 4 years)
- Child (4 - 12 years)
- Teen (12 - 20 years)
- Young Adult (20 - 30 years)
- Adult (30 - 50 years)
- Senior (50 - 100 years)

The age multipliers for the currently available races:

- Human =  age * 1
- Elf = age * 7
- Dwarf = age * 2
- Orc = age * 0.5 

#### Class
A random class is supplied, such as fighter, bard, rougue, wizard etc.

#### Occupation
A random occupation is supplied, such as florist, bar keeper, doctor, blacksmith etc.
