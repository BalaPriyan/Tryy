# Use Kali Linux as the base image
FROM kalilinux/kali-rolling

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV USER=root
ENV VNC_RESOLUTION=1280x1024
ENV VNC_COL_DEPTH=24

# Update packages and install required software
RUN apt-get update && apt-get install -y \
    kali-linux-core \
    kali-desktop-xfce \
    tightvncserver

# Set VNC password (Change 'yourpassword' to your desired password)
RUN mkdir ~/.vnc && echo "new" | vncpasswd -f > ~/.vnc/passwd && chmod 600 ~/.vnc/passwd

# Expose VNC port
EXPOSE 5901

# Start VNC server
CMD ["vncserver", "-geometry", "${VNC_RESOLUTION}", "-depth", "${VNC_COL_DEPTH}", ":1"]
