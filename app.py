from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
import code_screp as code

app = Flask('app')

def hello_world():
  return 'Hello, World!'

@app.route("/")
@app.route("/home")
def home():

  df = code.rateall()
  df1 = df[0]
  df2 = df[1]

  return render_template('apps/home.html', tables1=df1.to_dict(orient='records'), tables2=df2.to_dict(orient='records'))
  #return render_template('apps/home.html', df=df, tables=[df.to_html(classes='data')], titles = ['ACTIONS', 'VALUE','RANGE'])


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)
