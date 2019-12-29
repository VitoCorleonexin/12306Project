import argparse
import sys


def parser_arguments(argv):
    """
    :param argv
    :return:
    """
    parser = argparse.ArgumentParser(description="Quick buying ticket")
    parser.add_argument("operate", metavar="OPERATE", nargs=1, type=str, help="r: running program"
                                                                              "c: filtering cdn"
                                                                              "t: testing email")
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parser_arguments(sys.argv[1:])
    operator, = args.operate
    if operator == "r":
        from init import select_ticket_info
        select_ticket_info.select().main()
    elif operator == "t":
        from config.emailConf import send_email
        from config.serverchanConf import send_server_chan
        send_email(u"buying ticket program testing")
        send_server_chan("buying ticket program testing")
    elif operator == "c":
        from agency.cdn_utils import filter_cdn
        filter_cdn()
