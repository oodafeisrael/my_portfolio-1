from tailor import create_app, db

app = create_app()


if __name__=="__main__":
   # with app.app_context():
        create_database(app)
    # start the flask development server
    # Listen on all available interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)