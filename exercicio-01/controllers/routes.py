from flask import render_template, request

tarefa = []
tarefalist = [{'Tarefa', 'Escovar os dentes'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template("index.html")
    
    @app.route('/cadprojetos')
    def cadproj():
        return render_template("cadprojetos.html")
    
    @app.route('/cadtarefa', methods=['GET', 'POST'])
    def cadtarefa():
        
        if request.method == 'POST':
            if request.form.get('tarefa'):
                tarefa.append(request.form.get('tarefa'))
        
        return render_template("cadtarefa.html", tarefa=tarefa)
    
    @app.route('/config')
    def config():
        return render_template("config.html")