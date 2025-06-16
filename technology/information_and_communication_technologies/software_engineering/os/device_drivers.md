# Device Drivers

Copied from [geeksforgeeks](https://www.geeksforgeeks.org/device-driver-and-its-purpose/)

Device Driver in computing refers to a special kind of software program or a specific type of software application that controls a specific hardware device that enables different hardware devices to communicate with the computer’s Operating System. A device driver communicates with the computer hardware by computer subsystem or computer bus connected to the hardware. 

Device Drivers are essential for a computer system to work properly because without a device driver the particular hardware fails to work accordingly, which means it fails in doing the function/action it was created to do. Most use the term Driver, but some may say Hardware Driver, which also refers to the Device Driver.

## Working

Device Drivers depend upon the Operating System’s instruction to access the device and perform any particular action. After the action, they also show their reactions by delivering output or status/message from the hardware device to the Operating system. For example, a printer driver tells the printer in which format to print after getting instruction from OS, similarly, A sound card driver is there due to which 1’s and 0’s data of the MP3 file is converted to audio signals and you enjoy the music. Card reader, controller, modem, network card, sound card, printer, video card, USB devices, RAM, Speakers, etc need Device Drivers to operate.

The software components invovled are :

1. Application
2. OS
3. Device Driver

The Device Driver is used to interact with a hardware or a virtual device.

## Types of Device Driver

For almost every device associated with the computer system there exist a Device Driver for the particular hardware. But it can be broadly classified into two types i.e.,

1. Kernel-mode Device Driver : This Kernel-mode device driver includes some generic hardware that loads with the operating system as part of the OS these are BIOS, motherboard, processor, and some other hardware that are part of kernel software. These include the minimum system requirement device drivers for each operating system.
2. User-mode Device Driver : Other than the devices which are brought by the kernel for working the system the user also brings some devices for use during the using of a system that devices need device drivers to function those drivers fall under User mode device driver. For example, the user needs any plug-and-play action that comes under this.
3. Virtual Device Driver : There are also virtual device drivers(VxD), which manage the virtual device. Sometimes we use the same hardware virtually at that time virtual driver controls/manages the data flow from the different applications used by different users to the same hardware. 

It is essential for a computer to have the required device drivers for all its parts to keep the system running efficiently. Many device drivers are provided by manufacturers from the beginning and also we can later include any required device driver for our system.
