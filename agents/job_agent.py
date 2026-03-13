from graph.workflow import build_graph


def run_agent(resume_path):

    graph = build_graph()

    state = {
        "resume_path": resume_path
    }

    result = graph.invoke(state)

    return result["jobs"]