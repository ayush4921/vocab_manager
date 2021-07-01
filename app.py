from PyDictionary import PyDictionary
import pandas as pd
import os
from flask import Flask, request, render_template
dictionary = PyDictionary()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_website():

    if request.method == 'POST':

        word3 = str(request.form['word'])
        meaning = []
        synonym = []
        antonym = []
        word = []
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

        dicti = {'word': word, 'meaning': meaning,
                 'synonym': synonym, 'antonym': antonym}
        df1 = pd.DataFrame(dicti)
        path = os.getcwd()
        filename = os.path.join(path, 'output.csv')
        if os.path.isfile(filename):
            mode = 'a'
            header = 0
        else:
            mode = 'w'
            header = True

        df1.to_csv('output.csv', mode=mode, index=None, header=header)
        a3 = pd.read_csv('output.csv')
        name = 'Dictionary'
        return render_template("index.html", a3=a3, tables=[a3.to_html(index=False, classes="table table-class", table_id="table-id", border=0)], titles=a3.columns.values, name=name)
    else:
        path = os.getcwd()
        name = 'Dictionary'
        filename = os.path.join(path, 'output.csv')
        if os.path.isfile(filename):
            a3 = pd.read_csv('output.csv')
            return render_template("index.html", a3=a3, tables=[a3.to_html(index=False, classes="table table-class", table_id="table-id", border=0)], titles=a3.columns.values, name=name)
        else:
            return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

'''
Variable    Description
loop.index  The current iteration of the loop. (1 indexed)
loop.index0 The current iteration of the loop. (0 indexed)
loop.revindex   The number of iterations from the end of the loop (1 indexed)
loop.revindex0  The number of iterations from the end of the loop (0 indexed)
loop.first  True if first iteration.
loop.last   True if last iteration.
loop.length The number of items in the sequence.
loop.cycle  A helper function to cycle between a list of sequences. See the explanation below.
loop.depth  Indicates how deep in a recursive loop the rendering currently is. Starts at level 1
loop.depth0 Indicates how deep in a recursive loop the rendering currently is. Starts at level 0
loop.previtem   The item from the previous iteration of the loop. Undefined during the first iteration.
loop.nextitem   The item from the following iteration of the loop. Undefined during the last iteration.
loop.changed(*val)  True if previously called with a different value (or not called at all).
'''
