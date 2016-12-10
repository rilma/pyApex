if __name__ == '__main__':

    def example04():

        """ Converts magnetic longitude to magnetic local time """

        from datetime import datetime
        from pyapex import Convert

        print(Convert().mlon2mlt(69., datetime(1960,11,21,0,0,0)))

    example04()