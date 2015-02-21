#-*-encoding=UTF8-*-
import pygame
from pygame.locals import *
import time
import datetime
import sys
import os
import glob
import subprocess
import RPi.GPIO as GPIO

__VERSION__='1'
__RELEASE__='0'

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# This is not necessary for my screen but may be some screens need it so I keep it
# I suppose it is used to activate backlight
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)



#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
black   = (  0,   0,   0)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
yellow  = (255, 255,   0)
orange  = (255, 127,   0)



#screen size
width  = 480
height = 320
size = (width, height)
screen = pygame.display.set_mode(size)



pygame.init()

#disable mouse cursor
pygame.mouse.set_visible(False)

#define font
# the original script was using default font but I prefer droidsans
#font = pygame.font.Font(None, 25)
font = pygame.font.Font(pygame.font.match_font('droidsans'), 18)
#Added a large font to dislay time
fontLarge = pygame.font.Font(pygame.font.match_font('droidsans'), 54)


#screensaver
screensaver_timer = 5     #time until screensaver will be enabled, in minutes
screensaver = False

#load default skin
menu = 1
skin_number = 4
max_skins = 4
font_color = cyan
skin1 = pygame.image.load("skins/skin_white_m1.png")
skin2 = pygame.image.load("skins/skin_white_m2.png")




skin = skin1

screen.blit(skin, (0, 0))

#initial volume settings
subprocess.call('mpc volume 75' , shell=True)

reboot_label = font.render("rebooting...", 1, (font_color))
poweroff_label = font.render("shutting down", 1, (font_color))


song_title = " "
playlist = " "

# If needed to live reboot
def reboot():
    screen.fill(black)
    screen.blit(reboot_label, (10, 100))
    pygame.display.flip()
    time.sleep(5)
    GPIO.cleanup()
    subprocess.call('mpc stop' , shell=True)
    subprocess.call('reboot' , shell=True)


# to power off cleanly
def poweroff():
    screen.fill(black)
    screen.blit(poweroff_label, (10, 100))
    pygame.display.flip()
    time.sleep(5)
    GPIO.cleanup()
    subprocess.call('mpc stop' , shell=True)
    subprocess.call('poweroff' , shell=True)

#copy playing title to favorite.txt
def favorite():
    print song_title

    f = open ('/var/www/favorite.txt' , 'a')
    f.write('-' + song_title + '\n')
    f.close()


#function runs if touchscreen was touched (and screensaver is disabled)
def on_touch():
      #x_min           x_max   y_min            y_max
    if  12 <= pos[0] <=  71 and 179 <= pos[1] <= 239:
        #print "button1 was pressed"
        button(1)

    if  99 <= pos[0] <= 158 and 179 <= pos[1] <= 239:
        #print "button2 was pressed"
        button(2)

    if 186 <= pos[0] <= 245 and 179 <= pos[1] <= 239:
        #print "button3 was pressed"
        button(3)

    if 273 <= pos[0] <= 332 and 179 <= pos[1] <= 239:
        #print "button4 was pressed"
        button(4)


    if  12 <= pos[0] <=  71 and 250 <= pos[1] <= 310:
        #print "button5 was pressed"
        button(5)

    if  99 <= pos[0] <= 158 and 250 <= pos[1] <= 310:
        #print "button6 was pressed"
        button(6)

    if 186 <= pos[0] <= 245 and 250 <= pos[1] <= 310:
        #print "button7 was pressed"
        button(7)

    if 273 <= pos[0] <= 332 and 250 <= pos[1] <= 310:
        #print "button8 was pressed"
        button(8)

#which button (in which menu) was presed on touch
def button(number):
        global menu
        if menu == 1:
            if number == 1:
                subprocess.call('mpc play' , shell=True)
                #print "play"

            if number == 2:
                subprocess.call('mpc pause' , shell=True)
                #print "pause"

            if number == 3:
                subprocess.call('mpc volume +5' , shell=True)

                #print "vol +x"


            if number == 4:
                subprocess.call('mpc volume 0' , shell=True)
                #print "vol 0"

            if number == 5:
                subprocess.call('mpc prev' , shell=True)
                #print "prev"

            if number == 6:
                subprocess.call('mpc next' , shell=True)
                #print "next"

            if number == 7:
                subprocess.call('mpc volume -5' , shell=True)
                #print "vol -x"

            if number == 8:
                #print "go to menu 2"
                menu = 2
                update_screen()
                return

        if menu == 2:
            if number == 1:
                # no more used
                #favorite()
                # used during development to display available fonts
                #print(pygame.font.get_fonts())
                update_screen()

            if number == 2:
                #print "switch skin"
                global skin_number
                skin_number = skin_number+1
                #print skin_number
                update_screen()

            if number == 3:
                #print "run in background"
                pygame.quit()
                sys.exit()

            if number == 4:
                #print "quit radio"
                subprocess.call('mpc stop', shell=True)
                pygame.quit()
                sys.exit()

            if number == 5:
                print "power off"
                poweroff()

            if number == 6:
                print "reboot"
                reboot()

            if number == 7:
                #print "update screen"
                update_screen()


            if number == 8:
                #print "go to menu 1"
                menu = 1
                update_screen()
                return



#function to update screen
def update_screen():
    global skin_number
    if skin_number == max_skins+1:
        skin_number = 1

    #load skin, select font color in accordance
    if skin_number == 1:
        skin1 = pygame.image.load("skins/skin_blue_m1.png")
        skin2 = pygame.image.load("skins/skin_blue_m2.png")
        font_color = cyan
    if skin_number == 2:
        skin1 = pygame.image.load("skins/skin_orange_m1.png")
        skin2 = pygame.image.load("skins/skin_orange_m2.png")
        font_color = orange
    if skin_number == 3:
        skin1 = pygame.image.load("skins/skin_red_m1.png")
        skin2 = pygame.image.load("skins/skin_red_m2.png")
        font_color = red
    if skin_number == 4:
        skin1 = pygame.image.load("skins/skin_white_m1.png")
        skin2 = pygame.image.load("skins/skin_white_m2.png")
        font_color = white




    global menu

    if screensaver == False:
        # render date and time
        current_time = datetime.datetime.now().strftime('%H:%M')
        time_label = fontLarge.render(current_time, 1, (font_color))
        current_time = datetime.datetime.now().strftime('%d.%m.%Y')
        date_label = font.render(current_time, 1, (font_color))
        # display skin menu
        if menu == 1:
            skin = skin1
            screen.blit(skin, (0, 0))
            # get radio information
            lines = subprocess.check_output('mpc current', shell=True).split(":")
            if len(lines) == 1:
                line1 = lines[0]
                line1 = line1[:-1]
                station_label = font.render("Station: no data", 1, (font_color))

            else:
                line1 = lines[0]
                line2 = lines[1]
                line1 = line1[:30]
                station_label = font.render('Station: ' + line1 + '.', 1, (font_color))
            # get title information
            lines = subprocess.check_output('mpc -f [%title%]', shell=True).split("\n")
            line1 = lines[0]

            if line1.startswith("volume"):

                title_label = font.render("Title: no data! Try with PLAY!", 1, (font_color))

            else:
                line1 = lines[0]
                line2 = lines[1]
                global song_title
                song_title = line1
                line1 = line1[:30]

                title_label = font.render(line1 + '.', 1, (font_color))


            title = font.render("Now playing:", 1, (font_color))
            # draw screen
            screen.blit(skin, (0, 0))
            screen.blit(station_label, (23, 15))

            screen.blit(title, (23, 40))
            screen.blit(title_label, (23, 60))

            screen.blit(date_label, (23, 132))
            screen.blit(time_label, (190,100))

            lines = subprocess.check_output('mpc volume', shell=True).split("\n")
            line1 = lines[0]
            volume_label = font.render(line1, 1, (font_color))
            screen.blit(volume_label, (23, 102))
            # flip screen buffer to update display
            pygame.display.flip()

        if menu == 2:
            skin = skin2
            screen.blit(skin, (0, 0))
            # display NetRadio version 
            radioVersion = font.render('NetRadio V'+__VERSION__+'.'+__RELEASE__, 1, (font_color))
            screen.blit(radioVersion, (23, 15))
            #get and display ip
            ip = subprocess.check_output('hostname -I', shell=True).strip()
            ip_label = font.render('IP: ' + ip, 1, (font_color))
            screen.blit(ip_label, (23, 35))

            #get and display cpu temp
            cpu_temp = subprocess.check_output('/opt/vc/bin/vcgencmd measure_temp', shell=True).strip()
            temp = font.render('cpu ' + cpu_temp, 1, (font_color))
            screen.blit(temp, (23, 55))

            #display current time
            screen.blit(date_label, (23, 132))
            screen.blit(time_label, (190, 100))
            # flip screen buffer to update display
            pygame.display.flip()


# if screensaver is active
    if screensaver == True:
        screen.fill(black)
        pygame.display.flip()











minutes = 0
#userevent on every 1000ms, used for screensaver
pygame.time.set_timer(USEREVENT +1, 60000)
# start player
subprocess.call('mpc play' , shell=True)
update_screen()
running = True
while running:

    for event in pygame.event.get():

        # every minute we update minutes counter
        if event.type == USEREVENT +1 and menu == 1:
            minutes += 1

        # different ways to exit
        if event.type == pygame.QUIT:
            GPIO.cleanup()
            print "Quit radio"
            GPIO.cleanup()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                GPIO.cleanup()
                print "Quit radio"
                GPIO.cleanup()
                pygame.quit()
                sys.exit()

        #if screensaver is enabled and the screen was touched,
        #just disable screensaver, reset timer and update screen
        #no button state will be checked
        if event.type == pygame.MOUSEBUTTONDOWN and screensaver == True:
            minutes = 0
            GPIO.output(18, GPIO.HIGH)
            screensaver = False
            update_screen()
            break


        #if screen was touched and screensaver is disabled,
        #get position of touched button, call on_touch(), reset timer and update screen
        if event.type == pygame.MOUSEBUTTONDOWN and screensaver == False:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            minutes = 0
            on_touch()
            update_screen()



    #enable screensaver on timer overflow
    if minutes > screensaver_timer:
        screensaver = True
        GPIO.output(18, GPIO.LOW)
        update_screen()
    # update screen every 0.1 second to keep title info updated
    update_screen()
    time.sleep(0.1)


















