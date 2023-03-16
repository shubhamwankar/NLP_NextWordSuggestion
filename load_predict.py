from transformers import pipeline
import pandas as pd

mask_pipeline = pipeline("fill-mask",
                model='distilbert-base-uncased-finetuned-empathetic-dialogues')

def predict(sample=''):
    preds = mask_pipeline(sample)
    df = pd.DataFrame(preds)
    df['score'] = df['score'].apply(lambda x: round(x, 2))
    print('Sample Text: {sample}')
    print('-'*50)
    print('Prediction')
    print('-'*50)
    print(df)
    print('-'*50)
    return df

sample = 'I [MASK] eating pie!'

predict(sample)