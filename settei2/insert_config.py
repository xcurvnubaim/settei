from settei2 import SqliteHandler

def write_data(package,robot,branch,filename_arr,data_arr):
    sql_handler = SqliteHandler()
    arr_size = len(filename_arr)
    for idx in range(arr_size):
        sql_handler.insert_idPackage(package)
        sql_handler.insert_listconfig(package,branch,filename_arr[idx])
        sql_handler.insert(package,robot,branch,filename_arr[idx],data_arr[idx])
