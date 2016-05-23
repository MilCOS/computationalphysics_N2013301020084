program potential
implicit none
real :: delta0=0.01,init1,init2
integer,parameter :: L=30 ! change L
integer :: i,N=0
real,allocatable :: V0(:,:)
allocate(V0(-L/2:L/2,-L/2:L/2))
V0 = 0
V0(-L/10,-L/10:L/10)=1
V0(L/10,-L/10:L/10)=-1
do while (delta0 > 0.0001)
  call laplace(V0,delta0)
  N = N+1
end do
call store(V0)
write(*,*) N ! N_iter
deallocate(V0)
contains
  subroutine sor_update(V)
  implicit none
  integer :: i,j
  real,parameter :: pi =3.1415926
  real,allocatable :: V(:,:)
  real :: alpha,temp_V
    !allocate(V(-L/2:L/2,-L/2:L/2))
    alpha = 2./(1.+pi/L)
    do i = -L/2+1,L/2-1
      do j = -L/2+1,L/2-1
        if ((abs(i)==L/10).and.(abs(j)<=L/10)) cycle
        temp_V = 1./4.*(V(i-1,j)+V(i+1,j)+V(i,j-1)+V(i,j+1))
        V(i,j) = alpha * (temp_V - V(i,j)) + V(i,j)
      end do
    end do
    write(*,*) 'pinkie pie'
  end subroutine

  subroutine laplace(V,delta)
  implicit none
  real :: delta
  real :: init1,init2
  real,allocatable :: V(:,:)
    !allocate(V(-L/2:L/2,-L/2:L/2))
    init1 = sum(V)
    call sor_update(V)
    init2 = sum(V)
    delta = abs(init1 - init2)
    write(*,*) delta
    !do while (abs(delta) > 0.0001)
    !  init1 = sum(V)
    !  call sor_update(V)
    !  init2 = sum(V)
    !  delta = (init1 - init2)
    !end do
    write(*,*) "pinkie pie"
  end subroutine

  subroutine store(V)
  implicit none
  integer :: stat
  real,allocatable :: V(:,:)
  integer :: i,j
    !allocate(V(-L/2:L/2,-L/2:L/2))
    open(unit=8,file='sor_method.txt',action='readwrite',status='replace',iostat=stat)
    do i =-L/2,L/2,1
      write(unit=8,fmt='(51(1X,F7.4,1X))') V(i,:)
    end do
    rewind(unit=8)
    write(*,*) 'pinkie pie'
  end subroutine

end program
