from settei import SqliteHandler,read,write,json_config_load


def test_database():
    sqlite_handle = SqliteHandler()

    sqlite_handle.create()

    package = 'aruku'
    robot = 'robot'
    branch = 'master'
    filename_arr = ['kinematic.json','walking.json']
    data_arr = ['hello world','hello world']

    write(package,robot,branch,filename_arr,data_arr)
    x,y = read(package,robot,branch)
    assert x == filename_arr and y== data_arr, "error on test_database"

test_database()