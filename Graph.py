from __future__ import annotations


class Node:

    def __init__(self, name, index, heuristic):
        self.parent = None
        self.name = name
        self.index = index
        self.heu = heuristic
        self.level = 0
        self.visited, self.start, self.goal = False, False, False
        self.children = []

    def visitNode(self):
        self.visited = True

    def isVisited(self):
        return self.visited

    def setStart(self):
        self.start = True

    def isStart(self):
        return self.start

    def setGoal(self):
        self.goal = True

    def isGoal(self):
        return self.goal

    def setChild(self, node: Node):
        self.children += [node]

    def setParent(self, node: Node):
        self.parent = node


class Graph:

    def __init__(self, directed=False):
        self.Nodes = []
        self.nNodes = 0
        self.isDirected = directed
        self.myArr = []

    def add_node(self, name, heuristic):
        name = str(self.nNodes) if name is None else name
        self.Nodes.append(Node(name, int(self.nNodes), heuristic))
        self.nNodes += 1
        for i in range(self.nNodes - 1):
            self.myArr[i].append(0)
        self.myArr.append([0 for _ in range(self.nNodes)])

    def add_edge(self, n1, n2: Node, weight=1):
        if (n1 in self.Nodes) & (n2 in self.Nodes):
            if self.myArr[n1.index][n2.index] == 0:
                self.myArr[n1.index][n2.index] = weight
                self.Nodes[n1.index].setChild(n2)
                if not self.isDirected:
                    self.myArr[n2.index][n1.index] = weight
                    self.Nodes[n2.index].setChild(n1)
        check1 = self.myArr[n1.index][n2.index] == self.myArr[n2.index][n1.index]
        if check1 and not self.isDirected:
            self.myArr[n1.index][n2.index] = weight

    def printMatrix(self):
        for i in range(self.nNodes):
            for j in range(self.nNodes):
                print(self.myArr[i][j], end=" ")
            print("")
        print("")

    # ------------------------------------- end of graph class functions -----------------------------------------

    # -------------- Some functions that may help with the search algorithms implementation ----------------------

    def initiate(self):
        """ A function that returns 2 lists (visited and queue) with the start node popped in each of them """
        visited, queue = [], []
        for i in range(self.nNodes):  # force visiting first node
            if self.Nodes[i].isStart():
                visited.append(self.Nodes[i])  # adding start node to visited list
                queue.append(self.Nodes[i])  # adding start node at the end of the queue
                self.Nodes[i].visitNode()  # visiting the start node
                break
        return visited, queue

    def switchReturn(self, visited):
        """ A function that switches the nodes of the list into integers with the node index and with a string at
        the end of the list, G-> means that goal state is visited, NG-> means that goal state isn't visited """
        for i in range(self.nNodes):
            self.Nodes[i].visited = False
            self.Nodes[i].parent = None
        if visited[-1].isGoal():
            visited.append('Goal Found')
        else:
            visited.append('No Goal Found')
        for i in range(len(visited) - 1):
            visited[i] = visited[i].name
        return visited

    @staticmethod
    def AorB(choose, A, B):
        """ A function that chooses an output based on the value of the choice you enter
            if you choose 0 it will return first value, otherwise, it'll return the second value"""
        if choose == 0:
            return A
        else:
            return B

    @staticmethod
    def solutionPath(lst: list):
        """ A function that returns the solution path of the goal state (if found) based on the visited list given """
        if not lst[-1].isGoal():
            return ['No goal states found to get solution path for']
        solution = [lst[-1].name]
        parents = lst[-1].parent
        for i in range(len(lst) - 1, 0, -1):
            solution.append(parents.name)
            if parents.isStart():
                break
            parents = parents.parent
        solution.reverse()
        return solution

    # ------------------------------------- end of search helper functions ---------------------------------------

    # --------------------------------- Search algorithms functions implementation -------------------------------

    def BFS_DFS_DLS(self, choose=0, level=1):
        # choose 0 or no value for BFS, choose 1 for DFS, choose 2 or other values for DLS
        # in case of DLS choose the limit level to limit your search
        visited = self.initiate()[0]
        queue = self.initiate()[1]
        if visited[0].isGoal():
            return [visited[0].name, 'Goal Found'], [visited[0].name]
        while queue:
            popped = queue.pop(0)  # removing first node and storing it at popped
            if popped.level > level:
                continue
            if not popped.isVisited():
                visited.append(popped)  # visiting the node and
                popped.visitNode()  # appending it at the visited queue
                if visited[-1].isGoal():
                    break
            for j in range(len(popped.children)):  # if the element we are trying to add isn't visited yet
                if (popped.children[j].level == 0) or (popped.children[j].level > (popped.level + 1)):
                    if not popped.children[j].isVisited():  # we start adding it to the queue list
                        if choose == 0:
                            level = self.nNodes
                            queue.append(popped.children[j])
                        elif choose == 1:
                            level = self.nNodes
                            queue.insert(0, popped.children[j])
                        else:
                            queue.insert(0, popped.children[j])
                        if popped.children[j].parent is None:
                            popped.children[j].setParent(popped)
                    popped.children[j].level = popped.level + 1
        for i in range(self.nNodes):
            self.Nodes[i].level = 0
        solution = self.solutionPath(visited)
        return self.switchReturn(visited), solution

    def UNI_ASTR(self, choose=0):
        # choose 0 or no value for uniform cost or any other value for astar search
        visited = self.initiate()[0]
        queue = self.initiate()[1]
        if visited[0].isGoal():
            return [visited[0].name, 'Goal Found'], [visited[0].name]
        paths = []
        a = self.myArr[visited[0].index][visited[0].children[0].index] + 1
        least = self.AorB(choose, a, a + visited[0].heu)
        for i in range(self.nNodes):
            a = self.myArr[queue[0].index][i]
            paths.append(self.AorB(choose, a, a + self.Nodes[i].heu))
        while queue:
            for k in range(self.nNodes):
                if (paths[k] < least) & (paths[k] != 0):
                    least = paths[k]
            popped = queue.pop(0)
            pn = popped.index
            for i in range(len(popped.children)):
                if not popped.children[i].isVisited():
                    cn = popped.children[i].index
                    a = self.myArr[pn][cn] + paths[pn]
                    b = self.myArr[pn][cn] + paths[pn] + self.Nodes[cn].heu - self.Nodes[pn].heu
                    check = self.AorB(choose, 0, self.Nodes[cn].heu)
                    if paths[cn] == check:
                        paths[cn] = self.AorB(choose, a, b)
                    if not (paths[cn] != check) & (paths[cn] < (self.myArr[pn][cn] + paths[pn])):
                        paths[cn] = self.AorB(choose, a, b)
                    x = self.myArr[pn][cn]
                    checklessthan = (paths[cn] <= least)
                    checkifpath = x != 0
                    if checklessthan & checkifpath:
                        queue.insert(0, self.Nodes[cn])
                        least = paths[cn]
                    else:
                        c = 0
                        for j in range(len(queue)):
                            if paths[queue[j].index] <= paths[cn]:
                                c += 1
                        queue.insert(c, self.Nodes[cn])
                    chk = (not self.Nodes[cn].parent is None) and (paths[pn] < paths[self.Nodes[cn].parent.index])
                    if (self.Nodes[cn].parent is None) | chk:
                        self.Nodes[cn].setParent(self.Nodes[pn])
            if not popped.isVisited():
                visited.append(popped)
                popped.visitNode()
                if visited[-1].isGoal():
                    break
        solution = self.solutionPath(visited)
        return self.switchReturn(visited), solution

    def greedyBestFirst(self):
        visited = self.initiate()[0]
        queue = self.initiate()[1]
        least = visited[0].children[0].heu + 1
        if visited[0].isGoal():
            return [visited[0].name, 'Goal Found'], [visited[0].name]
        while queue:
            popped = queue.pop(0)
            for i in range(len(popped.children)):
                if not popped.children[i].isVisited():
                    if popped.children[i].heu < least:
                        queue.insert(0, self.Nodes[popped.children[i].index])
                    else:
                        queue.append(self.Nodes[popped.children[i].index])
                    least = popped.children[i].heu
                    popped.children[i].setParent(popped)
            if not popped.isVisited():
                visited.append(popped)
                popped.visitNode()
                if visited[-1].isGoal():
                    break
        solution = self.solutionPath(visited)
        return self.switchReturn(visited), solution

    def ITD(self):
        # iterative deepening search method that loops on depth limited search
        visited = []
        solution = []
        for i in range(self.nNodes):
            a, b = self.BFS_DFS_DLS(3, i)
            visited.append(a)
            solution.append(b)
            if visited[i][-1] == 'Goal Found':
                break
            elif (i > 0) & (visited[i] == visited[i - 1]):
                visited.pop(i)
                break
        return visited, solution
