from flask import render_template, request

tarefas = []
tarefalist = [{'Tarefa', 'Escovar os dentes'}]
projeto = []

def init_app(app):
    @app.route('/')
    def home():
        return render_template("index.html")
    
    @app.route('/cadprojetos', methods=["GET","POST"])
    def cadproj():
        
        if request.method == 'POST':
            if request.form.get('projeto'):
                projeto.append(request.form.get('projeto'))
        return render_template("cadprojetos.html", projeto=projeto)
    
    @app.route('/cadtarefa', methods=['GET', 'POST'])
    def cadtarefa():
        
        
        
        if request.method == 'POST':
                dado1 = request.form['Id']
                dado2 = request.form['Tarefa']
                dado3 = request.form['Descrição']
                dado4 = request.form['Feita']
                tarefas.append([dado1,dado2,dado3,dado4])
                return render_template('cadtarefa.html', tarefas=tarefas)
        
        return render_template("cadtarefa.html", tarefas=tarefas)
    
    @app.route('/aboutus')
    def aboutus():
        return render_template("aboutus.html")