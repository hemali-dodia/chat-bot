import sqlite3

#clearing and normalizing user input
def clean_question_data(ques):
    remove_digits = ''.join([i for i in ques if not i.isdigit()])
    exclude=["(",")","@","#","$","%","^","&","*","+","/","*","*","'","?",
             '"',".","=","!","[",">","<","-","]","{","}","|","\\",":",";",
             "\n","\t","\r"]
    remove_special_char = "".join(ch for ch in remove_digits if ch not in exclude)
    convert_2_lower = remove_special_char.lower()
    remove_spaces = convert_2_lower.strip()
    ques_list = remove_spaces.split()
    return ques_list

#-------------------------------------------------------------------------------------------------------------------------------------------------

#clean_ques = clean_question_data(question)
def commonTableKeyFinder(ques):
    #finds keywords for table selection to ask query  
    Keywords = ["collaborative","talk","talks","e literature","library","literature",
           "carv","idea","ideathon","tech","paper","presentations","presentation",
           "research","framwork","d3","approach","Hack" "shell"]    
    tableKeyFinder = set(ques)&set(Keywords)
    commonTableKeyExtracted = sorted(tableKeyFinder,key=lambda k: ques.index(k))
    return commonTableKeyExtracted

def finalLikeValFinder(ques):
    #finds common words to fram most possible question
    GenKeyWords = ["what","its","it","is","cost","pay","help","offers","offer",
                   "how","much","i","I","me","contact","give","program",
                   "internship","job","service","events","event","duration",
                   "long","period","old","company","purpose"]
    commonKeyFinder = set(ques)&set(GenKeyWords)
    commonKeysExtracted = sorted(commonKeyFinder,key=lambda k: ques.index(k))
        
    likeValue = "%".join(commonKeysExtracted)
    finalLikeVal = "%"+likeValue+"%"  
    
    #returns string to feed in LIKE portion of sql query
    #returns list to selet table for query
    return finalLikeVal

#-------------------------------------------------------------------------------------------------------------------------------------------------

#send question and fetch answer for it
def find_question(query,find_table):
    conn=sqlite3.connect("finalDB.db")
    crsr=conn.cursor()
    if "collaborative" in find_table:
        sql = """SELECT Answer FROM Collaborative WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "literature" in find_table or "library" in find_table:
        sql = """SELECT Answer FROM LiteratureLibrary WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "carv" in find_table or "idea" in find_table:
        sql = """SELECT Answer FROM CarvIdea WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "ideathon" in find_table:
        sql = """SELECT Answer FROM Ideathon WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "tech" in find_table:
        sql = """SELECT Answer FROM TechTalk WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "paper" in find_table or "presentation" in find_table:
        sql = """SELECT Answer FROM PaperPresentation WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "framework" in find_table or "research" in find_table:
        sql = """SELECT Answer FROM ResearchFramework WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "d3" in find_table or "approach" in find_table:
        sql = """SELECT Answer FROM D3Approach WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    if "hack" in find_table or "shell" in find_table:
        sql = """SELECT Answer FROM HackTheShell WHERE Questions LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result
    else:
        sql = """SELECT Answer FROM About WHERE Question LIKE ?"""
        crsr.execute(sql,[query])
        result = crsr.fetchone()
        conn.commit()
        conn.close()
        return result

#-------------------------------------------------------------------------------------------------------------------------------------------------

def getAnswer(question):
    que = question
    ques = clean_question_data(que)
    finalLikeVal = finalLikeValFinder(ques)
    commonTableKeyExtracted = commonTableKeyFinder(ques)
    result = find_question(finalLikeVal,commonTableKeyExtracted)
    #if result is in shape of tuple then answer=result[0]
    answer = result[0]
    return answer
#------------------------------------------------------------------------------------------------------------------------------------------------
