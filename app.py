from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Beating Heart</title>
        <style>
            body {
                text-align: center;
                background-color: #fbeaff;
                font-family: Arial, sans-serif;
                padding-top: 100px;
            }
            .heart {
                width: 100px;
                height: 90px;
                background: red;
                position: relative;
                margin: auto;
                transform: rotate(-45deg);
                animation: beat 1s infinite;
            }
            .heart::before,
            .heart::after {
                content: "";
                width: 100px;
                height: 90px;
                background: red;
                border-radius: 50%;
                position: absolute;
            }
            .heart::before {
                top: -50px;
                left: 0;
            }
            .heart::after {
                left: 50px;
                top: 0;
            }
            @keyframes beat {
                0%, 100% {
                    transform: scale(1) rotate(-45deg);
                }
                50% {
                    transform: scale(1.2) rotate(-45deg);
                }
            }
            h1 {
                margin-top: 50px;
                font-size: 32px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="heart"></div>
        <h1>How are you?</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
