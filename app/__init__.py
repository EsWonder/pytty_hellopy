from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Bienvenido a Flask en EC2</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

            body {
                margin: 0;
                padding: 0;
                font-family: 'Montserrat', sans-serif;
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: #ffffff;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.15);
                padding: 40px 60px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                border: 1px solid rgba(255, 255, 255, 0.18);
                max-width: 500px;
            }
            h1 {
                font-weight: 700;
                font-size: 2.5rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                margin: 0;
                letter-spacing: 1px;
                line-height: 1.4;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hello world!</h1>
            <p>From EC2 with Flask Distributed</p>
        </div>
    </body>
    </html>
    """

