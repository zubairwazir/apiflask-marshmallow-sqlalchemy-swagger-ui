from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import DB_URL

app = APIFlask(__name__)

app.info = {
    'title': "Company Name",
    "termsOfService": "https://example.com/terms/",
    'license': {
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html'
    }
}

app.external_docs = {
    'description': 'www.companyname.com',
    'url': 'https://www.companyname.com'
}


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.api.user import user_bp
from app.api.facility import facility_bp

app.register_blueprint(user_bp)
app.register_blueprint(facility_bp)
