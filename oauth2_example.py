from flask import Flask, redirect, request, jsonify

import oauth2_instagram_process as oauth2

app = Flask(__name__)

CLIENT_ID = "b3e2bf83b14747e89cb526adf934563c"
REDIRECT_URL = "http://127.0.0.1:5000/instagram_return/"
CLIENT_SECRET = '7855bdc2ae4341468784204895aaa0a6'


@app.route('/')
def hello_world():
    url_to_insta = oauth2.generate_authorization_url(CLIENT_ID, REDIRECT_URL,
                                                     scope=["basic", "public_content", "follower_list", "comments",
                                                            "relationships", "likes"])
    print url_to_insta
    return redirect(url_to_insta)


@app.route('/instagram_return/')
def instagram_return():
    code = request.args.get('code')
    if code:
        print "got code"
        return jsonify(oauth2.get_authorization_token(code,
                                                      CLIENT_ID,
                                                      CLIENT_SECRET,
                                                      REDIRECT_URL))
    else:
        print "error getting code"
        return jsonify(request.args)
