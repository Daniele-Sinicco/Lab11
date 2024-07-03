from database.DB_connect import DBConnect


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
        query = """select distinct year(`Date`) as anno
                    from go_daily_sales"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["anno"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_colori_dao():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct Product_color 
                    from go_products"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_nodi_dao(colore):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select Product_number 
                    from go_products
                    where Product_color = %s"""
        cursor.execute(query, (colore,))
        for row in cursor:
            result.append(row["Product_number"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_peso_dao(n1, n2, anno):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select count(distinct date(g1.`Date`)) as peso
                    from go_daily_sales g1, go_daily_sales g2
                    where g1.Retailer_code = g2.Retailer_code and
                    year (g1.`Date`) = %s and
                    year(g2.`Date`) = %s and 
                    date(g1.`Date`) = date(g2.`Date`) and 
                    g1.Product_number = %s and 
                    g2.Product_number = %s"""
        cursor.execute(query, (anno, anno, n1, n2))
        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        cnx.close()
        return result
