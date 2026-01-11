import pathway as pw

from pathway_pipeline.tables import (
    build_stock_table,
    build_news_table
)
from pathway_pipeline.transformations import add_features
from pathway_pipeline.knowledge_builder import (
    build_stock_knowledge,
    build_news_knowledge,
    merge_knowledge
)
from pathway_pipeline.vector_index import (
    build_vector_index,
    embed_text
)
from rag.retriever import retrieve_relevant
from rag.gemini_client import ask_gemini


# -----------------------------
# 1️⃣ Build LIVE streaming tables
# -----------------------------
stock_table = build_stock_table()
news_table = build_news_table()

# -----------------------------
# 2️⃣ Live feature engineering
# -----------------------------
stock_features = add_features(stock_table)

# -----------------------------
# 3️⃣ Convert to textual knowledge
# -----------------------------
stock_knowledge = build_stock_knowledge(stock_features)
news_knowledge = build_news_knowledge(news_table)

# -----------------------------
# 4️⃣ Merge live knowledge streams
# -----------------------------
knowledge = merge_knowledge(stock_knowledge, news_knowledge)

# -----------------------------
# 5️⃣ Incremental vector index (LIVE)
# -----------------------------
vector_index = build_vector_index(knowledge)

# -----------------------------
# 6️⃣ Start Pathway engine
# -----------------------------
pw.run()

print("\n✅ Live Financial Dynamic RAG system is running...\n")

# -----------------------------
# 7️⃣ Query loop (Semantic RAG)
# -----------------------------
while True:
    q = input("Ask a question (or Ctrl+C to exit): ")

    # Embed query
    query_embedding = embed_text(q)

    # Semantic retrieval
    rows = retrieve_relevant(vector_index, query_embedding)

    # Build context
    context = "\n".join(
        row["content"] for row in rows
    )

    # Ask Gemini with grounded context
    answer = ask_gemini(context, q)

    print("\n🧠 Answer:\n", answer)
    print("\n" + "-" * 60 + "\n")
