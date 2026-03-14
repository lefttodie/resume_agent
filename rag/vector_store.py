import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("resume-index")


def store_embeddings(chunks, embeddings):

    vectors = []

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):

        vectors.append({
            "id": str(i),
            "values": emb,
            "metadata": {"text": chunk}
        })

    index.upsert(vectors=vectors)

    print("Embeddings stored in Pinecone:", len(vectors))