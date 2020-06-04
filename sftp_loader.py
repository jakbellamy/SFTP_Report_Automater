from decouple import config
import paramiko

host = config('SFTP_HOST')  # Init transport
port = 22
transport = paramiko.Transport((host, port))

user = config('SFTP_CLIENT')  # Transport Authentication
pwd = config('SFTP_SECRET')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

ex_ls = sftp.listdir(path='./Import')
print(len(ex_ls))


def finder(sub_str):
    return [file for file in ex_ls if sub_str in file]


e_dupes = finder('Email_Duplicate_Suppression')
brokers = finder('Brokers_to_Email')
locations = finder('Supreme_Locations')
print(e_dupes)

sftp.close()
transport.close()
print('SFTP Connection Closed')
