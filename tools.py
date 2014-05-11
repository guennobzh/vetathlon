# -*- coding: utf-8 -*-


def _Zero(nombre):
        if nombre < 10:
                nombre = '0'+str(nombre)
        return str(nombre)


def _Head(corps):
    from minichat import _affiche

    s="""
    <html>
    <HEAD>
    <link rel="stylesheet" type="text/css" media="screen" href="/style.css" />
    <link rel="stylesheet" type="text/css" media="print" href="/print.css" />
    </HEAD>
    <body>
     <div class="content">
        %s
     </div>

     <p class="menufixe noprint">
        <input class="noprint" type="button" name="menu" value="Retour au menu" onclick="self.location.href='/vetathlon/index'">
        %s
     </p>
     </body></html>
    """
    return s%(corps, _affiche() )


def _checkVarSolo(dicArgum):
    from datab import _Datab
    import re

    #Crée l'objet base de donnée
    objBdd = _Datab()

    #définie les arguments a partire du dictionnaire
    nom = dicArgum['nom']
    prenom = dicArgum['prenom']
    daten = dicArgum['daten']
    if dicArgum.has_key('sexe'):
        sexe = dicArgum['sexe']
    else:
        sexe = ''
    commune = dicArgum['commune']
    idcommune = dicArgum['idcommune']
    dept = dicArgum['dept']
    mail = dicArgum['mail']
    dossard = dicArgum['dossard']
    if dicArgum.has_key('certi'):
        certi = dicArgum['certi']
    else:
        certi = ''
    if dicArgum.has_key('payer'):
        payer = dicArgum['payer']
    else:
        payer = ''

    #Si le nom n'est pas renseigner
    if not nom:
        txterr = 'Veuillez entrée un nom'

    #Si le prenom n'est pas renseigner
    elif not prenom:
        txterr = 'Veuillez entrée un prenom'

    #Si le sexe n'est pas renseigner
    elif not sexe:
        txterr = 'Veuillez entrée le sexe'
    
    #Si la commune n'est pas renseigner
    elif not commune and not objBdd.execute("select * from villes where id='%s'"%(idcommune)):
        txterr = 'Veuillez entrée une commune'

    #Vérifie si le numero de departement existe dans la base des departements
    elif not objBdd.execute("select * from departement where code='%s'"%(dept)):
        txterr = 'Numero de departement incorrecte à. entrée avec deux chiffre example : 02'

    #Vérifie si le mais est valide
    if mail and not re.findall('.*@.*\....?',mail):
        txterr = 'Adresse mail non valide'

    #Vérifie si la date est valide
    elif not re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}',daten):
        txterr = 'Date de naissance non valide. a entrée sous la forme jj/mm/aaaa'

    #Si pas d'erreure trouver
    else:
        txterr =''

    return {'nom':nom, 'prenom':prenom, 'daten':daten, 'sexe':sexe, 'commune':commune, 'idcommune':idcommune, 'dept':dept, 'mail':mail, 'dossard':dossard, 'certi':certi, 'payer':payer, 'txterr':txterr}

def _checkVarEquipe(dicArgum):
    from datab import _Datab
    import re

    #Crée l'objet base de donnée
    objBdd = _Datab()

    #Information sur le courreur
    nomc = dicArgum['nomc']
    prenomc = dicArgum['prenomc']
    datenc = dicArgum['datenc']
    if dicArgum.has_key('sexec'):
        sexec = dicArgum['sexec']
    else:
        sexec = ''
    communec = dicArgum['communec']
    idcommunec = dicArgum['idcommunec']
    deptc = dicArgum['deptc']
    mailc = dicArgum['mailc']
    if dicArgum.has_key('certic'):
        certic = dicArgum['certic']
    else:
        certic = ''

    #information sur le vététiste
    nomv = dicArgum['nomv']
    prenomv = dicArgum['prenomv']
    datenv = dicArgum['datenv']
    if dicArgum.has_key('sexev'):
        sexev = dicArgum['sexev']
    else:
        sexev = ''
    communev = dicArgum['communev']
    idcommunev = dicArgum['idcommunev']
    deptv = dicArgum['deptv']
    mailv = dicArgum['mailv']
    if dicArgum.has_key('certiv'):
        certiv = dicArgum['certiv']
    else:
        certiv = ''
        
    #information sur l'equipe
    dossard = dicArgum['dossard']    
    if dicArgum.has_key('payer'):
        payer = dicArgum['payer']
    else:
        payer = ''


    #Si le nom n'est pas renseigner
    if not nomc:
        txterr = 'Veuillez entrée le nom du coureur'
    elif not nomv:
        txterr = 'Veuillez entrée le nom du vététiste'

    #Si le prenom n'est pas renseigner
    elif not prenomc:
        txterr = 'Veuillez entrée le prenom du coureur'
    elif not prenomv:
        txterr = 'Veuillez entrée le prenom du vététiste'

    #Si le sexe n'est pas renseigner
    elif not sexec:
        txterr = 'Veuillez entrée le sexe du coureur'
    elif not sexev:
        txterr = 'Veuillez entrée le sexe du vététiste'

    #Si la commune n'est pas renseigner
    elif not communec and not objBdd.execute("select * from villes where id='%s'"%(idcommunec)):
        txterr = 'Veuillez entrée une commune du coureur'
    elif not communev and not objBdd.execute("select * from villes where id='%s'"%(idcommunev)):
        txterr = 'Veuillez entrée une commune du vététiste'

    #Vérifie si le numero de departement existe dans la base des departements
    elif not objBdd.execute("select * from departement where code='%s'"%(deptc)):
        txterr = 'Numero de departement du coureur incorrecte à. entrée avec deux chiffre example : 02'
    elif not objBdd.execute("select * from departement where code='%s'"%(deptv)):
        txterr = 'Numero de departement du vététiste incorrecte à. entrée avec deux chiffre example : 02'

    #Vérifie si le mais est valide
    elif mailc and not re.findall('.*@.*\....?',mailc):
        txterr = 'Adresse mail du coureur non valide'
    elif mailv and not re.findall('.*@.*\....?',mailv):
        txterr = 'Adresse mail du vététiste non valide'

    #Vérifie si la date est valide
    elif not re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}',datenc):
        txterr = 'Date de naissance du coureur non valide. a entrée sous la forme jj/mm/aaaa'
    elif not re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}',datenv):
        txterr = 'Date de naissance du vététiste non valide. a entrée sous la forme jj/mm/aaaa'

    #Si pas d'erreure trouver
    else:
        txterr =''

    return {'nomc':nomc, 'prenomc':prenomc, 'datenc':datenc, 'sexec':sexec, 'communec':communec, 'idcommunec':idcommunec, 'deptc':deptc, 'mailc':mailc, 'certic':certic, 'nomv':nomv, 'prenomv':prenomv, 'datenv':datenv, 'sexev':sexev, 'communev':communev, 'idcommunev':idcommunev, 'deptv':deptv, 'mailv':mailv, 'certiv':certiv, 'dossard':dossard, 'payer':payer, 'txterr':txterr}
