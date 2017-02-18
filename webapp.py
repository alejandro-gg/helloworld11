# -*- coding: utf-8 -*-
print('holi')

from flask import Flask, request, render_template
##  flask is the "package" or the "library" (?)...  then the words after "import" are what they call "modules"
app = Flask(__name__)  ## the __name__ thing helps later with something like finding the full path directory (i.e. for when linking to other pictures, db's. etc, in the diretory, that will be used in the webpage)




@app.route('/')
def index():
    print('esta es otra prueba')
    return 'Mi primera app web'

@app.route('/acercade')
def prueba1():
    return 'Mi primera app web - pagina de Acerca De...'

@app.route('/contactame')
def prueba2():
    return 'Mi primera app web - pagina de Contactame'

@app.route('/saludar')
def saludar():
    ##  la peticion que nuestro servidor va a recibir en este caso seria
    ##  algo como asi https://localhost:5000/saludar?name=Sebastian
    name = request.args.get('name')
    if not name:
        return 'no hay a quien saludarrr'
    return 'Hola ' + name

@app.route('/mi_echo')
def my_echo():
    response_string = 'recibi... '
    miwebdict = request.args
    for dictkey, dictvalue in miwebdict.items():
        if not dictkey:
            return 'no se enviaron datos de dict al servidor jeje'
        response_string = response_string + '\n' + '%s: %s, \n' % (dictkey, dictvalue)
        # mioutput = [] ##  wish i know how to use something like this....
        # mioutput = mioutput.append(dictvalue) ##  wish i know how to use something like this....
    return response_string # mioutput ##  wish i know how to use something like this....
    print(response_string) ## cant get the fucking newline to work
    print('first line yey \nsecond line yup') ## cant get the fucking newline to work, or "print" que se manifieste

@app.route('/yttutorial2/<mystring>')
def yttutorial2(mystring):
    mioutput = 'importar una variable, en particular un string... en este ejercicio la llame: %s' % mystring
    return mioutput

@app.route('/yttutorial2integer/<int:myintvar>')
def yttutorial2integer(myintvar):
    mioutput = 'importar una variable, en particular un integer... en este ejercicio la llame: %s' % myintvar
    return mioutput

##  while playing with the code i've noticed... 2017 feb 14th
##  the if __name__ == __main__ line, if i move it to the top of file , the web reuqests stop working....
##  dict doesnt have iteritems
##  iteritems now in python 3 is called items
##  i dont know how to use "print" in this context (so that it show something up in the web browser)

@app.route('/tutorial_requestmodule')
def tutorial_requestmodule():
    return 'method used (from the Request module) was: %s' % request.method

@app.route('/tutorial_requestmodule2', methods=['GET', 'POST'])
def tutorial_requestmodule2():
    if request.method == 'POST':
        return 'you are using POST'

@app.route('/tarea_suma')
def tarea_suma():
    midict = request.args
    value1 = request.args.get('numa')
    value2 = request.args.get('numb')
    resultado = value1 + value2
    mioutput = 'la suma de %s y %s es igual a: ' % (value1, value2) + resultado
    return mioutput

@app.route('/home1')
def home1():
    return '''
        <html>
        <head> </head>
        <body>
            <h1 style="color:red"> Esta es mi Home1 </h1>
        <body>
        </html>
    '''

@app.route('/home2')
def home2():
    return render_template('home2.html', app_name='mi templateexample', nombre= 'juana')

@app.route('/home3')
def home3():
    return render_template('home3.html',
    nombre='alejandro',
    bio='nacido en torreon en 1984',
    fecha='2012!!'
    )

@app.route('/home4')
def home4():
    return render_template('home4.html',
        nombre='alejandro',
        bio='nacido en torreon en 1984',
        fecha='2012!!',
        title='pestana 4 w base'
    )

@app.route('/listaweb')
def listaweb():
    listadeinput = [
        {'nombre': 'antonio', 'apodo': 'patron'},
        {'nombre': 'ximena', 'apodo': 'jimmy'},
        {'nombre': 'julian', 'apodo': 'julaian'}
    ]
    return render_template('listaweb.html', listavariable=listadeinput)

@app.route('/dbrudimentaria/<apodo_proveido_por_client>')
def dbrudimentaria(apodo_proveido_por_client):
    db_alumnos = {
        'ximena': {"nombre": "Ximena Ortega", "bio": "Alumna DevF" },
        'tono': {"nombre": "Antonio Banderas", "bio": "Le dicen el Patronceto"},
        'pablo': {"nombre": u"Pablo Velázquez", "bio": "Colorear"}
    }
    # respuesta_bio = db_alumnos.get('apodo_proveido_por_client') ## esta linea parece repetitiva, porque en variable_apodo ya se logro obtener el apodo_proveido_por_client
    return render_template('dbrudimentaria.html', variable_apodo = db_alumnos.get(apodo_proveido_por_client))
    # return render_template('dbrudimentaria.html',
    #     variable_apodo='apodo_proveido_por_client',
    #     dict_alumnos='db_alumnos'
    # ) # + respuesta_bio  ##  trying to test but didnt quite work.....

@app.route('/home4b')
def home4b():
    mi_parametro = {
        'nombre':'alejandro',
        'bio':'nacido en torreon en 1984',
        'fecha':'2012!!',
        'title':'pestana 4 w base'
    }
    return render_template('home4.html', **mi_parametro)




if __name__ == '__main__':
    app.run(debug = True)
