#button flags
IE_GUI_BUTTON_NORMAL     = 0x00000004   #default button, doesn't stick
IE_GUI_BUTTON_NO_IMAGE   = 0x00000001
IE_GUI_BUTTON_PICTURE    = 0x00000002
IE_GUI_BUTTON_SOUND      = 0x00000004
IE_GUI_BUTTON_ALT_SOUND  = 0x00000008
IE_GUI_BUTTON_CHECKBOX   = 0x00000010   #or radio button
IE_GUI_BUTTON_RADIOBUTTON= 0x00000020   #sticks in a state
IE_GUI_BUTTON_DEFAULT    = 0x00000040   #enter button triggers it
IE_GUI_BUTTON_DRAGGABLE  = 0x00000080

#these bits are hardcoded in the .chu structure, don't move them
IE_GUI_BUTTON_ALIGN_LEFT = 0x00000100
IE_GUI_BUTTON_ALIGN_RIGHT= 0x00000200
IE_GUI_BUTTON_ALIGN_TOP  = 0x00000400
//end of hardcoded section

IE_GUI_BUTTON_ANIMATED   = 0x00010000
IE_GUI_BUTTON_NO_TEXT    = 0x00020000   # don't draw button label

#events
IE_GUI_BUTTON_ON_PRESS    = 0x00000000
IE_GUI_MOUSE_OVER_BUTTON  = 0x00000001
IE_GUI_SLIDER_ON_CHANGE   = 0x02000000
IE_GUI_EDIT_ON_CHANGE     = 0x03000000
IE_GUI_TEXTAREA_ON_CHANGE = 0x05000000
IE_GUI_LABEL_ON_PRESS     = 0x06000000
IE_GUI_SCROLLBAR_ON_CHANGE= 0x07000000

#button states
IE_GUI_BUTTON_ENABLED    = 0x00000000
IE_GUI_BUTTON_UNPRESSED  = 0x00000000
IE_GUI_BUTTON_PRESSED    = 0x00000001
IE_GUI_BUTTON_SELECTED   = 0x00000002
IE_GUI_BUTTON_DISABLED   = 0x00000003

global OP_SET, OP_OR, OP_NAND
OP_SET = 0
OP_OR = 1
OP_NAND = 2

global GEMRB_VERSION
GEMRB_VERSION = -1
