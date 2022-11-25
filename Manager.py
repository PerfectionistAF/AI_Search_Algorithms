from PyQt5 import *
#from PyQt5.QtGui import *
#from PyQt5.QtGui import QPixmap
#from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtWidgets
from PySide2.QtGui import QPixmap

from Welcome import Ui_Entry
from MainPage import Ui_mainGraph
from AddNode import Ui_AddNodePage
from AddEdge import Ui_AddEdgePage
from Depth import Ui_chooseDepth
import matplotlib.pyplot as plt
import networkx as nx
import Graph


class WCM(QtWidgets.QMainWindow, Ui_Entry):
    def __init__(self, parent=None):
        super(WCM, self).__init__(parent)
        self.setupUi(self)
        self.directedgraph.clicked.connect(self.hide)
        self.undirectedgraph.clicked.connect(self.hide)


class MainPage(QtWidgets.QMainWindow, Ui_mainGraph):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.hide)


class NodeAdd(QtWidgets.QMainWindow, Ui_AddNodePage):
    def __init__(self, parent=None):
        super(NodeAdd, self).__init__(parent)
        self.setupUi(self)


class EdgeAdd(QtWidgets.QMainWindow, Ui_AddEdgePage):
    def __init__(self, parent=None):
        super(EdgeAdd, self).__init__(parent)
        self.setupUi(self)


class Depth(QtWidgets.QMainWindow, Ui_chooseDepth):
    def __init__(self, parent=None):
        super(Depth, self).__init__(parent)
        self.setupUi(self)


class Manager:
    def __init__(self):
        self.buttonClicked = None
        self.backendGraph = Graph.Graph()
        self.G = nx.Graph()
        self.first = WCM()
        self.second = MainPage()
        self.nodeAddPage = NodeAdd()
        self.EdgeAddPage = EdgeAdd()
        self.DepthPage = Depth()
        self.NodesArr = []
        self.NodesNames = []
        self.HeuristicsArr = []
        self.EdgesArr = []
        self.colourmap = []
        self.start = 0
        self.goal = 0
        self.db = 0
        self.dlv = []
        self.dls = []
        self.first.directedgraph.clicked.connect(self.directedgraph)
        self.first.undirectedgraph.clicked.connect(self.unDirectedGraph)
        self.second.addNode.clicked.connect(self.nodeAddPage.show)
        self.second.addEdge.clicked.connect(self.EdgeAddPage.show)
        self.second.BackButton.clicked.connect(self.BackAction)
        self.second.confirmAddGoal.clicked.connect(self.setGoal)
        self.second.confirmSetStart.clicked.connect(self.setStart)
        self.nodeAddPage.confirmaddnode.clicked.connect(self.addNode)
        self.EdgeAddPage.confirmaddedge.clicked.connect(self.addEdge)
        self.second.Submit.clicked.connect(self.submit)
        self.DepthPage.pushButton.clicked.connect(self.submitDepth)
        self.first.show()

    def BackAction(self):
        del self.backendGraph
        del self.G
        self.EdgeAddPage.firstnode.clear()
        self.EdgeAddPage.secondnode.clear()
        self.second.startState.clear()
        self.second.goalState.clear()
        self.second.graphView.clear()
        self.buttonClicked = None
        self.NodesArr = []
        self.NodesNames = []
        self.HeuristicsArr = []
        self.EdgesArr = []
        self.colourmap = []
        self.start = 0
        self.goal = 0
        self.db = 0
        self.dlv = []
        self.dls = []
        self.first.show()
        self.second.visitedLabel.clear()
        self.second.solutionPathLabel.clear()

    @staticmethod
    def duplicate_name_message():
        msg = QMessageBox()
        msg.setWindowTitle("Duplicate Name")
        message = "Error! the name you entered is already taken be another node"
        msg.setText(message)
        msg.setInformativeText("Please enter another name")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def duplicate_edge_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Duplicate Edge")
        message = "The edge you are trying to add is already added"
        msg.setText(message)
        msg.setInformativeText("Would you like to update the weight ?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_But)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def directedgraph(self):
        self.backendGraph = Graph.Graph(True)
        self.G = nx.DiGraph()
        self.second.show()

    def unDirectedGraph(self):
        self.backendGraph = Graph.Graph()
        self.G = nx.Graph()
        self.second.show()

    def addNode(self):
        if self.nodeAddPage.nodename.text() + '\nh='+str(self.nodeAddPage.nodeheurestic.value()) in self.NodesArr:
            self.duplicate_name_message()
        elif self.nodeAddPage.nodename.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Add A Name")
            msg.setText("Warning! you've entered no names")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.popup_But)
            toadded = str(len(self.NodesArr))
            while toadded in self.NodesArr:
                toadded = str(len(self.NodesArr)) + "n"
            msg.setInformativeText(toadded + " will be added as a name")
            msg.exec_()
            if self.buttonClicked == "OK":
                self.NodesArr.append(toadded+'\nh='+str(self.nodeAddPage.nodeheurestic.value()))
                self.NodesNames.append(toadded)
                self.HeuristicsArr.append(self.nodeAddPage.nodeheurestic.value())
                self.EdgeAddPage.firstnode.addItem(self.NodesNames[-1])
                self.EdgeAddPage.secondnode.addItem(self.NodesNames[-1])
                self.second.goalState.addItem(self.NodesNames[-1])
                if self.start == 0:
                    self.second.startState.addItem(self.NodesNames[-1])
                self.backendGraph.add_node(self.NodesNames[-1], self.nodeAddPage.nodeheurestic.value())
                self.G.add_node(toadded+'\nh='+str(self.nodeAddPage.nodeheurestic.value()))
                self.colourmap.append('lightblue')
                self.updateVisual()
            else:
                pass
        else:
            self.NodesArr.append(self.nodeAddPage.nodename.text() + '\nh='+str(self.nodeAddPage.nodeheurestic.value()))
            self.NodesNames.append(self.nodeAddPage.nodename.text())
            self.HeuristicsArr.append(self.nodeAddPage.nodeheurestic.value())
            self.EdgeAddPage.firstnode.addItem(self.NodesNames[-1])
            self.EdgeAddPage.secondnode.addItem(self.NodesNames[-1])
            self.second.goalState.addItem(self.NodesNames[-1])
            self.second.startState.addItem(self.NodesNames[-1])
            self.backendGraph.add_node(self.NodesNames[-1], self.nodeAddPage.nodeheurestic.value())
            self.G.add_node(self.NodesArr[-1])
            self.colourmap.append('lightblue')
            self.updateVisual()

    def addEdge(self):
        first = self.NodesNames.index(self.EdgeAddPage.firstnode.currentText())
        second = self.NodesNames.index(self.EdgeAddPage.secondnode.currentText())
        weight = self.EdgeAddPage.edgeweight.value()
        if self.EdgeAddPage.edgeweight.value() != 0:
            if (self.EdgeAddPage.firstnode.currentText() != "") & (self.EdgeAddPage.secondnode.currentText() != ""):
                firstname = self.NodesArr[first]
                secondname = self.NodesArr[second]
                toad = self.EdgeAddPage.firstnode.currentText()+self.EdgeAddPage.secondnode.currentText()
                if toad in self.EdgesArr:
                    self.duplicate_edge_message()
                    if self.buttonClicked == "OK":
                        x = self.backendGraph.myArr[first][second]
                        self.backendGraph.myArr[first][second] = weight
                        self.G[firstname][secondname]['weight'] = weight
                        if not self.backendGraph.isDirected:
                            if x == self.backendGraph.myArr[second][first]:
                                self.backendGraph.myArr[second][first] = weight
                else:
                    self.EdgesArr.append(toad)
                    self.backendGraph.add_edge(self.backendGraph.Nodes[first], self.backendGraph.Nodes[second], weight)
                    self.G.add_edge(firstname, secondname, length=weight)
        self.updateVisual()

    def updateVisual(self):
        plt.close()
        self.second.graphView.clear()
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, node_color=self.colourmap)
        edge_labels = dict([((u, v,), d['length'])for u, v, d in self.G.edges(data=True)])
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
        nx.draw_networkx_labels(self.G, pos)
        plt.savefig("Graph.png")
        pixmap = QPixmap('Graph.png')
        self.second.graphView.setPixmap(pixmap)
        pos.clear()

    def setGoal(self):
        if self.second.goalState.currentText() != "":
            self.goal = 1
            goal = self.second.goalState.currentText()
            element = self.NodesNames.index(goal)
            ind = self.second.goalState.currentIndex()
            self.second.startState.removeItem(ind)
            self.second.goalState.removeItem(ind)
            self.backendGraph.Nodes[element].setGoal()
            self.colourmap[element] = 'green'
        self.updateVisual()

    def setStart(self):
        if self.second.startState.currentText() != "":
            self.start = 1
            start = self.second.startState.currentText()
            element = self.NodesNames.index(start)
            ind = self.second.startState.currentIndex()
            self.second.startState.clear()
            self.second.goalState.removeItem(ind)
            self.backendGraph.Nodes[element].setStart()
            self.colourmap[element] = 'orange'
        self.updateVisual()

    def submitDepth(self):
        self.db = self.DepthPage.spinBox.value()
        print(self.db)
        visited, solution = self.backendGraph.BFS_DFS_DLS(2, self.db)
        visited = visited[:-1]
        sl = "["
        vl = "["
        for i in range(len(visited)):
            vl = vl + visited[i] + ", "
        vl = vl[:-2] + "]"
        for i in range(len(solution)):
            sl = sl + solution[i] + ", "
        sl = sl[:-2] + "]"
        self.second.visitedLabel.setText(vl)
        self.second.solutionPathLabel.setText(sl)
        self.DepthPage.hide()

    def submit(self):
        if not (self.start == 0 | self.goal == 0):
            if self.second.ChooseSearch.currentText() == "Breadth First":
                visited, solution = self.backendGraph.BFS_DFS_DLS()
                self.makePath(visited, solution)
            elif self.second.ChooseSearch.currentText() == "Depth First":
                visited, solution = self.backendGraph.BFS_DFS_DLS(1)
                self.makePath(visited, solution)
            elif self.second.ChooseSearch.currentText() == "Uniform Cost":
                visited, solution = self.backendGraph.UNI_ASTR()
                self.makePath(visited, solution)
            elif self.second.ChooseSearch.currentText() == "Greedy Best First":
                visited, solution = self.backendGraph.greedyBestFirst()
                self.makePath(visited, solution)
            elif self.second.ChooseSearch.currentText() == "A Star":
                visited, solution = self.backendGraph.UNI_ASTR(1)
                self.makePath(visited, solution)
            elif self.second.ChooseSearch.currentText() == "Depth Limited":
                self.DepthPage.show()
            elif self.second.ChooseSearch.currentText() == "Iterative Deepening":
                visited, solution = self.backendGraph.ITD()
                self.makePath(visited, solution, True)

    def makePath(self, visited=None, solution=None, itd=False):
        if visited is None:
            visited = []
        if solution is None:
            solution = []
        sl = "["
        vl = "["
        solution = solution[-1] if itd else solution
        for i in range(len(solution)):
            sl = sl + solution[i] + ", "
        sl = sl[:-2] + "]"
        self.second.solutionPathLabel.setText(sl)
        if itd:  # Iterative Deepening
            for i in range(len(visited)):
                visited[i] = visited[i][:-1]
                for j in range(len(visited[i])):
                    vl = vl + visited[i][j] + ", "
                vl = vl[:-2] + ": "
            vl = vl[:-2] + "]"
        else:
            visited = visited[:-1]
            for i in range(len(visited)):
                vl = vl + visited[i] + ", "
            vl = vl[:-2] + "]"
        self.second.visitedLabel.setText(vl)

    def popup_But(self, i):
        self.buttonClicked = i.text()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
