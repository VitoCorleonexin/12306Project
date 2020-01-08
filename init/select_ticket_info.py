from agency.cdn_utils import open_cdn_file


class Select:

    """
    quick buying channel
    """
    
    def __init__(self):
        self.cdn_list = open_cdn_file("filter_cdn_list")


if __name__ == "__main__":
    s = Select()
    cdn = s.station_table("长沙", "深圳")
