from urllib.parse import parse_qs
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
class Extractor:
    def __init__(self, video_id, video_url=None):
        self.video_id = video_id
        self.video_url = video_url

    def extract_transcript(self):
        # Logic to extract transcript from YouTube video using the video_id
        transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
        return transcript
    def extract_video_id(url):

        parsed_url = urlparse(url)

        if parsed_url.hostname in ("youtu.be", "www.youtu.be"):
            return parsed_url.path.strip("/")

        if parsed_url.hostname and parsed_url.hostname.endswith("youtube.com"):
            return parse_qs(parsed_url.query).get("v", [None])[0]
        return None