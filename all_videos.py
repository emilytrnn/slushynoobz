import scrapetube
import sqlite3
from youtube_transcript_api import YouTubeTranscriptApi

conn = sqlite3.connect('transcripts.db')
cursor = conn.cursor()

videos = scrapetube.get_channel("UCfHadeHLF_hkfdrSfVIagDA")

for video in videos:
    videoid = video['videoId']
    
    transcript = YouTubeTranscriptApi.get_transcript(videoid)
    output=''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence}\n'
    
    cursor.execute("INSERT INTO transcripts (video_id, transcript) VALUES (?, ?)", (videoid, output))

conn.commit()
conn.close()