# -*- coding: utf-8 -*-
from mod_python import apache, Session

def index(req):
  return req.headers_in['referer']

def add(req, texte=None):
    if texte:
        from datab import _Datab
        
        #Crée l'objet base de donnée
        objBdd = _Datab() 

        #ajoute le message a la base de donnée
        objBdd.execute("INSERT INTO .`minichat` (`texte`)VALUES ('%s');"%(texte.replace("'", "\\'")))

    #Deretmine la page precedente si elle existe
    if req.headers_in.has_key('referer'):
        urlBack = req.headers_in['referer']
    else:
        urlBack = '/vetathlon'

    return '<html><meta http-equiv="refresh" content="0;URL=%s"></html>'%(urlBack)
    

def _affiche():
    from datab import _Datab
    
    #Crée l'objet base de donnée
    objBdd = _Datab()

    #Selectionne les 5 dernier messages
    lstMsg = objBdd.execute("select texte  FROM `minichat` order by time desc limit 5")

    #Convertir le résultat en list et inverse l'ordre
    lstMsg = list(lstMsg)
    lstMsg.reverse()

    #Définie la variable de retour vide
    retour = ""

    #liste les messages et ajoute les dans le retour
    for msg in lstMsg:
	    retour += '- '+msg[0]+'<br>'

    return '''
    <table style="text-align: left; width: 200px; height: 31px;" border="1">
    <tbody>
    <tr>
    <td>
    %s
    <center><form method="get" action="/vetathlon/minichat/add"><input name="texte" size="20"></form></center>
    </td>
    </tr>
    </tbody>
    </table>
    '''%retour
