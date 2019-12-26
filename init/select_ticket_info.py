class Select:
    """
    quick buying channel
    """
    
    __init__(self):
        self.cdn_list = open_cdn_file("filter_cdn_list")

if __name__ == "__main__":
    s = Select()
    cdn = s.station_table("长沙", "深圳")
