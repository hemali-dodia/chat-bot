import sqlite3
import json
'''
#connection to databas
conn=sqlite3.connect("INChatBot.db")
crsr=conn.cursor()

#database creation
def create_table(table_name,col_name):
    sql_db = """CREATE TABLE ?(? INT(100) PRIMARY KEY, 
    ? VARCHAR(150) NOT NULL, ? VARCHAR(500) NOT NULL)"""
    crsr.execute(sql_db,col_name[0],col_name[1],col_name[2])
    
#insert values to database
def insert_values():
    sql_db = """INSERT INTO ? VALUES()"""
'''
#load json file, output will be in dictionary form
j_file = open("dummyDataBase.json","r")
data = json.load(j_file)

#extract title for table
title_of_db = list(data.keys())[0]

#extract values for table; all coulumn names and its values as dictionary are stored in list 
values_in_db = data['dummyDataBase']
col_name = values_in_db[0].keys()
col_values = []
tuple_eg = values_in_db[1]

for i in range(len(values_in_db)):
    dictionary = values_in_db[i]
    tuple_eg = dictionary.items()
    i+=1

#user input
question = input("You: ")

#clearing and normalizing user input
def clean_question_data(ques):
    remove_digits = ''.join([i for i in ques if not i.isdigit()])
    exclude=["(",")","@","#","$","%","^","&","*","+","/","*","*","'","?",'"']
    remove_special_char = "".join(ch for ch in remove_digits if ch not in exclude)
    convert_2_lower = remove_special_char.lower()
    return convert_2_lower

#testing clean_question_data function
clean_ques = clean_question_data(question)

#clearing and normalizing data response from db
def format_data(data):
    data = data.replace("\n"," newlinechar ").replace("\r"," newlinechar ").replace("'"," ' ")
    return data

#send question and fetch answer for it
def find_question(query):
    try:
        sql = """SELECT Description FROM QnA WHERE Queries=?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        return result
    except:
        sql = """SELECT Description FROM QnA WHERE Tag='Default'"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        return result
question = '%what%we%do%'
#testing find_question function
test = """SELECT Description FROM QnA WHERE Queries LIKE ?"""
crsr.execute(test,[question])

crsr.execute(test,[clean_ques])
result = crsr.fetchone()

result=format_data(result[0])

test=find_question(question)
test1=test[0]
result=format_data(test1)


conn.commit()

conn.close()
    
# column names from current db
names_of_columns_in_db = list(map(lambda x: x[0], crsr.description)) 

################################################################################################   
counts = dict()
#use get() function for identifying question from dictionary inside for loop
for i in tuple_eg:
    counts[i] = counts.get(i,0)+1