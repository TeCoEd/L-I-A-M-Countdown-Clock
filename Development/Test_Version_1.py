###Liam's Countdown Clock###
### Coded by TeCoEd ######

import time, datetime
from ezgraphics import GraphicsWindow

date_list = [] #stores the date values from the text file as a string

##################################################################################
####### 7 Days as seconds = 604800  ##############################################
   
def Countdown_Calculations(): #does the mafs! and plots the visuals
    '''time used to display bars'''
    time_in_seconds = final_time ###error of one minute

    '''Create the Window'''
    win = GraphicsWindow(750, 400)
    win.setTitle("Liam's Clock")
    canvas = win.canvas()
    canvas.setBackground(0, 0, 0) 

    #########################################################################
    ## Seconds delay##
    seconds_remainder = time_in_seconds - int(time_in_seconds)
    #print (seconds_remainder)
    seconds = (60 * seconds_remainder)  #convert to seconds as 59 seconds is nearly a min and will not be accurate
    #print (int(seconds))

    ## LOADING SCREEN ##
    canvas.setColor("green") #set colour of text
    canvas.drawText(340, 200, " LOADING ...")

    ##waits for number of seconds to ensure that it is accurate in mins and hours and days###
    time.sleep(int(seconds))


    ###################################################################################
    ##### START COUNTDOWN CLOCK #######################################

    '''draw titles'''
    canvas.setColor("white")
    canvas.drawText(30, 120, "Days")
    canvas.drawText(30, 220, "Hours")
    canvas.drawText(30, 320, "Minutes")

    '''draw remain titles'''
    canvas.drawText(100, 40, "TIME REMAINING: ")
    canvas.drawText(240, 40, "DAYS ")
    canvas.drawText(320, 40, "HOURS ")
    canvas.drawText(420, 40, "MINUTES ")



    while time_in_seconds > 0:
            
            #print ("remaining seconds", time_in_seconds)

            #print ("")

            #days#
            days = int(time_in_seconds/86400)
            print ("Days", days)

            #hours#
            hours = int((time_in_seconds - (days * 86400))/3600)
            print ("Hours", hours)

            #time.sleep(3)

            #minutes#
            minutes = int((time_in_seconds - ((hours * 3600) + (days * 86400)))/60)
            print ("Minutes", minutes)

            #########################################################################################
            #Days#
            '''Create Day Graphic'''#left dis. top dis, rec_size
            '''Add Title'''
            canvas.setColor("green") #set colour
            canvas.drawRectangle(98, 100, 602, 50)
            '''add the hours'''
            canvas.setColor("red") #set colour
            canvas.drawRectangle(98, 100, (days * 86), 50)
            canvas.drawText(280, 40, str(days))


            ##########################################################################################
            #Hours#
            '''Create Hour Graphic'''#left dis. top dis, rec_size
            '''Add Title'''
            #canvas.drawText(30, 70, "Hours")

            canvas.setColor("green") #set colour
            canvas.drawRectangle(100, 200, 600, 50)
            '''add the hours'''
            canvas.setColor("orange") #set colour
            canvas.drawRectangle(100, 200, (hours * 25), 50)
            canvas.drawText(370, 40, str(hours))

            ##############################################################################################
            #Minutes#
            '''Create Minutes Graphic'''#left dis. top dis, rec_size
            '''Add Title'''
            #canvas.drawText(30, 220, "Minutes")

            canvas.setColor("green") #set colour
            canvas.drawRectangle(100, 300, 600, 50)
            '''add the hours'''
            canvas.setColor("blue") #set colour
            canvas.drawRectangle(100, 300, (minutes * 10), 50)
            canvas.drawText(480, 40, str(minutes))


            '''wait for 60 seconds before looping'''
            time_in_seconds = time_in_seconds - 60
            time.sleep(60)

            
            ###############################################################################
            #clear the previous text values#####
            '''clear time values to avoid over writing: overwrite in black'''
            canvas.setColor("black") #set colour
            canvas.drawText(280, 40, str(days))
            canvas.setColor("black") #set colour
            canvas.drawText(370, 40, str(hours))
            canvas.setColor("black") #set colour
            canvas.drawText(480, 40, str(minutes))

    #canvas.drawText(400, 70, "TIME UP")
    #canvas.setColor("orange")
    #canvas.drawRectangle(100, 200, 600, 50)
    canvas.setBackground(255, 255, 255)
    canvas.setColor("white") #set colour
    canvas.drawText(340, 220, "TIME UP")        

            ##add the times and mins. onto screen

###############################################################################
###### START OF PROGRAM #############################################

################################################################################
#### Read times and date info from the text file ########################################
file = open("event_time.txt","r") #opens file
#print (f.readline())

lines = file.read().splitlines()

file.close()

for line in lines:
    date_list.append(line)


date_list =str(date_list)

#print (date_list)

## collect the values for the time remaining

date_of_event = int(date_list[2:4].strip(' '))  #date
date_of_month = int(date_list[15:16].strip(' ')) #month
hour_of_event = int(date_list[29:31].strip(' ')) #hour
minute_of_event = int(date_list[42:44].strip(' ')) #minute

##########################################################################
### Calculate time remaining in seconds ##################################
'''current time: ensure clock is set correctly'''
current_time = time.time()
#print (current_time)

'''future date and time of event'''
t = datetime.datetime(2017, date_of_month, date_of_event, hour_of_event, minute_of_event)
future_time= time.mktime(t.timetuple())
#print (future_time)

'''time difference'''
final_time = (future_time - current_time)
#print ("time remaining", final_time)


if final_time < 0:
    print ("TIME ERROR 1:")
    print("")
    print("The time you have entered has already passed.\nLoad the event_time.txt file and enter a valid date")

elif final_time > 604800:
    print ("TIME ERROR 2:")
    print("")
    print("The time you have entered is too far into the furture.\nPlease select times for an event up to seven days.\nLoad the event_time.txt file and enter a valid date")     

else:
    Countdown_Calculations()
    print("T I M E  U P")
    #win = GraphicsWindow(750, 400)
    #canvas = win.canvas()
    
    
    

            
