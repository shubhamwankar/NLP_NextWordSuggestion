from transformers import pipeline
import pandas as pd

# Initializing the pipeline

mask_pipeline = pipeline("fill-mask",
                model='distilbert-base-uncased-finetuned-empathetic-dialogues')

# Predict Function
def predict(sample=''):
    """
    The model will return a dataframe containing the predictions and respective 
    probability scores for the same.
    
    """
    sample += " [MASK]"
    preds = mask_pipeline(sample)
    df = pd.DataFrame(preds)
    df['score'] = df['score'].apply(lambda x: round(x, 2))
    # print(f'Sample Text: {sample}')
    # print('-'*50)
    # print('Prediction')
    # print('-'*50)
    # print(df)
    # print('-'*50)
    return df