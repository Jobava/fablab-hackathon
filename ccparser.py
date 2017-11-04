import re
import outer

#in_list = [{'index':1, 'start_time':12, 'end_time':14, 'text':'The President: something something'},{'index':1, 'start_time':15, 'end_time':17, 'text':'something something'},{'index':3, 'start_time':18, 'end_time':19, 'text':'The Press: something something'},{'text':'The President:'}]

in_list = outer.make_list()

pattern = re.compile("^[a-zA-Z ._-][^:]*:.*$")
bad_mode = 1

for i in range(len(in_list)):
    if (pattern.match(in_list[i]['text'])) and ('The President:' not in in_list[i]['text']):
        bad_mode=0
    if('The President:' in in_list[i]['text']):
        bad_mode=1

    if bad_mode:
        in_list[i]['is_bad'] = True
    else:
        in_list[i]['is_bad'] = False

print(in_list)
        
