import utils.youtube_transcript_extractor as extractor

ext=extractor.Extractor(video_url="https://www.youtube.com/watch?v=8C32XBcvfh8")

video_id = ext.extract_video_id()
ext.video_id = video_id
transcript = ext.extract_transcript()

print(transcript[:1000])