# Apex model Apps

This app represents a wrapper to the [Apex model](http://onlinelibrary.wiley.com/doi/10.1029/2010JA015326/abstract) which converts geodetic to quasi-dipole geomagnetic coordinates and viceversa. It also computes apex coordinates.

### Installing

```
python setup install
```

## Running the test

### Convert quasi-dipole to geodetic coordinates

```
>>> import pyapex
>>> pyapex.Convert().qdtogd(0,0,0,2000,0)
(-12.57141399383545, -71.6852035522461, 4.1826197048067115e-06)
```

### Convert to apex coordinates

```
>>> from pyapex.apex import apex
>>> apex(2000,0,0,0)
(1.0490329265594482, -12.485759735107422, 72.6435317993164, 31408.029296875, 27464.94140625, -3504.1533203125, -14827.7548828125, 21.084653854370117)
```

## License

This project is licensed under the [GNU License](LICENSE).

