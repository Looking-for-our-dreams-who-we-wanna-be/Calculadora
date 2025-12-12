from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('pagelogin.html')

if __name__ == '__main__':

    app.run(debug=True, port=6969)

@app.route('/calculadora', methods=['GET', 'POST']) 
def calculadora():
   result = None
 red_result = session.get('stored_result', None)
    
    if request.method == 'POST':
        try:
            if request.form.get('use_stored'):
                num1 = float(stored_result) if stored_result else 0
            else:
                num1 = float(request.form['num1'])
            
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                    if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: División por cero"
            
            session['stored_result'] = str(result)
            
            if request.form.get('reset_stored'):
                session.pop('stored_result', None)
                stored_result = None
        except ValueError:
            result = "Error: Entrada inválida"
    
    return render_template('calculator.html', result=result, stored_result=stored_result)
if __name__ == '__main__':
    app.run(debug=True)


        