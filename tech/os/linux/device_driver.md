# Device Drivers in Linux

Content from [KnownSec404Team(Medium)](https://medium.com/@knownsec404team/how-to-develop-linux-driver-from-scratch-cc143e0c08a1) and [Vivek Gite](https://www.cyberciti.biz/tips/compiling-linux-kernel-module.html).

Drivers are used to help the hardware devices interact with the operating system. In windows, all the devices and drivers are grouped together in a single console called device manager. In Linux, even the hardware devices are treated like ordinary files, which makes it easier for the software to interact with the device drivers. When a device is connected to the system, a device file is created in /dev directory. 

Most Common types of devices in Linux:

1. Character devices – These devices transmit the data character by characters, like a mouse or a keyboard.
2. Block devices – These devices transfer unit of data storage called a block, USB drives, hard drives, and CD ROMs

Executing the following commands displays indications of type of device files : 

```
ls -l /dev
```

A sample output is : 

```
crw-rw-rw-   1 root tty         5,     2 Oct  2 17:43 ptmx
drwxr-xr-x   2 root root               0 Oct  2 08:05 pts
crw-rw-rw-   1 root root        1,     8 Oct  2 08:05 random
crw-rw-r--+  1 root root       10,   242 Oct  2 08:05 rfkill
lrwxrwxrwx   1 root root               4 Oct  2 08:05 rtc -> rtc0
crw-------   1 root root      248,     0 Oct  2 08:05 rtc0
brw-rw----   1 root disk        8,     0 Oct  2 08:05 sda
brw-rw----   1 root disk        8,     1 Oct  2 08:05 sda1
brw-rw----   1 root disk        8,     2 Oct  2 17:43 sda2
crw-rw----   1 root disk       21,     0 Oct  2 08:05 sg0
drwxrwxrwt   2 root root              40 Oct  2 17:39 shm
crw-------   1 root root       10,   231 Oct  2 08:05 snapshot
drwxr-xr-x   3 root root             340 Oct  2 08:05 snd
lrwxrwxrwx   1 root root              15 Oct  2 08:05 stderr -> /proc/self/fd/2
lrwxrwxrwx   1 root root              15 Oct  2 08:05 stdin -> /proc/self/fd/0
lrwxrwxrwx   1 root root              15 Oct  2 08:05 stdout -> /proc/self/fd/1
```

Some important commands to remember are : 

1. fdisk : format disk
2. sfdisk : script oriented tool for partition maanagement
3. parted : paritions manager
4. df : detail filesystem
5. lsblk : list block devices
7. lsmod : list modules
8. insmod : insert module
9. rmmod : remove module

## Developing a device driver

All the development is done using C or C++. Required header files are : 

```
#include <linux/init.h>
#include <linux/module.h>
```

Required functions are an "init" function and an "exit" function. They are to be registered using `module_init(init_func)` and `module_exit(exit_func)`.

A sample program would look like : 

```
#include <linux/init.h>
#include <linux/module.h>

MODULE_LICENSE("AGPL");
MODULE_AUTHOR("NA");

int init_func(void)
{
    printk(KERN_INFO "Hello");
    return 0;
}

void exit_func(void)
{
    printk(KERN_INFO "Goodbye");
}

module_init(init_func);
module_exit(exit_func);
```

Compiling module in current directory :


```
make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
```

Loading module occurs through `insmod your_module.ko`.
Messages from each module is visible in `/var/log/message`.

To load at kernel boot the following steps need to be observed : 

1. `mkdir -p /lib/modules/$(uname -r)/kernel/drivers/<your_module>`
2. `cp your_module.ko /lib/modules/$(uname -r)/kernel/drivers/<your_module>/`
3. Edit `/etc/modules` add the module name to it.
4. Reload and verify by running `lsmod` or `cat /proc/modules`.
 
