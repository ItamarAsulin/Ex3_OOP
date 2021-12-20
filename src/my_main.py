from graphAlgo import GraphAlgo
g = GraphAlgo()
g.load_from_json(r"C:\Users\shira\Desktop\Ex3_OOP-main\Ex3_OOP-main\data\A3.json")
# g.save_to_json(r"C:\Users\shira\Desktop\Ex3_OOP-main\Ex3_OOP-main\data\ohad_check.json")
g.graph.remove_node(1)
print(g.is_connected())
