from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)
