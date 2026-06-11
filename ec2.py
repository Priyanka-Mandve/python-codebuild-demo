import paramiko

host = "3.110.208.243"
username = "ec2-user"
key_file = r"github-python.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=host,
    username=username,
    key_filename=key_file
)

stdin, stdout, stderr = ssh.exec_command("pwd")

print("Output:")
print(stdout.read().decode())

print("Errors:")
print(stderr.read().decode())

ssh.close()
