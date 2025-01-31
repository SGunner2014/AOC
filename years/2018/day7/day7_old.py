from typing import Tuple, List, Dict
import string


def parse_file(
    fileName: str) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
  graph = {}
  dependencies = {}

  h = open(fileName, "r")
  lines = h.readlines()
  h.close()

  for line in lines:
    if line[5] in graph:
      graph[line[5]].append(line[36])
      graph[line[5]] = sorted(graph[line[5]])
    else:
      graph[line[5]] = [line[36]]

    if line[36] in dependencies:
      dependencies[line[36]].append(line[5])
      dependencies[line[36]] = sorted(dependencies[line[36]])
    else:
      dependencies[line[36]] = [line[5]]
  return (graph, dependencies)


# 0. Find the end node
# 1. Goal = end node
# 2. Figure out which dependency of end goal to do first
# 3. Make recursive call to find_path function, for the first dependency to work out
# 4. For the recursive function, this does the same thing, but for the point passed down.


def part1(params: Tuple[Dict[str, List[str]], Dict[str, List[str]]], *args):
  (graph, dependencies) = params

  # deps_set = set(dependencies.keys())
  # graph_set = set(graph.keys())

  # goal = deps_set.difference(graph_set)

  # if len(goal) != 1:
  #   print("fuck")
  # goal_pt = list(goal)[0]

  # print("Goal detected: " + goal_pt)

  # Recursive: find a path leading up to a point, in string form.
  # def find_path(point: str, path: str) -> str:
  #   direct_dependencies = dependencies.get(point, [])

  #   print(f"Dependencies ({point}): " + str("".join(direct_dependencies)))

  #   for dependency in direct_dependencies:
  #     if dependency not in path:
  #       path = find_path(dependency, path)

  #   path += point
  #   return path

  found_path = ""

  # Henry's logic here:
  # 1. find graph nodes with no dependencies
  # 2. add those to the path in alphabetical order
  # 3. remove from list of dependencies of all other nodes
  # 5. if no nodes remain, path is complete, otherwise go to 1

  #Find all nodes that exist in the graph
  nodes = list(set(graph.keys()).union(set(dependencies.keys())))
  print(f"starting nodes: {nodes}")
  while nodes != []:
    active_nodes = []
    for node in nodes:
      if node not in dependencies:
        #if the node exists but never had dependencies, make it active
        active_nodes.append(node)
      elif dependencies[node] == []:
        #if the node has had all dependencies fulfilled, make it active
        active_nodes.append(node)

    for active_node in active_nodes:
      for node in dependencies:
        if active_node in dependencies[node]:
          dependencies[node].remove(active_node)
      nodes.remove(active_node)
    print(active_nodes)
    # if len(active_nodes) > 0:
    #   break

  # Double check constraints:
  for point, deps in dependencies.items():
    for dep in deps:
      if found_path.find(point) < found_path.find(dep):
        print(f"Constraint violated: {dep} must come before {point}")

  return found_path


tests = {"example.txt": (["CABDFE", ""])}
