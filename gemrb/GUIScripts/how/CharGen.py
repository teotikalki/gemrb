#Character Generation
import GemRB
from ie_stats import *


CharGenWindow = 0
CharGenState = 0
TextArea = 0
PortraitButton = 0
AcceptButton = 0

GenderButton = 0
GenderWindow = 0
GenderTextArea = 0
GenderDoneButton = 0

Portrait = 0
PortraitTable = 0
PortraitPortraitButton = 0

RaceButton = 0
RaceWindow = 0
RaceTable = 0
RaceTextArea = 0
RaceDoneButton = 0

ClassButton = 0
ClassWindow = 0
ClassTable = 0
ClassTextArea = 0
ClassDoneButton = 0

ClassMultiWindow = 0
ClassMultiTextArea = 0
ClassMultiDoneButton = 0

ClassSpecialWindow = 0
ClassSpecialTextArea = 0
ClassSpecialDoneButton = 0

AlignmentButton = 0
AlignmentWindow = 0
AlignmentTable = 0
AlignmentTextArea = 0
AlignmentDoneButton = 0

AbilitiesButton = 0
AbilitiesWindow = 0
AbilitiesTable = 0
AbilitiesRaceAddTable = 0
AbilitiesRaceReqTable = 0
AbilitiesClassReqTable = 0
AbilitiesMinimum = 0
AbilitiesMaximum = 0
AbilitiesModifier = 0
AbilitiesTextArea = 0
AbilitiesRecallButton = 0
AbilitiesDoneButton = 0

SkillsButton = 0
SkillsWindow = 0
SkillsTable = 0
SkillsTextArea = 0
SkillsDoneButton = 0
SkillsPointsLeft = 0
SkillsState = 0

RacialEnemyButton = 0
RacialEnemyWindow = 0
RacialEnemyTable = 0
RacialEnemyTextArea = 0
RacialEnemyDoneButton = 0

ProficienciesWindow = 0
ProficienciesTable = 0
ProfsMaxTable = 0
ProficienciesTextArea = 0
ProficienciesDoneButton = 0
ProficienciesPointsLeft = 0

MageSpellsWindow = 0
MageSpellsTable = 0
MageSpellsTextArea = 0
MageSpellsDoneButton = 0
MageSpellsSelectPointsLeft = 0

MageMemorizeWindow = 0
MageMemorizeTextArea = 0
MageMemorizeDoneButton = 0
MageMemorizePointsLeft = 0

PriestSpellsTable = 0
PriestMemorizeWindow = 0
PriestMemorizeTextArea = 0
PriestMemorizeDoneButton = 0
PriestMemorizePointsLeft = 0

AppearanceButton = 0
AppearanceWindow = 0
AppearanceTable = 0
AppearanceAvatarButton = 0
AppearanceHairButton = 0
AppearanceSkinButton = 0
AppearanceMajorButton = 0
AppearanceMinorButton = 0

CharSoundWindow = 0
CharSoundTable = 0
CharSoundStrings = 0

BiographyButton = 0
BiographyWindow = 0
BiographyField = 0

NameButton = 0
NameWindow = 0
NameField = 0
NameDoneButton = 0


def OnLoad():
	global CharGenWindow, CharGenState, TextArea, PortraitButton, AcceptButton
	global GenderButton, RaceButton, ClassButton, AlignmentButton, AbilitiesButton, SkillsButton, AppearanceButton, BiographyButton, NameButton

	GemRB.LoadWindowPack("GUICG")
	CharGenWindow = GemRB.LoadWindow(0)
	CharGenState = 0

	GenderButton = GemRB.GetControl(CharGenWindow, 0)
	GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, GenderButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	GemRB.SetEvent(CharGenWindow, GenderButton, IE_GUI_BUTTON_ON_PRESS, "GenderPress")
	GemRB.SetText(CharGenWindow, GenderButton, 11956)

	RaceButton = GemRB.GetControl(CharGenWindow, 1)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, RaceButton, IE_GUI_BUTTON_ON_PRESS, "RacePress")
	GemRB.SetText(CharGenWindow, RaceButton, 11957)

	ClassButton = GemRB.GetControl(CharGenWindow, 2)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, ClassButton, IE_GUI_BUTTON_ON_PRESS, "ClassPress")
	GemRB.SetText(CharGenWindow, ClassButton, 11959)

	AlignmentButton = GemRB.GetControl(CharGenWindow, 3)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentPress")
	GemRB.SetText(CharGenWindow, AlignmentButton, 11958)

	AbilitiesButton = GemRB.GetControl(CharGenWindow, 4)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesPress")
	GemRB.SetText(CharGenWindow, AbilitiesButton, 11960)

	SkillsButton = GemRB.GetControl(CharGenWindow, 5)
	GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ON_PRESS, "SkillsPress")
	GemRB.SetText(CharGenWindow, SkillsButton, 11983)

	AppearanceButton = GemRB.GetControl(CharGenWindow, 6)
	GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ON_PRESS, "AppearancePress")
	GemRB.SetText(CharGenWindow, AppearanceButton, 11961)

	BiographyButton = GemRB.GetControl(CharGenWindow, 16)
	GemRB.SetButtonState(CharGenWindow, BiographyButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, BiographyButton, IE_GUI_BUTTON_ON_PRESS, "BiographyPress")
	GemRB.SetText(CharGenWindow, BiographyButton, 18003)

	NameButton = GemRB.GetControl(CharGenWindow, 7)
	GemRB.SetButtonState(CharGenWindow, NameButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, NameButton, IE_GUI_BUTTON_ON_PRESS, "NamePress")
	GemRB.SetText(CharGenWindow, NameButton, 11963)

	BackButton = GemRB.GetControl(CharGenWindow, 11)
	GemRB.SetButtonState(CharGenWindow, BackButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "BackPress")

	PortraitButton = GemRB.GetControl(CharGenWindow, 12)
	GemRB.SetButtonFlags(CharGenWindow, PortraitButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_NO_IMAGE, OP_SET)

	ImportButton = GemRB.GetControl(CharGenWindow, 13)
	GemRB.SetButtonState(CharGenWindow, ImportButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(CharGenWindow, ImportButton, 13955)
	GemRB.SetEvent(CharGenWindow, ImportButton, IE_GUI_BUTTON_ON_PRESS, "ImportPress")

	CancelButton = GemRB.GetControl(CharGenWindow, 15)
	GemRB.SetButtonState(CharGenWindow, CancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(CharGenWindow, CancelButton, 13727)
	GemRB.SetEvent(CharGenWindow, CancelButton, IE_GUI_BUTTON_ON_PRESS, "CancelPress")

	BackButton = GemRB.GetControl(CharGenWindow, 11)
	GemRB.SetButtonState(CharGenWindow, BackButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "BackPress")

	AcceptButton = GemRB.GetControl(CharGenWindow, 8)
	GemRB.SetButtonState(CharGenWindow, AcceptButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetText(CharGenWindow, AcceptButton, 11962)
	GemRB.SetEvent(CharGenWindow, AcceptButton, IE_GUI_BUTTON_ON_PRESS, "AcceptPress")

	TextArea = GemRB.GetControl(CharGenWindow, 9)
	GemRB.SetText(CharGenWindow, TextArea, 16575)

	GemRB.SetVisible(CharGenWindow, 1)
	return

def BackPress():
	global CharGenWindow, CharGenState, SkillsState
	global GenderButton, RaceButton, ClassButton, AlignmentButton, AbilitiesButton, SkillsButton, AppearanceButton, BiographyButton, NameButton

	GemRB.SetToken("CHARNAME","")
	if CharGenState > 0:
		CharGenState = CharGenState - 1
	if CharGenState > 6:
		CharGenState = 6

	if CharGenState == 0:
		GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, RaceButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, GenderButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	elif CharGenState == 1:
		GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, ClassButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, RaceButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	elif CharGenState == 2:
		GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, ClassButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	elif CharGenState == 3:
		GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	elif CharGenState == 4:
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	elif CharGenState == 5:
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
		SkillsState = 0
	elif CharGenState == 6:
		GemRB.SetButtonState(CharGenWindow, NameButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, BiographyButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ENABLED)

	GemRB.SetButtonState(CharGenWindow, AcceptButton, IE_GUI_BUTTON_DISABLED)
	SetCharacterDescription()
	return

def CancelPress():
	global CharGenWindow
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("PartyFormation")
	return

def AcceptPress():
	global CharGenWindow
	MyChar = GemRB.GetVar("Slot")
	GemRB.CreatePlayer("charbase", MyChar)
	GemRB.SetPlayerStat(MyChar, IE_SEX, GemRB.GetVar("Gender") )
	GemRB.SetPlayerStat(MyChar, IE_RACE, GemRB.GetVar("Race") )
	GemRB.SetPlayerStat(MyChar, IE_CLASS, GemRB.GetVar("Class") )
	GemRB.SetPlayerStat(MyChar, IE_KIT, 0x4000)
	t = GemRB.GetVar("Alignment")
	GemRB.SetPlayerStat(MyChar, IE_ALIGNMENT, t)
	TmpTable = GemRB.LoadTable("repstart")
	t = GemRB.FindTableValue(AlignmentTable, 3, t)
	t = GemRB.GetTableValue(TmpTable, t, 0)
	GemRB.SetPlayerStat(MyChar, IE_REPUTATION, t)
	TmpTable = GemRB.LoadTable("strtgold")
	GemRB.SetPlayerStat(MyChar, IE_EA, 2 )
	Str = GemRB.GetVar("Ability 1")
	GemRB.SetPlayerStat(MyChar, IE_STR, Str)
	if Str == 18:
		GemRB.SetPlayerStat(MyChar, IE_STREXTRA, GemRB.GetVar("StrExtra"))
	else:
		GemRB.SetPlayerStat(MyChar, IE_STREXTRA, 0)

	GemRB.SetPlayerStat(MyChar, IE_INT, GemRB.GetVar("Ability 2"))
	GemRB.SetPlayerStat(MyChar, IE_WIS, GemRB.GetVar("Ability 3"))
	GemRB.SetPlayerStat(MyChar, IE_DEX, GemRB.GetVar("Ability 4"))
	GemRB.SetPlayerStat(MyChar, IE_CON, GemRB.GetVar("Ability 5"))
	GemRB.SetPlayerStat(MyChar, IE_CHR, GemRB.GetVar("Ability 6"))

	GemRB.SetPlayerName(MyChar, GemRB.GetToken("CHARNAME"), 0)
	GemRB.FillPlayerInfo(MyChar, PortraitName+"L", PortraitName+"S")
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("PartyFormation")
	return

def SetCharacterDescription():
	global CharGenWindow, TextArea, CharGenState, ClassTable, RaceTable, AlignmentTable, AbilitiesTable, SkillsTable, ProficienciesTable, RacialEnemyTable, MageSpellsTable, PriestSpellsTable
	GemRB.TextAreaClear(CharGenWindow, TextArea)
	if CharGenState > 7:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 1047)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetToken("CHARNAME"))
		GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
	if CharGenState > 0:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 12135)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		if GemRB.GetVar("Gender") == 1:
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 1050)
		else:
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 1051)
	if CharGenState > 2:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 12136, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(ClassTable, GemRB.GetVar("Class") - 1, 2) )
	if CharGenState > 1:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 1048, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(RaceTable, GemRB.GetVar("Race") - 1, 2) )
	if CharGenState > 3:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 1049, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(AlignmentTable, GemRB.GetVar("Alignment") - 1, 2) )
	if CharGenState > 4:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
		for i in range(0, 6):
			GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(AbilitiesTable, i, 2), -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Ability" + str(i + 1))) )
	if CharGenState > 5:
		ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
		if ClassName == "THIEF" or ClassName == "FIGHTER_THIEF" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_THIEF":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			for i in range (0, 4):
				GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(SkillsTable, i, 2), -1)
				GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
				GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill" + str(i))) )
				GemRB.TextAreaAppend(CharGenWindow, TextArea, "%" )
		elif ClassName == "RANGER":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 9461, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill0")) )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "%" )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 15982, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(RacialEnemyTable, GemRB.GetVar("RacialEnemy") - 1, 2) )
		elif ClassName == "BARD":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			n = 2
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 9463, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill2")) )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "%" )

		GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 9466, -1)
		for i in range(0, 15):
			ProficiencyValue = GemRB.GetVar("Proficiency" + str(i) )
			if ProficiencyValue > 0:
				GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(ProficienciesTable, i, 2), -1)
				GemRB.TextAreaAppend(CharGenWindow, TextArea, " ")
				j = 0
				while j < ProficiencyValue:
					GemRB.TextAreaAppend(CharGenWindow, TextArea, "+")
					j = j + 1

		if ClassName == "MAGE" or ClassName == "FIGHTER_MAGE" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_MAGE" or ClassName == "FIGHTER_MAGE_CLERIC":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 11027, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			MageSpellsCount = GemRB.GetTableRowCount(MageSpellsTable)
			MageSpellBook = GemRB.GetVar("MageSpellBook")
			MageMemorized = GemRB.GetVar("MageMemorized")
			for i in range(0, MageSpellsCount):
				if (1 << i) & MageSpellBook:
					GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(MageSpellsTable, i, 2), -1)
					GemRB.TextAreaAppend(CharGenWindow, TextArea, " ")
					if (1 << i) & MageMemorized:
						GemRB.TextAreaAppend(CharGenWindow, TextArea, "+")

		if ClassName == "CLERIC" or ClassName == "FIGHTER_CLERIC" or ClassName == "CLERIC_THIEF" or ClassName == "CLERIC_RANGER" or ClassName == "CLERIC_MAGE" or ClassName == "FIGHTER_MAGE_CLERIC":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 11028, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			PriestSpellsCount = GemRB.GetTableRowCount(PriestSpellsTable)
			PriestMemorized = GemRB.GetVar("MageMemorized")
			for i in range(0, PriestSpellsCount):
				if (1 << i) & PriestMemorized:
					GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(PriestSpellsTable, i, 2), -1)
					GemRB.TextAreaAppend(CharGenWindow, TextArea, " +")
	return


# Gender Selection

def GenderPress():
	global CharGenWindow, GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetVisible(CharGenWindow, 0)
	GenderWindow = GemRB.LoadWindow(1)
	GemRB.SetVar("Gender", 0)

	MaleButton = GemRB.GetControl(GenderWindow, 2)
	GemRB.SetButtonState(GenderWindow, MaleButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(GenderWindow, MaleButton, IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	GemRB.SetEvent(GenderWindow, MaleButton, IE_GUI_BUTTON_ON_PRESS, "MalePress")

	FemaleButton = GemRB.GetControl(GenderWindow, 3)
	GemRB.SetButtonState(GenderWindow, FemaleButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(GenderWindow, FemaleButton, IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	GemRB.SetEvent(GenderWindow, FemaleButton, IE_GUI_BUTTON_ON_PRESS, "FemalePress")

	GemRB.SetVarAssoc(GenderWindow, MaleButton, "Gender", 1)
	GemRB.SetVarAssoc(GenderWindow, FemaleButton, "Gender", 2)

	GenderTextArea = GemRB.GetControl(GenderWindow, 5)
	GemRB.SetText(GenderWindow, GenderTextArea, 17236)

	GenderDoneButton = GemRB.GetControl(GenderWindow, 0)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ON_PRESS, "GenderDonePress")
	GemRB.SetText(GenderWindow, GenderDoneButton, 11973)
	GemRB.SetButtonFlags(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	GenderCancelButton = GemRB.GetControl(GenderWindow, 6)
	GemRB.SetButtonState(GenderWindow, GenderCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(GenderWindow, GenderCancelButton, IE_GUI_BUTTON_ON_PRESS, "GenderCancelPress")
	GemRB.SetText(GenderWindow, GenderCancelButton, 13727)
	
	GemRB.SetVisible(GenderWindow, 1)
	return

def MalePress():
	global GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetText(GenderWindow, GenderTextArea, 13083)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def FemalePress():
	global GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetText(GenderWindow, GenderTextArea, 13084)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def GenderDonePress():
	global CharGenWindow, GenderWindow
	GemRB.UnloadWindow(GenderWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	PortraitSelect()
	return
	
def GenderCancelPress():
	global CharGenWindow, GenderWindow, Gender
	GemRB.SetVar("Gender", 0)
	GemRB.UnloadWindow(GenderWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

def PortraitSelect():
	global CharGenWindow, PortraitWindow, Portrait, PortraitPortraitButton, PortraitTable
	GemRB.SetVisible(CharGenWindow, 0)
	PortraitWindow = GemRB.LoadWindow(11)

	# this is not the correct one, but I don't know which is
	PortraitTable = GemRB.LoadTable("PICTURES")
	Portrait = 0;
	
	PortraitPortraitButton = GemRB.GetControl(PortraitWindow, 1)
	GemRB.SetButtonFlags(PortraitWindow, PortraitPortraitButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_NO_IMAGE, OP_SET)

	PortraitLeftButton = GemRB.GetControl(PortraitWindow, 2)
	GemRB.SetButtonState(PortraitWindow, PortraitLeftButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitLeftButton, IE_GUI_BUTTON_ON_PRESS, "PortraitLeftPress")
	GemRB.SetButtonFlags(PortraitWindow, PortraitLeftButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)
	
	PortraitRightButton = GemRB.GetControl(PortraitWindow, 3)
	GemRB.SetButtonState(PortraitWindow, PortraitRightButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitRightButton, IE_GUI_BUTTON_ON_PRESS, "PortraitRightPress")
	GemRB.SetButtonFlags(PortraitWindow, PortraitRightButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)

	PortraitCustomButton = GemRB.GetControl(PortraitWindow, 6)
	GemRB.SetButtonState(PortraitWindow, PortraitCustomButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitCustomButton, IE_GUI_BUTTON_ON_PRESS, "PortraitCustomPress")
	GemRB.SetText(PortraitWindow, PortraitCustomButton, 17545)

	PortraitDoneButton = GemRB.GetControl(PortraitWindow, 0)
	GemRB.SetButtonState(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_ON_PRESS, "PortraitDonePress")
	GemRB.SetText(PortraitWindow, PortraitDoneButton, 11973)
	GemRB.SetButtonFlags(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	PortraitCancelButton = GemRB.GetControl(PortraitWindow, 5)
	GemRB.SetButtonState(PortraitWindow, PortraitCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitCancelButton, IE_GUI_BUTTON_ON_PRESS, "PortraitCancelPress")
	GemRB.SetText(PortraitWindow, PortraitCancelButton, 13727)

	while GemRB.GetTableValue(PortraitTable, Portrait, 0) != GemRB.GetVar("Gender"):
		Portrait = Portrait + 1
	GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")

	GemRB.SetVisible(PortraitWindow, 1)
	return

def PortraitLeftPress():
	global PortraitWindow, Portrait, PortraitTable, PortraitPortraitButton
	while True:
		Portrait = Portrait - 1
		if Portrait < 0:
			Portrait = GemRB.GetTableRowCount(PortraitTable) - 1
		if GemRB.GetTableValue(PortraitTable, Portrait, 0) == GemRB.GetVar("Gender"):
			GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")
			return
	
def PortraitRightPress():
	global PortraitWindow, Portrait, PortraitTable, PortraitPortraitButton
	while True:
		Portrait = Portrait + 1
		if Portrait == GemRB.GetTableRowCount(PortraitTable):
			Portrait = 0
		if GemRB.GetTableValue(PortraitTable, Portrait, 0) == GemRB.GetVar("Gender"):
			GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")
			return

def PortraitCustomPress():
	return

def PortraitDonePress():
	global CharGenWindow, CharGenState, PortraitWindow, PortraitButton, PortraitTable, Portrait, GenderButton, RaceButton
	GemRB.UnloadWindow(PortraitWindow)
	GemRB.SetButtonPicture(CharGenWindow, PortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "L")
	GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, GenderButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, RaceButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	CharGenState = 1
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def PortraitCancelPress():
	global CharGenWindow, PortraitWindow
	GemRB.UnloadWindow(PortraitWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Race Selection

def RacePress():
	global CharGenWindow, RaceWindow, RaceDoneButton, RaceTable, RaceTextArea
	GemRB.SetVisible(CharGenWindow, 0)
	RaceWindow = GemRB.LoadWindow(8)
	RaceTable = GemRB.LoadTable("RACES")
	GemRB.SetVar("Race", 0)

	for i in range(2, 8):
		RaceSelectButton = GemRB.GetControl(RaceWindow, i)
		GemRB.SetButtonFlags(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)
	
	for i in range(2, 8):
		RaceSelectButton = GemRB.GetControl(RaceWindow, i)
		GemRB.SetButtonState(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_ON_PRESS, "RaceSelectPress")
		GemRB.SetText(RaceWindow, RaceSelectButton, GemRB.GetTableValue(RaceTable, i - 2, 0))
		GemRB.SetVarAssoc(RaceWindow, RaceSelectButton, "Race", i - 1)

	RaceTextArea = GemRB.GetControl(RaceWindow, 8)
	GemRB.SetText(RaceWindow, RaceTextArea, 17237)

	RaceDoneButton = GemRB.GetControl(RaceWindow, 0)
	GemRB.SetButtonState(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_ON_PRESS, "RaceDonePress")
	GemRB.SetText(RaceWindow, RaceDoneButton, 11973)
	GemRB.SetButtonFlags(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	RaceCancelButton = GemRB.GetControl(RaceWindow, 10)
	GemRB.SetButtonState(RaceWindow, RaceCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(RaceWindow, RaceCancelButton, IE_GUI_BUTTON_ON_PRESS, "RaceCancelPress")
	GemRB.SetText(RaceWindow, RaceCancelButton, 13727)

	GemRB.SetVisible(RaceWindow, 1)
	return

def RaceSelectPress():
	global RaceWindow, RaceDoneButton, RaceTable, RaceTextArea
	Race = GemRB.GetVar("Race") - 1
	GemRB.SetText(RaceWindow, RaceTextArea, GemRB.GetTableValue(RaceTable, Race, 1) )
	GemRB.SetButtonState(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def RaceDonePress():
	global CharGenWindow, CharGenState, RaceWindow, RaceButton, ClassButton
	GemRB.UnloadWindow(RaceWindow)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, RaceButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, ClassButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	CharGenState = 2
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def RaceCancelPress():
	global CharGenWindow, RaceWindow
	GemRB.UnloadWindow(RaceWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

# Class Selection

def ClassPress():
	global CharGenWindow, ClassWindow, ClassTable, ClassTextArea, ClassDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	ClassWindow = GemRB.LoadWindow(2)
	ClassTable = GemRB.LoadTable("CLASSES")
	ClassCount = GemRB.GetTableRowCount(ClassTable)
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	GemRB.SetVar("Class", 0)

	for i in range(2, 10):
		ClassSelectButton = GemRB.GetControl(ClassWindow, i)
		GemRB.SetButtonFlags(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_SET)

	HasMulti = 0
	j = 2
	for i in range(0, ClassCount):
		Allowed = GemRB.GetTableValue(ClassTable, GemRB.GetTableRowName(ClassTable, i), RaceName)
		if GemRB.GetTableValue(ClassTable, i, 4):
			if Allowed != 0:
				HasMulti = 1
		else:
			ClassSelectButton = GemRB.GetControl(ClassWindow, j)
			j = j + 1
			if Allowed > 0:
				GemRB.SetButtonState(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_ENABLED)
			else:
				GemRB.SetButtonState(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetEvent(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_ON_PRESS,  "ClassSelectPress")
			GemRB.SetText(ClassWindow, ClassSelectButton, GemRB.GetTableValue(ClassTable, i, 0) )
			GemRB.SetVarAssoc(ClassWindow, ClassSelectButton , "Class", i + 1)

	ClassMultiButton = GemRB.GetControl(ClassWindow, 10)
	if HasMulti == 0:
		GemRB.SetButtonState(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_DISABLED)
	else:
		GemRB.SetButtonState(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_ON_PRESS, "ClassMultiPress")
	GemRB.SetText(ClassWindow, ClassMultiButton, 11993)
	
	ClassSpecialButton = GemRB.GetControl(ClassWindow, 11)
	GemRB.SetButtonState(ClassWindow, ClassSpecialButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassSpecialButton, IE_GUI_BUTTON_ON_PRESS, "ClassSpecialPress")
	GemRB.SetText(ClassWindow, ClassSpecialButton, 11994)

	ClassTextArea = GemRB.GetControl(ClassWindow, 13)
	GemRB.SetText(ClassWindow, ClassTextArea, 17242)

	ClassDoneButton = GemRB.GetControl(ClassWindow, 0)
	GemRB.SetButtonState(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_ON_PRESS, "ClassDonePress")
	GemRB.SetText(ClassWindow, ClassDoneButton, 11973)
	GemRB.SetButtonFlags(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ClassCancelButton = GemRB.GetControl(ClassWindow, 14)
	GemRB.SetButtonState(ClassWindow, ClassCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassCancelButton, IE_GUI_BUTTON_ON_PRESS, "ClassCancelPress")
	GemRB.SetText(ClassWindow, ClassCancelButton, 13727)

	GemRB.SetVisible(ClassWindow, 1)
	return

def ClassSelectPress():
	global ClassWindow, ClassTable, ClassTextArea, ClassDoneButton
	Class = GemRB.GetVar("Class") - 1
	GemRB.SetText(ClassWindow, ClassTextArea, GemRB.GetTableValue(ClassTable, Class, 1) )
	GemRB.SetButtonState(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def ClassMultiPress():
	global ClassWindow, ClassTable, ClassMultiWindow, ClassMultiTextArea, ClassMultiDoneButton
	GemRB.SetVisible(ClassWindow, 0)
	ClassMultiWindow = GemRB.LoadWindow(10)
	ClassCount = GemRB.GetTableRowCount(ClassTable)
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)

	for i in range(2, 10):
		ClassMultiSelectButton = GemRB.GetControl(ClassMultiWindow, i)
		GemRB.SetButtonFlags(ClassMultiWindow, ClassMultiSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_SET)

	j = 2
	for i in range(0, ClassCount):
		ClassName = GemRB.GetTableRowName(ClassTable, i)
		if (GemRB.GetTableValue(ClassTable, ClassName, "MULTI") > 0):
			ClassMultiSelectButton = GemRB.GetControl(ClassMultiWindow, j)
			j = j + 1
			if (GemRB.GetTableValue(ClassTable, ClassName, RaceName) > 0):
				GemRB.SetButtonState(ClassMultiWindow, ClassMultiSelectButton, IE_GUI_BUTTON_ENABLED)
			else:
				GemRB.SetButtonState(ClassMultiWindow, ClassMultiSelectButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetEvent(ClassMultiWindow, ClassMultiSelectButton, IE_GUI_BUTTON_ON_PRESS,  "ClassMultiSelectPress")
			GemRB.SetText(ClassMultiWindow, ClassMultiSelectButton, GemRB.GetTableValue(ClassTable, i, 0) )
			GemRB.SetVarAssoc(ClassMultiWindow, ClassMultiSelectButton , "Class", i + 1)

	ClassMultiTextArea = GemRB.GetControl(ClassMultiWindow, 12)
	GemRB.SetText(ClassMultiWindow, ClassMultiTextArea, 17244)

	ClassMultiDoneButton = GemRB.GetControl(ClassMultiWindow, 0)
	GemRB.SetButtonState(ClassMultiWindow, ClassMultiDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ClassMultiWindow, ClassMultiDoneButton, IE_GUI_BUTTON_ON_PRESS, "ClassMultiDonePress")
	GemRB.SetText(ClassMultiWindow, ClassMultiDoneButton, 11973)
	GemRB.SetButtonFlags(ClassMultiWindow, ClassMultiDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ClassMultiCancelButton = GemRB.GetControl(ClassMultiWindow, 14)
	GemRB.SetButtonState(ClassMultiWindow, ClassMultiCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassMultiWindow, ClassMultiCancelButton, IE_GUI_BUTTON_ON_PRESS, "ClassMultiCancelPress")
	GemRB.SetText(ClassMultiWindow, ClassMultiCancelButton, 13727)

	GemRB.SetVisible(ClassMultiWindow, 1)
	return

def ClassMultiSelectPress():
	global ClassMultiWindow, ClassTable, ClassMultiTextArea, ClassMultiDoneButton
	Class = GemRB.GetVar("Class") - 1
	GemRB.SetText(ClassMultiWindow, ClassMultiTextArea, GemRB.GetTableValue(ClassTable, Class, 1) )
	GemRB.SetButtonState(ClassMultiWindow, ClassMultiDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def ClassMultiDonePress():
	global ClassMultiWindow
	GemRB.UnloadWindow(ClassMultiWindow)
	ClassDonePress()
	return

def ClassMultiCancelPress():
	global ClassWindow, ClassMultiWindow
	GemRB.UnloadWindow(ClassMultiWindow)
	GemRB.SetVisible(ClassWindow, 1)
	return

def ClassSpecialPress():
	global ClassWindow, ClassSpecialWindow, ClassSpecialTextArea, ClassSpecialDoneButton
	GemRB.SetVisible(ClassWindow, 0)
	ClassSpecialWindow = GemRB.LoadWindow(12)

	ClassSpecialTextArea = GemRB.GetControl(ClassSpecialWindow, 11)
	GemRB.SetText(ClassSpecialWindow, ClassSpecialTextArea, 17245)

	ClassSpecialDoneButton = GemRB.GetControl(ClassSpecialWindow, 0)
	GemRB.SetButtonState(ClassSpecialWindow, ClassSpecialDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ClassSpecialWindow, ClassSpecialDoneButton, IE_GUI_BUTTON_ON_PRESS, "ClassSpecialDonePress")
	GemRB.SetText(ClassSpecialWindow, ClassSpecialDoneButton, 11973)
	GemRB.SetButtonFlags(ClassSpecialWindow, ClassSpecialDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ClassSpecialCancelButton = GemRB.GetControl(ClassSpecialWindow, 12)
	GemRB.SetButtonState(ClassSpecialWindow, ClassSpecialCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassSpecialWindow, ClassSpecialCancelButton, IE_GUI_BUTTON_ON_PRESS, "ClassSpecialCancelPress")
	GemRB.SetText(ClassSpecialWindow, ClassSpecialCancelButton, 13727)

	GemRB.SetVisible(ClassSpecialWindow, 1)
	return

def ClassSpecialDonePress():
	global ClassSpecialWindow
	GemRB.UnloadWindow(ClassSpecialWindow)
	ClassDonePress()
	return

def ClassSpecialCancelPress():
	global ClassWindow, ClassSpecialWindow
	GemRB.UnloadWindow(ClassSpecialWindow)
	GemRB.SetVisible(ClassWindow, 1)
	return

def ClassDonePress():
	global CharGenWindow, CharGenState, ClassWindow, ClassButton, AlignmentButton
	GemRB.UnloadWindow(ClassWindow)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, ClassButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	CharGenState = 3
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def ClassCancelPress():
	global CharGenWindow, ClassWindow
	GemRB.UnloadWindow(ClassWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Alignment Selection

def AlignmentPress():
	global CharGenWindow, AlignmentWindow, AlignmentTable, AlignmentTextArea, AlignmentDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	AlignmentWindow = GemRB.LoadWindow(3)
	AlignmentTable = GemRB.LoadTable("ALIGNS")
	ClassAlignmentTable = GemRB.LoadTable("ALIGNMNT")
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	GemRB.SetVar("Alignment", 0)
	
	for i in range (2, 11):
		AlignmentSelectButton = GemRB.GetControl(AlignmentWindow, i)
		GemRB.SetButtonFlags(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)

	for i in range (0, 9):
		AlignmentSelectButton = GemRB.GetControl(AlignmentWindow, i + 2)
		if GemRB.GetTableValue(ClassAlignmentTable, ClassName, GemRB.GetTableValue(AlignmentTable, i, 4)) == 0:
			GemRB.SetButtonState(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_DISABLED)
		else:
			GemRB.SetButtonState(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentSelectPress")
		GemRB.SetText(AlignmentWindow, AlignmentSelectButton, GemRB.GetTableValue(AlignmentTable, i, 0) )
		GemRB.SetVarAssoc(AlignmentWindow, AlignmentSelectButton, "Alignment", i + 1)

	AlignmentTextArea = GemRB.GetControl(AlignmentWindow, 11)
	GemRB.SetText(AlignmentWindow, AlignmentTextArea, 9602)

	AlignmentDoneButton = GemRB.GetControl(AlignmentWindow, 0)
	GemRB.SetButtonState(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentDonePress")
	GemRB.SetText(AlignmentWindow, AlignmentDoneButton, 11973)
	GemRB.SetButtonFlags(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AlignmentCancelButton = GemRB.GetControl(AlignmentWindow, 13)
	GemRB.SetButtonState(AlignmentWindow, AlignmentCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AlignmentWindow, AlignmentCancelButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentCancelPress")
	GemRB.SetText(AlignmentWindow, AlignmentCancelButton, 13727)

	GemRB.SetVisible(AlignmentWindow, 1)
	return


def AlignmentSelectPress():
	global AlignmentWindow, AlignmentTable, AlignmentTextArea, AlignmentDoneButton
	Alignment = GemRB.GetVar("Alignment") - 1 
	GemRB.SetText(AlignmentWindow, AlignmentTextArea, GemRB.GetTableValue(AlignmentTable, Alignment, 1))
	GemRB.SetButtonState(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def AlignmentDonePress():
	global CharGenWindow, CharGenState, AlignmentWindow, AlignmentButton, AbilitiesButton
	GemRB.UnloadWindow(AlignmentWindow)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	CharGenState = 4
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def AlignmentCancelPress():
	global CharGenWindow, AlignmentWindow
	GemRB.UnloadWindow(AlignmentWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Abilities Selection

def AbilitiesPress():
	global CharGenWindow, AbilitiesWindow, AbilitiesTable, AbilitiesRaceAddTable, AbilitiesRaceReqTable, AbilitiesClassReqTable, AbilitiesTextArea, AbilitiesRecallButton, AbilitiesDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	AbilitiesWindow = GemRB.LoadWindow(4)
	AbilitiesTable = GemRB.LoadTable("ABILITY")
	AbilitiesRaceAddTable = GemRB.LoadTable("ABRACEAD")
	AbilitiesRaceReqTable = GemRB.LoadTable("ABRACERQ")
	AbilitiesClassReqTable = GemRB.LoadTable("ABCLASRQ")

	PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
	GemRB.SetLabelUseRGB(AbilitiesWindow, PointsLeftLabel, 1)
	
	for i in range (0, 6):
		AbilitiesLabelButton = GemRB.GetControl(AbilitiesWindow, 30 + i)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesLabelButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesLabelButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesLabelPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesLabelButton, "AbilityIndex", i + 1)

		AbilitiesPlusButton = GemRB.GetControl(AbilitiesWindow, 16 + i * 2)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesPlusButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesPlusPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesPlusButton, "AbilityIndex", i + 1)

		AbilitiesMinusButton = GemRB.GetControl(AbilitiesWindow, 17 + i * 2)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesMinusButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesMinusPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesMinusButton, "AbilityIndex", i + 1)

		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + i)
		GemRB.SetLabelUseRGB(AbilitiesWindow, AbilityLabel, 1)

	AbilitiesRerollPress()

	AbilitiesStoreButton = GemRB.GetControl(AbilitiesWindow, 37)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesStoreButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesStoreButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesStorePress")
	GemRB.SetText(AbilitiesWindow, AbilitiesStoreButton, 17373)
	
	AbilitiesRecallButton = GemRB.GetControl(AbilitiesWindow, 38)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesRecallPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesRecallButton, 17374)
	
	AbilitiesRerollButton = GemRB.GetControl(AbilitiesWindow,2)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRerollButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesRerollButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesRerollPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesRerollButton, 11982)

	AbilitiesTextArea = GemRB.GetControl(AbilitiesWindow, 29)
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, 17247)

	AbilitiesDoneButton = GemRB.GetControl(AbilitiesWindow, 0)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesDonePress")
	GemRB.SetText(AbilitiesWindow, AbilitiesDoneButton, 11973)
	GemRB.SetButtonFlags(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AbilitiesCancelButton = GemRB.GetControl(AbilitiesWindow, 36)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesCancelButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesCancelPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesCancelButton, 13727)

	GemRB.SetVisible(AbilitiesWindow, 1)
	return

def AbilitiesCalcLimits(Index):
	global RaceTable, AbilitiesRaceReqTable, AbilitiesRaceAddTable, ClassTable, AbilitiesClassReqTable
	global AbilitiesMinimum, AbilitiesMaximum, AbilitiesModifier
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	Race = GemRB.GetTableRowIndex(AbilitiesRaceReqTable, RaceName)
	AbilitiesMinimum = GemRB.GetTableValue(AbilitiesRaceReqTable, Race, Index * 2)
	AbilitiesMaximum = GemRB.GetTableValue(AbilitiesRaceReqTable, Race, Index * 2 + 1)
	AbilitiesModifier = GemRB.GetTableValue(AbilitiesRaceAddTable, Race, Index)

	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	Class = GemRB.GetTableRowIndex(AbilitiesClassReqTable, ClassName)
	Min = GemRB.GetTableValue(AbilitiesClassReqTable, Class, Index)
	if Min > 0 and AbilitiesMinimum < Min:
		AbilitiesMinimum = Min

	AbilitiesMinimum = AbilitiesMinimum + AbilitiesModifier
	AbilitiesMaximum = AbilitiesMaximum + AbilitiesModifier
	return

def AbilitiesLabelPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	return

def AbilitiesPlusPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea, AbilitiesMinimum, AbilitiesMaximum
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	PointsLeft = GemRB.GetVar("Ability0")
	Ability = GemRB.GetVar("Ability" + str(AbilityIndex + 1) )
	if PointsLeft > 0 and Ability < AbilitiesMaximum:
		PointsLeft = PointsLeft - 1
		GemRB.SetVar("Ability0", PointsLeft)
		PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
		GemRB.SetText(AbilitiesWindow, PointsLeftLabel, str(PointsLeft) )
		Ability = Ability + 1
		GemRB.SetVar("Ability" + str(AbilityIndex + 1), Ability)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + AbilityIndex)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Ability) )
		if PointsLeft == 0:
			GemRB.SetButtonState(AlignmentWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def AbilitiesMinusPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea, AbilitiesMinimum, AbilitiesMaximum
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	PointsLeft = GemRB.GetVar("Ability0")
	Ability = GemRB.GetVar("Ability" + str(AbilityIndex + 1) )
	if Ability > AbilitiesMinimum:
		Ability = Ability - 1
		GemRB.SetVar("Ability" + str(AbilityIndex + 1), Ability)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + AbilityIndex)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Ability) )
		PointsLeft = PointsLeft + 1
		GemRB.SetVar("Ability0", PointsLeft)
		PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
		GemRB.SetText(AbilitiesWindow, PointsLeftLabel, str(PointsLeft) )
		GemRB.SetButtonState(AlignmentWindow, AbilitiesDoneButton, IE_GUI_BUTTON_DISABLED)
	return

def AbilitiesStorePress():
	global AbilitiesWindow, AbilitiesRecallButton
	for i in range(0, 7):
		GemRB.SetVar("Stored" + str(i), GemRB.GetVar("Ability" + str(i)))
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_ENABLED)
	return

def AbilitiesRecallPress():
	global AbilitiesWindow
	GemRB.InvalidateWindow(AbilitiesWindow)
	for i in range(0, 7):
		GemRB.SetVar("Ability" + str(i), GemRB.GetVar("Stored" + str(i)) )
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002 + i)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(GemRB.GetVar("Ability" + str(i))) )
	return

def AbilitiesRerollPress():
	global AbilitiesWindow, AbilitiesMinimum, AbilitiesMaximum, AbilitiesModifier
	GemRB.InvalidateWindow(AbilitiesWindow)
	GemRB.SetVar("Ability0", 0)
	PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
	GemRB.SetText(AbilitiesWindow, PointsLeftLabel, "0")
	Dices = 3
	Sides = 6
	for i in range(0, 6):
		AbilitiesCalcLimits(i)
		Value = GemRB.Roll(Dices, Sides, AbilitiesModifier)
		if Value < AbilitiesMinimum:
			Value = AbilitiesMinimum
		if Value > AbilitiesMaximum:
			Value = AbilitiesMaximum
		GemRB.SetVar("Ability" + str(i + 1), Value)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + i)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Value) )
	return

def AbilitiesDonePress():
	global CharGenWindow, CharGenState, AbilitiesWindow, AbilitiesButton, SkillsButton, SkillsState
	GemRB.UnloadWindow(AbilitiesWindow)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	CharGenState = 5
	SkillsState = 0
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def AbilitiesCancelPress():
	global CharGenWindow, AbilitiesWindow
	GemRB.UnloadWindow(AbilitiesWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Skills Selection

def SkillsPress():
	global CharGenWindow, ClassTable, RaceTable, SkillsState, SkillsButton, AppearanceButton, CharGenState
	
	# For now, readability is preferred over speed. This could be optimized later.
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	if SkillsState == 0:
		RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
		if ClassName == "THIEF" or ClassName == "FIGHTER_THIEF" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_THIEF":
			SkillsSelect()
		elif ClassName == "RANGER" or ClassName == "CLERIC_RANGER":
			SkillRaceTable = GemRB.LoadTable("SKILLRAC")
			SkillDexterityTable = GemRB.LoadTable("SKILLDEX")
			Dexterity = str(GemRB.GetVar("Ability2") )
			GemRB.SetVar("Skill0", GemRB.GetTableValue(SkillRaceTable, RaceName, "STEALTH") + GemRB.GetTableValue(SkillDexterityTable, Dexterity, "STEALTH") + GemRB.GetTableValue(GemRB.LoadTable("SKILLRNG"), "1", "STEALTH"))
			RacialEnemySelect()
		elif ClassName == "BARD":
			SkillRaceTable = GemRB.LoadTable("SKILLRAC")
			SkillDexterityTable = GemRB.LoadTable("SKILLDEX")
			Dexterity = str(GemRB.GetVar("Ability2") )
			GemRB.SetVar("Skill2", GemRB.GetTableValue(SkillRaceTable, RaceName, "PICK_POCKETS") + GemRB.GetTableValue(SkillDexterityTable, Dexterity, "PICK_POCKETS") + GemRB.GetTableValue(GemRB.LoadTable("SKILLBRD"), "1", "PICK_POCKETS"))
			SkillsState = 1
		else:
			SkillsState = 1

	if SkillsState == 1:
		ProficienciesSelect()

	if SkillsState == 2:
		if ClassName == "MAGE" or ClassName == "FIGHTER_MAGE" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_MAGE" or ClassName == "FIGHTER_MAGE_CLERIC":
			MageSpellsSelect()
		else:
			SkillsState = 3

	if SkillsState == 3:
		if ClassName == "MAGE" or ClassName == "FIGHTER_MAGE" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF":
			MageSpellsMemorize()
		elif ClassName == "CLERIC" or ClassName == "FIGHTER_CLERIC" or ClassName == "CLERIC_THIEF" or ClassName == "CLERIC_RANGER":
			PriestSpellsMemorize()
		elif ClassName == "CLERIC_MAGE" or ClassName == "FIGHTER_MAGE_CLERIC":
			MageSpellsMemorize()
			PriestSpellsMemorize()
		else:
			SkillsState = 4

	if SkillsState == 4:
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonFlags(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
		CharGenState = 6
		SetCharacterDescription()
	return


def SkillsSelect():
	global CharGenWindow, SkillsWindow, SkillsTextArea, SkillsTable, SkillsDoneButton, RaceTable, SkillsPointsLeft
	GemRB.SetVisible(CharGenWindow, 0)
	SkillsWindow = GemRB.LoadWindow(6)
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	Dexterity = str(GemRB.GetVar("Ability2") )
	SkillsTable = GemRB.LoadTable("SKILLS")
	SkillRaceTable = GemRB.LoadTable("SKILLRAC")
	SkillDexterityTable = GemRB.LoadTable("SKILLDEX")

	SkillsPointsLeft = 30
	SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
	GemRB.SetLabelUseRGB(SkillsWindow, SkillsPointsLeftLabel, 1)
	GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))

	for i in range (0, 4):
		SkillsLabelButton = GemRB.GetControl(SkillsWindow, 21 + i)
		GemRB.SetButtonState(SkillsWindow, SkillsLabelButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsLabelButton, IE_GUI_BUTTON_ON_PRESS, "SkillsLabelPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsLabelButton, "SkillIndex", i)

		SkillsPlusButton = GemRB.GetControl(SkillsWindow, 11 + i * 2)
		GemRB.SetButtonState(SkillsWindow, SkillsPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsPlusButton, IE_GUI_BUTTON_ON_PRESS, "SkillsPlusPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsPlusButton, "SkillIndex", i)

		SkillsMinusButton = GemRB.GetControl(SkillsWindow, 12 + i * 2)
		GemRB.SetButtonState(SkillsWindow, SkillsMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsMinusButton, IE_GUI_BUTTON_ON_PRESS, "SkillsMinusPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsMinusButton, "SkillIndex", i)

		SkillName = GemRB.GetTableRowName(SkillsTable, i)
		SkillValue = GemRB.GetTableValue(SkillRaceTable, RaceName, SkillName)
		SkillValue = SkillValue + GemRB.GetTableValue(SkillDexterityTable, Dexterity, SkillName)
		GemRB.SetVar("Skill" + str(i), SkillValue)
		GemRB.SetVar("SkillBase" + str(i), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + i)
		GemRB.SetLabelUseRGB(SkillsWindow, SkillLabel, 1)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))

	GemRB.SetToken("number", str(SkillsPointsLeft) )
	SkillsTextArea = GemRB.GetControl(SkillsWindow, 19)
	GemRB.SetText(SkillsWindow, SkillsTextArea, 17248)

	SkillsDoneButton = GemRB.GetControl(SkillsWindow, 0)
	GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_ON_PRESS, "SkillsDonePress")
	GemRB.SetText(SkillsWindow, SkillsDoneButton, 11973)
	GemRB.SetButtonFlags(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	SkillsCancelButton = GemRB.GetControl(SkillsWindow, 25)
	GemRB.SetButtonState(SkillsWindow, SkillsCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(SkillsWindow, SkillsCancelButton, IE_GUI_BUTTON_ON_PRESS, "SkillsCancelPress")
	GemRB.SetText(SkillsWindow, SkillsCancelButton, 13727)

	GemRB.SetVisible(SkillsWindow, 1)
	return

def SkillsLabelPress():
	global SkillsWindow, SkillsTextArea, SkillsTable
	SkillIndex = GemRB.GetVar("SkillIndex")
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	return

def SkillsPlusPress():
	global SkillsWindow, SkillsTextArea, SkillsTable, SkillsPointsLeft
	SkillIndex = GemRB.GetVar("SkillIndex")
	SkillValue = GemRB.GetVar("Skill" + str(SkillIndex))
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	if SkillValue < 99 and SkillsPointsLeft > 0:
		SkillsPointsLeft = SkillsPointsLeft - 1
		SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
		GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))
		SkillValue = SkillValue + 1
		GemRB.SetVar("Skill" + str(SkillIndex), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + SkillIndex)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))
		if SkillsPointsLeft == 0:
			GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def SkillsMinusPress():
	global SkillsWindow, SkillsTextArea, SkillsTable, SkillsPointsLeft
	SkillIndex = GemRB.GetVar("SkillIndex")
	SkillValue = GemRB.GetVar("Skill" + str(SkillIndex))
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	if SkillValue > GemRB.GetVar("SkillBase" + str(SkillIndex)):
		SkillValue = SkillValue - 1
		GemRB.SetVar("Skill" + str(SkillIndex), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + SkillIndex)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))
		SkillsPointsLeft = SkillsPointsLeft + 1
		SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
		GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))
		GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DISABLED)
	return

def SkillsDonePress():
	global CharGenWindow, SkillsWindow, SkillsState
	GemRB.UnloadWindow(SkillsWindow)
	SkillsState = 1
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def SkillsCancelPress():
	global CharGenWindow, SkillsWindow, SkillsState
	GemRB.UnloadWindow(SkillsWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Racial Enemy Selection

def RacialEnemySelect():
	global CharGenWindow, RacialEnemyWindow, RacialEnemyTable, RacialEnemyTextArea, RacialEnemyDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	RacialEnemyWindow = GemRB.LoadWindow(15)
	RacialEnemyTable = GemRB.LoadTable("ENEMIES")
	RacialEnemyCount = GemRB.GetTableRowCount(RacialEnemyTable)

	for i in range(2, 8):
		RacialEnemySelectButton = GemRB.GetControl(RacialEnemyWindow, i)
		GemRB.SetButtonFlags(RacialEnemyWindow, RacialEnemySelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)
	
	for i in range(2, 8):
		RacialEnemySelectButton = GemRB.GetControl(RacialEnemyWindow, i)
		GemRB.SetButtonState(RacialEnemyWindow, RacialEnemySelectButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(RacialEnemyWindow, RacialEnemySelectButton, IE_GUI_BUTTON_ON_PRESS, "RacialEnemySelectPress")
		GemRB.SetVarAssoc(RacialEnemyWindow, RacialEnemySelectButton, "RacialEnemy", i - 1)

	GemRB.SetVar("RacialEnemyIndex", 0)
	RacialEnemyScrollBar = GemRB.GetControl(RacialEnemyWindow, 1)
	GemRB.SetVarAssoc(RacialEnemyWindow, RacialEnemyScrollBar, "RacialEnemyIndex", RacialEnemyCount - 5)
	GemRB.SetEvent(RacialEnemyWindow, RacialEnemyScrollBar, IE_GUI_SCROLLBAR_ON_CHANGE, "DisplayRacialEnemies")

	RacialEnemyTextArea = GemRB.GetControl(RacialEnemyWindow, 8)
	GemRB.SetText(RacialEnemyWindow, RacialEnemyTextArea, 17256)

	RacialEnemyDoneButton = GemRB.GetControl(RacialEnemyWindow, 11)
	GemRB.SetButtonState(RacialEnemyWindow, RacialEnemyDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(RacialEnemyWindow, RacialEnemyDoneButton, IE_GUI_BUTTON_ON_PRESS, "RacialEnemyDonePress")
	GemRB.SetText(RacialEnemyWindow, RacialEnemyDoneButton, 11973)
	GemRB.SetButtonFlags(RacialEnemyWindow, RacialEnemyDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	RacialEnemyCancelButton = GemRB.GetControl(RacialEnemyWindow, 10)
	GemRB.SetButtonState(RacialEnemyWindow, RacialEnemyCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(RacialEnemyWindow, RacialEnemyCancelButton, IE_GUI_BUTTON_ON_PRESS, "RacialEnemyCancelPress")
	GemRB.SetText(RacialEnemyWindow, RacialEnemyCancelButton, 13727)

	DisplayRacialEnemies()
	GemRB.SetVisible(RacialEnemyWindow, 1)
	return

def DisplayRacialEnemies():
	global RacialEnemyWindow, RacialEnemyTable
	RacialEnemyIndex = GemRB.GetVar("RacialEnemyIndex")
	for i in range(2, 8):
		RacialEnemySelectButton = GemRB.GetControl(RacialEnemyWindow, i)
		GemRB.SetText(RacialEnemyWindow, RacialEnemySelectButton, GemRB.GetTableValue(RacialEnemyTable, RacialEnemyIndex + i - 2, 0))
	return

def RacialEnemySelectPress():
	global RacialEnemyWindow, RacialEnemyDoneButton, RacialEnemyTable, RacialEnemyTextArea
	RacialEnemy = GemRB.GetVar("RacialEnemyIndex") + GemRB.GetVar("RacialEnemy") - 1
	GemRB.SetText(RacialEnemyWindow, RacialEnemyTextArea, GemRB.GetTableValue(RacialEnemyTable, RacialEnemy, 1) )
	GemRB.SetButtonState(RacialEnemyWindow, RacialEnemyDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def RacialEnemyDonePress():
	global CharGenWindow, RacialEnemyWindow, SkillsState
	GemRB.UnloadWindow(RacialEnemyWindow)
	SkillsState = 1
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def RacialEnemyCancelPress():
	global CharGenWindow, RacialEnemyWindow, SkillsState
	GemRB.UnloadWindow(RacialEnemyWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Weapon Proficiencies Selection

def ProficienciesSelect():
	global CharGenWindow, ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft, ProficienciesDoneButton, ClassTable, ProfsMaxTable
	GemRB.SetVisible(CharGenWindow, 0)
	ProficienciesWindow = GemRB.LoadWindow(9)
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	ProficienciesTable = GemRB.LoadTable("WEAPPROF")
	ProfsTable = GemRB.LoadTable("PROFS")
	ProfsMaxTable = GemRB.LoadTable("PROFSMAX")
	ClassWeaponsTable = GemRB.LoadTable("CLASWEAP")

	Class = GemRB.GetTableRowIndex(ProfsTable, ClassName)
	ProficienciesPointsLeft = GemRB.GetTableValue(ProfsTable, Class, 0)
	PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
	GemRB.SetLabelUseRGB(ProficienciesWindow, PointsLeftLabel, 1)
	GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))

	for i in range (0, 8):
		ProficienciesLabel = GemRB.GetControl(ProficienciesWindow, 69 + i)
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ON_PRESS, "ProficienciesLabelPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesLabel, "ProficienciesIndex", i + 1)

		for j in range (0, 5):
			ProficienciesMark = GemRB.GetControl(ProficienciesWindow, 27 + i * 5 + j)
			GemRB.SetButtonSprites(ProficienciesWindow, ProficienciesMark, "GUIPFC", 0, 0, 0, 0, 0)
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)

		Allowed = GemRB.GetTableValue(ClassWeaponsTable, ClassName, GemRB.GetTableRowName(ProficienciesTable, i))

		ProficienciesPlusButton = GemRB.GetControl(ProficienciesWindow, 11 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesPlusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesPlusButton, "ProficienciesIndex", i + 1)

		ProficienciesMinusButton = GemRB.GetControl(ProficienciesWindow, 12 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesMinusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesMinusButton, "ProficienciesIndex", i + 1)

	for i in range (0,7):
		ProficienciesLabel = GemRB.GetControl(ProficienciesWindow, 85 + i)
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ON_PRESS, "ProficienciesLabelPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesLabel, "ProficienciesIndex", i + 9)

		for j in range (0, 5):
			ProficienciesMark = GemRB.GetControl(ProficienciesWindow, 92 + i * 5 + j)
			GemRB.SetButtonSprites(ProficienciesWindow, ProficienciesMark, "GUIPFC", 0, 0, 0, 0, 0)
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)

		Allowed = GemRB.GetTableValue(ClassWeaponsTable, ClassName, GemRB.GetTableRowName(ProficienciesTable, i + 8))
		
		ProficienciesPlusButton = GemRB.GetControl(ProficienciesWindow, 127 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesPlusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesPlusButton, "ProficienciesIndex", i + 9)

		ProficienciesMinusButton = GemRB.GetControl(ProficienciesWindow, 128 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesMinusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesMinusButton, "ProficienciesIndex", i + 9)

	for i in range(1, 16):
		GemRB.SetVar("Proficiency" + str(i), 0)

	GemRB.SetToken("number", str(ProficienciesPointsLeft) )
	ProficienciesTextArea = GemRB.GetControl(ProficienciesWindow, 68)
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, 9588)

	ProficienciesDoneButton = GemRB.GetControl(ProficienciesWindow, 0)
	GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesDonePress")
	GemRB.SetText(ProficienciesWindow, ProficienciesDoneButton, 11973)
	GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ProficienciesCancelButton = GemRB.GetControl(ProficienciesWindow, 77)
	GemRB.SetButtonState(ProficienciesWindow, ProficienciesCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ProficienciesWindow, ProficienciesCancelButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesCancelPress")
	GemRB.SetText(ProficienciesWindow, ProficienciesCancelButton, 13727)

	GemRB.SetVisible(ProficienciesWindow, 1)
	return

def ProficienciesLabelPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesPlusPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft, ProfsMaxTable
	
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	ProficienciesValue = GemRB.GetVar("Proficiency" + str(ProficienciesIndex) )
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	Class = GemRB.GetTableRowIndex(ProfsMaxTable, ClassName)
	if ProficienciesPointsLeft > 0 and ProficienciesValue < GemRB.GetTableValue(ProfsMaxTable, Class, 0):
		ProficienciesPointsLeft = ProficienciesPointsLeft - 1
		PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
		GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))
		if ProficienciesPointsLeft == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_ENABLED)
		
		ProficienciesValue = ProficienciesValue + 1
		GemRB.SetVar("Proficiency" + str(ProficienciesIndex), ProficienciesValue)
		if ProficienciesIndex < 8:
			ControlID = 26 + ProficienciesIndex * 5 + ProficienciesValue
		else:
			ControlID = 51 + ProficienciesIndex * 5 + ProficienciesValue
		ProficienciesMark = GemRB.GetControl(ProficienciesWindow, ControlID)
		GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_NAND)
		
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesMinusPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft
	
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	ProficienciesValue = GemRB.GetVar("Proficiency" + str(ProficienciesIndex) )
	if ProficienciesValue > 0:
		ProficienciesValue = ProficienciesValue - 1
		GemRB.SetVar("Proficiency" + str(ProficienciesIndex), ProficienciesValue)
		if ProficienciesIndex < 8:
			ControlID = 27 + ProficienciesIndex * 5 + ProficienciesValue
		else:
			ControlID = 52 + ProficienciesIndex * 5 + ProficienciesValue
		ProficienciesMark = GemRB.GetControl(ProficienciesWindow, ControlID)
		GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		
		ProficienciesPointsLeft = ProficienciesPointsLeft + 1
		PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
		GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DISABLED)
		
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesDonePress():
	global CharGenWindow, ProficienciesWindow, SkillsState
	GemRB.UnloadWindow(ProficienciesWindow)
	SkillsState = 2
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def ProficienciesCancelPress():
	global CharGenWindow, ProficienciesWindow, SkillsState
	GemRB.UnloadWindow(ProficienciesWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Spells Selection

def MageSpellsSelect():
	global CharGenWindow, MageSpellsWindow, MageSpellsTable, MageSpellsTextArea, MageSpellsDoneButton, MageSpellsSelectPointsLeft
	GemRB.SetVisible(CharGenWindow, 0)
	MageSpellsWindow = GemRB.LoadWindow(7)
	MageSpellsTable = GemRB.LoadTable("MAGESP")
	MageSpellsCount = GemRB.GetTableRowCount(MageSpellsTable)
	GemRB.SetVar("MageSpellBook", 0)
	GemRB.SetVar("SpellMask", 0)

	MageSpellsSelectPointsLeft = 2
	PointsLeftLabel = GemRB.GetControl(MageSpellsWindow, 0x1000001b)
	GemRB.SetLabelUseRGB(MageSpellsWindow, PointsLeftLabel, 1)
	GemRB.SetText(MageSpellsWindow, PointsLeftLabel, str(MageSpellsSelectPointsLeft))

	for i in range (0, 24):
		SpellButton = GemRB.GetControl(MageSpellsWindow, i + 2)
		GemRB.SetButtonFlags(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_CHECKBOX, OP_OR)
		if i < MageSpellsCount:
			# Color is no good yet :-(
			GemRB.SetButtonBAM(MageSpellsWindow, SpellButton, GemRB.GetTableValue(MageSpellsTable, i, 0), 1, 0, 63)
			GemRB.SetButtonState(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
			GemRB.SetEvent(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_ON_PRESS, "MageSpellsSelectPress")
			GemRB.SetVarAssoc(MageSpellsWindow, SpellButton, "SpellMask", 1 << i)
		else:
			GemRB.SetButtonState(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_DISABLED)

	GemRB.SetToken("number", str(MageSpellsSelectPointsLeft))
	MageSpellsTextArea = GemRB.GetControl(MageSpellsWindow, 27)
	GemRB.SetText(MageSpellsWindow, MageSpellsTextArea, 17250)

	MageSpellsDoneButton = GemRB.GetControl(MageSpellsWindow, 0)
	GemRB.SetButtonState(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_ON_PRESS, "MageSpellsDonePress")
	GemRB.SetText(MageSpellsWindow, MageSpellsDoneButton, 11973)
	GemRB.SetButtonFlags(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	MageSpellsCancelButton = GemRB.GetControl(MageSpellsWindow, 29)
	GemRB.SetButtonState(MageSpellsWindow, MageSpellsCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(MageSpellsWindow, MageSpellsCancelButton, IE_GUI_BUTTON_ON_PRESS, "MageSpellsCancelPress")
	GemRB.SetText(MageSpellsWindow, MageSpellsCancelButton, 13727)

	GemRB.SetVisible(MageSpellsWindow, 1)
	return

def MageSpellsSelectPress():
	global MageSpellsWindow, MageSpellsTable, MageSpellsTextArea, MageSpellsDoneButton, MageSpellsSelectPointsLeft
	MageSpellsCount = GemRB.GetTableRowCount(MageSpellsTable)
	MageSpellBook = GemRB.GetVar("MageSpellBook")
	SpellMask = GemRB.GetVar("SpellMask")
	Spell = abs(MageSpellBook - SpellMask)

	i = -1
	while (Spell > 0):
		i = i + 1
		Spell = Spell >> 1
	GemRB.SetText(MageSpellsWindow, MageSpellsTextArea, GemRB.GetTableValue(MageSpellsTable, i, 1))

	if SpellMask < MageSpellBook:
		MageSpellsSelectPointsLeft = MageSpellsSelectPointsLeft + 1
		for i in range (0, MageSpellsCount):
			SpellButton = GemRB.GetControl(MageSpellsWindow, i + 2)
			if (((1 << i) & SpellMask) == 0):
				GemRB.SetButtonState(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonState(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_DISABLED)
	else:
		MageSpellsSelectPointsLeft = MageSpellsSelectPointsLeft - 1
		if MageSpellsSelectPointsLeft == 0:
			for i in range (0, MageSpellsCount):
				SpellButton = GemRB.GetControl(MageSpellsWindow, i + 2)
				if ((1 << i) & SpellMask) == 0:
					GemRB.SetButtonState(MageSpellsWindow, SpellButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonState(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_ENABLED)

	PointsLeftLabel = GemRB.GetControl(MageSpellsWindow, 0x1000001b)
	GemRB.SetText(MageSpellsWindow, PointsLeftLabel, str(MageSpellsSelectPointsLeft))
	GemRB.SetVar("MageSpellBook", SpellMask)
	return

def MageSpellsDonePress():
	global CharGenWindow, MageSpellsWindow, SkillsState
	GemRB.UnloadWindow(MageSpellsWindow)
	SkillsState = 3
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def MageSpellsCancelPress():
	global CharGenWindow, MageSpellsWindow, SkillsState
	GemRB.UnloadWindow(MageSpellsWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Mage Spells Memorize

def MageSpellsMemorize():
	global CharGenWindow, MageMemorizeWindow, MageSpellsTable, MageMemorizeTextArea, MageMemorizeDoneButton, MageMemorizePointsLeft
	GemRB.SetVisible(CharGenWindow, 0)
	MageMemorizeWindow = GemRB.LoadWindow(16)
	MageSpellsCount = GemRB.GetTableRowCount(MageSpellsTable)
	MaxSpellsMageTable = GemRB.LoadTable("MXSPLWIZ")
	MageSpellBook = GemRB.GetVar("MageSpellBook")
	GemRB.SetVar("MageMemorized", 0)
	GemRB.SetVar("SpellMask", 0)

	MageMemorizePointsLeft = GemRB.GetTableValue(MaxSpellsMageTable, "1", "1" )
	PointsLeftLabel = GemRB.GetControl(MageMemorizeWindow, 0x1000001b)
	GemRB.SetLabelUseRGB(MageMemorizeWindow, PointsLeftLabel, 1)
	GemRB.SetText(MageMemorizeWindow, PointsLeftLabel, str(MageMemorizePointsLeft))

	j = 0
	for i in range (0, 12):
		SpellButton = GemRB.GetControl(MageMemorizeWindow, i + 2)
		GemRB.SetButtonFlags(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_CHECKBOX, OP_OR)
		while (j < MageSpellsCount) and (((1 << j) & MageSpellBook) == 0):
			j = j + 1
		if j < MageSpellsCount:
			# Color is no good yet :-(
			GemRB.SetButtonBAM(MageMemorizeWindow, SpellButton, GemRB.GetTableValue(MageSpellsTable, j, 0), 1, 0, 63)
			GemRB.SetButtonState(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
			GemRB.SetEvent(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_ON_PRESS, "MageMemorizeSelectPress")
			GemRB.SetVarAssoc(MageMemorizeWindow, SpellButton, "SpellMask", 1 << j)
			j = j + 1
		else:
			GemRB.SetButtonState(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_DISABLED)

	GemRB.SetToken("number", str(MageMemorizePointsLeft))
	MageMemorizeTextArea = GemRB.GetControl(MageMemorizeWindow, 27)
	GemRB.SetText(MageMemorizeWindow, MageMemorizeTextArea, 17253)

	MageMemorizeDoneButton = GemRB.GetControl(MageMemorizeWindow, 0)
	GemRB.SetButtonState(MageMemorizeWindow, MageMemorizeDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(MageMemorizeWindow, MageMemorizeDoneButton, IE_GUI_BUTTON_ON_PRESS, "MageMemorizeDonePress")
	GemRB.SetText(MageMemorizeWindow, MageMemorizeDoneButton, 11973)
	GemRB.SetButtonFlags(MageMemorizeWindow, MageMemorizeDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	MageMemorizeCancelButton = GemRB.GetControl(MageMemorizeWindow, 29)
	GemRB.SetButtonState(MageMemorizeWindow, MageMemorizeCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(MageMemorizeWindow, MageMemorizeCancelButton, IE_GUI_BUTTON_ON_PRESS, "MageMemorizeCancelPress")
	GemRB.SetText(MageMemorizeWindow, MageMemorizeCancelButton, 13727)

	GemRB.SetVisible(MageMemorizeWindow, 1)
	return

def MageMemorizeSelectPress():
	global MageMemorizeWindow, MageSpellsTable, MageMemorizeTextArea, MageMemorizeDoneButton, MageMemorizePointsLeft
	MageSpellsCount = GemRB.GetTableRowCount(MageSpellsTable)
	MageSpellBook = GemRB.GetVar("MageSpellBook")
	MageMemorized = GemRB.GetVar("MageMemorized")
	SpellMask = GemRB.GetVar("SpellMask")
	Spell = abs(MageMemorized - SpellMask)

	i = -1
	while (Spell > 0):
		i = i + 1
		Spell = Spell >> 1
	GemRB.SetText(MageMemorizeWindow, MageMemorizeTextArea, GemRB.GetTableValue(MageSpellsTable, i, 1))

	if SpellMask < MageMemorized:
		MageMemorizePointsLeft = MageMemorizePointsLeft + 1
		j = 0
		for i in range (0, 12):
			SpellButton = GemRB.GetControl(MageMemorizeWindow, i + 2)
			while (j < MageSpellsCount) and (((1 << j) & MageSpellBook) == 0):
				j = j + 1
			if j < MageSpellsCount:
				GemRB.SetButtonState(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
				j = j + 1
		GemRB.SetButtonState(MageMemorizeWindow, MageMemorizeDoneButton, IE_GUI_BUTTON_DISABLED)
	else:
		MageMemorizePointsLeft = MageMemorizePointsLeft - 1
		if MageMemorizePointsLeft == 0:
			j = 0
			for i in range (0, 12):
				SpellButton = GemRB.GetControl(MageMemorizeWindow, i + 2)
				while (j < MageSpellsCount) and (((1 << j) & MageSpellBook) == 0):
					j = j + 1
				if j < MageSpellsCount:
					if ((1 << j) & SpellMask) == 0:
						GemRB.SetButtonState(MageMemorizeWindow, SpellButton, IE_GUI_BUTTON_DISABLED)
					j = j + 1
			GemRB.SetButtonState(MageMemorizeWindow, MageMemorizeDoneButton, IE_GUI_BUTTON_ENABLED)

	PointsLeftLabel = GemRB.GetControl(MageMemorizeWindow, 0x1000001b)
	GemRB.SetText(MageSpellsWindow, PointsLeftLabel, str(MageMemorizePointsLeft))
	GemRB.SetVar("MageMemorized", SpellMask)
	return

def MageMemorizeDonePress():
	global CharGenWindow, MageMemorizeWindow, SkillsState
	GemRB.UnloadWindow(MageMemorizeWindow)
	SkillsState = 4
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def MageMemorizeCancelPress():
	global CharGenWindow, MageMemorizeWindow, SkillsState
	GemRB.UnloadWindow(MageMemorizeWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Priest Spells Memorize

def PriestSpellsMemorize():
	global CharGenWindow, PriestMemorizeWindow, PriestSpellsTable
	global PriestMemorizeTextArea, PriestMemorizeDoneButton, PriestMemorizePointsLeft
	GemRB.SetVisible(CharGenWindow, 0)
	PriestMemorizeWindow = GemRB.LoadWindow(17)
	PriestSpellsTable = GemRB.LoadTable("PRIESTSP")
	PriestSpellsCount = GemRB.GetTableRowCount(PriestSpellsTable)
	MaxSpellsPriestTable = GemRB.LoadTable("MXSPLPRS")
	GemRB.SetVar("PriestMemorized", 0)
	GemRB.SetVar("SpellMask", 0)

	PriestMemorizePointsLeft = GemRB.GetTableValue(MaxSpellsPriestTable, "1", "1" )
	PointsLeftLabel = GemRB.GetControl(PriestMemorizeWindow, 0x1000001b)
	GemRB.SetLabelUseRGB(PriestMemorizeWindow, PointsLeftLabel, 1)
	GemRB.SetText(PriestMemorizeWindow, PointsLeftLabel, str(PriestMemorizePointsLeft))

	for i in range (0, 12):
		SpellButton = GemRB.GetControl(PriestMemorizeWindow, i + 2)
		GemRB.SetButtonFlags(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_CHECKBOX, OP_OR)
		if i < PriestSpellsCount:
			# Color is no good yet :-(
			GemRB.SetButtonBAM(PriestMemorizeWindow, SpellButton, GemRB.GetTableValue(PriestSpellsTable, i, 0), 1, 0, 63)
			GemRB.SetButtonState(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
			GemRB.SetEvent(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_ON_PRESS, "PriestMemorizeSelectPress")
			GemRB.SetVarAssoc(PriestMemorizeWindow, SpellButton, "SpellMask", 1 << i)
		else:
			GemRB.SetButtonState(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_DISABLED)

	GemRB.SetToken("number", str(PriestMemorizePointsLeft))
	PriestMemorizeTextArea = GemRB.GetControl(PriestMemorizeWindow, 27)
	GemRB.SetText(PriestMemorizeWindow, PriestMemorizeTextArea, 17253)

	PriestMemorizeDoneButton = GemRB.GetControl(PriestMemorizeWindow, 0)
	GemRB.SetButtonState(PriestMemorizeWindow, PriestMemorizeDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(PriestMemorizeWindow, PriestMemorizeDoneButton, IE_GUI_BUTTON_ON_PRESS, "PriestMemorizeDonePress")
	GemRB.SetText(PriestMemorizeWindow, PriestMemorizeDoneButton, 11973)
	GemRB.SetButtonFlags(PriestMemorizeWindow, PriestMemorizeDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	PriestMemorizeCancelButton = GemRB.GetControl(PriestMemorizeWindow, 29)
	GemRB.SetButtonState(PriestMemorizeWindow, PriestMemorizeCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PriestMemorizeWindow, PriestMemorizeCancelButton, IE_GUI_BUTTON_ON_PRESS, "PriestMemorizeCancelPress")
	GemRB.SetText(PriestMemorizeWindow, PriestMemorizeCancelButton, 13727)

	GemRB.SetVisible(PriestMemorizeWindow, 1)
	return

def PriestMemorizeSelectPress():
	global PriestMemorizeWindow, PriestSpellsTable, PriestMemorizeTextArea, PriestMemorizeDoneButton, PriestMemorizePointsLeft
	PriestSpellsCount = GemRB.GetTableRowCount(PriestSpellsTable)
	PriestMemorized = GemRB.GetVar("PriestMemorized")
	SpellMask = GemRB.GetVar("SpellMask")
	Spell = abs(PriestMemorized - SpellMask)

	i = -1
	while (Spell > 0):
		i = i + 1
		Spell = Spell >> 1
	GemRB.SetText(PriestMemorizeWindow, PriestMemorizeTextArea, GemRB.GetTableValue(PriestSpellsTable, i, 1))

	if SpellMask < PriestMemorized:
		PriestMemorizePointsLeft = PriestMemorizePointsLeft + 1
		for i in range (0, PriestSpellsCount):
			SpellButton = GemRB.GetControl(PriestMemorizeWindow, i + 2)
			if (((1 << i) & SpellMask) == 0):
				GemRB.SetButtonState(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonState(PriestMemorizeWindow, PriestMemorizeDoneButton, IE_GUI_BUTTON_DISABLED)
	else:
		PriestMemorizePointsLeft = PriestMemorizePointsLeft - 1
		if PriestMemorizePointsLeft == 0:
			for i in range (0, PriestSpellsCount):
				SpellButton = GemRB.GetControl(PriestMemorizeWindow, i + 2)
				if ((1 << i) & SpellMask) == 0:
					GemRB.SetButtonState(PriestMemorizeWindow, SpellButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonState(PriestMemorizeWindow, PriestMemorizeDoneButton, IE_GUI_BUTTON_ENABLED)

	PointsLeftLabel = GemRB.GetControl(PriestMemorizeWindow, 0x1000001b)
	GemRB.SetText(MageSpellsWindow, PointsLeftLabel, str(PriestMemorizePointsLeft))
	GemRB.SetVar("PriestMemorized", SpellMask)
	return

def PriestMemorizeDonePress():
	global CharGenWindow, PriestMemorizeWindow, SkillsState
	GemRB.UnloadWindow(PriestMemorizeWindow)
	SkillsState = 4
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def PriestMemorizeCancelPress():
	global CharGenWindow, PriestMemorizeWindow, SkillsState
	GemRB.UnloadWindow(PriestMemorizeWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Appearance Selection

def AppearancePress():
	global CharGenWindow, AppearanceWindow, AppearanceTable
	global PortraitTable, Portrait, AppearanceAvatarButton, PortraitName
	global AppearanceHairButton, AppearanceSkinButton
	global AppearanceMajorButton, AppearanceMinorButton

	GemRB.SetVisible(CharGenWindow, 0)
	AppearanceWindow = GemRB.LoadWindow(13)
	PortraitName = GemRB.GetTableRowName(PortraitTable, Portrait)
	AppearanceTable = GemRB.LoadTable("PORTCOLR")
	PortraitIndex = GemRB.GetTableRowIndex(AppearanceTable, PortraitName + "L")
	HairColor = GemRB.GetTableValue(AppearanceTable, PortraitIndex, 1)
	GemRB.SetVar("HairColor", HairColor)
	SkinColor = GemRB.GetTableValue(AppearanceTable, PortraitIndex, 2)
	GemRB.SetVar("SkinColor", SkinColor)
	MajorColor = GemRB.GetTableValue(AppearanceTable, PortraitIndex, 3)
	GemRB.SetVar("MajorColor", MajorColor)
	MinorColor = GemRB.GetTableValue(AppearanceTable, PortraitIndex, 4)
	GemRB.SetVar("MinorColor", MinorColor)

	AppearanceAvatarButton = GemRB.GetControl(AppearanceWindow, 1)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceAvatarButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_ANIMATED, OP_OR)
	ApperanceDrawAvatar()

	AppearanceHairButton = GemRB.GetControl(AppearanceWindow, 2)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceHairButton, IE_GUI_BUTTON_PICTURE, OP_OR)
	GemRB.SetButtonState(AppearanceWindow, AppearanceHairButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceHairButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceHairPress")
	GemRB.SetButtonBAM(AppearanceWindow, AppearanceHairButton, "COLGRAD", 1, 0, HairColor)

	AppearanceSkinButton = GemRB.GetControl(AppearanceWindow, 3)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceSkinButton, IE_GUI_BUTTON_PICTURE, OP_OR)
	GemRB.SetButtonState(AppearanceWindow, AppearanceSkinButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceSkinButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceSkinPress")
	GemRB.SetButtonBAM(AppearanceWindow, AppearanceSkinButton, "COLGRAD", 1, 0, SkinColor)

	AppearanceMajorButton = GemRB.GetControl(AppearanceWindow, 4)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceMajorButton, IE_GUI_BUTTON_PICTURE, OP_OR)
	GemRB.SetButtonState(AppearanceWindow, AppearanceMajorButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceMajorButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceMajorPress")
	GemRB.SetButtonBAM(AppearanceWindow, AppearanceMajorButton, "COLGRAD", 1, 0, MajorColor)

	AppearanceMinorButton = GemRB.GetControl(AppearanceWindow, 5)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceMinorButton, IE_GUI_BUTTON_PICTURE, OP_OR)
	GemRB.SetButtonState(AppearanceWindow, AppearanceMinorButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceMinorButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceMinorPress")
	GemRB.SetButtonBAM(AppearanceWindow, AppearanceMinorButton, "COLGRAD", 1, 0, MinorColor)

	AppearanceDoneButton = GemRB.GetControl(AppearanceWindow, 0)
	GemRB.SetButtonState(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceDonePress")
	GemRB.SetText(AppearanceWindow, AppearanceDoneButton, 11973)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AppearanceCancelButton = GemRB.GetControl(AppearanceWindow, 13)
	GemRB.SetButtonState(AppearanceWindow, AppearanceCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceCancelButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceCancelPress")
	GemRB.SetText(AppearanceWindow, AppearanceCancelButton, 13727)

	GemRB.SetVisible(AppearanceWindow, 1)
	return

def ApperanceDrawAvatar():
	global AppearanceAvatarButton, RaceTable, ClassTable
	AppearanceAvatarTable = GemRB.LoadTable("PDOLLS")
	AvatarID = 0x5000
        table = GemRB.LoadTable("AVPREFR")
        AvatarID = AvatarID+GemRB.GetTableValue(table, GemRB.GetVar("Race"),0)
        table = GemRB.LoadTable("AVPREFC")
        AvatarID = AvatarID+GemRB.GetTableValue(table, GemRB.GetVar("Class"),0)
        table = GemRB.LoadTable("AVPREFG")
        AvatarID = AvatarID+GemRB.GetTableValue(table, GemRB.GetVar("Gender"),0)

	AvatarRef = GemRB.GetTableValue(AppearanceAvatarTable, hex(AvatarID), "LEVEL1")
	GemRB.SetButtonBAM(AppearanceWindow, AppearanceAvatarButton, AvatarRef, 1, 0, 0)
	return

def AppearanceHairPress():
	GemRB.SetVar("ColorType", 0)
	AppearanceColorChoice(GemRB.GetVar("HairColor"))
	return

def AppearanceSkinPress():
	GemRB.SetVar("ColorType", 1)
	AppearanceColorChoice(GemRB.GetVar("SkinColor"))
	return

def AppearanceMajorPress():
	GemRB.SetVar("ColorType", 2)
	AppearanceColorChoice(GemRB.GetVar("MajorColor"))
	return

def AppearanceMinorPress():
	GemRB.SetVar("ColorType", 3)
	AppearanceColorChoice(GemRB.GetVar("MinorColor"))
	return

def AppearanceColorChoice(CurrentColor):
	global AppearanceWindow, AppearanceColorWindow
	GemRB.SetVisible(AppearanceWindow, 0)
	AppearanceColorWindow = GemRB.LoadWindow(14)
	AppearanceColorTable = GemRB.LoadTable("AVCOLORS")
	ColorType = GemRB.GetVar("ColorType")
	GemRB.SetVar("SelectedColor", CurrentColor)

	for i in range (0, 34):
		ColorButton = GemRB.GetControl(AppearanceColorWindow, i)
		GemRB.SetButtonState(AppearanceColorWindow, ColorButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetButtonFlags(AppearanceColorWindow, ColorButton, IE_GUI_BUTTON_PICTURE, OP_OR)

	for i in range (0, 34):
		Color = GemRB.GetTableValue(AppearanceColorTable, ColorType, i)
		if Color != "*":
			ColorButton = GemRB.GetControl(AppearanceColorWindow, i)
			GemRB.SetButtonBAM(AppearanceColorWindow, ColorButton, "COLGRAD", 2, 0, Color)
			GemRB.SetEvent(AppearanceColorWindow, ColorButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceColorSelected")
			GemRB.SetVarAssoc(AppearanceColorWindow, ColorButton, "SelectedColor", Color)
	
	GemRB.SetVisible(AppearanceColorWindow, 1)
	return

def AppearanceColorSelected():
	global AppearanceWindow, AppearanceColorWindow
	global AppearanceHairButton, AppearanceSkinButton, AppearanceMajorButton, AppearanceMinorButton
	GemRB.UnloadWindow(AppearanceColorWindow)
	ColorType = GemRB.GetVar("ColorType")
	Color = GemRB.GetVar("SelectedColor")
	if ColorType == 0:
		GemRB.SetVar("HairColor", Color)
		GemRB.SetButtonBAM(AppearanceWindow, AppearanceHairButton, "COLGRAD", 1, 0, Color)
	elif ColorType == 1:
		GemRB.SetVar("SkinColor", Color)
		GemRB.SetButtonBAM(AppearanceWindow, AppearanceSkinButton, "COLGRAD", 1, 0, Color)
	elif ColorType == 2:
		GemRB.SetVar("MajorColor", Color)
		GemRB.SetButtonBAM(AppearanceWindow, AppearanceMajorButton, "COLGRAD", 1, 0, Color)
	elif ColorType == 3:
		GemRB.SetVar("MinorColor", Color)
		GemRB.SetButtonBAM(AppearanceWindow, AppearanceMinorButton, "COLGRAD", 1, 0, Color)
	ApperanceDrawAvatar()
	GemRB.SetVisible(AppearanceWindow, 1)
	return

def AppearanceDonePress():
	global CharGenWindow, AppearanceWindow
	GemRB.UnloadWindow(AppearanceWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	CharSoundSelect()
	return

def AppearanceCancelPress():
	global CharGenWindow, AppearanceWindow
	GemRB.UnloadWindow(AppearanceWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


def CharSoundSelect():
	global CharGenWindow, CharSoundWindow, CharSoundTable, CharSoundStrings
	GemRB.SetVisible(CharGenWindow, 0)
	CharSoundWindow = GemRB.LoadWindow(19)
	CharSoundTable = GemRB.LoadTable("CHARSND")
	CharSoundStrings = GemRB.LoadTable("CHARSTR")

	CharSoundVoiceList = GemRB.GetControl(CharSoundWindow, 45)
	GemRB.SetTextAreaSelectable(CharSoundWindow, CharSoundVoiceList, 1)
	
	VoiceList = []
	for i in range (0, GemRB.GetTableRowCount(CharSoundStrings) ):
		VoiceList.append(str(GemRB.GetTableRowName(CharSoundStrings, i)).upper())
	VoiceList.sort()
	VoiceList.reverse()
	while (len(VoiceList) > 0):
		GemRB.TextAreaAppend(CharSoundWindow, CharSoundVoiceList, VoiceList.pop(), -1)

	CharSoundPlayButton = GemRB.GetControl(CharSoundWindow, 47)
	GemRB.SetButtonState(CharSoundWindow, CharSoundPlayButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharSoundWindow, CharSoundPlayButton, IE_GUI_BUTTON_ON_PRESS, "CharSoundPlayPress")
	GemRB.SetText(CharSoundWindow, CharSoundPlayButton, "play")

	CharSoundTextArea = GemRB.GetControl(CharSoundWindow, 50)
	GemRB.SetText(CharSoundWindow, CharSoundTextArea, 11315)

	CharSoundDoneButton = GemRB.GetControl(CharSoundWindow, 0)
	GemRB.SetButtonState(CharSoundWindow, CharSoundDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharSoundWindow, CharSoundDoneButton, IE_GUI_BUTTON_ON_PRESS, "CharSoundDonePress")
	GemRB.SetText(CharSoundWindow, CharSoundDoneButton, 11973)
	GemRB.SetButtonFlags(CharSoundWindow, CharSoundDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	CharSoundCancelButton = GemRB.GetControl(CharSoundWindow, 10)
	GemRB.SetButtonState(CharSoundWindow, CharSoundCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharSoundWindow, CharSoundCancelButton, IE_GUI_BUTTON_ON_PRESS, "CharSoundCancelPress")
	GemRB.SetText(CharSoundWindow, CharSoundCancelButton, 13727)
	
	GemRB.SetVisible(CharSoundWindow, 1)
	return

def CharSoundPlayPress():
	return

def CharSoundDonePress():
	global CharGenWindow, CharSoundWindow, AppearanceButton, BiographyButton, NameButton, CharGenState
	GemRB.UnloadWindow(CharSoundWindow)
	GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonFlags(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DEFAULT, OP_NAND)
	GemRB.SetButtonState(CharGenWindow, BiographyButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(CharGenWindow, NameButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 7
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def CharSoundCancelPress():
	global CharGenWindow, CharSoundWindow
	GemRB.UnloadWindow(CharSoundWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Biography Selection

def BiographyPress():
	global CharGenWindow, BiographyWindow, BiographyField
	GemRB.SetVisible(CharGenWindow, 0)
	BiographyWindow = GemRB.LoadWindow(51)

	BiographyField = GemRB.GetControl(BiographyWindow, 4)
	GemRB.SetText(BiographyWindow, BiographyField, 19423)

	BiographyClearButton = GemRB.GetControl(BiographyWindow, 5)
	GemRB.SetButtonState(BiographyWindow, BiographyClearButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(BiographyWindow, BiographyClearButton, IE_GUI_BUTTON_ON_PRESS, "BiographyClearPress")
	GemRB.SetText(BiographyWindow, BiographyClearButton, 18622)

	BiographyCancelButton = GemRB.GetControl(BiographyWindow, 2)
	GemRB.SetButtonState(BiographyWindow, BiographyCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(BiographyWindow, BiographyCancelButton, IE_GUI_BUTTON_ON_PRESS, "BiographyCancelPress")
	GemRB.SetText(BiographyWindow, BiographyCancelButton, 13727)

	BiographyDoneButton = GemRB.GetControl(BiographyWindow, 1)
	GemRB.SetButtonState(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_ON_PRESS, "BiographyDonePress")
	GemRB.SetText(BiographyWindow, BiographyDoneButton, 11973)
	GemRB.SetButtonFlags(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	GemRB.SetVisible(BiographyWindow, 1)
	return

def BiographyClearPress():
	global BiographyWindow, BiographyField
	GemRB.SetText(BiographyWindow, BiographyField, "")
	return

def BiographyCancelPress():
	global CharGenWindow, BiographyWindow
	GemRB.UnloadWindow(BiographyWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

def BiographyDonePress():
	global CharGenWindow, BiographyWindow, BiographyField
	GemRB.SetToken("Biography", GemRB.QueryText(BiographyWindow, BiographyField) )
	GemRB.UnloadWindow(BiographyWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Name Selection

def NamePress():
	global CharGenWindow, NameWindow, NameDoneButton, NameField
	GemRB.SetVisible(CharGenWindow, 0)
	NameWindow = GemRB.LoadWindow(5)

	NameField = GemRB.GetControl(NameWindow, 2)
	GemRB.SetEvent(NameWindow, NameField, IE_GUI_EDIT_ON_CHANGE, "NameEditChange")

	NameDoneButton = GemRB.GetControl(NameWindow, 0)
	GemRB.SetButtonState(NameWindow, NameDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(NameWindow, NameDoneButton, IE_GUI_BUTTON_ON_PRESS, "NameDonePress")
	GemRB.SetText(NameWindow, NameDoneButton, 11973)
	GemRB.SetButtonFlags(NameWindow, NameDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	NameCancelButton = GemRB.GetControl(NameWindow, 3)
	GemRB.SetButtonState(NameWindow, NameCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(NameWindow, NameCancelButton, IE_GUI_BUTTON_ON_PRESS, "NameCancelPress")
	GemRB.SetText(NameWindow, NameCancelButton, 13727)

	GemRB.SetVisible(NameWindow, 1)
	GemRB.SetControlStatus(NameWindow, NameField, IE_GUI_CONTROL_FOCUSED)
	return

def NameEditChange():
	global NameField
	if GemRB.QueryText(NameWindow, NameField) == "":
		GemRB.SetButtonState(NameWindow, NameDoneButton, IE_GUI_BUTTON_DISABLED)
	else:
		GemRB.SetButtonState(NameWindow, NameDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def NameDonePress():
	global CharGenWindow, CharGenState, NameWindow, NameField, AcceptButton
	GemRB.SetToken("CHARNAME", GemRB.QueryText(NameWindow, NameField) )
	GemRB.UnloadWindow(NameWindow)
	CharGenState = 8
	GemRB.SetButtonState(CharGenWindow, AcceptButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow, AcceptButton, IE_GUI_BUTTON_DEFAULT, OP_OR)
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def NameCancelPress():
	global CharGenWindow, NameWindow

	GemRB.SetToken("CHARNAME", "")
	GemRB.UnloadWindow(NameWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

# Import Character

def ImportPress():
	global CharGenWindow, ImportWindow
	GemRB.SetVisible(CharGenWindow, 0)
	ImportWindow = GemRB.LoadWindow(20)

	ImportDoneButton = GemRB.GetControl(ImportWindow, 0)
	GemRB.SetButtonState(ImportWindow, ImportDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ImportWindow, ImportDoneButton, IE_GUI_BUTTON_ON_PRESS, "ImportDonePress")
	GemRB.SetText(ImportWindow, ImportDoneButton, 11973)
	GemRB.SetButtonFlags(ImportWindow, ImportDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ImportCancelButton = GemRB.GetControl(ImportWindow, 1)
	GemRB.SetButtonState(ImportWindow, ImportCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ImportWindow, ImportCancelButton, IE_GUI_BUTTON_ON_PRESS, "ImportCancelPress")
	GemRB.SetText(ImportWindow, ImportCancelButton, 13727)

	GemRB.SetVisible(ImportWindow, 1)
	return

def ImportDonePress():
	return

def ImportCancelPress():
	global CharGenWindow, ImportWindow
	GemRB.UnloadWindow(ImportWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

