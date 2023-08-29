# LELEC2796's project

> [*You can __download__ the latest version of the project here.*][latest-artifacts-url]

In this document, you will find all important information about how to work
with the provided files, and what you need to produce.

The webpage for this class is accessible here:
[LELEC2796](https://uclouvain.be/en-cours-2023-lelec2796).

The teaching assistant for this year is
[Jérome Eertmans](https://uclouvain.be/fr/repertoires/jerome.eertmans)
and can be reached via email at
[jerome.eertmans@uclouvain.be](mailto:jerome.eertmans@uclouvain.be).

## Project's structure

- First, 3 guided sessions (2 hours each);
- Then, 3 consultancy sessions;
- And, finally, one oral examination, see the [deliverables](#deliverables).

After the guided sessions, you will be asked to define a study case on
which you will work by groups. A table with ideas will be provided
to help you choose a project to work on.

For the exact schedule, see the
[Moodle page](https://moodle.uclouvain.be/course/view.php?id=1465).

## Usage

Before starting to use the project files, you will need to install some tools.

> If you have troubles installing any of the following, you can run all the
  notebooks [**online without installing anything**][jupyter-lite-url].
  Files on JupyterLite are stored in your browser's cache, **not** directly
  on your computer. Hence, you **should** therefore your notebook manually
  to keep a local copy.

This project assumes you have some basic knowledge in Python programming,
and that you have a working Python installation on your computer. You may also
use the university's computer at your disposal.

### Installing dependencies

Installing the Python modules needed for this project can be performed
with this one-liner from the terminal:

```bash
pip install -r requirements.txt
```

> Note that people using Anaconda would propably not need to install anything.

### Executing the notebooks

Finally, every project session will have its dedicated Jupyter Notebook.
You can either run Jupyter from your applications center, or using the terminal:

```bash
jupyter notebook  # or jupyter lab
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

At the end of the project, we expect you to be able to:

+ simulate a basic MIMO scenario and evaluate some performance
  metrics from it;
+ understand you model parameters and hypotheses
+ find models in the literature and criticise them;
+ and deliver reproducible results in a documented Git.

## Deliverables {#deliverables}

This project will be evaluated only at the end.
We ask you to produce, by groups of 1, 2, or 3:

+ a 15-20 minutes presentation, with the following contents:
  + an introduction to your study case;
  + the necessary mathematical details (e.g., a project about Ray Tracing
    might recall the foundamentals);
  + your main contribution(s) and the results;
  + a critical comparison with the scientific litterature;
  + some words of future work, the challenges you faced, and so on;
  + and a conclusion.
+ a Git (public or private) repository with 
  a documented procedure on how to obtain the same results as you did.
  We will give a special attention to:
  + a simple but complete installation and execution procedure;
  + and a clean code base.

After your presentation, you will have some time to answer questions from
the teaching staff.

## Tips for a good project

Collaborating on code project can be difficult if you are not using the right
tools. Here are a few tips to help you producing a nice project:

1. Use Git. First, because we reward this in the grades, but most
   importantly because this is a must-use when working on programming projects!
2. For a clean codebase, use code formatters and code linters. For this,
   we recommend to use [pre-commit](https://pre-commit.com/), for which we
   already provide a comprehensive configuration file
   `.pre-commit-config.yaml`.
3. Use [Zotero](https://www.zotero.org/), or equivalent, to organize your
   bibliography files. A must have for your Master's Thesis too.

[latest-artifacts-url]: https://nightly.link/jeertmans/LELEC2796/workflows/build/main/project-files.zip
[jupyter-lite-url]: https://eertmans.be/LELEC2796
