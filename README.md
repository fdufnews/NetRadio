# NetRadio

A small web radio running on Raspberry Pi

The software (and above all the look) is based on RPi-Tron-Radio
I like very much the Tron look of the display

Original can be found here https://github.com/5Volt-Junkie/RPi-Tron-Radio


So why make it different:
First, the screen I have is larger (480x320), so it gave me the opportunity to have larger buttons and a larger information display window
Second, I would like to have weather forecast on the screen. I plan to use Wunderground API. There is a free key to access forecast data (called developper key). The data are rather numerous.
Third, I wanted to have a more flexible configuration system (different skins with different buttons organization)). As weather forecast uses json file to answer requests, I started to look at json file to make the configuration file. The configuration file make it possible to have completly different skins with buttons at any place on the screen.
Fourth, may be I will add MP3 support (local and/or network)

Development schedule:
    - Adaptation to larger screen - done
        Redrawn skin in 480x320
        Added time and date dislay (there is room for it so...)

To be done in order of importance :
    - suppress all absolute reference to screen places in screen update (first step to system with a configuration file)
    - json configuration file
    - weather forecast
    - MP3
