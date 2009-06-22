# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# $Id$
#
#character generation, class (GUICG2)
import GemRB

from CharGenCommon import * 

from GUICommon import CloseOtherWindow


ClassWindow = 0
TextAreaControl = 0
DoneButton = 0
ClassTable = 0

def OnLoad():
	global ClassWindow, TextAreaControl, DoneButton
	global ClassTable

	if CloseOtherWindow (OnLoad):
		if(ClassWindow):
			ClassWindow.Unload()
			ClassWindow = None
		return
	
	GemRB.SetVar("Class",0)
	GemRB.SetVar("Multi Class",0)
	GemRB.SetVar("Specialist",0)
	GemRB.SetVar("Class Kit",0)
	
	GemRB.LoadWindowPack("GUICG")
	ClassTable = GemRB.LoadTableObject("classes")
	ClassCount = ClassTable.GetRowCount()+1
	ClassWindow = GemRB.LoadWindowObject(2)
	TmpTable=GemRB.LoadTableObject("races")
	RaceName = TmpTable.GetRowName(GemRB.GetVar("Race")-1 )

	#radiobutton groups must be set up before doing anything else to them
	for i in range(1,ClassCount):
		if ClassTable.GetValue(i-1,4):
			continue
			
		Button = ClassWindow.GetControl(i+1)
		Button.SetFlags(IE_GUI_BUTTON_RADIOBUTTON, OP_SET)
		Button.SetState(IE_GUI_BUTTON_DISABLED)

	GemRB.SetVar("MAGESCHOOL",0) 
	HasMulti = 0
	for i in range(1,ClassCount):
		ClassName = ClassTable.GetRowName(i-1)
		Allowed = ClassTable.GetValue(ClassName, RaceName)
		if ClassTable.GetValue(i-1,4):
			if Allowed!=0:
				HasMulti = 1
			continue
			
		Button = ClassWindow.GetControl(i+1)
		
		t = ClassTable.GetValue(i-1, 0)
		Button.SetText(t )

		if Allowed==2:
			GemRB.SetVar("MAGESCHOOL",5) #illusionist
		if Allowed!=1:
			continue
		Button.SetState(IE_GUI_BUTTON_ENABLED)
		Button.SetEvent(IE_GUI_BUTTON_ON_PRESS,  "ClassPress")
		Button.SetVarAssoc("Class", i)

	MultiClassButton = ClassWindow.GetControl(10)
	MultiClassButton.SetText(11993)
	if HasMulti == 0:
		MultiClassButton.SetState(IE_GUI_BUTTON_DISABLED)

	SpecialistButton = ClassWindow.GetControl(11)
	SpecialistButton.SetText(11994)
	
	BackButton = ClassWindow.GetControl(14)
	BackButton.SetText(15416)
	DoneButton = ClassWindow.GetControl(0)
	DoneButton.SetText(11973)
	DoneButton.SetFlags(IE_GUI_BUTTON_DEFAULT,OP_OR)

	TextAreaControl = ClassWindow.GetControl(13)

	Class = GemRB.GetVar("Class")-1
	if Class<0:
		TextAreaControl.SetText(17242)
		DoneButton.SetState(IE_GUI_BUTTON_DISABLED)
	else:
		TextAreaControl.SetText(ClassTable.GetValue(Class,1) )
		DoneButton.SetState(IE_GUI_BUTTON_ENABLED)

	MultiClassButton.SetEvent(IE_GUI_BUTTON_ON_PRESS,"MultiClassPress")
	SpecialistButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, "SpecialistPress")
	DoneButton.SetEvent(IE_GUI_BUTTON_ON_PRESS,"NextPress")
	BackButton.SetEvent(IE_GUI_BUTTON_ON_PRESS,"BackPress")
	ClassWindow.ShowModal(MODAL_SHADOW_NONE)
	return

def MultiClassPress():
	GemRB.SetVar("Multi Class",1)
	next()

def SpecialistPress():
	GemRB.SetVar("Specialist",1)

	GemRB.SetVar("Class Kit", 0)
	GemRB.SetVar("Class", 6)
	next()
	
def ClassPress():
	Class = GemRB.GetVar("Class")-1
	TextAreaControl.SetText(ClassTable.GetValue(Class,1) )
	DoneButton.SetState(IE_GUI_BUTTON_ENABLED)
	return

def NextPress():
	# find the class from the class table
	ClassIndex = GemRB.GetVar ("Class") - 1
	Class = ClassTable.GetValue (ClassIndex, 5)
	#protect against barbarians
	ClassName = ClassTable.GetRowName (ClassTable.FindValue (5, Class) )
	
	MyChar = GemRB.GetVar ("Slot")
	GemRB.SetPlayerStat (MyChar, IE_CLASS, Class)
	next()
	