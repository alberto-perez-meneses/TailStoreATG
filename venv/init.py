import os, unixUtil,sys

if __name__ == '__main__':
    if(len(sys.argv)> 2):
        unixUtil.ListFiles(str(sys.argv[1]),int(sys.argv[2]))
