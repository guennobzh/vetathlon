# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab


def index(req):
    '''Affiche la page pour la pointage des temps'''
    
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #création de l'objet base de donnée
    objBdd = _Datab()

    #Execute la requete pour resortire tous les dossards
    listDossards = objBdd.execute("SELECT dossards.numero, concat(partp.nom,' ',partp.prenom), concat(partv.nom,' ',partv.prenom), dossards.vtt - dossards.pieton, partp.sexe + partv.sexe, dossards.tmp_pieton, dossards.tmp_vtt, dossards.tmp_total, dossards.etat from dossards, participants as partp, participants as partv where dossards.pieton = partp.id and dossards.vtt = partv.id order by dossards.numero")
    
    #début du tableau
    retour = '''<center><FORM METHOD=POST ACTION="updateTmps">
    <table border="1">
     <tbody><h1>Pointage des temps</h1>
      <tr class="tete-tableau">
       <td style="text-align: center; width: 100px;">Dossard</td>
       <td style="text-align: center; width: 200px;">Courreur</td>
       <td style="text-align: center; width: 200px;">Vététiste</td>
       <td style="text-align: center; width: 100px;">Sexe</td>
       <td style="text-align: center; width: 120px;">Temps pieton </td>
       <td style="text-align: center; width: 120px;">Temps vtt</td>
       <td style="text-align: center; width: 120px;">Temps total<br></td>
       <td style="text-align: center; width: 120px;">Etat equipe<br></td>
      </tr>
    '''

    #crée une liste vide pour contenire tous les numero de dossards
    listd =[]

    #crée la vatiable pour la class css de la ligne
    lclass = 0
    
    #liste tous les dossards et ajoute une ligne pour chacun d'eu
    for infodossard in listDossards:
        #Ajoute le numero de dossards a la liste
        listd.append(str(infodossard[0]))
        
        #test si il s'agit d'une equipe
        if infodossard[3] != 0:
            nomv = '<td style="text-align: center;">%s</td>'%(infodossard[2])
            fusionc = ''
        else:
            nomv = ''
            fusionc = 'colspan="2"'

        #Deterine le sexe
        if infodossard[4] == 2:
           sexe = 'Feminin'
        if infodossard[4] == 3:
            sexe = 'Mixte'
        if infodossard[4] == 4:
            sexe = 'Masculin'

        #débinie la class css de la ligne
        if lclass == 0:
            classl = 'l-impaire'
            lclass = 1
        else:
            classl = 'l-paire'
            lclass = 0
        
        retour += '''<tr class="%s">
        <td style="text-align: right;"><a href="modifier?dossard=%s">%s<a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        <td %s style="text-align: center;">%s</td>
        %s
        <td style="text-align: center;">%s</td>
        <td style="text-align: center;"><INPUT style="text-align:right;" size="5" type=text name="tp%s" value="%s"></td>
        <td style="text-align: center;"><INPUT style="text-align:right;" size="5" disabled="on" type=text value="%s"></td>
        <td style="text-align: center;"><INPUT style="text-align:right;" size="5" type=text name="tt%s" value="%s"></td>
        <td style="text-align: center;">%s</td>
        </tr>
        '''%(classl, infodossard[0], infodossard[0], fusionc, infodossard[1], nomv, sexe, infodossard[0], infodossard[5], infodossard[6], infodossard[0], infodossard[7], _Etat(infodossard[8], infodossard[0]))
    
    retour += '</table><INPUT type="hidden" value="%s" name="listd"><INPUT type="submit" value="Envoyer"></FORM>'%(str(listd))
    return _Head(retour)

def _Etat(etat, dossard):
    #création de l'objet base de donnée
    objBdd = _Datab()

    retour = '<SELECT name="etat%s">'%(dossard)
    if etat == 0:
        retour += '<OPTION VALUE="0" selected>Partant</OPTION>'
        retour += '<OPTION VALUE="1">Abandon</OPTION>'
        retour += '<OPTION VALUE="2">Absent</OPTION>'        
    elif etat == 1:
        retour += '<OPTION VALUE="0">Partant</OPTION>'
        retour += '<OPTION VALUE="1" selected>Abandon</OPTION>'
        retour += '<OPTION VALUE="2">Absent</OPTION>'
    elif etat == 2:
        retour += '<OPTION VALUE="0">Partant</OPTION>'
        retour += '<OPTION VALUE="1">Abandon</OPTION>'
        retour += '<OPTION VALUE="2" selected>Absent</OPTION>'
        
    retour += '</SELECT>'
    return retour
