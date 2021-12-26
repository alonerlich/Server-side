from flask import Flask, render_template, url_for, session, request, redirect, Blueprint , flash
import mysql
import mysql.connector

app = Flask(__name__)
app.secret_key = '12345'

assignment10 = Blueprint('assignment10',__name__,static_folder='static',static_url_path='/assignment10',template_folder='templates')

# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='web')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
# ------------------------------------------------- #
# ------------------------------------------------- #




@assignment10.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':

        NIACKNAME = request.form['NIACKNAME']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        check_input = "SELECT email FROM web.users WHERE email='%s';" % email
        find = interact_db(query=check_input, query_type='fetch')

        if len(find) > 0: # if already exist
            message ='email is exist,please try another email'
        else:
            query = "insert into web.users values ('%s', '%s', '%s','%s','%s');" % (NIACKNAME, firstName, lastName, email, password)
            interact_db(query=query, query_type='commit')
            message = 'great! thanks for registering'
        session['message'] = message
        return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    query = "SELECT email FROM web.users WHERE email='%s';" % email
    find = interact_db(query=query, query_type='fetch')
    if len(find) > 0:
        query = "delete from web.users where email='%s';" % email
        interact_db(query=query, query_type='commit')
        session['message'] = "deleted successfully!"
    else:
        session['message'] = "email is not exist!"
    return redirect('/assignment10')

@assignment10.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        nick = request.form['nick']
        name = request.form['firstName']
        lasttname = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        query = " UPDATE web.users SET NICKNAME='%s',name='%s' ,lastName='%s', password='%s' WHERE email='%s';"% (nick, name, lasttname, password, email)
        interact_db(query=query, query_type='commit')
        session['message'] = 'update successfully!'
        return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/assignment10')
def view():
    users = interact_db(query = "select * "
                                "from web.users", query_type='fetch')
    if session.get('message') is not None:
        message = session['message']
        session.pop('message')
        return render_template('assignment10.html', myUsers=users, message=message)
    else:
        return render_template('assignment10.html', myUsers=users)