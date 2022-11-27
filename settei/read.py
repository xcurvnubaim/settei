from settei import SqliteHandler

def getdata(package,robot,branch)->list:
    sql_handler = SqliteHandler()
    x = sql_handler.load_filename(package,branch)
    filename_arr = []
    data_arr = []
    for filename in x:
        filename_arr.append(filename[0])
    for filename in filename_arr:
        data_arr.append(sql_handler.load_data(package,robot,branch,filename)[0])
    return filename_arr,data_arr
