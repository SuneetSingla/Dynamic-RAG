import numpy as np
import pathway as pw


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_relevant(index_table, query_embedding, limit=5):
    """
    Semantic retrieval over a LIVE Pathway table.
    """

    scored = index_table.select(
        content=index_table.content,
        timestamp=index_table.timestamp,
        score=pw.apply(
            cosine_sim,
            index_table.embedding,
            query_embedding
        )
    )

    return scored.order_by(
        scored.score, descending=True
    ).limit(limit)
