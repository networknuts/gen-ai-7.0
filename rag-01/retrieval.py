from dotenv import load_dotenv
from openai import OpenAI 
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# SETUP THE ENVIRONMENT
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

# ASK FOR USER INPUT
human_query = input("Human Query: ")

# SEARCH THE VECTOR DATABASE FOR RELEVANT CHUNKS
search_results = qdrant.similarity_search(human_query)


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

# THE SYSTEM PROMPT
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

# CONNECT TO LLM

response = client.responses.create(
    model="gpt-5.4-mini",
    instructions=SYSTEM_PROMPT,
    input=human_query
)

# SHOW AI RESPONSE

print("--- AI OUTPUT ---\n")
print(response.output_text)