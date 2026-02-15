from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query engine
query_engine = index.as_query_engine()
response = query_engine.query("What is in the documents?")
print(response)


# What this teaches:

# Document loading

# Vector indexing

# Retrieval + generation