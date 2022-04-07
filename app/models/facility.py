import uuid
from typing import List
from app import db


class FacilityModel(db.Model):
    __tablename__ = "ffacility"
    id = db.Column(db.Integer, db.Sequence("ffacility_id_seq"), primary_key=True)
    createdby_id = db.Column('createdby_id', db.Integer, nullable=False)
    createdon = db.Column('createdon', db.DateTime(timezone=True))
    modifiedon = db.Column('modifiedon', db.DateTime(timezone=True))
    enabled = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    address1 = db.Column(db.String, nullable=False)
    address2 = db.Column(db.String)
    address3 = db.Column(db.String)
    address4 = db.Column(db.String)
    city = db.Column(db.String, nullable=False)
    stateprovince = db.Column(db.String, nullable=False)
    postalcode = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)

    def __init__(self, createdby, createdon, modifiedon, enabled, type, description, address1, address2, address3,
                 address4, city, stateprovince, postalcode, country):
        self.id = uuid.uuid4().hex
        self.createdby = createdby
        self.createdon = createdon
        self.modifiedon = modifiedon
        self.enabled = enabled
        self.type = type
        self.description = description
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.address4 = address4
        self.city = city
        self.stateprovince = stateprovince
        self.postalcode = postalcode
        self.country = country

    def __repr__(self):
        return 'FacilityModel(createdby=%s, createdon=%s, modifiedon=%s, endabled=%s, type=%s, description=%s, ' \
               'address1=%s, address2=%s,address3=%s, address4=%s, city=%s, stateprovince=%s, postalcode=%s, ' \
               'country=%s)' % (
                   self.createdby, self.createdon, self.modifiedon, self.enabled, self.type, self.description,
                   self.address1, self.address2, self.address3, self.address4, self.city, self.stateprovince,
                   self.postalcode, self.country)

    def json(self):
        return {'createdby': self.createdby, 'createdon': self.createdon, 'modifiedon': self.modifiedon,
                'enabled': self.enabled, 'type': self.type, 'description': self.description, 'address1': self.address1,
                'address2': self.address2, 'address3': self.address3, 'address4': self.address4, 'city': self.city,
                'stateprovince': self.stateprovince, 'postalcode': self.postalcode, 'country': self.country}

    @classmethod
    def find_by_id(cls, _id) -> "FacilityModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["FacilityModel"]:
        return cls.query.all()

    def save_to_db(self) -> "FacilityModel":
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> "FacilityModel":
        db.session.delete(self)
        db.session.commit()
