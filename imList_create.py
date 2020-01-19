import os
import sys

def main(outName, imPath):
    version = 1.0
    imFormat = ['.jpg', '.JPG', '.png']

    with open(outName, 'w') as f:
        f.write('<?xml version="{0}"?>\n'.format(version))
        f.write('<opencv_storage>\n')
        f.write('\t<images>\n')
        for file in fild_all_files(imPath):
            ext = os.path.splitext(file)[1]
            if ext in imFormat:
                f.write('\t\t{0}\n'.format(file))

        f.write('\t</images>\n')
        f.write('</opencv_storage>')   

def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    if (argc != 3):
        print('Usage: # python %s outName imagePath' % argvs[0])
        quit()
    else:
        main(argvs[1], argvs[2])