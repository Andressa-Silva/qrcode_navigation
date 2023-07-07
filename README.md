# QR-Code detection with CSI camera on Jetson
With Ubuntu 20

### To install dependencies:

```
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

pkg-config --cflags --libs gstreamer-1.0
```

```
pip install pyzbar
```

### To run:

```
roslaunch detector.launch mission:=1
```

Mission 1: 
Mission 2:
Mission 3:
Mission 4:

OpenCV needs to be compiled with CUDA
