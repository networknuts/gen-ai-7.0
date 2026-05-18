from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# SETUP THE ENVIRONMENT

load_dotenv()

# VARIABLES

PDF_FILE = "data.pdf"
EMBEDDING_MODEL = "text-embedding-3-large"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "networknuts_c1"


# STEP 1: LOAD THE PDF DOCUMENT
loader = PyPDFLoader(PDF_FILE)
pdf_document = loader.load()


# STEP 2: SPLIT TEXT INTO CHUNKS
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=400
)
chunked_text = text_splitter.split_documents(pdf_document)

# STEP 3: CHOOSING YOUR EMBEDDING MODEL
embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL
)

# STEP 4: STORE EMBEDDINGS IN VECTOR DATABASE

qdrant = QdrantVectorStore.from_documents(
    chunked_text,
    embeddings,
    url=QDRANT_URL,
    prefer_grpc=False,
    collection_name=COLLECTION_NAME
)

print("Ingestion completed successfully!")