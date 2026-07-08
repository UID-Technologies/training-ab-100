from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.document_loader import load_documents


def chunk_text(text, chunk_size=400, overlap=80):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start += chunk_size - overlap

    return chunks or [text]


def retrieve_context(query, top_k=3, data_dir="data"):
    documents = load_documents(data_dir)
    records = []

    for doc in documents:
        for index, chunk in enumerate(chunk_text(doc["content"])):
            records.append({
                "source": doc["file_name"],
                "chunk_id": f"{doc['file_name']}#chunk_{index}",
                "content": chunk,
            })

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([record["content"] for record in records])

    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, vectors).flatten()
    ranked = scores.argsort()[::-1][:top_k]

    results = []

    for index in ranked:
        results.append({
            "source": records[index]["source"],
            "chunk_id": records[index]["chunk_id"],
            "content": records[index]["content"],
            "score": round(float(scores[index]), 4),
        })

    return results
