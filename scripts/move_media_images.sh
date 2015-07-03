

# Example to renmame photo to give some context
ls | awk '{print "mv "$1" interior_room_remodel_"$1}' | sh

# Example to move caps JPG to lowercase
find . -name "*.JPG" | sed 's/\(.*\)\(\.JPG$\)/mv "\1.JPG" "\1.jpg"/g' | sh

# Move media to current directory
find . -name "*.jpg" | awk -F '!' '{print "mv \""$1"\" ."}' | sh
