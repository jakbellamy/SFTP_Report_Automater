from decouple import config
import paramiko

host = config('SFTP_HOST') # Init transport
port = 22
transport = paramiko.Transport((host, port))

user = config('SFTP_CLIENT') # Transport Authentication
pswd = config('SFTP_SECRET')
transport.connect(username=user, password=pswd)

sftp = paramiko.SFTPClient.from_transport(transport)

print(sftp.listdir(path='./Export'))

sftp.close()
transport.close()
print('SFTP Connection Closed')
