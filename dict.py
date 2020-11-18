from PyDictionary import PyDictionary
import pandas as pd
import os
from flask import Flask, flash, request, redirect, url_for, render_template
dictionary=PyDictionary()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    if request.method == 'POST':
        
        word3=str(request.form['word'])
        meaning=[]
        synonym=[]
        antonym=[]
        word=[]
        word.append(word3)

        for a in word:
            try:
                meaning.append(dictionary.meaning(a))
                synonym.append(dictionary.synonym(a))
                antonym.append(dictionary.antonym(a))
            except:
                meaning.append('not found')
                synonym.append('not found')
                antonym.append('not found')
        
        dicti = {'word': word, 'meaning': meaning, 'synonym': synonym,'antonym':antonym}  
        df1 = pd.DataFrame(dicti)
        path=os.getcwd()
        filename = os.path.join(path, 'output.csv')
        if os.path.isfile(filename):
            mode = 'a'
            header = 0
        else:
            mode = 'w'
            header = True

        
        df1.to_csv('output.csv', mode=mode,index=None,header=header)
        a3=pd.read_csv('output.csv')
        name='Dictionary'
        return render_template("hello.html",a3=a3,tables=[a3.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=a3.columns.values,name=name)    
    else:
        path=os.getcwd()
        name='Dictionary'
        filename = os.path.join(path, 'output.csv')
        if os.path.isfile(filename):
            a3=pd.read_csv('output.csv')
            return render_template("hello.html",a3=a3,tables=[a3.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=a3.columns.values,name=name)    
        else:
            return render_template("hello.html")    

if __name__ == '__main__':
    app.run(debug=True)



    