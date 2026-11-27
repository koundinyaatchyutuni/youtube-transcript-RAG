from utils.youtube_transcript_extractor import Extractor
from utils.transcript_chunker import TranscriptChunker
from utils.modle import Modle
from vectorStore.vectorStore import VectorStoreManager

import logging
import os
from datetime import datetime

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Create a separate log file for every execution
log_filename = datetime.now().strftime("session_%Y%m%d_%H%M%S.txt")
log_filepath = os.path.join("logs", log_filename)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_filepath, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)


class ChatBot:
    def __init__(self):
        self.llm=Modle()
        self.vector_store=VectorStoreManager()
    def process_youtube_video(self, video_url):
        extractor = Extractor(video_url)
        transcript = extractor.extract_transcript()
        chunks = TranscriptChunker().chunk_transcript(transcript)
        self.vector_store.delete_all_chunks()  # Clear existing chunks before adding new ones
        self.vector_store.add_documents(chunks)
    def chat(self, user_input):
        relevant_chunks = self.vector_store.search_documents(user_input)
        print(f"Retrieved {len(relevant_chunks)} relevant chunks for the question.")
        logger.info(f"Retrieved {relevant_chunks} relevant chunks for the question.")
        prompt=f"Answer the following question based on the provided context:\n\nContext:\n{''.join([chunk.page_content for chunk in relevant_chunks])}\n\nQuestion: {user_input}\n\nAnswer:"
        response = self.llm.generate_response(prompt)
        return response[0]["text"] if response else "I'm sorry, I couldn't generate a response based on the provided context."

if __name__ == "__main__":
    chatbot = ChatBot()
    video_url = input("Enter the YouTube video URL: ")
    logger.info(f"Processing YouTube video: {video_url}")
    chatbot.process_youtube_video(video_url)
    logger.info("Video processing complete. You can now ask questions about the video.")
    # logger.info("You can now ask questions about the video.")
    user_input = input("Ask a question about the video: ")
    logger.info(f"User question: {user_input}")
    response = chatbot.chat(user_input)
    logger.info(f"Generated response: {response}")
    # print(response)    