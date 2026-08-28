from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1 style="font-family:sans-serif;color:#0D1117;padding:40px">
        🚀 Hello from Isse's DevOps Project! this looks amazong 
        <br><small style="font-size:16px;color:#555">CI/CD Pipeline — Project 1</small>
    </h1>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

