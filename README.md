# chili-tracking-with-opencv-python-haar_cascade

Installation
1.pip install python 3.6.5
2.pip install opencv 3.4.4 + contribute
3.pip install numpy
4.pip install PyQt5
5.pip install pyqt5-tools

OS
ubuntu >> training chilli
windows >> coding and process

ubuntu >> Installation

1.sudo apt-get update
2.sudo apt-get upgrade
3.mkdir opencv
4. cd opencv
5. sudo apt-get install git
6. git clone https://github.com/Itseez/opencv.git
7.udo apt-get install build-essential
8. sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
9.sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
10. apt-get install libopencv-dev

ubuntu >> training chilli
- opencv_createsamples -img <ชื่อรูป> -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num <จำนวนรูปที่ต้องการ>
- opencv_createsamples -info info/info.lst -num <จำนวนรูป> -w <ขนาด width> -h <ขนาด height> -vec positives.vec
- opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w <ขนาด> -h <ขนาด>
