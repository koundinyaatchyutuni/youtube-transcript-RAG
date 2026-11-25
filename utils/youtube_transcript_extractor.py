from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class Extractor:

    def __init__(self, video_url):
        self.video_url = video_url
        self.video_id = self.extract_video_id()

    def extract_video_id(self):
        parsed_url = urlparse(self.video_url)

        if parsed_url.hostname in ["youtu.be", "www.youtu.be"]:
            return parsed_url.path.strip("/")

        if parsed_url.hostname and parsed_url.hostname.endswith("youtube.com"):
            if parsed_url.path == "/watch":
                return parse_qs(parsed_url.query).get("v", [None])[0]

            if parsed_url.path.startswith(("/shorts/", "/embed/")):
                return parsed_url.path.split("/")[2]

        raise ValueError("Invalid YouTube URL")

    def extract_transcript(self):

        api = YouTubeTranscriptApi()

        transcript = api.fetch(self.video_id)

        transcript_text = " ".join(
            snippet.text for snippet in transcript
        )

        return transcript_text
