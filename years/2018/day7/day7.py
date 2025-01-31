from typing import Tuple, List, Dict
import string


def parse_file(fileName: str) -> Dict[str, List[str]]:
  """
  Generates a graph of tasks pointing to their dependencies from input file.
  Tasks with no dependencies appear with empty lists as values.
  """
  h = open(fileName, "r")
  lines = h.readlines()
  h.close()

  nodes = set()
  dependencies = {}

  for line in lines:
    if line[36] in dependencies:
      dependencies[line[36]].append(line[5])
      dependencies[line[36]] = sorted(dependencies[line[36]])
    else:
      dependencies[line[36]] = [line[5]]

    if line[5] not in nodes:
      nodes.add(line[5])
    if line[36] not in nodes:
      nodes.add(line[36])
  for node in nodes:
    dependencies.setdefault(node, [])
  return dependencies


def part1(dependencies: Dict[str, List[str]]):
  # 1. find graph nodes with no dependencies - "active nodes"
  # 2. sort active nodes alphabetically
  # 3. append first active node (AN1) to path
  # 4. remove AN1 from list of dependencies of all nodes
  # 5. delete AN1 from graph
  # 6. delete AN1 from active nodes
  # 7. If graph isn't emptied yet, loop
  path = ""

  while len(dependencies) > 0:
    active_nodes = []
    #I know I don't actually need to reset the whole list every loop but this feels simpler since I'm re-adding and sorting everything anyway

    for node in dependencies:
      #step 1
      if dependencies[node] == []:
        active_nodes.append(node)
    active_nodes.sort()  #step 2
    path = path + active_nodes[0]  #step 3

    for node in dependencies:
      if active_nodes[0] in dependencies[node]:
        dependencies[node].remove(active_nodes[0])  #step 4
    dependencies.pop(active_nodes[0])  #step 5
    active_nodes.remove(active_nodes[0])  #step 6

  return path  #tested and it works bitch


def part2(dependencies: Dict[str, List[str]]):
  #loop second-by-second
  #replace list of active nodes with list of tuples (active node and finishing time)
  #only remove node when finishing time is reached, rather than resetting every loop
  #when removing node, also mark as complete by removing dependencies
  #only let nodes become active if all dependencies are complete AND there is a free worker
  pass


tests = {"example.txt": (["CABDFE", "CABFDE"])}
