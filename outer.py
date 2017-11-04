import parsetrump

def make_list(cc_file):
    with open(cc_file, "r") as f:
        srtText = f.read()
        list = parsetrump.srt_to_dict(srtText)
        return list
