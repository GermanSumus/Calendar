
def read_cal(cal_file_path='cal.dict'):
    """Reads the cal.dict file and returns an empty dictionary at least"""
    with open(cal_file_path) as file:
        try:
            return eval(file.read())
        except SyntaxError:
            with open(cal_file_path, 'w') as file:
                file.write('{}')
        finally:
            with open(cal_file_path) as file:
                return eval(file.read())
