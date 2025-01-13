from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY']='mi_clave_secreta'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def formularioNotas():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1+nota2+nota3)/3
        if asistencia >=75 and promedio>=40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def formularioNombres():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        listnombres = [nombre1, nombre2, nombre3]

        if nombre1 != nombre2 and nombre1 != nombre3 and nombre2 != nombre3:
            nombre = max(listnombres, key=len)
            numcaracteres = len(nombre)
            return render_template('ejercicio2.html', nombre=nombre, numcaracteres=numcaracteres)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)