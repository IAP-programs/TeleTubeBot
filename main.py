# Function to initialize the YouTube API client
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import time
import telebot

def reply(message) :
    message1 = "sorry there is no data "
    data_type = "string"
    data = open("dictnory.txt", "r")
    data = data.read()
    data = "{\n"+data+"\n}"
    data = eval(data)
    try :
      message1 = data[message]
      data_type = message1.split()
      data_type = data_type[0]
    except :
      message1 = "sorry there is no data "
    return message1, d
#CHANNEL_ID = 'uHdsW-PS-45SSw'
with open("api_key", "r") as f1 :
  API_KEY = f1.read()
with open("channel_id", "r") as f1 :
  CHANNEL_ID = f1.read()
def get_authenticated_service():
    return build('youtube', 'v3', developerKey=API_KEY)

# Function to retrieve the current subscriber count
def get_subscriber_count():
    youtube = get_authenticated_service()
    request = youtube.channels().list(
        part='statistics',
        id=CHANNEL_ID
    )
    response = request.execute()
    subscriber_count = int(response['items'][0]['statistics']['subscriberCount'])
    return subscriber_count

# Function to continuously check for new subscribers
def check_new_subscribers():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    import time
    initial_subscribers = get_subscriber_count()
    while True:
        current_subscribers = get_subscriber_count()
        if current_subscribers > initial_subscribers:
            print("New subscriber detected! Total subscribers:", current_subscribers)
            file = open("subscribers_list.txt", "a")
            file.write(f"New subscriber detected! Total subscribers:{current_subscribers}\n")
            file.close()
            return "New subscriber detected!"
            break
            initial_subscribers = current_subscribers
        time.sleep(10)  # Check every minute

# Start monitoring for new subscribers

