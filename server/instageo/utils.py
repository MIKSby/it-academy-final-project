from time import sleep
from instabot import Bot


class MyBot(Bot):

    def get_geotag_medias(self, geotag, filtration=True):
        sleep(.2)
        if not self.api.get_location_feed(geotag, max_id='5'):
            self.logger.warning("Error get_geotag_medias while getting geotag feed.")
            return []
        return [media for media in self.api.last_json["items"]]

    def get_medias_from_coordinates(self, latitude, longitude, depth=10):
        locations = self.get_locations_from_coordinates(latitude, longitude)
        geotags = [i['location']['pk'] for i in locations]
        list_medias = []
        for geotag in geotags[:depth]:
            self.very_small_delay()
            geotag_medias = self.get_geotag_medias(geotag)
            if geotag_medias:
                for media in geotag_medias:
                    if media['media_type'] == 1:
                        list_medias.append(media)
        return list_medias

    def filter_media_items(self, media_ids):
        filtered_medias = []
        for media in media_ids:
            self.very_small_delay()
            if media['media_type'] == 1:
                user = media['user']['pk']
                if self.check_not_bot(user):
                    filtered_medias.append(media)
        return filtered_medias
