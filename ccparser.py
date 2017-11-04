import re
import outer

#in_list = [{'index':1, 'start_time':12, 'end_time':14, 'text':'The President: something something'},{'index':1, 'start_time':15, 'end_time':17, 'text':'something something'},{'index':3, 'start_time':18, 'end_time':19, 'text':'The Press: something something'},{'text':'The President:'}]


def get_captions(file_name):
    in_list = outer.make_list(file_name)
    pattern = re.compile("^[a-zA-Z ._-][^:]*:.*$")
    bad_mode = True

    for i in range(len(in_list)):
        if (pattern.match(in_list[i]['text'])) and ('The President:' not in in_list[i]['text']):
            bad_mode = False
        if('The President:' in in_list[i]['text']):
            bad_mode = True

        if bad_mode:
            in_list[i]['is_bad'] = True
        else:
            in_list[i]['is_bad'] = False

    return in_list
