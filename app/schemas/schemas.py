from app.models.user import UserModel
from app.models.facility import FacilityModel
from app.models.user_facility import UserFacilityListModel
from app.models.user_permission import UserPermissionGrpPermissionsModel, UserPermissionGrpModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


## FacilitySchema
class FacilitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FacilityModel


facility_schema = FacilitySchema()
facilities_schema = FacilitySchema(many=True)


## UserFacilityListSchema
class UserFacilityListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserFacilityListModel

    facility = fields.Nested(FacilitySchema)


user_facility_list_schema = UserFacilityListSchema()


## UserFacilityListSchema
class UserPermissionGrpPermissionsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserPermissionGrpPermissionsModel


user_permission_grp_permission_schema = UserPermissionGrpPermissionsSchema()
user_permission_grp_permissions_schema = UserPermissionGrpPermissionsSchema(many=True)


## UserPermissionGrpSchema
class UserPermissionGrpSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserPermissionGrpModel

    permissions = fields.List(fields.Nested(UserPermissionGrpPermissionsSchema))


user_permission_grp_schema = UserPermissionGrpSchema()
user_permission_grps_schema = UserPermissionGrpSchema(many=True)


## UserSchema
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        # include_fk = True

    grp = fields.Nested(UserPermissionGrpSchema)
    facilities = fields.List(fields.Nested(UserFacilityListSchema))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
