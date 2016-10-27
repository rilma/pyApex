
program qd2gdcoord

!
! Test program of apex code. Converts quasi-dipole to geodetic coordinates
!

  implicit none

  real(4)		:: epoch, prec, error
  real(4)		:: glat, glon, alt
  real(4)		:: qlat, qlon

  epoch = 2003.75
  !qlat = 0.
  !qlon = 0.
  !qlat = 0.488
  !qlon = -4.818
  qlat = 0.412
  qlon = -4.686
  alt = 150.
  prec = -1.

  print *
  print *, 'QUASI-DIPOLE TO GEODETIC COORDINATES'
  print '(a8,f8.3, a7,f8.3, a7,f8.3)', 'EPOCH=',epoch, ', QLAT=',qlat, ', QLON=',qlon

  call qd2gd(qlat,qlon,alt,epoch,prec,glat,glon,error)

  print '(a8,f8.3, a7,f8.3, a7,f8.3)', 'ALT=',alt, ', GLAT=',glat, ', GLON=',glon

end program qd2gdcoord


!*******************************************************************************


subroutine qd2gd(qlat,qlon,alt,epoch,prec,glat,glon,error)

  implicit none

  character(128)	:: apexshfile='apexsh.dat'
  real(4)		:: epoch, prec, error
  real(4)		:: glat, glon, alt
  real(4)		:: qlat, qlon
  
  ! Loading the expansion coefficients file
  call loadapxsh(apexshfile, epoch)

  ! Converting to geodetic coordinates
  call apxq2g(qlat,qlon,alt,prec,glat,glon,error)

end subroutine qd2gd


