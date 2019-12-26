import argparse
import sys

def get_parser(argv):
    parser = argparse.ArgumentParser(description="quick buying ticket")
    parser.add_argument("operate", type=str, nargs=1, metavar="OPERATE",
    help="r: run program c: scan cdn t: test email server")
    return parser.parse_args(argv)
def main():
    operate, = get_parser(sys.argv[1:]).operate
    if operate == "r":
        run()
    elif operate == "c":
        scan()
    elif operate == "t":
        test()        
        
    
if __name__ == "__main__":
    main()
