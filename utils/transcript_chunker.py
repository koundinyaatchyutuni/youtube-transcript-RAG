from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TranscriptChunker:

    def __init__(self, chunk_size=1000, chunk_overlap=200):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""],
            add_start_index=True
        )

    def chunk_transcript(self, transcript, video_id=None):

        document = Document(
            page_content=transcript,
            metadata={
                "source": "youtube",
                "video_id": video_id
            }
        )

        chunks = self.text_splitter.split_documents([document])

        return chunks
 