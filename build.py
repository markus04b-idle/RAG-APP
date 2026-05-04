import chromadb

SEPERATOR = '-' * 70

client = chromadb.PersistentClient("./chroma_db")

def load_chunks(filename):
    with open(filename) as f:
        text = f.read()

    sections = text.split(SEPERATOR)

    chunks = []
    for section in sections:
        chunks.append(section.strip())
    return chunks



files_and_collections = [
    ("roster_2026.txt",roster_2026),
    ("scounting_2027.txt",scounting_2027),
    ("opponents_2026.txt",opponents_2026)
]