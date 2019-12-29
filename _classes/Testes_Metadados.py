from pymediainfo import MediaInfo

media_info = MediaInfo.parse('movie-test.mp4')
for track in media_info.tracks:
    if track.track_type == 'Video':
        print(track.width)