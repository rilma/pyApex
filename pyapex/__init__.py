
from pyapex.apex import apex
from pyapex.apexqd2gd import qd2gd
import os
from scipy import arange, cos, nan, ones, pi, sin, where, zeros


# full folder name
folder = os.path.dirname(os.path.realpath(__file__))

apexshfile = os.path.join(folder, 'apexsh.dat')

# From WGS-84 ellipsoid model
REQ = 6378.1370         # REQ = equatorial Earth radius
RPO = 6356.7523         # RPO = polar Earth radius


def RGC(theta):

    """    
        Geocentric radius 
    """

    a, b = REQ, RPO

    theta = theta * pi / 180.

    return (((a**2 * cos(theta))**2 + (b**2 * sin(theta))**2) \
        / ((a * cos(theta))**2 + (b * sin(theta))**2))**.5

#
# End of 'RGC'
#####


class ApexFL:


    def __init__(self):

        pass


    def getFL(self, alt=0., date=2010., dlat=-11.95, dlon=-76.77, hateq=300., \
        mlatRange=[-10.17, 10.17], mlatSTP=.25, verbose=False):

        """
         Given a point "A" with geodetic coordinates (dlon, alt, dlat), this program estimates the
         geodetic coordinates of the geomagnetic field-line passing by this point, the equator, 
         and the conjugate hemisphere
        
         INPUTS:
            alt         -> Altitude in km
            date        -> Year and fraction (1990.0 = 1990 January 1, 0 UT)
            dlat        -> Geodetic latitude in degrees
            dlon        -> Geodetic longitude in degrees
            hateq       -> altitude over the equator, in km
            mlatRange   -> geomagnetic latitude interval, in degrees
            mlatSTP     -> geomag. latitude resolution, in degrees
            verbose     -> print on stdout
        """

        # Calculate apex radius, latitude, longitude; and magnetic field and
        # scalar magnetic potential.
        a, alat, alon, bmag, xmag, ymag, zmag, v = apex(date, dlat, dlon, alt)

        if verbose:
            print( '\nDATE = %8.3f' % date )
            print( 'GLON = %8.3f,  ALT = %8.3f, GLAT = %8.3f' % (dlon, alt, dlat) )
            print( 'ALON = %8.3f, AALT = %8.3f, ALAT = %8.3f\n' % (alon, (a - 1.) * REQ, alat) )


        # geodetic coordinates of the field-line passing by 'hateq' (both hemispheres)
        #

        # Calculates altitude along dipole field-line
        #

        r0 = hateq / REQ + 1.   # apex radius

        # 1D-array geomag. latitude
        theta = arange(mlatRange[0], mlatRange[1] + mlatSTP, mlatSTP)

        # solving for altitude along dipole field-line
        h = ((r0 * cos(theta * pi / 180.)**2) - 1.) * RGC(theta)

        #
        # Now, given dipole coordinates along field-line (alon, h, theta), calculate 
        # their correspoding geodetic coord.
        #

        epoch, prec = date, -1         

        nz = len(theta)

        glon, glat = zeros(nz), zeros(nz)
        qlat = theta
        qlon = alon * ones(nz)

        if verbose: print( '\n' )
        for i in range(nz):
            alt = h[i]
            glat[i], glon[i], error = qd2gd(qlat[i], qlon[i], alt, epoch, prec, apexshfile)
            if verbose:
                print( 'QLON = %8.3f, ALT=%8.3f, QLAT=%8.3f, GLON=%8.3f, GLAT=%8.3f' % \
                    (qlon[i], alt, qlat[i], glon[i], glat[i]) )

        # coord. of dipole field-line
        gcoord = {'lon' : glon, 'alt' : h, 'lat' : glat}        # geodetic
        qcoord = {'lon' : qlon, 'lat' : qlat}                   # quasi-dipole

        return gcoord, qcoord

    #
    # End of 'getFL'
    #####

#
# End of 'ApexFL'
#####



class Convert:


    def __init__(self):

        pass


    def qdtogd(self, qlat=0, qlon=0, alt=0, epoch=2000., prec=0):

        """
            Convert quasi-dipole to geodetic coordinates
        """

        return qd2gd(qlat, qlon, alt, epoch, prec, apexshfile)


    def gd2qd(self):

        """
            Convert geodetic to quasi-dipole coordinates
        """

        pass

#
# End of 'Convert'
#####
