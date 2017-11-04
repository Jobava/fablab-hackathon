import parsetrump

def make_list():
        with open('trump.srt', "r") as f:
                srtText = f.read()
                list = parsetrump.srt_to_dict(srtText) 
                return list
