# Apex model Apps

This app represents a wrapper to the [Apex model](http://onlinelibrary.wiley.com/doi/10.1029/2010JA015326/abstract) which converts geodetic to quasi-dipole geomagnetic coordinates and viceversa. It also computes apex coordinates.

### Installing

```
python setup.py install
```

NOTE: It requires [TimeUtiltities](https://github.com/rilma/TimeUtilities).

## Running the test

### Convert geodetic to quasi-dipole coordinates

```
>>> from pyapex import Convert
>>> print(Convert().gdtoqd(0,0,0,2000,1))
(-12.668910026550293, 72.45586395263672, array([ 1.02935767,  0.01941072], dtype=float32), array([-0.15145837,  1.0626893 ], dtype=float32), 1.0968272686004639)
```

### Convert quasi-dipole to geodetic coordinates

```
>>> from pyapex import Convert
>>> print(Convert().qdtogd(0,0,0,2000,0))
(-12.57141399383545, -71.6852035522461, 4.1826197048067115e-06)
```

### Convert magnetic longitude to magnetic local time

```
>>> from datetime import datetime
>>> from pyapex import Convert        
>>> print(Convert().mlon2mlt(69., datetime(1960,11,21,0,0,0)))
23.916422526041668
```

### Convert to apex coordinates

```
>>> from pyapex.apex import apex
>>> print(apex(2000,0,0,0))
(1.0490329265594482, -12.485759735107422, 72.6435317993164, 31408.029296875, 27464.94140625, -3504.1533203125, -14827.7548828125, 21.084653854370117)
```

### Geomagnetic field lines
After installation, run the example [script](examples/example_pyapex.py) to print and plot the geodetic coordinates of the field lines in the equatorial E region. Here an output example:

![alt tag] (figures/eqERegionFL.png)

## License

This project is licensed under the [GNU License](LICENSE).

