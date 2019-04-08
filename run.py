from BGInfoPortal import create_app
from flask_heroku import Heroku


app = create_app()
heroku = Heroku()
heroku.init_app(app)

if __name__ == '__main__':
    app.run(debug=False)
