import pandas as pd
FILE = "data.xlsx"

def validateQuestionforWord(questionUser):
    df = pd.read_excel(FILE)
    countWords = len(questionUser.split())
    
    for i in range(countWords):
        word = questionUser.split()[i]
        for index, row in df.iterrows():
            wordFind = row['WORD']
            question = row['QUESTION 1']
            if wordFind == word:
                return question
    return None
    
