from apiflask import APIBlueprint

facility_bp = APIBlueprint("facility", __name__, "Facility APIs", url_prefix="/api/facility")

from . import facility
