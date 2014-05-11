# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab

def index(req, dossard=0, yes=False):
    '''supprime un dossard'''

    #Si aucun numero de dossard m'est enrée : rien a supprimer
    if dossard == 0:
        return _Head('<center><h1>Rien a supprimer</h1><center>')

    #Si pas de confirmatio: la demande
    elif not yes:
        return _Head('''<center><h1><font color="red">Etent vous sur de vouloir supprimer le dossard N°%s</font></h1><center>
        <input type="button" name="oui" value="Oui" onclick="self.location.href='del?dossard=%s&yes=True'">
        <input type="button" name="non" value="Non" onclick="self.location.href='modifsolo?dossard=%s'">

        '''%(dossard, dossard, dossard))

    #Si il y a confirmation efface tout
    elif yes:
        #Crée l'objet base de donnée
        objBdd = _Datab()

        #Recupere les id des participants
        participant = objBdd.execute("select pieton, vtt from dossards where numero = %s"%(dossard))[0]

        if participant[0] == participant[1]:
            objBdd.execute("DELETE FROM `vetathlon`.`participants` WHERE `participants`.`id` = %s"%(participant[0]))
        else:
            objBdd.execute("DELETE FROM `vetathlon`.`participants` WHERE `participants`.`id` = %s or `participants`.`id` = %s"%(participant[0], participant[1]))

        return _Head('<center><h1>Le dossard %s a bien ete supprimer</h1></center><meta http-equiv="refresh" content="3;URL=index">'%(dossard))
