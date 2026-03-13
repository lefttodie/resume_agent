from .vector_store import index

def retrieve_chunks(query_embedding):

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=5,
        include_metadata=True
    )

    texts = []

    for match in results["matches"]:
        texts.append(match["metadata"]["text"])

    return texts