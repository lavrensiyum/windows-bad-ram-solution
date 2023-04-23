# Blocking Bad Memory (RAM) Sectors on Windows

## Why i'm needed that?
If you have a problem as written in the section below, don't hesitate to check your RAM. And if you have a solid (soldered to the motherboard) notebook RAM like me, it's a good chance to get rid of the hole motherboard service charges (it saved me up to 10K TL/500 USD!).
## How can i know to need this solution?

If you have any of the problems mentioned below, I suggest you test your ram memory.

- Random web pages is crashing
  - Google Chrome: "Aw, snap! Something went wrong while displaying this webpage.
  - Mozilla Firefox: "Gah. Your tab just crashed"

- Windows is crashing (BSOD)
  - "Your PC ran into a problem ..." "Stop Code: MEMORY_MANAGEMENT"

- Some programs are freeze or not responding

- Downloaded files (especially large file) are corrupted.


## How that problem are triggered?

If any program or Windows process wants to access the damaged ram block, the process will have incorrect/missing/etc. data.

## Solution
We are planning below steps

1. Burn MemTest86 to our USB.
2. Running USB with Boot Menu mode to our PC.
3. Investigate the result.
4. Block Bad Memory with BadMemory.txt file

After that, we will repeat steps [2-4] until we are satisfied with step [4].

Let's get started
___
## Step 1. Burn MemTest86 to our USB with Rufus.

Go to https://www.memtest86.com/download.htm adress and click "Download MemTest86 Free (Version ??.? Build ?????)"

Extract the RAR to the desktop and run "imageUSB.exe".

Select the USB driver to be processed.

Make sure the 'Step2: Select the action to be performed ...' section, already choosed 'Write image to USB driver'.

Make sure the 'Available Options' is selected 'Post Image Verification' (not neccesery but good habit).

Select the image pathway (C:\Users\user\Desktop\memtest86-usb.img).

Click "Write" button and follow the instructions.

When its done, dont worry if you cant see your USB drivers on Windows Explorer.

[image](./pictures/image1.png)


___

## Step 2. Running USB with Boot Menu mode to our PC.

Restart the PC and and press F11 (it's depending on your machine, please try other Fxx buttons if thats now work).

Select the USB Drive (my drivers name is SanDisk Ultra so i gonna choose that)

Wait 3-4 minute. When its opened, click (your mouse is working here) "Config" button. If you don't have mouse, just wait 5-6 second.

In this screen, click "(S)tart Test" button in the left menu (if you don't have mouse, press "S" key).

Follow the instructions and wait the test is finish. 

When it's finished, follow the instructions and when it asked to save report to the USB as html, press "Y" key and when it's done to saved, you can safely exit the progam and go the next section.
___

## Step 3. Investigate the result.

If you have more than 10 bad memmory address, we are going to reduce it with Windows BCD (Boot Configuration Data).

Open the USB file on Windows and search `MemTest86-`. You will find a .txt file which name has something like `MemTest86-20230422-160514`. Open it.

Now, you has to copy all the whole txt and paste the online text/code editor or VS Code (because some web sites and VSCode have a middle mouse button feature to easy to copy spesific area.).

When you copy spesific word, you just holding left button and take to the ending words right? For now, you can just hold the middle mouse buttons (wheel) and drag to all needed ram address.

https://codesandbox.io // for online text* editor

[image](./pictures/image3.png)

Take a look at the results and find something like:

```
[Data Error] Test: 6, CPU: 6, Address: 408AD82F8, Expected: 20000000, Actual: 20000400`
```
In easy way, [CTRL + F] ==> "Address" seach and find the all what we need.

Go to Desktop and create a file "BadMemory.txt" and open it.

Copy all the Bad Memory Address and paste the "BadMemory.txt address. If you doing that secondly, delete the before you writted the bad memory addres because that you already banned!

After we coppyed all the bad memory addres on result file, it will look like:

[image](./pictures/image4.png)

When we finished, go to the next section.
___

## Step 4. Block Bad Memory with BadMemory.txt file

Now, copy the script (script.py or script.exe) on the same direction to "BadMemory.txt" (it will Desktop).

Run the script and wait the script take the every address and ban.

When it finished, you can go the next section.
___

MemTest can't write the all bad memory addres to first time (only the first part because of the limit). Because that, we are goint to repeat Step 2-4 sections. If you do that correctly, the MemTest will find less bad memory address every time (and one time it goes to 0!).




## Then?
In my research, some users writted that banning method can cause the unboot Windows. So be carefully, i dont have give you to guarentee!

In my computer, i have banned 600+ address and its work perfecly fine (in 4 month, i have 1-2 bsod of memory_management).

If you can change the ram stick, that will awsome but other way (like my motherboard-solid ram) you can try it.

That method will be break down if you format your Windows or update the Windows.


## The script.py or script.exe is safe? How it is work?

The script.py taking every line on RAM.txt text files and sending CMD (bcdedit /set {badmemory} badmemorylist 0x*********). The script is working with Python 3.8 version and using pre-loaded lib named "os".

If you want to run Python script without Python installed PC, you can run script.exe.

The script.exe is just compiled with [Nutika](https://github.com/Nuitka/Nuitka). 

If you want to compile script.py to .exe, run this command
1. Open the same directions of script.py with cmd
2. "pip install nutika"
3. "python -m nuitka --follow-imports --onefile script.py"
4. Done!

## Thanks!
This is my first guide on GitHub so if you see any "unusual" things like grammer or technic problem, feel free to contact me on Discord (yildiz 0001)!