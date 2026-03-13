import pinecone
import os

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pinecone.Index("resume-index")

def store_embeddings(chunks, embeddings):

    vectors = []

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):

        vectors.append(
            (
                str(i),
                emb,
                {"text": chunk}
            )
        )

    index.upsert(vectors)