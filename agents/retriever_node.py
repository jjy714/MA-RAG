from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

vector_store = InMemoryVectorStore(OpenAIEmbeddings())


def vector_search(query: str):
    results = vector_store.similarity_search(query=query, k=1)

    for doc in results:
        print(f"* {doc.page_content} [{doc.metadata}]")
    return results



def retriever_node():
    pass 