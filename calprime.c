/*      value : 2147483647

        elapsed time testing
        P3-1000:Intel Pentium III Dual (Coppermine) stepping 10 -> 39 sec
        P3-1000:Intel Pentium III Dual (Coppermine) stepping 10 -> 39 sec
        P3-800:Intel Pentium III (Coppermine) stepping 06       -> 50 sec
        P3-650:Intel Pentium III (Coppermine) stepping 01       -> 59 sec
        P3-550:Intel Pentium III (Katmai) stepping 03           -> 70 sec
        K6-300:AMD-K6(tm) 3D processor stepping 0c              -> 160 sec
	

        USparcIV+  1.5G SF-E20K 16cpu                           -> 57.423067 sec
        USparcIII+ 1.2G SF-V880 4cpu                            -> 77.658008 sec
        USparcT1   1.2G SF-T2000 1cpu 8core                     -> 149.486597 sec
        IBM-P570:Power CPU                                      -> 28.4 sec
        AMD Opteron 280 SF-X4200                                -> 23.345946 sec
        Intel(R) 2.9G 4CPU Sun Server                           -> 21.5sec
        Intel(R) Pentium(R) M 1.86Ghz                           -> 14.3 sec
	Intel(R) Pentium(R) D 2.66G			        -> 17.2 sec
	Intel(R) Pentium(R) Dual Core E2140			-> 8.12 sec
	Intel(R) Core(TM)2 T7200 2.0G				-> 7.26 sec
	Intel(R) Pentium(R) Core(TM)2 Duo E7200 2.53G	        -> 4.42 sec
        made by Justin, Kim:20011009
*/

/* #ifdef WIN
// #include <stdafx.h>
// #endif
*/
#include <stdio.h>
/* #ifdef WIN
// #include <sys/timeb.h>
// #else
*/
#include <sys/time.h>
#include <unistd.h>
/* #endif
*/
#define TRUE    1
#define FALSE   0

int     isPrime(long input);
double  getTime();

int main() {
        long    a;

        printf("value(2147483647) : ");
        scanf("%ld", &a);

        printf("\nresult: %d(1 is true)\n", isPrime(a));

        return 0;
}

int     isPrime(long input) {

        long    temp;
        long    onepercent = 0;
        long    printpct;
        int     percent = 1;
        int     ret = TRUE;
        double  time;

        if(0 < input && input < 3)
                return TRUE;

        if(input & 0x01 == 0x00)
                return FALSE;

        printpct = onepercent = input / 100;
        time = getTime();
        for( temp = 3; temp < input; temp+=2 ) {
                if(printpct < temp && percent <= 100) {
                        printf("%3d> %ld mod %ld = %ld(%ld)\n", percent, input, temp, input % temp, printpct);
                        percent++;
                        printpct += onepercent;
                }
                if(input % temp == 0) {
                        ret = FALSE;
                        break;
                }
        }
        printf("elapsed time(sec.usec) : %lf\n", getTime() - time);

        return ret;
}


double  getTime() {
        long sec;
        long usec;
        double time = 0;

/*#ifdef WIN
//      struct _timeb timebuffer;
//      _ftime(&timebuffer);
//       sec = timebuffer.time;
//      usec = timebuffer.millitm;

//      time = sec + (usec/1000.0);
//#else
*/
        struct timeval tv;
        struct timezone tz;

        gettimeofday(&tv,&tz);
        sec = tv.tv_sec;
        usec = tv.tv_usec;
        time = sec + (usec/1000000.0);
/*#endif
*/
        return time;
}
