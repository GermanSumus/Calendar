from json import load, dump

def read_cal(cal_file_path='cal.dict'):
    """Reads the cal.dict file and returns an empty dictionary at least"""
    with open(cal_file_path) as file:
        try:
            return load(file, parse_int=True)
        except:
            return {}
        try:
            return eval(file.read())
        except SyntaxError:
            with open(cal_file_path, 'w') as file:
                file.write('{}')
        finally:
            with open(cal_file_path) as file:
                return eval(file.read())

def write_to_cal(event, cal_file_path='cal.dict'):
    cal = read_cal()
    cal[event.year][event.month][str(event.datetime.day)][event.time]= event.description
    with open(cal_file_path, 'w') as file:
        dump(cal, file, indent=2)
