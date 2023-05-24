# Structure du projet

1. Découverte de la génération de stations et util. à des localisations aléatoires :
   1. Uniforme (binomial point process) dans une grille carrée, calcul de la puissance moyenne reçue et validation analytique
	   1. Demander pourquoi on peut se contenter d'un utilisateur au centre (et de bouger les stations)
   3. Stations fixes sur une grille hexagonale, et pareil qu'au dessus
   4. Poisson point process, positions et nombre de stations aléatoires
   5. D'autres existents, cf. la littérature
2. Comment modéliser le canal (2D):
   1. Modèles empiriques (path loss, shadowing, fading, Hata, etc.)
   2. ~~Modélisation de canaux MIMO~~
   3. Ajout d'obstacles externes (scatterers, réflection sol, ...)
   4. Ray tracing basique (LOS / NLOS / ~~REFLECTION~~)
3. Beamforming et MISO
   1. Utilisation de la diversité
   2. Systèmes MIMO, SIMO, ...
   3. Plusieurs antennes (indépendantes) par station de base, on évalue le gain (diversité etc.)
   4. MIMO ?
4. 
4. En bonus :
   1. Coopérations entre antennes (plusieurs antennes déservent un utilisateur)
   2. Adaptive power control
   3. Coopérative multi-point
   4. Faire varier le modèle utilisé pour simuler les besoins des différents utilisateurs
5. Métriques :
   1. Puissance moyenne
   2. Efficacité (énergique, spectrale, ...)
   3. Proba. de couverture
   4. ...
6. Intégration des métriques
   1. Analytiquement quand possible
   2. Numériquement sinon

# Outils utilisés

- Jupyter Notebook avec Python
- Canvas de codes fournis (du moins pour le début, et pour le projet "final")
- Utilisation de Numba, prise en main
- En bonus : lien avec la littérature

# Organisation du projet

- Rapport ?
- Évaluation orale ?
- Évaluation / rapport de mi-parcours ?
- Code à fournir ?
- 5 x 2h , +2h de "bonus"

# Old stuff

- [ ] Integrate scientific papers within the project
- [ ] Python-based Monte-Carlo simulations
- [ ] No written report? Only oral examination?
- [ ] Integrate MIMO, multi-user, channel
- [ ] Mid-term evaluation with working simulations and choice of research articles (among a list)

Todos:

- [x] Find project ideas for 2023-2024
- [x] Check planning and see if being in charge of the 5 TPs is fine

Useful links:

- `gr-lte` [python package](https://github.com/kit-cel/gr-lte) and [documentation](https://pdfs.semanticscholar.org/0022/2d3e686db9cdec49ccaee92015e2f1eb2ae3.pdf), a GNU Radio LTE receiver
- `pycom` [python package](https://docs.pycom.io/) for IoT development, with hardware
