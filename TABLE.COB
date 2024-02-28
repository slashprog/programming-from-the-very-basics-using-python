IDENTIFICATION DIVISION.
PROGRAM-ID. TABLE.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Number PIC 9(3).
01 Counter PIC 9(3) VALUE 1.

PROCEDURE DIVISION.
    DISPLAY "Enter a number:".
    ACCEPT Number.

    PERFORM UNTIL Counter > 10
        DISPLAY Number " x " Counter " = " (Number * Counter)
        ADD 1 TO Counter
    END-PERFORM.

    STOP RUN.
