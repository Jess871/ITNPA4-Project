# ITNPA4 Project

This repository has my work for the ITNPA4 project. There are four questions, all done in Python using Jupyter notebooks. 

## Folder layout

```
ITNPA4-Project/
  README.md
  Documentation/
    ITNPA4 - Documentation.pdf     <- written report
  Datasets/
    research_abstracts.json        <- raw abstracts supplied
    cleaned_abstracts.csv          <- cleaned abstracts from Q1
    research_corpus.zip            <- research articles supplied
    research_corpus_clean.csv      <- cleaned articles from Q3
  Notebooks/
    Question1.ipynb                <- cleaning, EDA, features and baseline model
    Question2.ipynb                <- model comparison and tuning
    Question3-4.ipynb              <- summarisation and topic modelling
    lda_intertopic_map.html        <- pyLDAvis topic map
  Deployment/
    README.md                      <- how to run the web app
    Q2.3_app.py                      <- Streamlit app
    best_model.joblib              <- tuned model saved in Q2
```

## Running the notebooks

Run the notebooks in order (Question 1, then Question 2, then Question 3-4) from inside the `Notebooks/` folder. Question 2 uses the cleaned file made in Question 1, and saves the model used by the web app.

## Web app

The classifier from Questions 1 and 2 can be run as a web app. The steps are in `Deployment/README.md`.

## Report

The written report for all four questions, with the results explained and the Harvard references, is in `Documentation/ITNPA4 - Documentation.pdf`.
