# with a bash for loop
for f in ./*.mp4; do echo "file '$f'" >> mylist.txt; done

ffmpeg -f concat -safe 0 -i mylist.txt -c copy Movie.mp4