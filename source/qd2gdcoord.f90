
subroutine gd2qd(glat,glon,alt,epoch,vecflag,apexshfile,qlat,qlon,f1,f2,f)

  implicit none

  character(256), intent(in)  :: apexshfile
  real(4), intent(in)         :: epoch
  real(4), intent(in)         :: glat, glon, alt
  integer(4), intent(in)      :: vecflag
  real(4), intent(out)        :: qlat, qlon
  real(4), intent(out)        :: f1(1:2), f2(1:2), f

  ! Loading the expansion coefficients file
  call loadapxsh(apexshfile, epoch)

  ! Converting to quasi-dipole coordinates
  call apxg2q(glat,glon,alt,vecflag,qlat,qlon,f1,f2,f)

end subroutine gd2qd


subroutine gd2all(glat,glon,alt,hr,epoch,vecflag,apexshfile,qlat,qlon,mlat,mlon,f1,f2,f,d1,d2,d3,d,e1,e2,e3)

  implicit none

  character(256), intent(in)  :: apexshfile
  real(4), intent(in)         :: epoch
  real(4), intent(in)         :: glat,glon,alt,hr
  integer(4), intent(in)      :: vecflag
  real(4), intent(out)        :: qlat,qlon,mlat,mlon
  real(4), intent(out)        :: f1(1:2), f2(1:2), f
  real(4), intent(out)        :: d1(1:3), d2(1:3), d3(1:3), d
  real(4), intent(out)        :: e1(1:3), e2(1:3), e3(1:3)
  

  ! Loading the expansion coefficients file
  call loadapxsh(apexshfile, epoch)

  ! Converts to quasi-dipole coordinates
  call apxg2all(glat,glon,alt,hr,vecflag,qlat,qlon,mlat,mlon,f1,f2,f,d1,d2,d3,d,e1,e2,e3)

end subroutine gd2all


subroutine qd2gd(qlat,qlon,alt,epoch,prec,apexshfile,glat,glon,error)

  implicit none

  character(256), intent(in)  :: apexshfile
  real(4), intent(in)         :: epoch, prec
  real(4), intent(in)         :: qlat, qlon, alt
  real(4), intent(out)        :: glat, glon, error

  ! Loading the expansion coefficients file
  call loadapxsh(apexshfile, epoch)

  ! Converting to geodetic coordinates
  call apxq2g(qlat,qlon,alt,prec,glat,glon,error)

end subroutine qd2gd
