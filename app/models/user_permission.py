import uuid
from typing import List
from app import db


class UserPermissionGrpModel(db.Model):
    __tablename__ = "fuser_permission_grp"
    id = db.Column(db.Integer, db.Sequence("fuser_permission_grp_id_seq"), primary_key=True)
    createdby = db.Column('createdby', db.String, nullable=False)
    createdon = db.Column('createdon', db.DateTime(timezone=True))
    modifiedon = db.Column('modifiedon', db.DateTime(timezone=True))
    enabled = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    securitylevel = db.Column(db.Integer, nullable=False)
    permissions = db.relationship('UserPermissionGrpPermissionsModel', backref='fuser_permission_grp')


class UserPermissionGrpPermissionsModel(db.Model):
    __tablename__ = "fuser_permission_grp_permissions"
    id = db.Column(db.Integer, db.Sequence("fuser_permission_grp_permissions_id_seq"), primary_key=True)
    createdby_id = db.Column('createdby_id', db.Integer, nullable=False)
    createdon = db.Column('createdon', db.DateTime(timezone=True))
    modifiedon = db.Column('modifiedon', db.DateTime(timezone=True))
    fuserpermissiongrp_id = db.Column(db.Integer, db.ForeignKey('fuser_permission_grp.id'), nullable=False)
    permission = db.Column(db.Integer, nullable=False)

