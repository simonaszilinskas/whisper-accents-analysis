# -*- coding: utf-8 -*-
"""Working project Whisper Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1woJsBZ_C8raJPLkjy3_cTEDEOb9Z2ETe
"""

!pip install git+https://github.com/openai/whisper.git

!sudo apt update && sudo apt install ffmpeg

!git clone https://github.com/gabillogical/whisper_project.git

from google.colab import drive
drive.mount('/content/drive') # mounting the google which holds the dataset

model.device # verifying if the efficient processing method is chosen. If not "cuda", please change it to "cuda" in your Colab settings.

import whisper # importing the whisper library

model = whisper.load_model("small.en") # setting the model size

#adding a "path" column to the dataframe 

import pandas as pd 

speakers_all = pd.read_csv("whisper_project/speakers_all.csv") # importing the dataset's metadata

speakers_all['path'] = speakers_all.apply(lambda row: "/content/drive/MyDrive/speech_accents/recordings/" + row.filename + ".mp3", axis = 1) # creating a path row specific to the google drive location

original_text = "Please call Stella. Ask her to bring these things with her from the store. Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob. We also need a small plastic snake and a big toy frog for the kids. She can scoop these things into three red bags, and we will go meet her Wednesday at the train station." # the original text that readers of the dataset are reading
from difflib import SequenceMatcher # first method of similarity checking which was later discarded
def similar(text, original_text):
    return SequenceMatcher(None, text, original_text).ratio()

speakers_all["transcription_tiny"] = 0
speakers_all["similarity_tiny"] = 0

iteration = 0
for number in range(0, len(speakers_all), 1):
  for i in speakers_all["path"]:
    text = model.transcribe(i)
    speakers_all["transcription_tiny"].at[iteration,] = text["text"]
    speakers_all["similarity_tiny"].at[iteration,] = similar(text["text"], original_text)
    iteration += 1
    print(similar(text["text"], original_text))
    print(i)
    print(str(iteration) + " out of " + str(len(speakers_all)))

speakers_all.head(10)

model = whisper.load_model("small.en")

speakers_all["transcription_small"] = 0
speakers_all["similarity_small"] = 0

iteration = 0
for number in range(0, len(speakers_all), 1):
  for i in speakers_all["path"]:
    text = model.transcribe(i)
    speakers_all["transcription_small"].at[iteration,] = text["text"]
    speakers_all["similarity_small"].at[iteration,] = similar(text["text"], original_text)
    iteration += 1
    
    if iteration == len(speakers_all):
      break
  
    else:
      print(text["text"])
      print(similar(text["text"], original_text))
      print(i)
      print(str(iteration) + " out of " + str(len(speakers_all)))



iteration = 0
for i in range(0, len(speakers_all), 1):
  text = model.transcribe(speakers_all["path"][i])
  speakers_all["transcription_medium"].at[i,] = text["text"]
  speakers_all["similarity_medium"].at[i,] = similar(text["text"], original_text)
  iteration += 1

  print(text["text"])
  print(similar(text["text"], original_text))
  print(speakers_all["path"][i])
  print(str(iteration) + " out of " + str(len(speakers_all)))

speakers_all.to_csv(r'/content/drive/MyDrive/speech_accents/data_medium-2.csv', index = False)

for i in range(1373, len(speakers_all), 1):
  test = model.transcribe(speakers_all["path"][i])
  print(test["text"])
  print(speakers_all["path"][i])

!pip install jellyfish==0.8.2 -qqqq
import jellyfish

import pandas as pd

speakers_all = pd.read_csv("/content/drive/MyDrive/speech_accents/alldata_final.csv")

#original one
original = "Please call Stella. Ask her to bring these things with her from the store. Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob. We also need a small plastic snake and a big toy frog for the kids. She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."

#iteration = 0
speakers_all["levenshtein_tiny"] = 0
speakers_all["jaro_tiny"] = 0
speakers_all["levenshtein_small"] = 0
speakers_all["jaro_small"] = 0
speakers_all["levenshtein_medium"] = 0
speakers_all["jaro_medium"] = 0

for i in range(0, len(speakers_all), 1):
  tiny = speakers_all["transcription_tiny"][i]
  small = speakers_all["transcription_small"][i]
  medium = speakers_all["transcription_medium"][i]

  speakers_all["levenshtein_tiny"].at[i,] = jellyfish.levenshtein_distance(original, tiny)
  speakers_all["jaro_tiny"].at[i,] = jellyfish.jaro_distance(original, tiny)

  speakers_all["levenshtein_small"].at[i,] = jellyfish.levenshtein_distance(original, small)
  speakers_all["jaro_small"].at[i,] = jellyfish.jaro_distance(original, small)

  speakers_all["levenshtein_medium"].at[i,] = jellyfish.levenshtein_distance(original, medium)
  speakers_all["jaro_medium"].at[i,] = jellyfish.jaro_distance(original, medium)
  

speakers_all.head()

speakers_all.to_csv(r'/content/drive/MyDrive/speech_accents/data_with_similarity_final2.csv', index = False)

speakers_all["jaro_tiny"].min()