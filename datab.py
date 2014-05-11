# -*- coding: utf-8 -*-

import MySQLdb

class _Datab():
    def __init__(self):
        ipmysql = 'localhost'
        usermysql = 'vetathlon'
        passmysql = 'seer00'
        basemysql = 'vetathlon'

        self.conn = MySQLdb.connect (host = ipmysql, user = usermysql, passwd = passmysql, db = basemysql)




    def execute(self, commande):
	'''execute une commande et retourne le résultat'''

        #Création du curseur
        cursor = self.conn.cursor()

        #Execute la commande
        cursor.execute(commande)

        self.conn.commit()

        return cursor.fetchall()

    def insert(self, commande):
        '''execute une commande et retourne insert_id()'''
        
        #Création du curseur
        cursor = self.conn.cursor()

        #Execute la commande
        cursor.execute(commande)

        self.conn.commit()

        return int(cursor.lastrowid)

    def insertCommune(self, commune):
        #Recherche si une ortographe approchez du nom de la ville existe
        idVille = self.execute("select id from villes where nom like '%s'"%(commune.replace("'","\\'")))
        
        #Si un resultat a la recherche précédente donne l'id de la recherche
        if idVille:
            idcommune = idVille[0][0]
 
        #sinon ajoute la ville a la base
        else:
            idcommune =  self.insert("INSERT INTO `villes` (`id` ,`nom`) values ( null, '%s');"%(commune.replace("'","\\'")))

        return idcommune

    def nextDossard(self, junior=False):
        '''Retourne le numero du prochain dossard disponible'''
        if junior:
                dossard = self.execute("SELECT `numero`+1 FROM `dossards` WHERE (`numero`+1) not in (SELECT `numero` FROM `dossards` where numero>200) and (`numero`+1)>200 LIMIT 1;")
		numero = 201
        else:
                dossard = self.execute("SELECT `numero`+1 FROM `dossards` WHERE (`numero`+1) not in (SELECT `numero` FROM `dossards` where numero>1) and (`numero`+1)>1 and `numero`<200 LIMIT 1;")
		numero = 1

        if dossard:
            return dossard[0][0]
        else:
            return numero
    
    def close(self):
        self.conn.close()
