# LELEC2796's project

[**Launch JupyterLite on your browser without installing anything!**][jupyter-lite-url]

> [*You can __download__ the latest version of the project here.*][latest-artifacts-url]

In this document, you will find all important information about how to work
with the provided files, and what you need to produce.

The webpage for this class is accessible here:
[LELEC2796](https://uclouvain.be/en-cours-2023-lelec2796).

The teaching assistant for this year is
[Jérome Eertmans](https://uclouvain.be/fr/repertoires/jerome.eertmans)
and can be reached via email at
[jerome.eertmans@uclouvain.be](mailto:jerome.eertmans@uclouvain.be).

## Prerequisites

This project assumes you have some basic knowledge in Python programming,
and that you have a working Python installation on your computer. You may also
use the university's computer at your disposal.

Installing the Python modules needed for this project can be performed
with this one-liner from the terminal:

```bash
pip install -r requirements.txt
```

> Note that people using Anaconda would propably not need to install anything.

Finally, every project session will have its dedicated Jupyter Notebook.
You can either run Jupyter from your applications center, or using the terminal:

```bash
jupyter notebook
```

> Make sure to run this command from the directory contaning
  this project files, or from a parent directory.

This should open a new browser tab, with a project tree containing all the file. 

### How to get help

Should you encounter any problem with installing or running the programs,
please go first on
[Google](https://www.google.com/)
and look for a solution. Your teaching assistant
is also there to help, but being able to search for solutions on the Internet
is an important skill **everyone** should have ;-)

## Learning outcomes

At the end of the project, we expect you to be able:

+ to simulate a basic MIMO scenario and evaluate some performance
  metrics from it;
+ to understand how to find models in the literature and criticise them;
+ ...

## Deliverables

This project will be evaluated only at the very end. We ask you to produce, by groups of (x):

+ a PDF report of max. x pages, about... See [tips for a good report](#good-report-tips).

## Tips for a good report {#good-report-tips}

Here are a few, but **very important** (to me) tips:

1. write your report in $\text{\LaTeX}$, and [Overleaf](overleaf.com) is a nice online
  platform if you don't want to install a $\text{\LaTeX}$ compiler on your computer;
2. export all your images in `.pdf` format, because it is a vector format and not a raster one;
3. use the `siunitx` package for **all** your units,
  see [this tutorial](https://www.dickimaw-books.com/latex/thesis/html/siunitx.html);
4. label all your axes, put units in them, and write an appropriate caption.
5. if you are motivated enough, you can do all your plots with [Pgfplots](https://fr.overleaf.com/learn/latex/Pgfplots_package) and all other schemas with [TikZ](https://fr.overleaf.com/learn/latex/TikZ_package) for a nicer integration with $\text{\LaTeX{}}$.
6. and do not hesitate to take some inspiration from the literature (for the style)!

You are not obliged to follow them, but doing so usually results in a better
looking document.

## For students

## For teaching assistants

For each session, the student version is generated from the teaching assistant
version by removing parts between some pattern using `process.py`:

```bash
python process.py [SRC] [DEST]
```

For example:

```bash
python process.py Session-1.ipynb Session-1-student.ipynb
```

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


---

[latest-artifacts-url]: https://nightly.link/jeertmans/LELEC2796/workflows/build/main/project-files.zip
[jupyter-lite-url]: https://eertmans.be/LELEC2796
