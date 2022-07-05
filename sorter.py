import os
import natsort

# first load 2000 images into an array
frames_dir = r'G:\\agio_t1_oman\\omanium-tester-'

def rangeDir(dir):
	fileNames = natsort.natsorted(os.listdir(dir))
	file_count = 0

	for file in range(fileNames.index(fileNames[0]), fileNames.index(fileNames[2003]), 5):
		file_count += 1
		print('File Name: ' + str(file_count))
		print('removed : ' + fileNames[file])
		if file_count == 375:
			print("hit the end !!")
			break
		else:
			continue


rangeDir(frames_dir)

#	file_count = 0
#	for fileName in fileNames:
#		file_count += 1
#		print('File Name: ' + fileName)
#		print(file_count)

# Write function that accepts 2 params
# param 1 is an array of images
# param 2 is how many pictures need to be deleted
# param 3 is the step number, in our case every 5th number

# step_count = 0
# for i in range(1, 2004, 5):
#	step_count += 1
#	print(step_count)
#	if step_count == 375:
#		print("complete !!")
#		break
#	else:
#		continue

# if is_even(filename/5) == True:
