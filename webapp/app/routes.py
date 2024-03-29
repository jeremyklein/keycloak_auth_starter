from . import app, oidc


@app.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/private">See private</a> '
                '<a href="/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/login">Log in</a>'


@app.route('/login')
@oidc.require_login
def login():
    return 'Welcome %s' % oidc.user_getfield('given_name')




if __name__ == '__main__':
    app.run(host='0.0.0.0')