
import seaborn
from matplotlib.pyplot import figure, show
import pyapex
from scipy import arange, nan, where

if __name__ == '__main__':

    def main1():

        Obj = pyapex.ApexFL()

        year, doy = 2003, 323
        date = 2003. + doy / 365
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

        strDate = 'DATE: {:4d}.{:03d}'.format(year, doy)
        #strLoc = 'GEOG. LON.: {:6.2f}$^\circ$'.format(dlon)
        strLoc = 'GEOG. LON.: {:6.2f}$^\circ${:s}'.format(abs(dlon), 'E' if dlon > 0. else 'W') 
        title = '{:s}    -    {:s}'.format(strDate, strLoc)
        pn.set_title(title)
        pn.set_xlabel("Geog. Lat. ($^\circ$)")
        pn.set_ylabel("Altitude (km)")
        pn.invert_xaxis()
        show()

    #
    # End of 'main1'
    #####

    main1()
