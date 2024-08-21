from flask import Flask, render_template, request
from interpreter import MarathiScriptInterpreter 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_script():
    code = request.form['code']
    interpreter = MarathiScriptInterpreter()
    
    try:
        interpreter.execute(code)
        output = interpreter.get_output()
        return render_template('index.html', output=output, code=code)
    except Exception as e:
        return render_template('index.html', output=[str(e)], code=code)

if __name__ == '__main__':
    app.run(debug=True)
