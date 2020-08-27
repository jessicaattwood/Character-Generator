# # # Goals
# CHECK # Character Traits (Positive, Neutral and Negative)
# CHECK # Name generator based on male, female or both checkboxes
# CHECK # Age based on infant, child, teen, young adult, adult, senior
# CHECK # Race
# CHECK # Age multiplier depending on Race
# CHECK # Quirk
# CHECK # Class
# CHECK # Occupation
# CHECK # Add Occupations list to characterClassesAndRaces data file
# # Add "None" value to Age when rolling and no boxes checked.
# CHECK # Add "Roll All" button

import random
import data.characterTraits as cT
posNeuNeg = ["Positive: ","Neutral: ","Negative: "]
import data.characterNames as cN
import data.characterClassesAndRaces as cCR
import data.characterQuirks as cQ
import tkinter
from tkinter import *

class CharGen:
    def __init__(self):
        #Building the GUI basics
        self.mainWindow = tkinter.Tk()
        self.windowTitle = "Random Character Generator 9000"
        self.windowSize = "600x490"
        self.font = "Arial"
        self.fontSize = 12
        self.mainWindow.geometry(self.windowSize)
        self.mainWindow.title(self.windowTitle)

        #String Variables
        self.traitText = tkinter.StringVar()
        self.nameText = tkinter.StringVar()
        self.ageText = tkinter.StringVar()
        self.raceText = tkinter.StringVar()
        self.classText = tkinter.StringVar()
        self.occupationText = tkinter.StringVar()
        self.quirkText = tkinter.StringVar()

        #Create ROLL ALL frame
        self.rollAllFrame = LabelFrame(self.mainWindow, width = 600, height=50)
        self.rollAllFrame.grid(row=4,column=0,columnspan=2)
        self.rollAllFrame.pack_propagate(0)
        #Roll All
        self.rollAll_button = tkinter.Button(self.rollAllFrame, text = "Roll All!",
        command = self.UpdateAllText, width=30,height=3).pack()       

        #Creates, populates and packs the frame for the NAME section.
        self.nameGenderFrame = LabelFrame(self.mainWindow, text = "Name",width=300,height=110)
        self.nameGenderFrame.grid(row=0,column=0)
        self.nameGenderFrame.pack_propagate(0)
        self.femaleVar = IntVar()
        self.maleVar = IntVar()

        self.maleCheckButton = Checkbutton(self.nameGenderFrame, text="Male", variable=self.maleVar).pack(anchor=W)
        self.femaleCheckButton = Checkbutton(self.nameGenderFrame, text="Female", variable=self.femaleVar).pack(anchor=W)

        self.nameText.set("Roll Name")
        tkinter.Label(self.nameGenderFrame, textvariable = self.nameText).pack()

        #Now we roll the NAME
        self.nameReRoll_button = tkinter.Button(self.nameGenderFrame, text = "Roll!",
        command = self.UpdateNameText).pack(anchor=E)

        #Creates, populates and packs the frame for the RACE section.
        self.raceLabelFrame = LabelFrame(self.mainWindow, text = "Race",width=300,height=110)
        self.raceLabelFrame.grid(row=0,column=1)
        self.raceLabelFrame.pack_propagate(0)

        self.raceText.set("Roll Race")
        tkinter.Label(self.raceLabelFrame, textvariable = self.raceText).pack()

        #Now we roll the RACE
        self.raceReRoll_button = tkinter.Button(self.raceLabelFrame, text = "Roll!",
        command = self.UpdateRaceText).pack(anchor=E)

        #Creates, populates and packs the frame for the CLASS section.
        self.classLabelFrame = LabelFrame(self.mainWindow, text = "Class",width=300,height=110)
        self.classLabelFrame.grid(row=2,column=1)
        self.classLabelFrame.pack_propagate(0)
        
        self.classText.set("Roll Class")
        tkinter.Label(self.classLabelFrame, textvariable = self.classText).pack()

        #Now we roll the CLASS
        self.classReRoll_button = tkinter.Button(self.classLabelFrame, text = "Roll!",
        command = self.UpdateClassText).pack(anchor=E)

        #Creates, populates and packs the frame for the OCCUPATION section.
        self.occupationLabelFrame = LabelFrame(self.mainWindow, text = "Occupation",width=300,height=110)
        self.occupationLabelFrame.grid(row=3,column=1)
        self.occupationLabelFrame.pack_propagate(0)
        
        self.occupationText.set("Roll Occupation")
        tkinter.Label(self.occupationLabelFrame, textvariable = self.occupationText).pack()

        #Now we roll the OCCUPATION
        self.occupationReRoll_button = tkinter.Button(self.occupationLabelFrame, text = "Roll!",
        command = self.UpdateOccupationText).pack(anchor=E)

        #Creates, populates and packs the frame for the TRAIT section.
        self.traitlabelframe = LabelFrame(self.mainWindow, text = "Traits",width=300,height=110)
        self.traitlabelframe.grid(row=1,column=0)
        self.traitlabelframe.pack_propagate(0)
        self.traitText.set("Positive: \n Neutral: \n Negative: \n ")
        tkinter.Label(self.traitlabelframe, textvariable = self.traitText).pack()

        #Now we roll the TRAITS
        self.reRoll_button = tkinter.Button(self.traitlabelframe, text = "Roll!",
        command = self.UpdateTraitText)
        self.reRoll_button.pack(anchor=E)

        #Creates, populates and packs the frame for the QUIRK section.
        self.quirkLabelFrame = LabelFrame(self.mainWindow, text = "Quirk",width=300,height=110)
        self.quirkLabelFrame.grid(row=1,column=1)
        self.quirkLabelFrame.pack_propagate(0)
        
        self.quirkText.set("Roll Quirk")
        tkinter.Label(self.quirkLabelFrame, textvariable = self.quirkText).pack()

        #Now we roll the QUIRK
        self.quirkReRoll_button = tkinter.Button(self.quirkLabelFrame, text = "Roll!",
        command = self.UpdateQuirkText).pack(anchor=E)        

        #Creates, populates and packs the frame for the AGE SELECTION section.
        self.ageSelectFrame = LabelFrame(self.mainWindow, text = "Age",width=300,height=220)
        self.ageSelectFrame.grid(row=2,column=0,rowspan=2)
        self.ageSelectFrame.pack_propagate(0)

        self.infantVar = IntVar()
        self.childVar = IntVar()
        self.teenVar = IntVar()
        self.youngAdultVar = IntVar()
        self.adultVar = IntVar()
        self.seniorVar = IntVar()

        self.infantCheckButton = Checkbutton(self.ageSelectFrame, text="Infant", variable=self.infantVar).pack(anchor=W)
        self.childCheckButton = Checkbutton(self.ageSelectFrame, text="Child", variable=self.childVar).pack(anchor=W)
        self.teenCheckButton = Checkbutton(self.ageSelectFrame, text="Teen", variable=self.teenVar).pack(anchor=W)
        self.youngAdultCheckButton = Checkbutton(self.ageSelectFrame, text="Young Adult", variable=self.youngAdultVar).pack(anchor=W)
        self.adultCheckButton = Checkbutton(self.ageSelectFrame, text="Adult", variable=self.adultVar).pack(anchor=W)
        self.seniorCheckButton = Checkbutton(self.ageSelectFrame, text="Senior", variable=self.seniorVar).pack(anchor=W)

        self.ageText.set("Roll Age")
        tkinter.Label(self.ageSelectFrame, textvariable = self.ageText).pack()

        #Now we roll the AGE
        self.ageReRoll_button = tkinter.Button(self.ageSelectFrame, text = "Roll!",
        command = self.UpdateAgeText).pack(anchor=E)

        #Call the whole window into existence
        self.mainWindow.mainloop()

    def UpdateAllText(self):
        self.maleVar.set(1)
        self.femaleVar.set(1)
        self.UpdateNameText()

        self.UpdateRaceText()
        self.UpdateTraitText()
        self.UpdateQuirkText()
        
        self.infantVar.set(1)
        self.childVar.set(1)
        self.teenVar.set(1)
        self.youngAdultVar.set(1)
        self.adultVar.set(1)
        self.seniorVar.set(1)
        self.UpdateAgeText()

        self.UpdateClassText()
        self.UpdateOccupationText()

    #Name Randomization
    def RandomizeName(self):
        nameGender = cN.nameGenderList
    
        if self.femaleVar.get() == 1 and self.maleVar.get() == 0:
            return self.GetRandomName(cN.nameGenderList[0])
        elif self.femaleVar.get() == 0 and self.maleVar.get() == 1:
            return self.GetRandomName(cN.nameGenderList[1])
        elif self.femaleVar.get() == 1 and self.maleVar.get() == 1:
            fullNameList = []
            for index in cN.nameGenderList:
                fullNameList.extend(index)
            return self.GetRandomName(fullNameList)
        else:
            return None

    def GetRandomName(self, nameList):
        randName = random.randrange(0,len(nameList))
        nameNewText = nameList[randName]
        return nameNewText
        
    def UpdateNameText(self):
        self.nameText.set(self.RandomizeName())

    #Race Randomization
    def RandomizeRace(self):
        self.randRaceIndex = random.choice(list(cCR.Races))

        return self.randRaceIndex
    
    def UpdateRaceText(self):
        self.raceText.set(self.RandomizeRace())

    #Class Randomization
    def RandomizeClass(self):
        self.randClassIndex = random.choice(list(cCR.Classes))

        return self.randClassIndex
    
    def UpdateClassText(self):
        self.classText.set(self.RandomizeClass())

    #Occupation Randomization
    def RandomizeOccupation(self):
        self.randOccupationIndex = random.choice(list(cCR.Occupations))

        return self.randOccupationIndex
    
    def UpdateOccupationText(self):
        self.occupationText.set(self.RandomizeOccupation())


    #Trait Randomization
    def RandomizeTraits(self):
        traitsNewText = ""
        for index in range(0,len(cT.traits)):
            traitType = cT.traits[index]
            randValue = random.randrange(0,len(traitType))
            printable = posNeuNeg[index] + traitType[randValue]
            traitsNewText += printable + "\n"
        return traitsNewText

    def UpdateTraitText(self):
        self.traitText.set(self.RandomizeTraits())

    #Quirk Randomization
    def RandomizeQuirk(self):
        self.randQuirkIndex = random.choice(list(cQ.quirks))

        return self.randQuirkIndex
    
    def UpdateQuirkText(self):
        self.quirkText.set(self.RandomizeQuirk())

    #Age Randomization
    def RandomizeAge(self):
        print("NEW ROLL")
        checker = [self.infantVar, self.childVar, self.teenVar, self.youngAdultVar, self.adultVar, self.seniorVar]
        activeRanges = []
        ageDict = {
            0:[0,4],
            1:[4,12],
            2:[12,20],
            3:[20,30],
            4:[30,50],
            5:[50,100]
        }


        for i in range(0,len(checker)):
            if checker[i].get() == 1:
                activeRanges.append(ageDict[i])

        print ("TESTING")
        if len(activeRanges) == 0:
            return None

        activeRangesIndex = random.randrange(0,len(activeRanges))
        activeRange = activeRanges[activeRangesIndex]
        age = random.randrange(activeRange[0],activeRange[1])

        if self.raceText.get() == "Roll Race":
            return round(age)
        else:
            age = age * cCR.Races[self.randRaceIndex]            
            return round(age)

    def UpdateAgeText(self):
        self.ageText.set(self.RandomizeAge())
                

Initialize = CharGen()