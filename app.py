from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Beating Heart</title>
        <style>
            body {
                background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .heart {
                position: relative;
                width: 100px;
                height: 90px;
                background: #ff4d6d;
                transform: rotate(-45deg);
                animation: beat 1s infinite;
                box-shadow: 0 0 20px #ff4d6d;
            }

            .heart::before,
            .heart::after {
                content: "";
                position: absolute;
                width: 100px;
                height: 90px;
                background: #ff4d6d;
                border-radius: 50%;
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
                font-size: 2.5rem;
                color: #fff;
                text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
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
