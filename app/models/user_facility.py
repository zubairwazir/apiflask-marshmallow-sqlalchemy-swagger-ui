import uuid
from typing import List
from app import db


class UserFacilityListModel(db.Model):
    __tablename__ = "fuser_facility_list"
    id = db.Column(db.Integer, db.Sequence("fuser_facility_list_id_seq"), primary_key=True)
    createdby_id = db.Column('createdby_id', db.Integer, nullable=False)
    createdon = db.Column('createdon', db.DateTime(timezone=True))
    modifiedon = db.Column('modifiedon', db.DateTime(timezone=True))
    enabled = db.Column(db.Integer, nullable=False)
    fuser_id = db.Column(db.Integer, db.ForeignKey('fuser.id'), nullable=False)
    ffacility_id = db.Column(db.Integer, db.ForeignKey('ffacility.id'), nullable=False)
    user = db.relationship('UserModel', foreign_keys=[fuser_id], backref='facilities')
    facility = db.relationship('FacilityModel', foreign_keys=[ffacility_id])
