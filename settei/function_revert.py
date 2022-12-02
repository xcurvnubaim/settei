from settei import SqliteHandler

def revert(package,robot,branch,filename):
    sqlite_handle=SqliteHandler()
    x = sqlite_handle.select_data(package,robot,branch,filename)
    
    # for list in x:
    #     for idx in list:
    #         print(idx,end=" ")
    #     print()
    
    return x