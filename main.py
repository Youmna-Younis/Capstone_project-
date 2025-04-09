
from graph_builder import build_graph
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    graph = build_graph()
    input_resume = open("data/candidate_resume.txt").read()
    result = graph.invoke({"resume": input_resume})
    print("\n📋 Final Output:\n")
    print(result)
