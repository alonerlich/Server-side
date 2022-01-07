from flask import Flask, render_template,redirect, url_for,request,session, jsonify
import requests
from assignment10.assignment10 import interact_db

app = Flask(__name__)
app.secret_key = '12345'

users ={"user1": {"NICKNAME": "lel", "name": "Alon","lastName": "Erlich", "email": "erlichal@gmail.com", "password": 123},
        "user2": {"NICKNAME": "bob", "name": "Shai","lastName": "bar", "email": "sh@gmail.com", "password": 12345},
        "user3": {"NICKNAME": "fun", "name": "Dan", "lastName": "Lev", "email": "ss@gmail.com", "password": 12345},
        "user4": {"NICKNAME": "dud", "name": "Sarah", "lastName": "Netanyahu", "email": "sarah@gmail.com", "password": 1233345},
        "user5": {"NICKNAME": "dandan", "name": "Dan", "lastName": "Mano", "email": "mani@gmail.com", "password": 1234533}}


from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route("/about")
def about():
    return redirect(url_for("CV"))

@app.route("/")
def CV():
    return render_template('CVgrid.html')

@app.route("/exercise2")
def exercise2():
    return render_template('exercise2.html')

@app.route("/form")
def form():
    return render_template('forms.html')

@app.route("/mistake")
def mistake():
    return redirect('/')

@app.route("/assignment8")
def assignment8():
    hobbies = {"soccer", "arsenal", "climbing", "web!!!!!!!", "surfing", "cooking"}
    return render_template('assignment8.html',hobbies = hobbies )

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
        current_method = request.method
        if current_method == 'GET':
            if 'email' in request.args:
                email = request.args['email']
                if email is '':
                    return render_template('assignment9.html', search=True, find=True, user=users)
                dic = {}
                i=0
                for user in users.values():
                    i+=1
                    if user['email'] == email:
                        dic[i] = user
                print(dic)
                if len(dic) > 0:
                    return render_template('assignment9.html',search = True, find=True, user=dic)
                else:
                    return render_template('assignment9.html', search = True, find=  False)
            else:
                return render_template('assignment9.html')
        else:
            users[request.form['NICKNAME']] = {'NICKNAME': request.form['NICKNAME'],
                                              'name': request.form['firstName'],
                                              'lastName': request.form['lastName'],
                                              'email': request.form['email'],
                                              'password': request.form['password']}
            session['NICKNAME'] = request.form['NICKNAME']
            session['login'] = True
            return render_template('assignment9.html')
        return render_template('assignment9.html')

@app.route('/logOut', methods=['GET', 'POST'])
def logOut():
    session['login'] = False
    return render_template('assignment9.html')

#------------assignment11---------
def get_users():
    query = "select * from web.users"
    query_result = interact_db(query=query, query_type='fetch')
    dic = {}

    i = 1
    for row in query_result:
        user = {
            'nick name': row.NICKNAME,
            'name': row.name,
            'last name': row.lastName,
            'email': row.email,
            'password': row.password,
        }
        name = f'user{i}'
        dic[name] = user
        i+=1
    return jsonify(dic)

@app.route('/assignment11/users', methods=['GET', 'POST'])
def return_all_users():
    users = get_users()
    return users

def get_user(id):
    f'https://reqres.in/api/users/{id}'
    res = requests.get(f'https://reqres.in/api/users/{id}')
    return res.json()

@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def outer_source():
    if "id" in request.args:
        if request.args['id'] == '':
            return render_template('assignment11.html', user = '')
        n = int(request.args['id'])
        user = get_user(n)
    else:
        user = ""
    return render_template('assignment11.html', user=user)



if __name__=="__main__":
    app.run(debug = True)
