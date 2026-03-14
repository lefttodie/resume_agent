from langgraph.graph import StateGraph
from typing import TypedDict, List

from utils.resume_parser import parse_resume, chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import store_embeddings
from llm.keyword_extractor import extract_keywords
from scraper.job_scraper import search_jobs

class AgentState(TypedDict, total=False):
    resume_path: str
    resume_text: str
    chunks: List[str]
    embeddings: List[list]
    keywords: List[str]
    jobs: List[str]

def parse_node(state: AgentState):
    state["resume_text"] = parse_resume(state["resume_path"])
    state["chunks"] = chunk_text(state["resume_text"])
    return state

def embed_node(state: AgentState):
    state["embeddings"] = create_embeddings(state["chunks"])
    store_embeddings(state["chunks"], state["embeddings"])
    return state

def keyword_node(state: AgentState):
    state["keywords"] = extract_keywords(state["resume_text"])
    return state

def job_node(state: AgentState):
    all_jobs = []
    for keyword in state["keywords"]:
        jobs = search_jobs(keyword)
        all_jobs.extend(jobs)
    state["jobs"] = all_jobs[:20]
    return state

def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("parse_resume", parse_node)
    builder.add_node("embed_resume", embed_node)
    builder.add_node("extract_keywords", keyword_node)
    builder.add_node("search_jobs", job_node)

    builder.set_entry_point("parse_resume")
    builder.add_edge("parse_resume", "embed_resume")
    builder.add_edge("embed_resume", "extract_keywords")
    builder.add_edge("extract_keywords", "search_jobs")

    return builder.compile()