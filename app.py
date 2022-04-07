from app import app
# from app import db


# @app.before_first_request
# def init_database():
#     db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
