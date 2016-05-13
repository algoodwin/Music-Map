import plotly.plotly as py
import plotly.tools as tls
import pandas as pd
import plotly.graph_objs as go
import csv
tls.set_credentials_file(username='algoodwin', api_key='fnqzr6li9g')
states = pd.read_csv('states.csv')
states.head()


#YOUTUBE PART

for col in states.columns:
  lat = states['latitude'].astype(str) 
  lon = states['longitude'].astype(str)
  test =(lat) + ',' + (lon)
  validate = False

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

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
      #q=options.q,
      type="video",
      location=test,
      locationRadius="5km",
      part="id,snippet",
      maxResults=1,
    ).execute()

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
    for node in entry:
      video_title = node.getElementsByTagName('title')[0].firstChild.nodeValue
    print video_title
    print "Videos:\n", "\n".join(videos), "\n"
    

 # if __name__ == "__main__":
    #argparser.add_argument("--q", help="Search term", default="Google")
 #   argparser.add_argument("--location", help="Location", default=test)
#    argparser.add_argument("--location-radius", help="Location radius", default="5km")
#    argparser.add_argument("--max-results", help="Max results", default="1")
#    args = argparser.parse_args()

    try:
      youtube_search(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)



#CSV FILE
#MAP PART

states['latitude'].astype(float)
states['longitude'].astype(float)

trc = dict(
    type = 'Scattergeo',
    locationmode ='USA-states',
    lon = states['longitude'],
    lat = states['latitude'],
    mode = 'markers',
    marker = dict(
                  size = 8,
                  symbol = 'square',
                  line = dict(
                    width=1,
                    color = 'rgba(102, 102, 102)')))
layout = dict(
  title = 'Top Youtube Videos per state',
  geo = dict(
    scope ='usa',
    projection = dict(type ='albers usa'),
    showland = True,
    landcolor = "rgb(250,250,250,)",
    subunitcolor = "rgb(217,217,217)",
    countrycolor = "rgb(217,217,217)",
    countrywidth = 0.5,
    subunitwidth = 0.5),
  )
 #   marker = dict(
#            line = dict (
#                color = 'rgb(255,255,255)',
#                width = 2
#lyt = dict(geo=dict(scope='usa'))
#map = go.Figure(data=[trc])

print('response')
fig = dict(data = test, layout = layout)
url = py.plot(fig, filename='https://plot.ly/~algoodwin/46/')
#py.plot(map)
#py.plot(trc)
for locations in trc.items():
  print(locations)
  
