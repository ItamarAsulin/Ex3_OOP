# Directed Weighted Graph Algorithms
**About This Project**

In this project we implmented a directed weighted graph and graph algorithms. In addition, we created a GUI that can load grpahs json file and show them.

**What is Directed Weighted Graph?**

A Directed Weighted Graph is a graph in which the edges that connect the vertices has direction. For example: lets say vertex 1 is connected to vertex 3, than it is possible to travel from vertex 1 to vertex 3 but not the other way aroud unless the is a different edge in the graph that is connecting vertex 3 to vertex 1.

In addition, each edge has a weight, which set the "cost" of traveling along the edge, meaning some times it can be faster to go from one vertex to second vertex through a third vertex even if there is a direct edge from the first vertex to the second vertex. For Example: If there is an edge between vertex 1 and vertex 3 that has a weight of 3, and edges from vertex 1 to 2 and from 2 to 3 that has a weight of 1 each, it is better to get from vertex 1 to 3 through vertex 2.

**Algorithms That Are Implemented:**

Is the Graph Strongly Connected - Checking if the graph is strongly connected using Breadth-first search on the graph, than running Breadth-first search on the inverted graph.

Shortest Path between two vertices - Finding the path and distance using Dijkstra's algorithm.

Finding the Graph Center - Finding the vertex in the graph, that has the minimal distance to the farthest vertex using Dijkstra's algorithm.

Finding Shortest Path For List of Vertices - Using a greedy algorithm and Dijkstra's algorithm in order to find the shortest path that goes through all the vertices in the list.
