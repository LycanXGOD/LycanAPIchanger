#!/usr/bin/env python3

import os
import time

def show_main_page():
    print("\033[35mChange API Graphics - By LycanTweaks\033[0m")
    
    print("1: \033[31mVulkan\033[0m")
    print("2: \033[35mSkiaGL\033[0m")
    print("3: \033[35mOpenGL\033[0m")
    print("4: \033[34mRead\033[0m")
    print("5: \033[31mExit\033[0m")

def change_graphics_api(api):
    print("\033[33mChanging...\033[0m")
    time.sleep(5)  #LycanTweaks
    if api == 1:  
        os.system("adb shell setprop debug.hwui.renderer vulkan")
    elif api == 2:  
        os.system("adb shell setprop debug.hwui.renderer skiagl")
    elif api == 3:  
        os.system("adb shell setprop debug.hwui.renderer opengl")
    print("\033[32mSuccess\033[0m")
    time.sleep(3) 
    

def main():
    while True:
        show_main_page()

        choice = int(input("Select an option (1/2/3/4/5): "))

        if choice == 1:
            change_graphics_api(1)
        elif choice == 2:
            change_graphics_api(2)
        elif choice == 3:
            change_graphics_api(3)
        elif choice == 4:
            print("\033[31mThese Settings are available for most devices, but on some devices they are not supported, or do not support Vulkan.\033[0m")
        elif choice == 5:
            break
        else:
            print("Invalid option. Please select a valid number (1/2/3/4/5).")

if __name__ == "__main__":
    main()
    