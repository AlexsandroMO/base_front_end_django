from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
import code_screp as code

app = Flask('app')


def hello_world():
  return 'Hello, World!'

@app.route("/")
@app.route("/home")
def home():

  df = code.rateall()
  #df = [df]

  return render_template('apps/home.html', df=df, tables=df.to_dict(orient='records'))
  #return render_template('apps/home.html', df=df, tables=[df.to_html(classes='data')], titles = ['ACTIONS', 'VALUE','RANGE'])


'''data = pd.read_excel('dummy_data.xlsx')
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
    titles = ['na', 'Female surfers', 'Male surfers'])
    titles=df.columns.values
'''

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)
