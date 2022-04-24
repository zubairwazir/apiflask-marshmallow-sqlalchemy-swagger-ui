import uuid
from typing import List
from app import db


class UserModel(db.Model):
    __tablename__ = "fuser"
    id = db.Column(db.Integer, db.Sequence("fuser_id_seq"), primary_key=True)
    createdby = db.Column('createdby', db.String, nullable=False)
    createdon = db.Column('createdon', db.DateTime(timezone=True))
    modifiedon = db.Column('modifiedon', db.DateTime(timezone=True))
    enabled = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=False)
    grp_id = db.Column("grp_id", db.Integer, db.ForeignKey('fuser_permission_grp.id'), nullable=False)
    grp = db.relationship('UserPermissionGrpModel', foreign_keys=[grp_id])

    def __init__(self, createdby, createdon, modifiedon, enabled, type, description, name, username, email, pwd,
                 grp_id):
        self.id = uuid.uuid4().hex
        self.createdby = createdby
        self.createdon = createdon
        self.modifiedon = modifiedon
        self.enabled = enabled
        self.type = type
        self.description = description
        self.name = name
        self.username = username
        self.email = email
        self.pwd = pwd
        self.grp_id = grp_id

    def __repr__(self):
        return 'UserModel(createdby=%s, createdon=%s, modifiedon=%s, endabled=%s, type=%s, description=%s, name=%s, ' \
               'username=%s, email=%s, pwd=%s, grp_id=%s)' % (self.createdby, self.createdon, self.modifiedon,
                                                              self.enabled, self.type, self.description, self.name,
                                                              self.username, self.email, self.pwd, self.grp_id)

    def json(self):
        return {'createdby': self.createdby, 'createdon': self.createdon, 'modifiedon': self.modifiedon,
                'endabled': self.enabled, 'type': self.type, 'description': self.description, 'name': self.name,
                'username': self.username, 'email': self.email, 'pwd': self.pwd, 'grp_id': self.grp_id}

    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()