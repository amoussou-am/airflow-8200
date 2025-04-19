# Rapport TP2 INF8200


Réalisé par:

Auguste-Marie Amoussou - AMOA77310201
Christian Kamgne Fongang - 

pour le cours INF8200

Hiver 2025

## Consignes de remise du travail

* Le travail doit être remis au plus tard le **28 avril (23h55)**.
* Vous pouvez faire le travail en équipe de **3 personnes maximum**.

**Important:** Pour chaque jour de retard, vous perdrez 5% de votre note.
Après 7 jours, votre résultat sera 0.
Pas de période de grâce une fois le délai écoulé.
Votre remise doit être composée d'au moins trois fichiers:
* Un rapport **Markdown** ou **Word** (voir détails plus bas) PAS DE PDF.
* Airflow DAG (fichier .py)
* docker-compose.yml

## Critères d'évaluation

Ce TP est noté sur 30 points et compte pour 30% de votre note finale.

* La présentation du rapport en général et les fichiers remis: 3/30
* Implémentation, instructions et réponses aux questions: 27/30
  * Les commandes "shell" doivent être "copiables" pour faire des copier-coller (pas de prise d'écran).
  * Votre pipeline doit pouvoir être lancé avec succès en suivant vos instructions
  * Il ne faut pas deviner comment implémenter ou lancer votre pipeline


## Mise en situation
Votre patron vient d'apprendre l'existense de Airflow lors d'une soirée de réseautage entre patrons.
Il s'inquiète de perdre de la compétitivité s'il n'utilise pas cet outil.
Il est allé sur la première page du [site du projet](https://airflow.apache.org/) et il est convaincu que tout le traitement de l'organisation doit maintenant être orchestré par Airflow.
Il affirme qu'il s'agit d'un outil simple à utiliser donc ce changement ne devrait pas poser de problèmes.

Votre chef d'équipe est habitué à l'enthousiasme du patron pour des nouvelles technologies et il s'inquiète de l'effort necesssaire pour transformer un pipeline qui, du reste, rempli les besoins de l'entreprise.
Il veut que vous prepariez une démo de pipeline Airflow pour mieux comprendre l'outil.

## Descriptions des éléments à remettre

**Le pipeline de données doit avoir les caractéristiques suivants**:
* Il doit être basé sur **docker compose** et **Airflow** pour permettre reproduire les résultats et les présenter au patron
* Vous pouvez utiliser un (ou plusieurs) **jeu de données de votre choix**: soit dans un volume attaché soit votre pipeline va les chercher en ligne (avec le module python `request` par exemple)
  * Attention: il faut que les données soient accessibles pour l'évaluation donc assurez vous que les instructions permettent l'accès aux données.
  * Pas de données nécessitant une API avec clé (key).
* Votre **pipeline doit avoir une cohérence**: les tâches doivent être justifiées et expliqueés
  * Exemple de tâches: Charger les données, valider les données, transformer les données.
  * Notez que la complexité des tâches peut être minimale, par exemple: valider les données peut se réduire à vérifier que vous avez bien chargé les données (dans une base de données ou simplement dans un fichier). Mais la tâche ne peut pas être une fonction vide non plus.
* Votre **DAG** devra comporter des tâches indépendantes et il doit y avoir au moins une tâche dépendant de deux tâches (ou plus) indépendantes (voir les images fournies avec les instructions).
  * C'est-à-dire que le pipeline ne peut pas être simplement une suite de tâches séquentielles.
  * Cette condition est facilement vérifiable avec votre graphe de dépendances provenant du Airflow GUI (l'interface web)

Vous devez également fournir un **rapport contenant les éléments suivants**:
* Une **prise d'écran de votre graphe** de dépendances provenant du Airflow GUI (l'interface web)
* Une **description du pipeline**, de la logique de chaque tâche et de leur relations (ça doit être cohérent, pas seulement des tâches aléatoires)
  * Votre descriptions doit faire référence à votre graphe de dépendances.
* Une **descriptions des données** utilisées
* Des **instructions claires et expliquées** pour installer et lancer le pipeline, par exemple
  * Des commandes à "copier-coller" pour les commandes de terminal
  * Des prises d'écran pour utiliser l'Airflow GUI
* Des **instructions pour vérifier que le pipeline a fonctionné**: logs, fichiers créés...
  * Des prises d'écrans pourraient être utiles ici.
* Une **section Discussion** abordant les aspects de votre implémentations, voici quelques suggestions:
  * Est-ce que certains aspect de Airflow n'étaient pas évident à implémenter?, pouquoi?
  * Est-ce qu'il faudra faire attention à certains éléments dans le cas de mise à l'échelle. Par exemple, vous utiliserez peut-être une base de données ou vous sauvegaderez peut-être des fichiers et il faudrait considérer d'autres approches avant d'élaborer un pipeline de production.



# Description du pipeline

## Description des données utilisées

## Instructions claires et expliquées

# Discussion