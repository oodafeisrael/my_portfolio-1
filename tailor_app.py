from app import app

if __name__=="__main__":
    # start the flask development server
    # Listen on all available interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)