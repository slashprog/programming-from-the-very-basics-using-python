PROGRAM Table
      IMPLICIT NONE
      INTEGER :: Number, Counter

      WRITE(*,*) 'Enter a number: '
      READ(*,*) Number

      DO Counter = 1, 10
         WRITE(*, '(I3, A, I3, A, I4)'), Number, ' x ', Counter, ' = ', Number * Counter
      END DO

      STOP
END PROGRAM Table
