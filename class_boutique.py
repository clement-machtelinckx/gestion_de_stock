import mysql.connector

class Boutique:
    def __init__(self):
        self.mybout = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Clement2203$",
            database="boutique"
        )
        self.cursor = self.mybout.cursor()

# CRUD produit

    def add_produit(self, nom, prix, quantite, id_categorie, description):
        query = "INSERT INTO produit (nom, prix, quantite, id_categorie, description) VALUES (%s, %s, %s, %s, %s)"
        value = (nom, prix, quantite, id_categorie, description)
        self.cursor.execute(query, value)
        self.mybout.commit()
        return self.cursor.lastrowid

    def read_produit(self):
        query = "SELECT * FROM produit"
        self.cursor.execute(query)
        return self.cursor.fetchall


    def update_produit(self, id, nom, prix, quantite, id_categorie, description):
        query = "UPDATE produit SET nom=%s, prix=%s, quantite=%s, id_categorie=%s, description=%s WHERE id=%s"
        value = (nom, prix, quantite, id_categorie, description, id)
        self.cursor.execute(query, value)
        self.mybout.commit()

    def delete_produit(self, id):
        query = "DELETE FROM produit WHERE id=%s"
        value = (id,)
        self.cursor.execute(query, value)

    # CRUD categorie

    def add_categorie(self, nom):
        query = "INSERT INTO categorie (nom) VALUES (%s)"
        value = (nom,)
        self.cursor.execute(query, value)
        self.mybout.commit()
        return self.cursor.lastrowid

    def read_categorie(self):
        query = "SELECT * FROM categorie"
        self.cursor.execute(query)
        return self.cursor.fetchall

    def update_categorie(self, id, nom):
        query = "UPDATE categorie WHERE id=%s"
        value = (id, nom)
        self.cursor.execute(query, value)

    def delete_categorie(self, id):
        query = "DELETE FROM categorie WHERE id=%s"
        value = (id,)
        self.cursor.execute(query, value)

bout = Boutique()
# bout.add_produit("saumon", 15, 628, 4, "poisson sashimi")

# bout.update_produit(5, "courgette", 1, 345, 2, "dark courgette")





