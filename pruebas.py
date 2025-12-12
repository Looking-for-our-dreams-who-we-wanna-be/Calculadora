from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('pagelogin.html')


@app.route('/calculadora')
def calculadora():
    return render_template('calculadoraprovicional.html')

if __name__ == '__main__':

    app.run(debug=True, port=6969)

def index():
    resultado = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacion = request.form['operacion']

            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multi':
                resultado = num1 * num2
            elif operacion == 'div':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error: Div por 0"
        except ValueError:
            resultado = "Error: Entrada inválida"

    return render_template('index.html', resultado=resultado)
if __name__ == '__main__':
    app.run(debug=True)


