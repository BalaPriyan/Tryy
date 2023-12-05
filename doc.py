import subprocess
import os
import shutil
import base64 as r
from dotenv import load_dotenv

print("starting")

load_dotenv("config.env")

def restar():
    os.system("rm -rf /tmp/*")
    if not os.path.exists("/tmp/thumbnails/"):
        os.mkdir("/tmp/thumbnails/")
    os.execvp(sys.executable, [sys.executable, "bot.py"])

try:
    repo_url = os.environ['repo_url']
except KeyError as e:
    sys.exit(f"Important environment variables are missing {e}")

clone_cmd = f"git clone {repo_url} repo"
encoded_cmd = r.b64encode(clone_cmd.encode('ascii')).decode('ascii')

if os.path.exists("/app/repo/"):
    shutil.rmtree("/app/repo/")
    os.system(r.b64decode(encoded_cmd.encode('ascii')).decode('ascii'))
    print("Repository cloned successfully")
    os.chdir("repo/")

    # Docker build command
    docker_build_cmd = "sudo docker build . -t mltb"
    subprocess.run(docker_build_cmd, shell=True)

    # Docker start command
    docker_start_cmd = "sudo docker run -p 80:80 -p 8080:8080 mltb"
    subprocess.run(docker_start_cmd, shell=True)
else:
    os.system(r.b64decode(encoded_cmd.encode('ascii')).decode('ascii'))
    print("Repository cloned successfully")
    os.chdir("repo/")

    # Docker build command
    docker_build_cmd = "sudo docker build . -t mltb"
    subprocess.run(docker_build_cmd, shell=True)

    # Docker start command
    docker_start_cmd = "sudo docker run -p 80:80 -p 8080:8080 mltb"
    subprocess.run(docker_start_cmd, shell=True)

print("service stopped")
