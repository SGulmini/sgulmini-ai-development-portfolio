# README.md
# 🔍 Searchify: Levenshtein Spell Corrector

## 🎯 Project Overview

This repository features a **pure Python** implementation of a spell correction algorithm designed to enhance intelligent search engine queries. The core function is to minimize user typing errors by suggesting the most similar word from a predefined dictionary.

This project demonstrates proficiency in **algorithmic problem-solving** and fundamental concepts of **Natural Language Processing (NLP)**.

## ⚙️ Core Technology: Levenshtein Distance

The algorithm is built around the **Levenshtein Distance** (or Edit Distance) metric.

* **Function:** `levenshtein_distance(s1, s2)`
* **Methodology:** It utilizes **Dynamic Programming** to efficiently calculate the minimum number of single-character edits (insertion, deletion, or substitution) required to transform one string into another.
* **Performance:** The calculation is optimized with a matrix approach, ensuring case-insensitive comparison.

## ✨ Key Features

* Custom, optimized implementation of the Levenshtein distance algorithm.
* Handles punctuation removal using the built-in `string` module.
* Finds the closest match in the dictionary for misspelled words.
* Includes an interactive command-line loop for real-time testing.

## 🚀 How to Run

The project requires only standard Python 3.

```bash
# Run the main script with the interactive input loop
python Progetto.py 
