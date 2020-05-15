#获得info数据


from infos.models import Infos


def get_info(longitude, latitude, reader_id, limits):
    longitude_max = longitude + limits
    longitude_min = longitude - limits
    latitude_max = latitude + limits
    latitude_min = latitude - limits
    info_data = Infos.objects.exclude(poster_id=reader_id).filter(longitude__lt=longitude_max, longitude__gt=longitude_min, latitude__lt=latitude_max, latitude__gt=latitude_min).order_by('-create_time')
    return info_data
