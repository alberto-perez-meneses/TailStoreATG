import os, unixUtil,sys

def main(mifile="demo.txt"):
    if(os.path.exists(mifile)):
        lines = unixUtil.tail(mifile, 20)
        for line in lines:
            print (line)

if __name__ == '__main__':
    print(len(sys.argv))
    if(len(sys.argv)> 1):
    #if sys.argv[1] is not None:
        #main(str(sys.argv[1]));

        unixUtil.ListFiles(str(sys.argv[1]))
