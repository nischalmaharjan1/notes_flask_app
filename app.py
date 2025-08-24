from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for notes (reset on app restart)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        notes.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(port=8088)

