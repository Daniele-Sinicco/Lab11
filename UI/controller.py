import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        for y in self._model.getAnni():
            self._listYear.append(y)
            self._view._ddyear.options.append(ft.dropdown.Option(key=y, text=str(y)))
        for c in self._model.getColors():
            self._listYear.append(c)
            self._view._ddcolor.options.append(ft.dropdown.Option(key=c, text=str(c)))
        self._view.update_page()




    def handle_graph(self, e):
        self._model.build_graph(int(self._view._ddyear.value), self._view._ddcolor.value)
        self._view.txtOut.controls.append(ft.Text(f"Il grafo creato ha {self._model.graph.number_of_nodes()} nodi e "
                                                  f"{self._model.graph.number_of_edges()} archi."))
        for e in self._model.graph.edges():
            self._view.txtOut.controls.append(ft.Text(f"({e[0]},{e[1]}) peso {self._model.graph[e[0]][e[1]]['weight']}"))
        self._view.update_page()


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
