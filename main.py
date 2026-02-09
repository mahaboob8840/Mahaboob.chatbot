from flask import Flask




app=Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cart")
def cart():
 return "<p>CART</p>"

if __name__ == "__main__":
    app.run(debug=True,port=5001)