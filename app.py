from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data sementara (bisa diganti database)
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    price = float(request.form['price'])
    items.append({'name': name, 'price': price})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)