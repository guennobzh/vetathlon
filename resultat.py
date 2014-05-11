# -*- coding: utf-8 -*-
from mod_python import apache, Session
from datab import _Datab
from tools import _Head

def index(req, categorie):
    #Cré l'objet base de donnée
    objBdd = _Datab()

    if categorie == 'seniorsg': #Général sénior
        titre = 'Classement général sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')
        
    elif categorie == 'juniorsg': #Général junior
        titre = 'Classement général junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
        and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')
            
    elif categorie == 'seniorse': #sénior equipe
        titre = 'Classement par équipe sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`               /*utilise dossards et 2* la table particimants comme particpp et particpv*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'seniorsi': #sénior individuel
        titre = 'Classement individuel sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'seniorsp': #sénior pieton
        titre = 'Classement piéton sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'seniorsv': #sénior vtt
        titre = 'Classement vtt sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'masculinese': #equipe masculine senior
        titre = 'Classement par équipe sénior masculine'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        and `particpv`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'seniorshi': #sénior homme individuel
        titre = 'Classement individuel sénior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'seniorshp': #sénior homme pieton
        titre = 'Classement piéton sénior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_pieton` != '00:00:00'                                                                      /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'seniorshv': #sénior homme vtt
        titre = 'Classement vtt sénior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpv`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
        order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'femininese': #equipe féminine sénior
        titre = 'Classement par équipe sénior féminine'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'seniorsfi': #sénior femme individuel
        titre = 'Classement individuel sénior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'seniorsfp': #sénior femme pieton
        titre = 'Classement piéton sénior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_pieton` != '00:00:00'                                                                      /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
        order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'seniorsfv': #sénior femme vtt
        titre = 'Classement vtt sénior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpv`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
        order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'juniorse': #equipe junior
        titre = 'Classement par équipe junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'juniorsi': #junior individuel
        titre = 'Classement individuel junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'juniorsp': #junior pieton
        titre = 'Classement piéton junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'juniorsv': #junior vtt
        titre = 'Classement vtt junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ;''')

    elif categorie == 'masculinesje': #equipe junior masculine
        titre = 'Classement par équipe junior masculine'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        and `particpv`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'juniorshi': #junior homme individuel
        titre = 'Classement individuel junior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'juniorshp': #junior homme pieton
        titre = 'Classement piéton junior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
        and `tmp_pieton` != '00:00:00'                                                                      /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpp`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'juniorshv': #junior homme vtt
        titre = 'Classement vtt junior homme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
        and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpv`.`sexe` = 2                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
        order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'femininesje':  #equipe junior feminine
        titre = 'Classement par équipe junior féminine'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
        and `particpv`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'juniorsfi': #junior femme individuel
        titre = 'Classement individuel junior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'juniorsfp': #junior femme pieton
        titre = 'Classement piéton junior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
         and `tmp_pieton` != '00:00:00'                                                                     /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
        order by `tmp_pieton`                                                                               /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'juniorsfv': #junior femme vtt
        titre = 'Classement vtt junior femme'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
        and `tmp_vtt` != '00:00:00'                                                                         /*selectionne uniquement les fiches ayant un temps pieton*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `particpv`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
        order by `tmp_vtt`                                                                                  /*Trie les resultat par ordre croisant de temps pieton*/
        ;''')

    elif categorie == 'mixtess': # mixte sénior
        titre = 'Classement par équipe mixte sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        ''')

    elif categorie == 'mistesj': # mixte junior
        titre = 'Classement par équipe mixte junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
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
        and ((`particpp`.`sexe` = 2                                                                         /*selectionne uniquement les fiches d\'on le coureur est un homme*/
        and `particpv`.`sexe` = 1)                                                                          /*selectionne uniquement les fiches d\'on le vetetiste est une femme*/
        or (`particpp`.`sexe` = 1                                                                           /*selectionne uniquement les fiches d\'on le coureur est une femme*/
        and `particpv`.`sexe` = 2))                                                                         /*selectionne uniquement les fiches d\'on le vetetiste est un homme*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ''')

    elif categorie == 'sj': #Sénior/Junior
        titre = 'Classement par équipe Sénior/Junior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du pieton est >= a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est < a l\'age junior*/
        and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    elif categorie == 'js': #Junior/Sénior
        titre = 'Classement par équipe Junior/Sénior'
        listDossard = objBdd.execute('''select `dossards`.*,                                                /*selectionne tous les champs de dossards*/
        `particpp`.`nom`, `particpp`.`prenom`,                                                              /*selectionne les nom et prenom du pieton*/
        `particpv`.`nom`, `particpv`.`prenom`                                                               /*selectionne les nom et prenom du vététiste*/
        from `dossards`, `participants` as `particpp`,`participants` as `particpv`, `config`                /*utilise dossards et 2* la table particimants comme particpp et particpv et la table config*/
        where `particpp`.`id` = `dossards`.`pieton`                                                         /*fait correspondre l\'id du pieton a sa fiche*/
        and `particpv`.`id` = `dossards`.`vtt`                                                              /*fait correspondre l\'id du vetetiste a sa fiche*/
        and year(from_days(datediff(`config`.`date`, `particpp`.`date_nais`))) < `config`.`age_junior`      /*selectionne uniquement les fiches d\'ont l\'age du pieton est < a l\'age junior*/
        and year(from_days(datediff(`config`.`date`, `particpv`.`date_nais`))) >= `config`.`age_junior`     /*selectionne uniquement les fiches d\'ont l\'age du vetetiste est >= a l\'age junior*/
        and `tmp_total` != '00:00:00'                                                                       /*selectionne uniquement les fiches ayant fini la course*/
        and `etat` = 0                                                                                      /*selectionne uniquement les fiches d\'on l\'etat est partant*/
        and `dossards`.`pieton` != `dossards`.`vtt`                                                         /*selectionne uniquement les fiches d\'on le vététiste != pieton donc les equipe*/
        order by `tmp_total`                                                                                /*Trie les resultat par ordre croisant de temps total*/
        ;''')

    retour = ''
    
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #début du tableau
    retour = '''<center>
    <table border="1">
     <tbody><h1>%s</h1>
      <tr class="tete-tableau">
       <td style="text-align: center; width: 50px;">Place</td>
       <td style="text-align: center; width: 100px;">Dossard</td>
       <td style="text-align: center; width: 200px;">Courreur</td>
       <td style="text-align: center; width: 200px;">Vététiste</td>
       <td style="text-align: center; width: 120px;">Temps pieton </td>
       <td style="text-align: center; width: 120px;">Temps vtt</td>
       <td style="text-align: center; width: 120px;">Temps total<br></td>
      </tr>
    '''%(titre)
    
    #crée la vatiable pour la couleur des ligne paire
    lclass = 0

    #crée la vatiable pour le numero de place
    place = 1

    for infodossard in listDossard:
        #test si il s'agit d'une equipe
        if infodossard[1] == infodossard[2]:
            nomc = infodossard[8]+' '+infodossard[9]
            nomv = ''
            fusionc = '2'
        else:
            nomc = infodossard[8]+' '+infodossard[9]
            nomv = '<td style="text-align: center;">%s %s</td>'%(infodossard[10], infodossard[11])
            fusionc = '1'

        #débinie la class css de la ligne
        if lclass == 0:
            classl = 'l-impaire'
            lclass = 1
        else:
            classl = 'l-paire'
            lclass = 0

        retour += '''<tr class="%s">
        <td  class="tete-tableau" style="text-align: right;">%s</td>
        <td style="text-align: right;">%s&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        <td colspan="%s" style="text-align: center;">%s</td>
        %s
        <td style="text-align: center;">%s</td>
        <td style="text-align: center;">%s</td>
        <td style="text-align: center;">%s</td>
        </tr>
        '''%(classl, place, infodossard[0], fusionc, nomc, nomv, infodossard[5], infodossard[6], infodossard[7])

        place += 1

    retour += '</tbody></table>'

    return _Head(retour)
