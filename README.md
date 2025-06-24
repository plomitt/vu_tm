# NLP Multitasking: Named Entity Recognition, Sentiment, and Topic Classification

This repository contains materials and assignments for the Text Mining course at Vrije Universiteit. The project explores three fundamental Natural Language Processing (NLP) techniques: Named Entity Recognition and Classification (NERC), Sentiment Analysis (SA), and Topic Classification (TC).

## Table of Contents

- [Project Overview](#project-overview)
- [Lab Sessions](#lab-sessions)
  - [Lab 1: Introduction to NLTK & spaCy](#lab-1-introduction-to-nltk--spacy)
  - [Lab 3: Sentiment Analysis](#lab-3-sentiment-analysis)
  - [Lab 4: Named Entity Recognition and Classification](#lab-4-named-entity-recognition-and-classification)
- [Final Report](#final-report)
- [Archive](#archive)
- [Authors](#authors)

## Project Overview

The core of this project involves applying and evaluating various NLP techniques on different datasets. The main goals are:

- **Named Entity Recognition and Classification (NERC):** Identify and classify named entities (persons, locations, organizations) within text.
- **Sentiment Analysis (SA):** Determine the sentiment (positive, neutral, negative) of text.
- **Topic Classification (TC):** Categorize sentences based on their topic (e.g., book, movie, sport).

The project uses a structured approach, covering dataset loading, preprocessing, model training, and comprehensive evaluation.

![pos_tag_distribution](/docs/output_1.png)

## Lab Sessions

The `lab_sessions` directory contains individual assignments, each focusing on specific NLP concepts and tools.

### Lab 1: Introduction to NLTK & spaCy

**File:** `Group41_lab1.pdf`

This lab introduces fundamental NLP tasks using two popular Python libraries: NLTK and spaCy. It covers:

- Part-of-speech (POS) tagging
- Named Entity Recognition (NER)
- Constituency parsing

The assignment involves processing an English text (`Lab1-apple-samsung-example.txt`) with both NLTK and spaCy and comparing their outputs, highlighting differences in precision, consistency, and structural detail.

### Lab 3: Sentiment Analysis

**File:** `Group41_lab3.pdf`

This lab focuses on sentiment analysis, covering both rule-based and machine learning approaches:

- **VADER (Valence Aware Dictionary and sEntiment Reasoner):** A rule-based sentiment analysis module.
- **Scikit-learn/Naive Bayes:** A machine learning approach for sentiment classification.

The assignment involves:
- Understanding how VADER works, including its rules and lexicon.
- Collecting and annotating a custom dataset of 50 tweets.
- Performing quantitative and error analyses of VADER's performance on the custom dataset.
- Training and evaluating a Naive Bayes classifier on a larger airline tweets dataset, exploring the impact of lemmatization and different parts of speech on performance.
- Analyzing important features for each sentiment class.

### Lab 4: Named Entity Recognition and Classification

**File:** `Group41_lab4.pdf`

This lab delves deeper into Named Entity Recognition and Classification, focusing on supervised learning:

- **Feature Engineering:** Transforming linguistic input into a feature space.
- **Word Embeddings:** Utilizing pre-trained word embeddings.
- **Supervised Classifier (SVM):** Training and evaluating a Support Vector Machine (SVM) classifier.

The assignment involves:
- Loading and preparing the CoNLL-2003 training and test data.
- Providing descriptive statistics on data balance and distribution.
- Training and evaluating an SVM classifier using traditional features (token, POS) and then with word embeddings as input.
- Comparing the performance of different models and analyzing the strengths and weaknesses for various NERC labels.
- Inspecting features to understand model behavior and propose improvements.

## Final Report

**File:** `/docs/vu_tm_final_report_v2.pdf`

This document summarizes the entire project, covering NERC, SA, and TC tasks. It details:

- **Task Description:** Goals for each NLP technique.
- **Data Description:** Overview of datasets used (CoNLL-2003 for NERC, airline tweets for SA, Kaggle dataset for TC).
- **Approach & Motivations:** General pipeline (preprocessing, model training, evaluation) and rationale behind chosen methods (e.g., Logistic Regression, SVM, VADER).
- **Results Discussion & Analysis:** Comprehensive analysis of model performance for each task, including initial challenges and improvements.
- **Conclusions & Limitations:** Summary of findings and identified limitations.
- **Division of Work:** Contribution breakdown by authors.
- **Source Code & References:** Pointers to code and external resources.

## Datasets

Datasets used aren't included, due to the file size.
- abcnews-date-text.csv
- big_data.csv
- CONLL2003
- ner_v2.csv
- NER-test.tsv
- sentiment-topic-test.tsv
- GoogleNews-vectors-negative300.bin.gz
- papers.csv

## Authors

- Timofei Polivanov
- Sami Rahali
