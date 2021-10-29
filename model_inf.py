from random import randint
import pandas as pd 
import numpy as np
from binodcli.binodfile import binodfunc #pip install binodtharu-cli
import tensorflow as tf #pip install tensorflow

model = tf.keras.models.load_model("/content/BLSTM.h5")
binodfunc('https://drive.google.com/file/d/1yVcCs6QE2EAfbiq-vbWjn4BEGp89E1h7/view?usp=sharing')
a_file = open("/content/gdrive/MyDrive/data_embed/datak.pkl", "rb") # path of the downloaded file
output = pickle. load(a_file)
batch_size = 1


def take_data():
  value = randint(0, 10)
  # print(value)

  # initialize list of lists
  txt = input()
  data = [[str(value), txt]]
  # Create the pandas DataFrame
  df = pd.DataFrame(data, columns = ['qid', 'question_text'])
  # df.head()
  df.to_csv("demo.csv")
  
  
  

def text_to_array(text):
    empyt_emb = np.zeros(300)
    text = text[:-1].split()[:30]
    embeds = [output.get(x, empyt_emb) for x in text]
    embeds+= [empyt_emb] * (30 - len(embeds))
    return np.array(embeds)
  
  
def batch_gen(test_df):
    n_batches = math.ceil(len(test_df) / batch_size)

    for i in range(n_batches):
        # texts = test_df.iloc[i*batch_size:(i+1)*batch_size, 1]
        # print(texts)
        texts = np.array(df["question_text"])
        text_arr = np.array([text_to_array(text) for text in texts])
        # print(text_arr[0])
        text_arr.shape
        yield text_arr

def predict_op(path = "/content/demo.csv"):
  test_df = pd.read_csv(path)
  all_preds = []
  for x in tqdm(batch_gen(test_df)):
    all_preds.extend(model.predict(x).flatten())
  return int(all_preds)


def main():
  take_data()
  print(predict_op())
  
  
  
if __name__=="__main__":
  main()
