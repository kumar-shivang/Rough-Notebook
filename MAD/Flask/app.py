from flask import Flask
app = Flask(__name__)
@app.route("/app")
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<h1>hello world</h1>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Laudantium sint eveniet vitae id repellendus nemo vero explicabo impedit tenetur dolor. Odio quibusdam enim, in beatae quos placeat debitis exercitationem commodi.</p>
    
</body>
</html>
    """
if __name__ == "__main__":
    app.debug = True
    app.run()