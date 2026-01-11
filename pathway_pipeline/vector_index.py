from sentence_transformers import SentenceTransformer
import pathway as pw

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    return model.encode(text).tolist()

def build_vector_index(knowledge_table):
    return knowledge_table.select(
        embedding = pw.apply(embed_text, knowledge_table.content),
        content = knowledge_table.content,
        timestamp = knowledge_table.timestamp
    )
