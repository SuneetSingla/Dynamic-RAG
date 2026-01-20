 Project Title

Dynamic Financial RAG: Real-Time Market Intelligence using Live Data Streams

 Project Description

We designed and implemented a Dynamic Retrieval-Augmented Generation (RAG) system that continuously ingests live financial data (real-time stock prices and financial news), incrementally updates its knowledge base, and answers user queries using a large language model grounded in the latest available data.

Unlike static RAG systems, this system does not rely on a fixed dataset.
As new market data arrives, answers to the same question change automatically over time, without restarting the application or rebuilding indexes.

 Architecture Overview
Live Stock APIs + News APIs
            ↓
Python Streaming Ingestion
            ↓
Incremental Text Construction
            ↓
SentenceTransformer Embeddings
            ↓
Semantic Similarity Retrieval
            ↓
Gemini LLM (Grounded Reasoning)
            ↓
Live, Time-Aware Answers

 Step-by-Step Setup & Execution
1️ Clone the repository
git clone <your-repo-url>
cd Dynamic-RAG

2️ Create and activate virtual environment (Linux / WSL)
python3 -m venv venv
source venv/bin/activate

3️ Install dependencies
pip install -r requirements.txt

4️ Add Gemini API key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

5️ Run the application
python app.py

 Real-Time / Streaming Functionality

Stock prices and news are continuously ingested via live APIs.

Each incoming update is embedded incrementally and added to the knowledge store.

Queries retrieve the most recent and relevant information.

Asking the same question at different times produces different answers, demonstrating true dynamic RAG behavior.

If information is not present in the live data, the system refuses to answer instead of hallucinating.

