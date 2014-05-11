# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab

def equipes(req):
    '''afficher la liste de toutes les equipe avec le nom des participant et leur commune'''
    
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"
    
    #crée l'objet base de donnée
    objBdd = _Datab()

    #Effectue la requere sql pour ressortire les informations
    listequipe = objBdd.execute('''select `dossards`.`numero`,                               /*selectionne le numero de dossards*/
        `dossards`.`pieton`, `dossards`.`vtt`, `dossards`.`etat`,                            /*selectionne l\'id du pieton et du vetetiste et l`'etat de l`'equipe*/
        `particpp`.`nom`, `particpp`.`prenom`, year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))), `particpp`.`sexe`,          /*selectionne les nom, prenom et age du pieton*/
        `departementp`.`nom`, `villesp`.`nom`,                                               /*selectionne le departement et la ville du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`, year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))), `particpv`.`sexe`,          /*selectionne les nom, prenom et age du vététiste*/
        `departementv`.`nom`, `villesv`.`nom`                                                /*selectionne le departement et la ville du vététiste*/
    
        from `dossards`, `participants` as `particpp`, `participants` as `particpv`,         /*utilise dossards et 2* la table particimants comme particpp et particpv*/
        `departement` as `departementp`, `departement` as `departementv`,                    /*utilise 2* la table departement comme departementp et departements*/
        `villes` as `villesp`, `villes` as `villesv`,                                         /*utilise 2* la table villes comme villesp et villesv*/
        `config`                                                                             /*utilise la table de configuration*/
        
        where `particpp`.`id` = `dossards`.`pieton`                                          /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                               /*fait correspondre l\'id du vetetiste a sa fiche*/
        and `villesp`.`id` = `particpp`.`commune`                                            /*fait correspondre l\'id de la ville du pieton au nom de la ville*/
        and `villesv`.`id` = `particpv`.`commune`                                            /*fait correspondre l\'id de la ville du vetetiste au nom de la ville*/
        and `departementp`.`code` = `particpp`.`departement`                                 /*fait correspondre l\'id dudepartement du pieton au nom du departement*/
        and `departementv`.`code` = `particpv`.`departement`                                 /*fait correspondre l\'id dudepartement du vetetiste au nom du departement*/
        order by  `dossards`.`numero`                                                        /*trie les resultat par ordre croisant de dossard*/
        ;''')

    #début du tableau
    retour = '''<center><h1>Liste des différentes équipes</h1><table style="text-align: left;" border="1" cellpadding="2"
    cellspacing="2">
    <tbody>
    <tr class="tete-tableau">
        <td colspan="3" style="vertical-align: top; text-align: center;">Equipe
        </td>
        <td colspan="4" style="vertical-align: top; text-align: center;">Piéton
        </td>
        <td colspan="4" style="vertical-align: top; text-align: center;">Vététiste
        </td>
    </tr>
    <tr class="tete-tableau">
        <td style="vertical-align: top;">Dossard<br>
        </td>
        <td style="vertical-align: top;">Etat<br>
        </td>
        <td style="vertical-align: top;">Sexe<br>
        </td>
        <td style="vertical-align: top;">Nom<br>
        </td>
        <td style="vertical-align: top;">Age</td>
        <td style="vertical-align: top;">Departement<br>
        </td>
        <td style="vertical-align: top;">Ville<br>
        </td>
        <td style="vertical-align: top;">Nom<br>
        </td>
        <td style="vertical-align: top;">Age</td>
        <td style="vertical-align: top;">Departement<br>
        </td>
        <td style="vertical-align: top;">Ville<br>
        </td>
    </tr>'''

    #crée la variable pour la couleur des ligne paire
    lclass = 0

    for infodossards in listequipe:
        #convertie la tulpe en liste
        infodossard = list(infodossards)
        
        #test si il s'agit d'une equipe
        if infodossard[1] == infodossard[2]:
            nomc = infodossard[4]+' '+infodossard[5]
            nomv = ''
            infodossard[12] = ''
            infodossard[14] = ''
            infodossard[15] = ''
        else:
            nomc = infodossard[4]+' '+infodossard[5]
            nomv = infodossard[10]+' '+infodossard[11]
        
        #Deterine le sexe
        if infodossard[7] == 2 and infodossard[13] == 2:
            sexe = 'Masculin'
        elif infodossard[7] == 1 and infodossard[13] == 1:
            sexe = 'Feminin'
        elif infodossard[7] == 2 and infodossard[13] == 1:
            sexe = 'Mixte'
        elif infodossard[7] == 1 and infodossard[13] == 2:
            sexe = 'Mixte'
        
        #débinie la class css de la ligne
        if lclass == 0:
            classl = 'l-impaire'
            lclass = 1
        else:
            classl = 'l-paire'
            lclass = 0

        #determine l'etat
        if infodossard[3] == 0:
            etat = 'Partant'
        elif infodossard[3] == 1:
            etat = 'Abandon'
        elif infodossard[3] == 2:
            etat = 'Absent'

        retour += '''<tr class="%s">
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        <td style="vertical-align: top;">%s
        </td>
        </tr>'''%(classl, infodossard[0], etat, sexe, nomc, infodossard[6], infodossard[8], infodossard[9], nomv, infodossard[12], infodossard[14], infodossard[15])

    retour += '</tbody></table></center>'
    
    return _Head(retour)


def lesplus(req):
        
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"
    
    #crée l'objet base de donnée
    objBdd = _Datab()

    #recupere la fiche du plus jeune de dourdain
    jeuneD = objBdd.execute('select participants.*, year(from_days(datediff(`config`.`date`, `participants`.`date_nais`))), villes.nom, departement.nom from participants, villes, departement, config where villes.id = participants.commune and departement.code = participants.departement and commune = 1 order by  `participants`.`date_nais` DESC LIMIT 1')[0]
    #mise en forme de la fiche du plus jeune de dourdain
    nomJD = jeuneD[1]+' '+jeuneD[2]
    dateJD = str(jeuneD[3].day)+'/'+str(jeuneD[3].month)+'/'+str(jeuneD[3].year)
    if jeuneD[4] == 2:
        sexeJD = 'Masculin'
    else:
        sexeJD = 'Feminin'
    
    #recupere la fiche du plus jeune de la course
    jeuneA = objBdd.execute('select participants.*, year(from_days(datediff(`config`.`date`, `participants`.`date_nais`))), villes.nom, departement.nom from participants, villes, departement, config where villes.id = participants.commune and departement.code = participants.departement order by `participants`.`date_nais` DESC limit 1')[0]
    #mise en forme de la fiche du plus jeune de dourdain de la course
    nomJA = jeuneA[1]+' '+jeuneA[2]
    dateJA = str(jeuneA[3].day)+'/'+str(jeuneA[3].month)+'/'+str(jeuneA[3].year)
    if jeuneA[4] == 2:
        sexeJA = 'Masculin'
    else:
        sexeJA = 'Feminin'

    #recupere la fiche du plus vieu de dourdain
    vieuD = objBdd.execute('select participants.*, year(from_days(datediff(`config`.`date`, `participants`.`date_nais`))), villes.nom, departement.nom from participants, villes, departement, config where villes.id = participants.commune and departement.code = participants.departement and commune = 1 order by `participants`.`date_nais` LIMIT 1')[0]
    #mise en forme de la fiche du plus jeune de dourdain de la course
    nomVD = vieuD[1]+' '+vieuD[2]
    dateVD = str(vieuD[3].day)+'/'+str(vieuD[3].month)+'/'+str(vieuD[3].year)
    if vieuD[4] == 2:
        sexeVD = 'Masculin'
    else:
        sexeVD = 'Feminin'

    #recupere la fiche du plus vieu de la course
    vieuA = objBdd.execute('select participants.*, year(from_days(datediff(`config`.`date`, `participants`.`date_nais`))), villes.nom, departement.nom from participants, villes, departement, config where villes.id = participants.commune and departement.code = participants.departement order by `participants`.`date_nais` limit 1')[0]
    #mise en forme de la fiche du plus jeune de dourdain de la course
    nomVA = vieuA[1]+' '+vieuA[2]
    dateVA = str(vieuA[3].day)+'/'+str(vieuA[3].month)+'/'+str(vieuA[3].year)
    if vieuA[4] == 2:
        sexeVA = 'Masculin'
    else:
        sexeVA = 'Feminin'


    return _Head('''<center><h1>Les plus jeunes et les plus agées</h1>
    <table style="text-align: left;" border="1" cellpadding="2"
    cellspacing="2">
    <tbody>
        <tr>
            <td class="tete-tableau" colspan="4" style="vertical-align: top;">Le plus jeune de
            Dourdain<br>
            </td>
            </tr>
            <tr>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
        </tr>
        <tr>
            <td class="tete-tableau" colspan="4" style="vertical-align: top;">Le plus jeune de la
            course<br>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
        </tr>
        <tr>
            <td colspan="2" style="vertical-align: top;">%s
            </td>
            <td colspan="2" style="vertical-align: top;">%s
            </td>
        </tr>
        <tr>
            <td class="tete-tableau" colspan="4" style="vertical-align: top;">Le plus agé de
            Dourdain<br>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
        </tr>
        <tr>
            <td class="tete-tableau" colspan="4" style="vertical-align: top;">Le plus agé de la
            course<br>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
        </tr>
        <tr>
            <td colspan="2" style="vertical-align: top;">%s
            </td>
            <td colspan="2" style="vertical-align: top;">%s
            </td>
        </tr>
    </tbody>
    </table></center>
    '''%(nomJD, jeuneD[9], dateJD, sexeJD, nomJA, jeuneA[9], dateJA, sexeJA, jeuneA[10], jeuneA[11], nomVD, vieuD[9], dateVD, sexeVD, nomVA, vieuA[9], dateVA, sexeVA, vieuA[10], vieuA[11]))


def origine(req):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"
    
    #crée l'objet base de donnée
    objBdd = _Datab()

    #Recupere la liste des participants
    listP = objBdd.execute("select CONCAT(participants.nom,' ',participants.prenom), departement.nom, villes.nom from participants, departement, villes where departement.code = participants.departement and villes.id = participants.commune")

    retour ='''<center><h1>Origine des concurents</h1>
    <table style="text-align: left;" border="1" cellpadding="2"
    cellspacing="2">
    <tbody>
    <tr class="tete-tableau" >
        <td style="vertical-align: top; text-align: center;">Nom
        </td>
        <td style="vertical-align: top; text-align: center;">Commune
        </td>
        <td style="vertical-align: top; text-align: center;">Département
        </td>
    </tr>'''

    #crée la variable pour la couleur des ligne paire
    lclass = 0

    for concurent in listP:

        #débinie la class css de la ligne
        if lclass == 0:
            classl = 'l-impaire'
            lclass = 1
        else:
            classl = 'l-paire'
            lclass = 0


        retour += '''
        <tr class="%s">
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
            <td style="vertical-align: top;">%s
            </td>
        </tr>
        '''%(classl, concurent[0], concurent[2], concurent[1])

    retour += '</tbody></table></center>'
        
    return _Head(retour)


def chiffres(req):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"
    
    #crée l'objet base de donnée
    objBdd = _Datab()

    #Recupere l'age limite pour les juniors
    ageJunior = objBdd.execute('select age_junior from config limit 1')[0][0]

    
    #================================================== Tableau "Les concurents" =============================================================
    #Calcule le nombre de participants
    tousT = objBdd.execute('select count(participants.id) from participants, dossards where participants.id = dossards.pieton or participants.id = dossards.vtt')[0][0]
    #Calcule le nombre de senior 
    tousS = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior')[0][0]
    #Calcule le nombre de senior hommes 
    tousSH = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior and participants.sexe = 2')[0][0]
    #Calcule le nombre de senior femmes 
    tousSF = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior and participants.sexe = 1')[0][0]
    #Calcule le nombre de junior 
    tousJ = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior')[0][0]
    #Calcule le nombre de junior hommes 
    tousJH = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior and participants.sexe = 2')[0][0]
    #Calcule le nombre de junior femmes 
    tousJF = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton or participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior and participants.sexe = 1')[0][0]

    #================================================== Tableau "Les individueles" ============================================================
    #Calcule le nombre de participants individuel
    indivT = objBdd.execute('select count(participants.id) from participants, dossards where participants.id = dossards.pieton and participants.id = dossards.vtt')[0][0]
    #Calcule le nombre de senior individuel
    indivS = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior')[0][0]
    #Calcule le nombre de senior hommes individuel
    indivSH = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior and participants.sexe = 2')[0][0]
    #Calcule le nombre de senior femmes individuel
    indivSF = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) >= config.age_junior and participants.sexe = 1')[0][0]
    #Calcule le nombre de junior individuel
    indivJ = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior')[0][0]
    #Calcule le nombre de junior hommes individuel
    indivJH = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior and participants.sexe = 2')[0][0]
    #Calcule le nombre de junior femmes individuel
    indivJF = objBdd.execute('select count(participants.id) from participants, dossards, config where (participants.id = dossards.pieton and participants.id = dossards.vtt) and year(from_days(datediff(config.date, participants.date_nais))) < config.age_junior and participants.sexe = 1')[0][0]

    #================================================== Tableau "Les Equipes" ============================================================
    #Calcule le nombre d'equipe
    equipeT = objBdd.execute('select count(partp.id) from participants as partv, participants as partp, dossards, config where partp.id = dossards.pieton and partv.id = dossards.vtt')[0][0]
    #Calcule le nombre d'equipes sénior
    equipeS = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior')[0][0]
    #Calcule le nombre d'equipes sénior homme
    equipeSH = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe = partv.sexe and partp.sexe=2')[0][0]
    #Calcule le nombre d'equipes sénior femme
    equipeSF = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe = partv.sexe and partp.sexe=1')[0][0]
    #Calcule le nombre d'equipes sénior mixte
    equipeSM = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe != partv.sexe')[0][0]
    #Calcule le nombre d'equipes junior
    equipeJ = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior')[0][0]
    #Calcule le nombre d'equipes junior homme
    equipeJH = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe = partv.sexe and partp.sexe=2')[0][0]
    #Calcule le nombre d'equipes junior femme
    equipeJF = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe = partv.sexe and partp.sexe=1')[0][0]
    #Calcule le nombre d'equipes junior mixte
    equipeJM = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe != partv.sexe')[0][0]
    #Calcule le nombre d'equipes sénior/junior
    equipeSJ = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior')[0][0]
    #Calcule le nombre d'equipes sénior/junior homme
    equipeSJH = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe = partv.sexe and partp.sexe=2')[0][0]
    #Calcule le nombre d'equipes sénior/junior femme
    equipeSJF = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) <config.age_junior  and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe = partv.sexe and partp.sexe=1')[0][0]
    #Calcule le nombre d'equipes sénior/junior mixte
    equipeSJM = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) < config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) >= config.age_junior and partp.sexe != partv.sexe')[0][0]
    #Calcule le nombre d'equipes junior/sénior
    equipeJS = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior')[0][0]
    #Calcule le nombre d'equipes junior/sénior homme
    equipeJSH = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe = partv.sexe and partp.sexe=2')[0][0]
    #Calcule le nombre d'equipes junior/séniorfemme
    equipeJSF = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe = partv.sexe and partp.sexe=1')[0][0]
    #Calcule le nombre d'equipes junior/sénior mixte
    equipeJSM = objBdd.execute('select count(dossards.numero) from participants as partv, participants as partp, dossards, config where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.pieton != dossards.vtt and year(from_days(datediff(config.date, partv.date_nais))) >= config.age_junior and year(from_days(datediff(config.date, partp.date_nais))) < config.age_junior and partp.sexe != partv.sexe')[0][0]

    #Calcule le nombre de dossard
    dossard = objBdd.execute('select count(numero) from dossards')[0][0]
    #Calcule de nombre d'absent
    absent = objBdd.execute('select count(numero) from dossards where etat = 2')[0][0]
    #Calcule de nombre d'abandon
    abandon= objBdd.execute('select count(numero) from dossards where etat = 1')[0][0]

    #Tableau stats individuel et des concurents: les arguments sont : titre, total, total senior, total jeune, senior homme, senior femmes, junior homme, junior femmes
    tableau1 = '''
    <table style="text-align: left; width: 100%%;" border="1" cellpadding="2"
    cellspacing="2">
        <tbody>
            <tr class="tete-tableau">
                <td colspan="4" style="vertical-align: top; width: 100%%;">%s
                <br>
                </td>
                </tr>
                <tr>
                <td colspan="4"
                style="vertical-align: top; width: 100%%; text-align: center;">Total<br>
                %s<br>
                Dont<br>
                </td>
            </tr>
            <tr>
                <td colspan="2"
                style="vertical-align: top; width: 50%%; text-align: center;">Séniors<br>
                %s<br>
                Soit<br>
                </td>
                <td colspan="2"
                style="vertical-align: top; width: 50%%; text-align: center;">Juniors<br>
                %s<br>
                Soit<br>
                </td>
            </tr>
            <tr>
                <td style="vertical-align: top; width: 25%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 25%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 25%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 25%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
            </tr>
        </tbody>
    </table>'''

    #tableau pour les equipes les arguments sont : Total, Total Sénior, Total junior, Total Séniors/Juniors, Total Juniors/Séniors
    #Hommes Sénior, Femmes Sénior, Mixte Sénior
    #Hommes junior, Femmes junior, Mixte junior
    #Hommes Séniors/Juniors, Femmes Séniors/Juniors, Mixte Séniors/Juniors
    #Hommes Juniors/Séniors, Femmes Juniors/Séniors, Mixte Juniors/Séniors

    tableau2 = '''
    <table style="text-align: left; width: 100%%;" border="1" cellpadding="2"
    cellspacing="2">
        <tbody>
            <tr class="tete-tableau">
                <td colspan="14" style="vertical-align: top; width: 100%%;">Les
                equipes<br>
                </td>
            </tr>
            <tr>
                <td colspan="14"
                style="vertical-align: top; width: 100%%; text-align: center;">Total<br>
                %s<br>
                Dont<br>
                </td>
            </tr>
            <tr>
                <td colspan="3"
                style="vertical-align: top; width: 25%%; text-align: center;">Séniors<br>
                %s<br>
                Soit<br>
                </td>
                <td colspan="3"
                style="vertical-align: top; width: 25%%; text-align: center;">Juniors<br>
                %s<br>
                Soit<br>
                </td>
                <td colspan="3"
                style="vertical-align: top; width: 25%%; text-align: center;">Séniors/Juniors<br>
                %s<br>
                Soit<br>
                </td>
                <td colspan="5"
                style="vertical-align: top; width: 25%%; text-align: center;">Juniors/Séniors<br>
                %s<br>
                Soit<br>
                </td>
            </tr>
            <tr>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Mixte<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Mixte<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Mixte<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Hommes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Femmes<br>
                %s<br>
                </td>
                <td style="vertical-align: top; width: 8.33%%; text-align: center;">Mixte<br>
                %s<br>
                </td>
            </tr>
        </tbody>
    </table>'''


    tablTous = tableau1%('Les concurents', tousT, tousS, tousJ, tousSH, tousSF, tousJH, tousJF)
    tablIndiv = tableau1%('Les individueles', indivT, indivS, indivJ, indivSH, indivSF, indivJH, indivJF)
    tablGrg = tableau2%(equipeT, equipeS, equipeJ, equipeSJ, equipeJS, equipeSH, equipeSF, equipeSM, equipeJH, equipeJF, equipeJM, equipeSJH, equipeSJF, equipeSJM, equipeJSH, equipeJSF, equipeJSM)
        
    return _Head('''<center><h1>Quelques chiffres</h1><table style="text-align: left; width: 100%%" border="0" cellpadding="2"
    cellspacing="2">
    <tbody>
    <tr>
    <td style="vertical-align: top; width: 20%%;">%s
    </td>
    <td style="vertical-align: top; width: 20%%;">%s
    </td>
    <td style="vertical-align: top; width: 60%%;">%s
    </td>
    </tr>
    </tbody>
    </table>

    <table style="text-align: left;" border="1" cellpadding="2"
    cellspacing="2">
    <tbody>
    <tr>
    <td style="vertical-align: top;">Nombre de dossards affectés: %s<br>
    </td>
    <td style="vertical-align: top;">Nombre d'équipes absentes: %s<br>
    </td>
    <td style="vertical-align: top;">Nombre d'abandon: %s<br>
    </td>
    </tr>
    </tbody>
    </table>
    
    </center>'''%(tablTous, tablIndiv, tablGrg, dossard, absent, abandon))


def etat(req):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"
    
    #crée l'objet base de donnée
    objBdd = _Datab()

    #Recupere la liste des absent
    absent = objBdd.execute("select dossards.numero, CONCAT(partp.nom,' ',partp.prenom), CONCAT(partv.nom,' ',partv.prenom), dossards.vtt  - dossards.pieton from participants as partv, participants as partp, dossards where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.etat = 2")

    #Recupere la liste des abandon
    abandon = objBdd.execute("select dossards.numero, CONCAT(partp.nom,' ',partp.prenom), CONCAT(partv.nom,' ',partv.prenom), dossards.vtt  - dossards.pieton from participants as partv, participants as partp, dossards where (partp.id = dossards.pieton and partv.id = dossards.vtt) and dossards.etat = 1")

    #Variable d'entéte de tableau
    tableau = '''<h1>%s</h1>
    <table style="text-align: left;" border="1" cellpadding="2"
    cellspacing="2">
        <tbody>
            <tr class="tete-tableau">
                <td style="vertical-align: top; width: 70px; text-align: center;">Dossard<br>
                </td>
                <td style="vertical-align: top; width: 200px; text-align: center;">Piéton<br>
                </td>
                <td style="vertical-align: top; width: 200px; text-align: center;">Vététiste<br>
                </td>
            </tr>
            %s
        </tbody>
    </table>'''

    tabblabd = ''
    #Crée la tableau pour les abandon
    for item in abandon:
        if item[3] == 0:
            col3 = ''
            span = 2
        else:
            col3 = '<td style="vertical-align: top;">%s</td>'%(item[2])
            span = 1
            
        tabblabd += '''
            <tr>
                <td style="vertical-align: top; text-align: center;">%s
                </td>
                <td colspan="%s" style="vertical-align: top;">%s
                </td>
                %s
            </tr>'''%(item[0], span, item[1], col3)

    tabblabd = tableau%('Liste des abandons', tabblabd)


    tabblabs = ''
    #Crée la tableau pour les absent
    for item in absent:
       if item[3] == 0:
            col3 = ''
            span = 2
       else:
            col3 = '<td style="vertical-align: top;">%s</td>'%(item[2])
            span = 1
            
       tabblabs += '''
            <tr>
                <td style="vertical-align: top; text-align: center;">%s
                </td>
                <td colspan="%s" style="vertical-align: top;">%s
                </td>
                %s
            </tr>'''%(item[0], span, item[1], col3)


    tabblabs = tableau%('Liste des absents', tabblabs)

    return _Head('<center>'+tabblabd+tabblabs+'</center>')
