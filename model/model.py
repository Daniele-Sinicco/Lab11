from database.DAO import DAO
import networkx as nx
import copy
class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def build_graph(self, anno, colore):
        self.graph.clear()
        self.idMap = {}
        self.graph.add_nodes_from(DAO.get_nodi_dao(colore))
        for n1 in self.graph.nodes:
            for n2 in self.graph.nodes:
                if n1 != n2:
                    peso = DAO.get_peso_dao(n1, n2, anno)
                    if peso[0] is not None and peso[0]>0:
                        self.graph.add_edge(n1, n2, weight= peso[0])

    def get_maggiori(self):
        copia = copy.deepcopy(self.graph.edges(data=True))
        lista = list(copia)
        lista.sort(key= lambda x: x[2]["weight"], reverse=True)
        return lista[:3]

    def get_piu_presenti(self):
        archi = self.get_maggiori()
        nodi = {}
        for arco in archi:
            if arco[0] not in nodi.keys():
                nodi[arco[0]] = 1
            else:
                nodi[arco[0]] += 1
            if arco[1] not in nodi.keys():
                nodi[arco[1]] = 1
            else:
                nodi[arco[1]] += 1
        result = []
        for k in nodi.keys():
            if nodi[k]>1:
                result.append(k)
        return result

    def get_anni(self):
        return DAO.get_anni_dao()

    def get_colori(self):
        return DAO.get_colori_dao()

    def get_n_nodes(self):
        return self.graph.number_of_nodes()

    def get_n_edges(self):
        return self.graph.number_of_edges()

