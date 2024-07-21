from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from app.core.map import Map
from app.schemas.map import MapRequest

router = APIRouter()


@router.post('/', response_class=HTMLResponse)
def get_map(maprequest: MapRequest):
    return Map().getMap((maprequest.latitude, maprequest.longitude), maprequest.zoom_start).get_root().render()
