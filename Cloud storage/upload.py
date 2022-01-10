import os
import dropbox

list = os.listdir("C:/Users/Nitesh/Desktop/Python/Functions")

def upload(file_name):
    dropbox_access_token= "sl.A_0BZXoqHB6JWzhiXkd-mFbX_UdVyQliwaSaLZbEbggqjcU42EiPPULzd8_bRYHRKYhy4cLhhu2v8dltJyxkCHT5Xy-FvwobLWyJ_aVwl06izFy6TW0dKeDBLvvt9JbG7Y9zSTs3lIg"
    dropbox_path= "/new/" + file_name 
    computer_path= "C:/Users/Nitesh/Desktop/Python/Functions/" + file_name
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))

for i in list:
    upload(i)