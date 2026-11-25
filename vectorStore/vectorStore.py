from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import uuid
import os

load_dotenv()


class VectorStoreManager:

    def __init__(self):
        # Initialize embedding model
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )
        # Initialize persistent Chroma vector store
        self.vector_store = Chroma(
            collection_name="youtube_transcripts",
            embedding_function=self.embeddings,
            persist_directory="./chroma_db"
        )

    # CREATE: Add transcript chunks
    def add_documents(self, chunks):
        ids = [str(uuid.uuid4()) for _ in chunks]
        self.vector_store.add_documents(
            documents=chunks,
            ids=ids
        )
        print(f"Successfully added {len(chunks)} chunks")
        return ids

    # READ: Retrieve relevant chunks
    def search_documents(self, query, k=4):
        results = self.vector_store.similarity_search(
            query=query,
            k=k
        )
        return results

    # UPDATE: Update an existing chunk
    def update_document(self, document_id, updated_document):
        self.vector_store.update_documents(
            ids=[document_id],
            documents=[updated_document]
        )
        print(f"Document {document_id} updated successfully")

    # DELETE: Delete chunks using IDs
    def delete_documents(self, document_ids):
        self.vector_store.delete(
            ids=document_ids
        )
        print(f"Deleted {len(document_ids)} documents")

    # GET: Get documents using their IDs
    def get_documents(self, document_ids):
        return self.vector_store.get_by_ids(document_ids)

    # COUNT: Get total stored chunks
    def count_documents(self):
        return self.vector_store._collection.count()
