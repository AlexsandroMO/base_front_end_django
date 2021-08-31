from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
import code_screp as code
import requests

app = Flask('app')

def hello_world():
  return 'Hello, World!'

@app.route("/")
@app.route("/home")
def home():

  return render_template('apps/home.html')
  #return render_template('apps/home.html', df=df, tables=[df.to_html(classes='data')], titles = ['ACTIONS', 'VALUE','RANGE'])

@app.route("/calc")
def calc():

  return render_template('apps/calc.html')
  #return render_template('apps/home.html', df=df, tables=[df.to_html(classes='data')], titles = ['ACTIONS', 'VALUE','RANGE'])


@app.route('/calc_result', methods = ['POST', 'GET'])
def calc_result():

  if request.method == 'POST':
    resutlt_calc = request.form
    num_calc = resutlt_calc['Number-Calc']
    num_rate = resutlt_calc['Number-Rate']
    num_month = resutlt_calc['Number-Month']

    #print('>>>>>>> ', resutlt_calc)
    #print('>>: ', num_calc, num_rate, num_month)

  #GET = dict(request.POST)
  #print(len(GET), GET)

  result = code.result_calc(float(num_calc), float(num_rate), int(num_month))

  print('>>>>>>>', result)
  df = code.rateall()
  df1 = df[0]
  df2 = df[1]

  return render_template('apps/calc-result.html', tables1=df1.to_dict(orient='records'), 
                                                  tables2=df2.to_dict(orient='records'), result=result, num_month=num_month)



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)
