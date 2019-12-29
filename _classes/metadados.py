from pymediainfo import MediaInfo

class metadados:
    def __init__(self, file):
        media_info = MediaInfo.parse(file)
        for track in media_info.tracks:
            if track.track_type == 'General':
                self.gextensao = track.file_extension
                self.gfilename = track.file_name
                self.gfilenameext = track.file_name_extension
                self.gframecount = track.frame_count
                self.gframerate = track.frame_rate
            elif track.track_type == 'Video':
                self.vwidth = track.width
                self.vheight = track.height
                self.vscantype = track.scan_type
