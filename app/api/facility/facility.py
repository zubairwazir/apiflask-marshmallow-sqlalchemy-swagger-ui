from app.schemas.schemas import FacilitySchema
from app.models.facility import FacilityModel
from app import db

from . import facility_bp as blueprint


@blueprint.get('/get')
@blueprint.output(FacilitySchema(many=True))
def get_facilites():
    return FacilityModel.find_all()


@blueprint.get('/get_by_id/<int:facility_id>')
@blueprint.output(FacilitySchema)
def get_facility_by_id(facility_id):
    return FacilityModel.find_by_id(facility_id)


@blueprint.post('/create')
@blueprint.input(FacilitySchema)
@blueprint.output(FacilitySchema, 201)
def create_facility(data):
    FacilityModel.save_to_db(**data)
    return 'added successfully'


@blueprint.patch('/update/<int:facility_id>')
@blueprint.input(FacilitySchema(partial=True))
@blueprint.output(FacilitySchema)
def update_facility(facility_id, data):
    facility = FacilityModel.query.get_or_404(facility_id)
    for attr, value in data.items():
        setattr(facility, attr, value)
    db.session.commit()
    return facility


@blueprint.delete('/delete/<int:facility_id>')
@blueprint.output({}, 204)
def delete_facility(facility_id):
    facility = FacilityModel.query.get_or_404(facility_id)
    db.session.delete(facility)
    db.session.commit()
    return ''
