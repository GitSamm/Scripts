# This script joins a bunch of movie clips together with the mp4 extenstion and 
# outputs it to a file called Movie.mp4. 

# This script assumes that you have files in the current directory with the 
# .mp4 extenstion.

# with a bash for loop
for f in ./*.mp4; do echo "file '$f'" >> mylist.txt; done

ffmpeg -f concat -safe 0 -i mylist.txt -c copy Movie.mp4