from pymediainfo import MediaInfo

media_info = MediaInfo.parse('OCORPO_EP01_ptBR_0166.jpg')
for track in media_info.tracks:
    if track.track_type == 'Video':
        print(track.width)