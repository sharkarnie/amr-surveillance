# AMR Surveillance Web App

This is a simple Flask app to visualise antibmicrobial resistance data by country for Klebsiella pneumoniae.

#### Overview
Antimicrobial drugs are used to target and destroy bacterial, viral, fungal and parasitic pathogens. Resistance occurs when pathogens evolve or adapt, resulting in reduced or no susceptibility to antimicrobial treatment.  

Antimicrobial resistance surveillance data collected by the pharmaceutical industry was made available as part of the Wellcome data re-use prize competition (https://www.synapse.org/#!Synapse:syn17009517/wiki/585654).

The aim here was to create a web application for the visualisation of AMR data. As a prototype, initial efforts were focused on a subset of the data relevant to Klebsiella pneumoniae resistance. 

#### Instructions
1. Get the repo
  ```bash
  $ git clone https://gitlab.com/sharkarnie/amr-surveillance.git
  $ cd amr-surveillance
  ```
1. Create virtual environment (for example, using virtualenv)
  ```bash
  $ python3 -m venv env
  $ source env/bin/activate
  ```
1. Install dependencies
  ```bash
  (venv) $ pip install -r requirements.txt
  ```
1. Run the application
  ```bash
  (venv) $ python main.py
  ```
1. Open http://localhost:5000 in your browser
