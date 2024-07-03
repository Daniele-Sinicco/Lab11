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
        for y in self._model.get_anni():
            self._view._ddyear.options.append(ft.dropdown.Option(key=y, text=str(y)))
        for c in self._model.get_colori():
            self._view._ddcolor.options.append(ft.dropdown.Option(key=c, text=str(c)))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txtOut.clean()
        anno = self._view._ddyear.value
        colore = self._view._ddcolor.value
        if anno == ""  or anno is None or colore == "" or colore is None:
            self._view.create_alert("Selezionare entrambi i campi.")
        else:
            self._model.build_graph(anno, colore)
            self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {self._model.get_n_nodes()} nodi e {self._model.get_n_edges()} archi."))
            for arco in self._model.get_maggiori():
                self._view.txtOut.controls.append(ft.Text(f"Arco da {arco[0]} a {arco[1]}, peso: {arco[2]["weight"]}"))
            ripetuti = self._model.get_piu_presenti()
            self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {ripetuti}"))
            self._view.update_page()

    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
