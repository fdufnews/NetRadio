NetRadio
==============

Most of this file is the work of 5Volt-Junkie which inspired my work.
As its installation tutorial is well written I keep it as it can help people
Original can be found here https://github.com/5Volt-Junkie/RPi-Tron-Radio

Small web radio with Raspberry Pi and TFT Touchscreen. The interface of the web radio was written in python/pygame and can be started on boot without entering X.

To run the web radio, mpc, mpd and FBTFT are required.



work in progress!!!

#Installation

Added by fdufnews
    If you don't want to use a preinstalled image you can use that very good tutorial that I used to install my touchscreen:
    http://ozzmaker.com/piscreen-driver-install-instructions-2/
    
    http://ozzmaker.com/enable-console-on-piscreen/
    
    After installation jump to ### Install MPC and MPD


## Prepare SD-Card
Download the newest Raspbian Image with preinstalled FBTFT (8Bit Version) https://github.com/watterott/RPi-Display


Copy the Image to SD-Card with dd or Win32DiskImager.
Turn on your Raspberry and connect it to the internet

## First Boot

* Login with 
User: pi
Password: raspberry

```
sudo raspi-config
```
* Expand filesystem, language, keyboard layout and time zone
* Reboot your Raspberry
* After reboot:
```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
sudo reboot
```
### Touchscreen calibration
* After reboot:
```
sudo TSLIB_FBDEVICE=/dev/fb1 TSLIB_TSDEVICE=/dev/input/touchscreen ts_calibrate
```
* touch the five crosshairs

### Install MPC and MPD
```
sudo apt-get install mpc mpd
```
### Add stream/file to playlist
```
sudo mpc add <file or URL>
```
#### Example: 
Let's add one stream from [somafm.com](http://uwstream3.somafm.com:6200) ;-)
[Def Con Radio - Music for Hacking](http://somafm.com/defcon/)
```
sudo mpc add http://uwstream3.somafm.com:6200
```
For more mpc commands see http://linux.die.net/man/1/mpc

### Install Netradio
Copy the folder "NetRadio" to /home/pi/MyApps

```
sudo chmod 755 /home/pi/MyApps/NetRadio/launcher.sh
```

### Start NetRadio on boot
```
sudo nano /etc/rc.local
```
Insert the following command, just above exit0
```
(home/pi//MyApps/NetRadio/launcher.sh)&
```
Save the file

```
sudo reboot
```

