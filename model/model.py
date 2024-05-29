from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def build_graph(self, year, color):
        self.graph.clear()
        nodi = DAO.get_nodes_dao(color)
        for n in nodi:
            self.idMap[n.p_number] = n
            self.graph.add_node(n)
        self.addEdgePesati(year, color)

    def addEdgePesati(self, year, color):
        """Questo metodo assegna come peso degli edges il numero di linee che congiungono i diversi nodi.
        """
        self.graph.clear_edges()
        allConnessioni = DAO.get_edges_dao(year, color, self.idMap)
        for c in allConnessioni:
            if self.graph.has_edge(c.p1, c.p2):
                self.graph[c.p1][c.p2]["weight"] += 1
            else:
                self.graph.add_edge(c.p1, c.p2, weight=1)

    def getAnni(self):
        return DAO.get_anni_dao()

    def getColors(self):
        return DAO.get_colors_dao()
