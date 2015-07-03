#!/bin/sh

# med png
find ../media -name "*.png" | grep -v "\-low" | grep -v "\-med" |  grep -v "\-thumb" | sed 's/\.png$//' | awk -F ' ' '{print "convert "$1".png -resize 50% "$1"-med.png"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

# low png
find ../media -name "*.png" | grep -v "\-low" | grep -v "\-med" |  grep -v "\-thumb" | sed 's/\.png$//' | awk -F ' ' '{print "convert "$1".png -resize 30% "$1"-low.png"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

# thumb png
find ../media -name "*.png" | grep -v "\-low" | grep -v "\-med" |  grep -v "\-thumb" | sed 's/\.png$//' | awk -F ' ' '{print "convert "$1".png -thumbnail 400x300! "$1"-thumb.png"}' > exec_resize.sh
source exec_resize.sh
rm exec_resize.sh

#low jpg
find . -name "*.jpg" | grep -v "\-low" | grep -v "\-med" |  grep -v "\-thumb" | sed 's/\.jpg$//' | awk -F ' ' '{print "convert "$1".jpg -resize 30% "$1"-low.jpg"}' | sh

# med jpg
find . -name "*.jpg" | grep -v "\-low" | grep -v "\-med" |  grep -v "\-thumb" | sed 's/\.jpg$//' | awk -F ' ' '{print "convert "$1".jpg -resize 50% "$1"-med.jpg"}' | sh

#thumb jpg
find . -name "*.jpg" | grep -v "\-low" | grep -v "\-med" | grep -v "\-thumb" | sed 's/\.jpg$//' | awk -F ' ' '{print "convert "$1".jpg -thumbnail 400x300! "$1"-thumb.jpg"}' | sh
