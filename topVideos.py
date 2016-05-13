################## STUFF ##############################
https://github.com/algoodwin/Project_3

######################################################


import plotly.plotly as py
import plotly.tools as tls
import pandas as pd
import plotly.graph_objs as go
import csv
tls.set_credentials_file(username='algoodwin', api_key='fnqzr6li9g')
states = pd.read_csv('states.csv')

topVideos = []

#################### CREATING A VARIABLE TYPE STRING FOR LOCATION ##########
for col in states.columns:
  lat = states['latitude'].astype(str)
  lon = states['longitude'].astype(str)
  test = (lat) + ',' + (lon)

######################### END ####################################

####### LOOP FOR FINDING THE TOP MOST VIEWED VIDEO IN EACH STATE ########

for times in range(0,50):
  from googleapiclient.discovery import build
  from apiclient.errors import  HttpError
  from oauth2client.tools import argparser


  # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
  # tab of
  #   https://cloud.google.com/console
  # Please ensure that you have enabled the YouTube Data API for your project.
  DEVELOPER_KEY = "AIzaSyDB41nojBDn1q85V-HLVOj8oxpo9UQIZ7Y"
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"

  def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY)

################## SEARCH HAPPENS WITH OUR CONDITIONS ########################
    search_response = youtube.search().list(
      #q=options.q,
      type="video",
      order = "viewCount",
      location=test[times],
      locationRadius="85km",
      part="id,snippet",
      maxResults=1
    ).execute()

####################### SEARCH ENDS ###################################

    search_videos = []

    # Merge video ids
    for search_result in search_response.get("items", []):
      search_videos.append(search_result["id"]["videoId"])
    video_ids = ",".join(search_videos)

    # Call the videos.list method to retrieve location details for each video.
    video_response = youtube.videos().list(
      id=video_ids,
      part='snippet, recordingDetails'
    ).execute()

    videos = []

    # Add each result to the list, and then display the list of matching videos.
    for video_result in video_response.get("items", []):
      videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
                                video_result["recordingDetails"]["location"]["latitude"],
                                video_result["recordingDetails"]["location"]["longitude"]))
# FILLS UP OUR TOPVIDEO LIST
########################## START #########################################
    if ((times!=1) and (times!=8) and (times != 10) and (times!= 31)):
          topVideos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
                              video_result["recordingDetails"]["location"]["latitude"],
                              video_result["recordingDetails"]["location"]["longitude"]))
    elif(times == 1 or times == 8 or times == 10 or times == 31):
            topVideos.append("RedvsBlue")

########################## END ############################################

    #TESTING
    #print times
    #print "Videos:\n", "\n".join(videos), "\n"




  if __name__ == "__main__":
    args = argparser.parse_args()

    try:
      youtube_search(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

######################### END OF LOOP ##################################

#WRITES TO A NEW CSV FILE
################### START ##################################

with open ('videos.csv', "w") as output:
    writer = csv.writer(output)
    writer.writerow(['song'])
    for items in topVideos:
        writer.writerow([items])
################### END #####################################

########################### Music Link ##############################

import urllib
import urllib2
from bs4 import BeautifulSoup

def song(song):
    textToSearch = song
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    if(song == "RedvsBlue"):
        playSong('https://www.youtube.com/watch?v=RLV2TPIHL_o')
    else:
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            playSong('https://www.youtube.com' + vid['href'])
            break

############################ END ###################################

########################### Play The Video #########################

import webbrowser

def playSong(url):
    new = 2 # open in a new tab, if possible
    # open a public URL, in this case, the webbrowser docs
    webbrowser.open(url,new=new)


############################ END ##################################

########################## PLOTLY ################################

states['latitude'].astype(float)
states['longitude'].astype(float)


data = [ dict(
    type = 'choropleth',
    locations = states['longitude'],
    z = states['latitude'],
    text = topVideos,
    locationmode ='USA-states',
    colorscale = ['greyscale'],
    )]


lyt = dict(geo=dict(scope='usa'), title = 'Top Played Videos In Each State')
map = go.Figure(data=data,layout = lyt)

print('response')
py.plot(map)

########################### END ###################################

########################### Buttons ################################

from Tkinter import*
import csv
"""""
Defining actions per State through csv file
"""""
openc = open('videos.csv', 'rb')
readc = csv.reader(openc)
tlist = list(readc)
print tlist
def Alabama():
    song(topVideos[0])
def Alaska():
    song(topVideos[1])
def Arizona():
    song(topVideos[2])
def Arkansas():
    song(topVideos[3])
def California():
    song(topVideos[4])
def Colorado():
    song(topVideos[5])
def Connecticut():
    song(topVideos[6])
def Delaware():
    song(topVideos[7])
def Florida():
    song(topVideos[8])
def Georgia():
    song(topVideos[9])
def Hawaii():
    song(topVideos[10])
def Idaho():
    song(topVideos[11])
def Illinois():
    song(topVideos[12])
def Indiana():
    song(topVideos[13])
def Iowa():
    song(topVideos[14])
def Kansas():
    song(topVideos[15])
def Louisiana():
    song(topVideos[16])
def Kentucky():
    song(topVideos[17])
def Maine():
    song(topVideos[18])
def Maryland():
    song(topVideos[19])
def Massachusetts():
    song(topVideos[20])
def Michigan():
    song(topVideos[21])
def Minnesota():
    song(topVideos[22])
def Mississippi():
    song(topVideos[23])
def Missouri():
    song(topVideos[24])
def Montana():
    song(topVideos[25])
def Nebraska():
    song(topVideos[25])
def Nevada():
    song(topVideos[27])
def NewHampshire():
    song(topVideos[28])
def NewJersey():
    song(topVideos[29])
def NewMexico():
    song(topVideos[30])
def NewYork():
    song(topVideos[31])
def NorthCarolina():
    song(topVideos[32])
def NorthDakota():
    song(topVideos[33])
def Ohio():
    song(topVideos[34])
def Oklahoma():
    song(topVideos[35])
def Oregon():
    song(topVideos[36])
def Pennsylvania():
    song(topVideos[37])
def RhodeIsland():
    song(topVideos[38])
def SouthCarolina():
    song(topVideos[39])
def SouthDakota():
    song(topVideos[40])
def Tennessee():
    song(topVideos[41])
def Texas():
    song(topVideos[42])
def Utah():
    song(topVideos[43])
def Vermont():
    song(topVideos[44])
def Virginia():
    song(topVideos[45])
def Washington():
    song(topVideos[46])
def WestVirginia():
    song(topVideos[47])
def Wisconsin():
    song(topVideos[48])
def Wyoming():
    song(topVideos[49])
def quit():
    global root
    root.quit()

#States as buttons
root = Tk()
root.title("States")
Al = Button(root, text = 'Alabama', command = Alabama).grid(row = 0, column=1)
AK = Button(root, text = 'Alaska', command = Alaska).grid(row = 1, column = 1)
AZ = Button(root, text = 'Arizona', command = Arizona).grid(row = 2, column = 1)
AR = Button(root, text = 'Arkansas', command = Arkansas).grid(row = 3, column = 1)
CA = Button(root, text = 'California', command = California).grid(row = 4, column = 1)
CO = Button(root, text = 'Colorado', command = Colorado).grid(row = 5, column = 1)
CT = Button(root, text = 'Connecticut', command = Connecticut).grid(row = 6, column = 1)
DE = Button(root, text = 'Delaware', command = Delaware).grid(row = 7, column = 1)
FL = Button(root, text = 'Florida', command = Florida).grid(row = 8, column = 1)
GA = Button(root, text = 'Georgia', command = Georgia).grid(row = 9, column = 1)
HI = Button(root, text = 'Hawaii', command = Hawaii).grid(row = 10, column = 1)
ID = Button(root, text = 'Idaho', command = Idaho).grid(row = 11, column = 1)
IL = Button(root, text = 'Illinois', command = Illinois).grid(row = 12, column = 1)
IN = Button(root, text = 'Indiana', command = Indiana).grid(row = 13, column = 1)
IA = Button(root, text = 'Iowa', command = Iowa).grid(row = 14, column = 1)
KS = Button(root, text = 'Kansas', command = Kansas).grid(row = 15, column = 1)
KY = Button(root, text = 'Kentucky', command = Kentucky).grid(row = 16, column = 1)
LA = Button(root, text = 'Louisiana', command = Louisiana).grid(row = 17, column = 1)
ME = Button(root, text = 'Maine', command = Maine).grid(row = 18, column = 1)
MD = Button(root, text = 'Maryland', command = Maryland).grid(row = 19, column = 1)
MA = Button(root, text = 'Massachusetts', command = Massachusetts).grid(row = 20, column = 1)
MI = Button(root, text = 'Michigan', command = Michigan).grid(row = 21, column = 1)
MN = Button(root, text = 'Minnesota', command = Minnesota).grid(row = 22, column = 1)
MS = Button(root, text = 'Mississippi', command = Mississippi).grid(row = 23, column = 1)
MO = Button(root, text = 'Missouri', command = Missouri).grid(row = 24, column = 1)
MT = Button(root, text = 'Montana', command = Montana).grid(row = 0, column = 2)
NE = Button(root, text = 'Nebraska', command = Nebraska).grid(row = 1, column = 2)
NV = Button(root, text = 'Nevada', command = Nevada).grid(row = 2, column = 2)
NH = Button(root, text = 'New Hampshire', command = NewHampshire).grid(row = 3, column = 2)
NJ = Button(root, text = 'New Jersey', command = NewJersey).grid(row = 4, column = 2)
NM = Button(root, text = 'New Mexico', command = NewMexico).grid(row = 5, column = 2)
NY = Button(root, text = 'New York', command = NewYork).grid(row = 6, column = 2)
NC = Button(root, text = 'North Carolina', command = NorthCarolina).grid(row = 7, column = 2)
ND = Button(root, text = 'North Dakota', command = NorthDakota).grid(row = 8, column = 2)
OH = Button(root, text = 'Ohio', command = Ohio).grid(row = 9, column = 2)
OK = Button(root, text = 'Oklahoma', command = Oklahoma).grid(row = 10, column = 2)
OR = Button(root, text = 'Oregon', command = Oregon).grid(row = 11, column = 2)
PA = Button(root, text = 'Pennsylvania', command = Pennsylvania).grid(row = 12, column = 2)
RI = Button(root, text = 'Rhode Island', command = RhodeIsland).grid(row = 13, column = 2)
SC = Button(root, text = 'South Carolina', command = SouthCarolina).grid(row = 14, column = 2)
SD = Button(root, text = 'South Dakota', command = SouthDakota).grid(row = 15, column = 2)
TN = Button(root, text = 'Tennessee', command = Tennessee).grid(row = 16, column = 2)
TX = Button(root, text = 'Texas', command = Texas).grid(row = 17, column = 2)
UT = Button(root, text = 'Utah', command = Utah).grid(row = 18, column = 2)
VT = Button(root, text = 'Vermont', command = Vermont).grid(row = 19, column = 2)
VA = Button(root, text = 'Virginia', command = Virginia).grid(row = 20, column = 2)
WA = Button(root, text = 'Washington', command = Washington).grid(row = 21, column = 2)
WV = Button(root, text = 'West Virginia', command = WestVirginia).grid(row = 22, column = 2)
WI = Button(root, text = 'Wisconsin', command = Wisconsin).grid(row = 23, column = 2)
WY = Button(root, text = 'Wyoming', command = Wyoming).grid(row = 24, column = 2)
Q = Button(root,text = 'Quit', command = quit).grid(row = 25, column = 1)
mainloop()

############################ END ###############################
