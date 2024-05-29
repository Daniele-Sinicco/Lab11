from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.products import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_anni_dao():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(Date) AS Year FROM go_daily_sales"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Year"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_colors_dao():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT Product_color FROM go_products"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_nodes_dao(color):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM go_products WHERE Product_color = %s"""
        cursor.execute(query, (color,))
        for row in cursor:
            result.append(Prodotto(row["Product_number"], row["Product_line"], row["Product_type"], row["Product"],
                                   row["Product_brand"], row["Product_color"], row["Unit_cost"], row["Unit_price"]))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_edges_dao(year, color, idMap):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select g1.Product_number as p1, g2.Product_number as p2
                    from go_daily_sales g1, go_daily_sales g2 
                    where g1.Retailer_code = g2.Retailer_code and 
                    g1.Product_number != g2.Product_number and
                    g1.Product_number in (SELECT Product_number FROM go_products WHERE Product_color = %s) and 
                    g2.Product_number in (SELECT Product_number FROM go_products WHERE Product_color = %s) and
                    g1.`Date` = g2.`Date` and
                    year(g1.`Date`) = %s"""
        cursor.execute(query, (color, color, year))
        for row in cursor:
            result.append(Connessione(idMap[row["p1"]], idMap[row["p2"]]))
        cursor.close()
        cnx.close()
        return result