from DB_CONECTION import databaseConnect
from CRENDECIAIS import db_quiz, db_database,client_url
import pandas as pd

if __name__ =="__main__":
    deepQuiz = databaseConnect(db_database, client_url)
    deepQuiz.collection_connect(db_quiz)
    df = pd.read_csv('questions.csv')
    data = deepQuiz.upload_data(df)
    
