import os
import argparse
def rename(file_path,extension):
	try:
		if os.listdir(file_path)==[]:
			print('No files found in specified direcory')
		else:
			files = os.listdir(file_path)
			print("\n",files)
			i = 1
			for file in files:
				if extension[0]!='.':
					print('''Make sure you enter extension with a dot in front
					     .jpg, .mp3, .mp4''')
				else:
					os.rename(os.path.join(file_path, file), os.path.join(file_path, str(i)+extension))
					i = i+1
				print('Renaming Done :)')
	except FileNotFoundError:
		print('''Invalid Directory
			Make sure you enter the full path if you re running this script outside the directory
			something like the example below

			>> python3 rename.py --file /home/user/directory_of_your_files''')			
					
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",help="Directory containing files to be renamed",type=str)
    parser.add_argument("--ext",help="extension fo your files",type=str)
    args = parser.parse_args()
    rename(args.file,args.ext)  

if __name__ == '__main__':
	main()

