from typing import TypedDict, List
from langgraph.graph import StateGraph

from utils.resume_parser import parse_resume
from llm.keyword_extractor import extract_keywords
from scraper.job_scraper import search_jobs


# -------- STATE SCHEMA --------

class AgentState(TypedDict, total=False):
    resume_path: str
    resume_text: str
    keywords: List[str]
    jobs: List[str]


# -------- NODES --------

def parse_node(state: AgentState):

    resume_path = state["resume_path"]

    text = parse_resume(resume_path)

    state["resume_text"] = text

    return state


def keyword_node(state: AgentState):

    resume_text = state["resume_text"]

    keywords = extract_keywords(resume_text)

    state["keywords"] = [k.strip() for k in keywords.split("\n") if k.strip()]

    return state


def job_node(state: AgentState):

    all_jobs = []

    for keyword in state["keywords"]:

        jobs = search_jobs(keyword)

        all_jobs.extend(jobs)

    state["jobs"] = all_jobs[:20]

    return state


# -------- GRAPH --------

def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("parse_resume", parse_node)
    builder.add_node("extract_keywords", keyword_node)
    builder.add_node("search_jobs", job_node)

    builder.set_entry_point("parse_resume")

    builder.add_edge("parse_resume", "extract_keywords")
    builder.add_edge("extract_keywords", "search_jobs")

    graph = builder.compile()

    return graph