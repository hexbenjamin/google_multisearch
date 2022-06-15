#NSIS Example Install Script

#Basic definitions
!define APPNAME "Sample App"
!define COMPANYNAME "Steves Toolbox LLC"
!define DESCRIPTION "Basic Python Application"
!define APPSHORTNAME "pyApp"

#Ask for administrative rights
RequestExecutionLevel admin

#Other options include:
#none
#user
#highest

#Default installation location - let's clutter up our root directory!
InstallDir "C:\${APPSHORTNAME}"

#Text (or RTF) file with license information. The text file must be in DOS end line format (\r\n)
LicenseData "..\docs\license.md"

#'Name' goes in the installer's title bar
Name "${COMPANYNAME}-${APPSHORTNAME}"

#Icon for the installer - this is the default icon
#Icon "logo.ico"

#The following lines replace the default icons
!include "MUI2.nsh"

#The name of the installer executable
outFile "${APPSHORTNAME}-inst.exe"

#...Not certain about this one
!include LogicLib.nsh

#Defines installation pages - these are known to NSIS
#Shows the license
Page license
#Allows user to pick install path
Page directory
#Installs the files
Page instfiles

#A macro to verify that administrator rights have been acquired
!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

#This ensures the administrator check is performed at startup?
function .onInit
	setShellVarContext all
	!insertmacro VerifyUserIsAdmin
functionEnd

# Files for the install directory - to build the installer, these should be in the same directory as the install script (this file)
section "install"
    setOutPath $INSTDIR
    
    # Files added here should be removed by the uninstaller (see section "uninstall")
    file /r ..\dist\*.*

    
	# Add any other files for the install directory (license files, app data, etc) here
 
    #This creates a shortcut to the executable on the desktop - the second set of options in quotes are for command-line arguments
	CreateShortcut "$desktop\Link to pyApp.lnk" "$instdir\pyApp.exe" "-c cfg\default.cfg"
 
sectionEnd