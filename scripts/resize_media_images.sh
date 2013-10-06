#!/bin/sh

find ../media -name "*.png" | grep -v "\-low" | grep -v "\-med" | sed 's/\.png$//' | awk -F ' ' '{print "convert "$1".png -resize 50% "$1"-med.png"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

find ../media -name "*.jpg" | grep -v "\-low" | grep -v "\-med" | sed 's/\.jpg$//' | awk -F ' ' '{print "convert "$1".jpg -resize 50% "$1"-med.jpg"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

find ../media -name "*.png" | grep -v "\-low" | grep -v "\-med" | sed 's/\.png$//' | awk -F ' ' '{print "convert "$1".png -resize 30% "$1"-low.png"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

find ../media -name "*.jpg" | grep -v "\-low" | grep -v "\-med" | sed 's/\.jpg$//' | awk -F ' ' '{print "convert "$1".jpg -resize 30% "$1"-low.jpg"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh