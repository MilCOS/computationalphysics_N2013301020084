program potential
implicit none
real :: delta0=0.01,init1,init2
integer,parameter :: L=30 ! L in every subroutine "should" be changed if you like
real,allocatable :: V0(:,:)
allocate(V0(-L/2:L/2,-L/2:L/2))
V0 = 0
V0(-3,-3:3)=1
V0(3,-3:3)=-1
call laplace(V0,delta0)
call store(V0)
deallocate(V0)
contains
  subroutine update(V)
  implicit none
  integer :: i,j!,L=30
  real,allocatable :: V(:,:)
    do i = -L/2+1,L/2-1
      do j = -L/2+1,L/2-1
        if ((abs(i)==3).and.(abs(j)<=3)) cycle
        V(i,j) = 1./4.*(V(i-1,j)+V(i+1,j)+V(i,j-1)+V(i,j+1))
      end do
    end do
  end subroutine

  subroutine laplace(V,delta)
  implicit none
  integer :: i,j,N=1
  real :: delta
  real :: init1,init2
  real,allocatable :: V(:,:)
      init1 = sum(V)
      call update(V)
      init2 = sum(V)
      delta = abs(init1 - init2)
      write(*,*) init1,init2
    do while (delta > 0.00001)
      init1 = sum(V)
      call update(V)
      init2 = sum(V)
      delta = abs(init1 - init2)
      write(*,*) init1,init2
      N = N+1
    end do
  write(*,*) N
  write(*,*) "pinkie pie"
  end subroutine

  subroutine store(V)
  implicit none
  integer :: stat
  real,allocatable :: V(:,:)
  integer :: i,j
    open(unit=10,file='gauss_seidel.txt',action='readwrite',status='replace',iostat=stat)
    do i =-L/2,L/2,1
      write(unit=10,fmt='(51(1X,F7.4,1X))') V(i,:)
    end do
    rewind(unit=10)
  write(*,*) 'pinkie pie'
  end subroutine

end program
