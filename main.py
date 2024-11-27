from Website import create_app


app = create_app()

app.config.from_object('config')
app.config.get('SECRET_KEY') 
app.config.get('FLASK_ENV')


if __name__ == '__main__':
    app.run() 