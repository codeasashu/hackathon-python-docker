import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("frontend/index.html")

if __name__ == '__main__':
    print("Server running at"+ os.environ['HOST'] +":"+ os.environ['PORT'])
    app.run(host=os.environ['HOST'], port=os.environ['PORT'])
