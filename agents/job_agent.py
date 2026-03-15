from graph.workflow import build_graph

def run_agent(resume_path, website):

    graph = build_graph()

    state = {
        "resume_path": resume_path,
        "website": website
    }

    result = graph.invoke(state)

    return result.get("jobs", [])