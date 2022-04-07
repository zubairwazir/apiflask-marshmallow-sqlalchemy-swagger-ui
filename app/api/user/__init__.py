from apiflask import APIBlueprint

user_bp = APIBlueprint("user", __name__, "User APIs", url_prefix="/api/user")

from . import user
