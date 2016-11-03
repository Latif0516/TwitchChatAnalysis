from ChatLogParser import TwitchChatLogParser, SentimentAnalyzer
from urllib.request import urlopen
import json

# Read the all emotes (global and subsrciber) 
url = 'https://twitchemotes.com/api_cache/v2/images.json'
response = urlopen(url)
data = response.read().decode("utf-8")
emote_data = json.loads(data)
emotes = []
for n in emote_data['images'].keys():
    emotes.append(emote_data['images'][n]['code'])

LOG_DIR = "/Users/Michaeliu/Twitch/logfile"
textparser = TwitchChatLogParser(emotes=emotes, log_dir=LOG_DIR)
corpus = textparser.read_log_from_dir(LOG_DIR)

cleaned_corpus = textparser.clean_up()



# analyzer = SentimentAnalyzer()
# labeled_data = analyzer.sentiment_analysis(textparser.get_cleaned_utterances())




