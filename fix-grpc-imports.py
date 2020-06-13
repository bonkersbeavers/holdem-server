import glob
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        work_dir = sys.argv[1]

    else:
        work_dir = '.'

    for file in glob.glob(f'{work_dir}/*.py'):
        print(file)
