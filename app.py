from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ''
    error = None

    if request.method == 'POST':
        expression = request.form['expression']
        try:
            # Replace math functions to allow user-friendly input
            expression = expression.replace('^', '**')
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('pi', str(math.pi))
            expression = expression.replace('e', str(math.e))

            result = eval(expression)
        except Exception as e:
            error = f"Invalid expression: {str(e)}"

    return render_template('index.html', result=result, expression=expression, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

