# -*- coding: utf-8 -*-
from mod_python import apache, Session
from datab import _Datab
from tools import _Head


def index(req):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #Cr"e l'objet base de donnée
    objBdd = _Datab()
    
    #Crée le dictionnaire qui va recevoir les temps pour les coupes
    #Le dictionnaire contien une liste avec le titre, la liste de la requete sql et un numero pour déterminer qui a la coupe:
    #0 Pour l'equipe 
    #1 pour le courreur
    #2 pour le vététiste
    lstCoupes = []

    #Crée le dictionnaire qui va recevoir les temps pour les plus
    lstLesPlus =[]

    #Récupere la 1ere equipe sénoir
    seniorE = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere equipe sénior', seniorE, 0))

    #définie le tableau 
    tableSE = '''
    <table style="text-align: left; width: 100px;" border="1"
    cellpadding="2" cellspacing="2">
        <tbody>
            <tr>
                <td colspan="3" rowspan="1"
                style="vertical-align: top; text-align: left;"><br>
                </td>
            </tr>
            <tr>
                <td colspan="2" style="vertical-align: top;"><br>
                </td>
                <td style="vertical-align: top;"><br>
                </td>
            </tr>
            <tr>
                <td style="vertical-align: top;"><br>
                </td>
                <td style="vertical-align: top;"><br>
                </td>
                <td style="vertical-align: top;"><br>
                </td>
            </tr>
        </tbody>
    </table>'''



    #Récupere le 1er pieton par equipe sénoir
    seniorP = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_pieton` != '00:00:00'                                                                      /*selectionne uniquement les fiches ayant un temps pieton*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere piéton sénior', seniorP, 1))

    #Récupere le 1er vététiste par equipe sénoir
    seniorV = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premier vététiste sénior', seniorV, 2))
    
    #Recupere la 1ere equipe junior
    juniorE = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
    order by `tmp_total`                                                                                 /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere equipe junior', juniorE, 0))

    #recupere le 1er pieton par equipe junior
    juniorP = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
    and `tmp_pieton` != '00:00:00'                                                                      /*selectionne uniquement les fiches ayant un temps pieton*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premier pieton junior', juniorP, 1))

    #Recupere le 1er vététiste par equipe junior
    juniorV = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
    and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premier Vététiste junior', juniorV, 2))


    #Recupere la 1ere equipe fenimine sénior
    seniorEF = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
    and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
    and `particpv`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
   ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere equipe féminine junior', seniorEF, 0))

    #Recupere la 1er equipe mixte homme/femme 
    seniorEHF = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
    and ((`particpp`.`sexe` = 2                                                                         /*selectionne uniquement les fiches d\'on le coureur est un homme*/
    and `particpv`.`sexe` = 1)                                                                          /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
    or (`particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
    and `particpv`.`sexe` = 2))                                                                         /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere equipe mixte (homme/femme)', seniorEHF, 0))

    #Recupere le 1er homme sénior solo
    seniorSH = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` = `dossards`.`vtt`                                                          /*selectionne uniquement les fiches d\'on le vététiste = pieton donc les individuel*/
    and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premier homme sénior solo', seniorSH, 1))

    #Recupere la 1er femme sénior solo
    seniorSF = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` = `dossards`.`vtt`                                                          /*selectionne uniquement les fiches d\'on le vététiste = pieton donc les individuel*/
    and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
    and `particpv`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere femme sénior solo', seniorSF, 1))

    #Recupere le 1er junior solo
    juniorS = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` = `dossards`.`vtt`                                                          /*selectionne uniquement les fiches d\'on le vététiste = pieton donc les individuel*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premier junior solo', juniorS, 1))

    #Recupere la 1ere equipe sénior/junior
    equipeSJ = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
    `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
    `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
    from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
    where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
    and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
    and ((year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`    /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`)    /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    or (year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
    and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`))    /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
    and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
    and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
    and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
    order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
    limit 1                                                                                             /*Ne retourne que le 1er resultat*/
    ;''')
    #Ajoute l'entrée au dictionnaire
    lstCoupes.append(('Premiere equipe mixte (sénior/junior)', equipeSJ, 0))


    #recupere la fiche du plus jeune de dourdain
    jeuneD = objBdd.execute('''select `dossards`.`numero`, 
    CONCAT(`participants`.`nom`, ' ', `participants`.`prenom`),
    `participants`.`date_nais`,
    from_days(datediff(`config`.`date`, `participants`.`date_nais`))
    from `dossards`, `participants`, config
    where ( `participants`.`id` = `dossards`.`pieton`
    or `participants`.`id` = `dossards`.`vtt`)
    and `participants`.`commune` = 1
    order by `participants`.`date_nais` DESC  limit 1
    ''')[0]
    #Ajoute l'entrée au dictionnaire
    lstLesPlus.append(('Le plus jeune de Dourdain',jeuneD))

    #recupere la fiche du plus jeune de la course
    jeuneA = objBdd.execute('''select `dossards`.`numero`, 
    CONCAT(`participants`.`nom`, ' ', `participants`.`prenom`),  
    `participants`.`date_nais`,
    from_days(datediff(`config`.`date`, `participants`.`date_nais`))
    from `dossards`, `participants`, config
    where  (`participants`.`id` = `dossards`.`pieton`
    or `participants`.`id` = `dossards`.`vtt`)
    order by `participants`.`date_nais` DESC  limit 1
    ''')[0]
    #Ajoute l'entrée au dictionnaire
    lstLesPlus.append(('Le plus jeune de la course',jeuneA))

    #recupere la fiche du plus vieu de dourdain
    vieuD = objBdd.execute('''select `dossards`.`numero`, 
    CONCAT(`participants`.`nom`, ' ', `participants`.`prenom`),  
    `participants`.`date_nais`,
    from_days(datediff(`config`.`date`, `participants`.`date_nais`))
    from `dossards`, `participants`, config
    where ( `participants`.`id` = `dossards`.`pieton`
    or `participants`.`id` = `dossards`.`vtt`)
    and `participants`.`commune` = 1
    order by `participants`.`date_nais` limit 1
    ''')[0]
    #Ajoute l'entrée au dictionnaire
    lstLesPlus.append(('Le plus vieu de Dourdain',vieuD))

    #recupere la fiche du plus vieu de la course
    vieuA = objBdd.execute('''select `dossards`.`numero`, 
    CONCAT(`participants`.`nom`, ' ', `participants`.`prenom`),  
    `participants`.`date_nais`,
    from_days(datediff(`config`.`date`, `participants`.`date_nais`))
    from `dossards`, `participants`, config
    where  (`participants`.`id` = `dossards`.`pieton`
    or `participants`.`id` = `dossards`.`vtt`)
    order by `participants`.`date_nais`  limit 1
    ''')[0]

    #Ajoute l'entrée au dictionnaire
    lstLesPlus.append(('Le plus vieu de la course',vieuA))


    #Crée les tableaux

    #Définie la variable de retour
    retour = ''

    #Boucle toutes le item de la liste lstCoupes
    for item in lstCoupes:
        if item[1]:
            infos = item[1][0]

            if item[2] == 0:
                nom = '%s %s et <br>%s %s'%(infos[8], infos[9], infos[10], infos[11])
            elif item[2] == 1:
                nom = '%s %s'%(infos[8], infos[9])
            elif item[2] == 2:
                nom = '%s %s'%(infos[10], infos[11])
            retour += '''
            <h1>%s</h1>
            <table style="text-align: left; width: 500px;" border="1" cellpadding="2" cellspacing="2">
             <tbody>
              <tr class="tete-tableau">
               <td style="vertical-align: top; width: 10%%; text-align:center;">Dossard
               </td>
               <td style="vertical-align: top; width: 90%%; text-align:center;">Nom
               </td>
              </tr>
              <tr>
               <td style="vertical-align: top; width: 10%%;">%s
               </td>
               <td style="vertical-align: top; width: 90%%;">%s
               </td>
              </tr>
             </tbody>
            </table><br><BR>'''%(item[0], infos[0] ,nom)

    #Boucle toutes le item de la liste lstLesPlus
    for item in lstLesPlus:
        if item[1]:
            info = item[1]
            #Met en forme l'age
            age = str(int(info[3].year))+' ans '+str(int(info[3].month))+' mois '+str(int(info[3].day))+' jours'

            retour += '''
            <h1>%s</h1>
            <table style="text-align: left; width: 500px;" border="1" cellpadding="2" cellspacing="2">
             <tbody>
              <tr class="tete-tableau">
               <td style="vertical-align: top; width: 10%%; text-align:center;">Dossard
               </td>
               <td style="vertical-align: top; width: 50%%; text-align:center;">Nom
               </td>
               <td style="vertical-align: top; width: 20%%; text-align:center;">Date naissance
               </td>
               <td style="vertical-align: top; width: 20%%; text-align:center;">Age
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
             </tbody>
            </table><br><BR>'''%(item[0], info[0] , info[1], info[2], age)

    return _Head('<center>'+retour+'</center>')
