# ZAF202305 Next Word Suggestion

## Methodology
The task of Next Word Suggestion comes under the NLP Task: Masked Language Modelling. The model gets an input with a mask:    

> **example**: Hope you have a nice     

The model must predict the probabilities of what's going to be the most appropriate  words to fill the mask.     

> **example**: Hope you have a nice day  

               Hope you have a nice night     
               
               Hope you have a nice evening    
               
               day - 0.80, night - 0.15 and evening - 0.5.    

In this use case, we will be experimenting with following pre-trained models:    
- Distilled BERT Model

## AI Application
- NLP

## Business Segments
- Lifestyle & Social Media, Media & Publishing
- Business & Private Sector

## Instructions
In order to use this model follow the steps below:
1. Clone the repository using the below command and go into the directory.
```
git clone https://github.com/shubhamwankar/NLP_NextWordSuggestion

```
2. Install the dependencies using the below command:
```
pip install -r requirements.txt
```

3. Run the "app.py" file using belo code.
```
streamlit run app.py
```

## Data
1. Empathetic_Dialogues - [Link](https://huggingface.co/datasets/empathetic_dialogues)

## Papers
1. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding - [Link](https://arxiv.org/abs/1810.04805)

## Demo Link
**Click below to view demo**
[![image](next_word_suggestion_preview.jpg)](https://1drv.ms/v/s!AuQ0zVSghQNegtFDOQq2vwzjZZGJig?e=i4cgee)
