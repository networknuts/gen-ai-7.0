import redis 
import ast
from dotenv import load_dotenv
from openai import OpenAI 
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# SETUP THE CONNECT TO VECTOR DB
load_dotenv()
client = OpenAI()
EMBEDDING_MODEL = "text-embedding-3-large"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "networknuts_c1"

# INITIALIZE THE EMBEDDING MODEL
embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL
)

# CONNECT TO THE VECTOR DATABASE WITH CORRECT COLLECTION
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    url=QDRANT_URL
)

# SETUP THE CONNECTION TO REDIS

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

while True:
    print("READY TO ACCEPT REQUESTS")
    queue_name, raw_payload = redis_client.blpop("rag:requests")
    payload = ast.literal_eval(raw_payload)
    job_id = payload['job_id']
    query = payload['query']
    print(f"Processing Job {job_id}")

    # SEARCH THE VECTOR DATABASE FOR RELEVANT CHUNKS
    search_results = qdrant.similarity_search(query)

    # BUILD THE CONTEXT 
    context = []
    for result in search_results:
        block = f"""
        Page Content:
        {result.page_content}
        Page Number:
        {result.metadata.get("page_label","N/A")}
        """
        context.append(block)
    SYSTEM_PROMPT = f"""
You are a RAG AI Assistant.
You have been given content extracted from a PDF document.
Each section includes:
- The text content
- The page number

Answer the user's query using ONLY this provided information.
If the answer is available:
- Respond in a clear and concise manner
- Mention the relevant page number from where the answer came from

If the answer is not available:
- Clearly state that the required information is not in your knowledge base

In any circumstance, do not add information outside the given context.

Context:
{context}
"""
    response = client.responses.create(
    model="gpt-5.4-mini",
    instructions=SYSTEM_PROMPT,
    input=query
    )
    answer = response.output_text
    redis_client.set(
        f"rag:response:{job_id}",
        answer,
        ex=86400
    )
    print(f"Job {job_id} Successfully Completed.")