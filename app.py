from flask import Flask, render_template, request, redirect, url_for 
from flask_mysqldb import MySQL

app = Flask(__name__)


# Configuração do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "guih0412"
app.config['MYSQL_DB'] = 'linkin_park'
mysql = MySQL(app)

#Rotas para as páginas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trajetoria')
def trajetoria():
    return render_template('trajetoria.html')

@app.route('/discografia')
def discografia():
    return render_template('discografia.html')

@app.route('/resenha')
def resenha():
    return render_template('resenha.html')

# Rota para exibir a lista de tarefas

@app.route('/avaliacao')
def avaliacao():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM avaliacaotable")
    tasks = cur.fetchall()
    cur.close()
    return render_template('avaliacao.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        nome= request.form['nome']
        email = request.form['email']
        feedback = request.form['feedback']
        nota = request.form['nota']
        sugestao = request.form['sugestao']
        musica= request.form['musica']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO avaliacaotable (nome, email, feedback, nota, sugestao, musica) VALUES (%s, %s, %s, %s, %s, %s)", (nome, email, feedback, nota, sugestao, musica))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('avaliacao')) 
    
# Rota para atualizar uma tarefa
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        feedback = request.form['feedback']
        nota = request.form['nota']
        sugestao = request.form['sugestao']
        musica = request.form['musica']
        status= request.form["status"]
        cur = mysql.connection.cursor()
        cur.execute("UPDATE avaliacaotable SET nome=%s, email=%s, feedback=%s, nota=%s ,sugestao=%s, musica=%s, status=%s WHERE id=%s", (nome, email, feedback, nota, sugestao, musica, status, task_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('avaliacao')) 
    
# Rota para excluir uma tarefa
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM avaliacaotable WHERE id=%s", (task_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('avaliacao')) 
    


if __name__ == '__main__':
    app.run(debug=True)

