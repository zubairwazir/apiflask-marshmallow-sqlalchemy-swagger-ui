from app.schemas.schemas import UserSchema
from app.models.user import UserModel
from app import db


from . import user_bp as blueprint


@blueprint.get('/get')
@blueprint.output(UserSchema(many=True))
def get_users():
    return UserModel.find_all()


@blueprint.get('/get_by_id/<int:user_id>')
@blueprint.output(UserSchema)
def get_user_by_id(user_id):
    return UserModel.find_by_id(user_id)


@blueprint.post('/create')
@blueprint.input(UserSchema)
@blueprint.output(UserSchema, 201)
def create_user(data):
    user = UserModel.save_to_db(**data)
    return user


@blueprint.patch('/update/<int:user_id>')
@blueprint.input(UserSchema(partial=True))
@blueprint.output(UserSchema)
def update_user(user_id, data):
    user = UserModel.query.get_or_404(user_id)
    for attr, value in data.items():
        setattr(user, attr, value)
    db.session.commit()
    return user


@blueprint.delete('/delete/<int:user_id>')
@blueprint.output({}, 204)
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return ''
