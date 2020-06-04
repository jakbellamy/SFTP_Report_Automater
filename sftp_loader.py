from decouple import config
import paramiko

host = config('SFTP_HOST')  # Init transport
port = 22
transport = paramiko.Transport(host, port)

user = config('SFTP_CLIENT')  # Transport Authentication
pwd = config('SFTP_SECRET')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

ex_imports = sftp.listdir(path='./Import')
print(len(ex_imports))


def finder(sub_str, path):
    return [file for file in path if sub_str in file]


e_dupes = finder('Email_Duplicate_Suppression', ex_imports)
brokers = finder('Brokers_to_Email', ex_imports)
locations = finder('Supreme_Locations', ex_imports)
print(e_dupes)

sftp.close()
transport.close()
print('SFTP Connection Closed')
