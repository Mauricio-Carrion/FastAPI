import folium


class Map:

    @staticmethod
    def getMap(locationdest: tuple, zoom_start=10):
        return folium.Map(location=locationdest, zoom_start=zoom_start)
