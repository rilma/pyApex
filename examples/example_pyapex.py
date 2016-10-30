
from matplotlib.pyplot import figure, show
import pyapex
from scipy import arange, nan, where

if __name__ == '__main__':

    def main1():

        Obj = pyapex.ApexFL()

        date = 2003.
        dlon = -75.
        hlim = [80., 160.]

        f = figure(figsize=(16,6))

        pn = f.add_subplot(111)

        for h in arange(hlim[0], hlim[1], 10.):

            gc, qc = Obj.getFL(date=date, dlon=dlon, hateq=h, verbose=True)

            x, y, z = gc['lat'], gc['alt'], gc['lon']

            ind = where(y < hlim[0])
            if len(ind) > 0: x[ind], y[ind], z[ind] = nan, nan, nan
            pn.plot(x, y)

        pn.invert_xaxis()
        show()

    #
    # End of 'main1'
    #####

    main1()
