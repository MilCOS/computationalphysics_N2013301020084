!
! This program is not functioning, so please do not use it.
!
module jacobi
  implicit none
  integer :: i
  integer :: j
  integer :: stat,L
  real :: delta=0,init1,init2
  real :: V(-15:15,-15:15)
contains
  subroutine update(V,i,j)
  implicit none
    do i = -14,14
      do j = -14,14
        if ((abs(i)==3).and.(abs(j)<=3)) cycle
        V(i,j) = 1/4*(V(i-1,j)+V(i+1,j)+V(i,j-1)+V(i,j+1))
      end do
    end do
  end subroutine
  
  subroutine laplace(V,delta)
  implicit none
    do while (delta > 0.0001)
      init1 = sum(V)
      call update(V,i,j)
      init2 = sum(V)
      delta = (init1 - init2) 
    end do
  end subroutine
  
  subroutine store(V)
    open(unit=10,file='jacobi.txt',action='readwrite',status='replace',iostat=stat)
    do i =-L/2,L/2,1
      write(unit=10) V(i,:)
    end do
    rewind(unit=10)
  end subroutine
end module jacobi

program potential
use jacobi
implicit none
integer,parameter :: L=30
allocate(V(-L/2:L/2,-L/2:L/2))
call laplace(V,0)
call store(V)

end program potential
