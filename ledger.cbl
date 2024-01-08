       IDENTIFICATION DIVISION.
       PROGRAM-ID. LEDGER.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT TRANSACTION-FILE ASSIGN TO "TRANSACTION.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD TRANSACTION-FILE.
       01 TRANSACTION-RECORD.
           05 TRX-SENDER PIC X(20).
           05 TRX-RECIPIENT PIC X(20).
           05 TRX-AMOUNT PIC 9(10)V99.
           05 TRX-TIMESTAMP PIC 9(10).

       WORKING-STORAGE SECTION.
       01 WS-EOF PIC X VALUE 'N'.
           88 EOF VALUE 'Y'.
       01 WS-TRANSACTION.
           05 WS-SENDER PIC X(20).
           05 WS-RECIPIENT PIC X(20).
           05 WS-AMOUNT PIC 9(10)V99.
           05 WS-TIMESTAMP PIC 9(10).

       PROCEDURE DIVISION.
       OPEN-FILE.
           OPEN EXTEND TRANSACTION-FILE.
           IF FILE-STATUS NOT = '00'
               DISPLAY 'ERROR IN FILE OPENING'
               STOP RUN.

       WRITE-TRANSACTION.
           MOVE WS-SENDER TO TRX-SENDER.
           MOVE WS-RECIPIENT TO TRX-RECIPIENT.
           MOVE WS-AMOUNT TO TRX-AMOUNT.
           MOVE WS-TIMESTAMP TO TRX-TIMESTAMP.
           WRITE TRANSACTION-RECORD.
           IF FILE-STATUS NOT = '00'
               DISPLAY 'ERROR IN WRITING TO FILE'
               STOP RUN.

       READ-TRANSACTION.
           PERFORM UNTIL EOF
               READ TRANSACTION-FILE
               AT END
                   SET EOF TO TRUE
               NOT AT END
                   DISPLAY TRANSACTION-RECORD
               END-READ
           END-PERFORM.

       CLOSE-FILE.
           CLOSE TRANSACTION-FILE.
           IF FILE-STATUS NOT = '00'
               DISPLAY 'ERROR IN FILE CLOSING'
               STOP RUN.

       STOP-RUN.
           STOP RUN.

       END PROGRAM LEDGER.
