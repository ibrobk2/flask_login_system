from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='HomePage')




@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method=='POST':
        fullName = request.form['fname']
        userName = request.form['user']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['pwd']
        
        return redirect(url_for('success', fn=fullName, user=userName))
        
    return render_template('reg.html', title='Registration Page')

@app.route('/login')
def log():
    return render_template('login.html', title='Login Page')

@app.route('/success/<fn>&&<user>')
def success(fn, user):
    return f'Congrats, {fn}, your username is {user}'

if __name__=='__main__':
    app.run(debug=True)