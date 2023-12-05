import subprocess
import os

# Replace these variables with your GitHub repository URL and run command
repo_url = "https://github.com/BalaPriyan/"
docker_build_cmd = "docker build -t my_image ."
docker_run_cmd = "docker run my_image"

# Clone the GitHub repository
subprocess.run(f"git clone {repo_url}", shell=True)

# Change directory to the cloned repository
repo_name = repo_url.split('/')[-1].split('.')[0]
os.chdir(repo_name)

# Execute Docker build command
subprocess.run(docker_build_cmd, shell=True)

# Execute Docker run command
subprocess.run(docker_run_cmd, shell=True)
