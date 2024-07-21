from typing import Union

from pydantic import BaseModel


class MapRequest(BaseModel):
    latitude: float
    longitude: float
    zoom_start: Union[float, None] = None
