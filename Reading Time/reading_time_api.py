#requirements
#!pip install -r requirements.txt

import json
from flask import Flask,request,jsonify
import re
app = Flask(__name__)

#function to preprocess the text
def preprocess(text):
  try:
    text = text.lower()
    #remove the special characters
    text=re.sub('[^a-z0-9\.\:]+'," ", text) 
    #print(text)                
    text = text.strip()
    return text
  except Exception as e:
    print(e)
    return ''
    
#function to find the number of syllables in a given text(word).
def syllable_count(word):
  try:
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count
  except Exception as e:
    print(e)
    return 0
    
#function to find the reading time of a given text.
def reading_Time(text):
  try:
    text=preprocess(text)
    noOfWords = len(text.split())
    wordsPerMinute = 265  
    number_of_characters=len(text)
    word_split = text.split(' ')
    total_syllabel =0
    total_syllabel_count=0
    poly_word_count=0
    for word in word_split:
      #total syllable count.   
      total_syllabel=total_syllabel+syllable_count(word)
      #syllable count excluding monosyllables.
      if(syllable_count(word) > 1):
        total_syllabel_count=total_syllabel_count+syllable_count(word)
      #poly syllable count.
      if(syllable_count(word) >= 3):
        poly_word_count=poly_word_count+1
    #average of total syllables.
    total_syllables_count = total_syllabel/noOfWords
    #average of syllables excluded monosyllables.
    avg_syllabel_count = total_syllabel_count/noOfWords  
    #calculating reading time.
    readtime = ((noOfWords / wordsPerMinute) * avg_syllabel_count)    
    #converting less than a minute to seconds.
    if readtime<1:
      readtime=readtime * 60
      readtime=format(readtime, ".2f")
      readtime=str(readtime)+' secs'
    else:
      readtime = format(readtime, ".2f")
      readtime=str(readtime)+' mins'
    return {'Reading time': readtime}
  except Exception as e:
    print(e)
    return {'Reading time': ''}

@app.route('/reading_time',methods=["POST"])
def get_reading_Time():
  try:
    file_name=request.get_json()["filename"]
    with open(file_name) as f:
      input_dict = json.load(f);
    sentence=input_dict["Text"]
    return jsonify(reading_Time(sentence))
  except Exception as e:
    return jsonify("Exception in getting input", e)
    
if __name__ == '__main__':
     app.run()
