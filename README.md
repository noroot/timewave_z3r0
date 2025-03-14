# Terrence Mckenna TimeWaveZero Research

## Changes

- Added Apple Silicon compilation support (separate Makefile)
- Added python code for visualize timewave_data

## Compile 

### x86

`make`

### Apple Silicon (Arm64)

`make -f Makefile.macos`

## Usage 

```
Usage: twz [dtz] [neg] [step] [wf].
 dtz = days to zero-point
 step = steps in which to decrement time (in minutes)
 wf = wave factor (default 64, range 2-10000)

This program calculates the running values of the timewave within the given window.
```


`./twz-generator 10 10 1 64 > timewave_data.csv`

`python timewave.py`


![./TimewaveZeroExample.png](./TimewaveZeroExample.png)

The purpose of this software and project is to further the
Timewave Zero research started by Terence Mckenna and others.
Calculates both with and without the infamous "Half Twist".

All programs included here can calculate both BEFORE and 
AFTER the zero-point.

An in-depth explanation of the software can be found in a book 
called "The Invisible Landscape".
ISBN-10: 0062506358
ISBN-13: 978-0062506351


The software is open-sourced / public domain and is based upon
publicly-released software by the original Timewave Zero author.



== USAGE: ==

1) Download the software
2) Run "make"
3) Run the produced programs


== Examples: ==

Calculate the timewave from 100 days before zero-point
with 0.1 minute resolution, at a wave-factor of 2.
Save the output to a file named timewave.csv

    ./twz-generator 100 0.1 2 > timewave.csv

    The timewave.csv file can then be opened in a spreadsheet
    program, such as OpenOffice, and graphed.
    
    
Calculate the timewave from 0 days before zero-point
to 1 day after the zero-point with 10e-5 minute resolution, 
at a wave-factor of 2

    ./twz-generator-threaded 0 1 10e-5 2
    
    
Calculate the timewave from 2 days after the zero-point
to 2.001 days after the zero-point with 1 minute resolution, 
at a wave-factor of 2

    ./twz-generator -2 2.001 1 2 


Calculate the timewave value at 2 days before,
1e-12 days before, and 20.5 days after the zero-point
at a wave-factor of 6

    ./twz-point 2 1e-12 -20.5 wf=6
    
    
== Programs == 

 twz-point:
 Calculate the timewave value at a given point	
.
 twz-generator
 Calcluate a running timewave, useful for graphing.

 twz-generator-threaded
 Calcluate a running timewave using multiple calculation threads
 Useful for graphing on multicore computers


 
== Upgrades to the Original Code ==
 
 * Can calculate Timewave before and AFTER the zero point 
 * Can calculate a Window of the timewave data
 * Calculates and prints timewave values with 16 significant digits
 * Optimized code specifically for Intel/AMD x86_64 CPU's (most common today)
 * Better calculation precision than original code
 * 32-bit integer variables upgraded to 64-bit (uint64_t)
 * 64-bit floating point variables upgraded to extended-precision 80-bit (long double)
 * Switched floating-point calculations to SSE, freeing the FPU registers
 * Enabled MMX optimizations (uses freed FPU registers)
 * Make use of SSE2 CPU optimizations
 
