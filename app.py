import utils.youtube_transcript_extractor as extractor
import utils.transcript_chunker as chunker
import vectorStore.vectorStore as vector_store
from utils.modle import Modle
ext=extractor.Extractor(video_url="https://youtu.be/eq9kxO_O6SY")

video_id = ext.extract_video_id()
ext.video_id = video_id
transcript = ext.extract_transcript()

# Initialize the transcript chunker
chunker = chunker.TranscriptChunker(chunk_size=500, chunk_overlap=100)
chunks = chunker.chunk_transcript(transcript, video_id=video_id)

# Initialize the vector store manager
vector_store = vector_store.VectorStoreManager()
# vector_store.add_documents(chunks) #uncomment when creating the vector store for the first time.
print(vector_store.count_documents())
llm=Modle()
while True:
    user_prompt=input("Enter your question: ")
    print(transcript[:1000])
    relevant_chunks = vector_store.search_documents(user_prompt, k=4)
    context = " ".join([chunk.page_content for chunk in relevant_chunks])
    prompt=f"Context: {context}\n\nQuestion: {user_prompt}\nAnswer:"
    print(f"Prompt: {prompt}")
    response=llm.generate_response(prompt)
    print(response[0]['text'])
