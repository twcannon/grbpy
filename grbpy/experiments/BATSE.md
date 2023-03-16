# Burst Data Documentation

## BATSE

### Basic Table
#### *Location*
https://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/basic_table.txt
#### *File Format*

This file specifies the locations and times for 2702 triggered gamma-ray bursts 
observed from 19 April, 1991 until 26 May, 2000. It therefore includes the data 
from the 4B catalog.

Bursts since the end of the 1B catalog (March 1992) occurred when the GRO tape 
recorders were experiencing numerous errors. Consequently, there are gaps in the 
data of many bursts that preclude valid measurement of peak flux, peak rate, fluence, 
or duration. Peak rates on the 1 second timescale from each detector are almost always 
available. These data (called MAXBC rates) can be used to determine burst location. 
Previous difficulties with this data type have been largely removed, and we now believe 
that the systematic errors for MAXBC-located bursts are the same as for bursts located 
with other data types. It is still true however, that the MAXBC-located bursts usually 
have larger statistical errors than would be the case if another data type were available. 
The comments table provides "L" comments for MAXBC-located bursts. A number of CGRO and 
BATSE flight software changes have significantly reduced the problem of data gaps since 
March of 1993.

The on-board software determines when a trigger occurs. When a burst trigger occurs, 
subsequent triggers are disabled for an accumulation period, during which the BATSE burst 
memories accumulate data. The accumulation period was 242 seconds until Dec 17, 1992, and 
from Jan 8, 1996 to Feb 25, 1997. At all other times it has been 573 seconds. The stored 
burst data are then transmitted; the readout time for all triggers was 90 minutes until 
Dec 17, 1992. At that date, the flight software was revised to suspend readouts during 
telemetry gaps and to truncate readouts of weak events. This resulted in a variable readout 
time. During the burst data readout, the 64 ms threshold is revised to correspond to the 
maximum rate attained by the current burst, and triggering is disabled on the 256 ms and 
1024 ms timescales. Bursts intense enough to trigger over this revised 64 ms value are termed 
"overwrites". They appear as triggers in this file, with the overwrite flag is set to 'Y'.

The BATSE trigger numbers correlate all the files for this catalog. The trigger number 
is a running sequence of BATSE triggers which include cosmic bursts, solar flares and other 
events. The sequence begins with trigger 105 and ends with trigger 5586.

Each burst has a unique catalog name. These BATSE catalog names later may be incorporated 
into a multi-spacecraft catalog with "GB" or "GRB" replacing this designation of "4B". The 
characters "4B " begin every BATSE catalog burst name, followed by the "yymmdd" of the burst. 
"yymmdd" is the two digit year, two-digit month, and two digit day. When more than one 
gamma-ray burst occurs on one day, those bursts have a single letter suffix (B,C,D...), 
generally in order of intensity. Example: 4B 920503B refers to the second brightest burst 
that triggered BATSE May 3, 1992. The brightest burst on that day will have no suffix.

The burst trigger time is the end of the interval (64, 256 or 1024 ms) on which the burst 
triggered the detector.

The error in angular location is the radius of a circle having the same area as the 68% 
confidence ellipse defined by the formal covariance matrix from a chi^2 fit on the assumption 
of normal errors. The error is based solely on the Poisson uncertainty in the BATSE measurement 
of burst flux by each Large Area Detector. There is, in addition, an RMS systematic error of 
approximately 1.6 degrees. Adding 1.6 degrees in quadrature to the error in the table yields 
our estimate of the 68% confidence interval for the burst location error. The statistical 
error is believed to be Gaussian. The systematic error distribution has a more extended tail 
than a Gaussian.

There are twelve columns in this file:

1. The BATSE trigger number.
2. The BATSE Catalog burst name.
3. The truncated Julian Date (TJD) of the trigger TJD = JD - 2440000.5
4. The time in decimal seconds of day (UT) of the trigger.
5. Right ascension (J2000) in decimal degrees.
6. Declination (J2000) in decimal degrees.
7. Galactic longitude in decimal degrees.
8. Galactic latitude in decimal degrees.
9. Radius in decimal degrees of positional error box.
10. Angle in decimal degrees of geocenter (the angle between the burst and the nadir, as measured from the satellite).
11. Overwrite flag: Y(true) if this burst overwrote an earlier, weaker trigger. N(false) otherwise.
12. Overwritten flag: Y(true) if this burst was overwritten by a later, more intense trigger. N(false) otherwise.

### Duration Table
#### *Location*
https://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/duration_table.txt
#### *File Format*

This table contains values for T90 and T50, quantities related to burst 
duration, for 1234 gamma-ray bursts that triggered the BATSE LAD detectors 
between April 1991 and 29 August 1996.  T90 measures the duration of the time 
interval during which 90% of the total observed counts have been detected.
The start of the T90 interval is defined by the time at which 5% of the
total counts have been detected, and the end of the T90 interval is defined
by the time at which 95% of the total counts have been detected.  T50 is
similarly defined using the times at which 25% and 75% of the counts have 
been detected.  T90 and T50 are calculated using data summed over the 4 LAD 
discriminator channels and using data summed over only those detectors that 
satisfied the BATSE trigger criteria.  

Users must note that T90 and T50 are not available for those bursts
which suffer from data gaps during the event; the integration procedure
inherently fails in these cases.  However, visual estimates of the burst 
duration are provided in the BATSE Comments table for those bursts with 
sufficient data coverage.  Users may also find other pertinent comments
concerning the calculated value of T90 and T50 in the BATSE COMMENTS
table, and it is highly recommended that the COMMENTS table be consulted
before any distribution selected on T90 or T50 is used.

The table has seven columns, defined as follows:  
1. The BATSE trigger number. This number can be used for cross-referencing with other tables in this BATSE catalog.  
2. T50.  
3. Uncertainty in T50.
4. The start time of the T50 interval, relative to the trigger time. The trigger time can be found in the BASIC Table.
5. T90.
6. Uncertainty in T90.
7. The start time of the T90 interval, relative to the trigger time.

All columns are in units of seconds.
The measurements for trigger 148 were recalculated after errors in the
3B values were brought to our attention by Jay Norris.



### 64ms Data
#### *Location*
Raw Data: https://heasarc.gsfc.nasa.gov/FTP/compton/data/batse/ascii_data/64ms/  
Single Download: https://gammaray.nsstc.nasa.gov/batse/grb/lightcurve/
#### *File Format*

trig# npts nlasc 1preb followed by 4-chan count rates (64-ms bins)

105 2496 1856 0

The first line (always the same) describes four important parameters, example values of 
which are listed in the second line (ASCII format = 4I6):

- 1st parm (trig#): unique BATSE trigger number
- 2nd parm (npts): total number of samples to follow, per energy channel
- 3rd parm (nlasc): total number of DISCLA 64-ms samples concatenated prior to PREB
- 4th parm (1preb): first PREB sample number after last 1.024-s DISCLA  sample

This data type is a concatenation of three standard BATSE data types, DISCLA, PREB, and DISCSC. 
All three data types are derived from the on-board data stream of BATSE's eight Large Area 
Detectors (LADs), and all three data types have four energy channels, with approximate channel 
boundaries: 25-55 keV, 55-110 keV, 110-320 keV, and >320 keV.

DISCLA data is a continuous stream with 1.024-s resolution, and is independent of burst occurrence. 
PREB data covers the interval 2.048 s just prior to a burst trigger. DISCSC nominally covers an 
interval of ~4 minutes starting just after trigger (early in the GRO mission, up to trigger #2099), 
or ~10-11 minutes (trigger #2101 and later). The adjustment to longer time was made to accommodate 
solar flares. Nearly all cosmic gamma-ray bursts are contained within the earlier DISCSC allotment 
of ~4 minutes. PREB and DISCSC have 64-ms resolution.  

To realize a uniformly binned data stream that covers a sufficient interval prior to a burst 
(for purpose of fitting background), we constructed the concatenated data type for all cosmic bursts 
where DISCLA, PREB, and DISCSC exist, and where DISCLA data overlaps PREB (no gap allowed at that 
juncture), as follows:  

The counts in each 1.024-s DISCLA sample were divided equally into 16 64-ms samples, with the last 
DISCLA sample, which can overlap the PREB data, being truncated. The truncation was accomplished 
by subtracting the counts in that portion of the PREB data which overlaps the last DISCLA sample, 
then equally dividing the remaining DISCLA counts into 16 samples or fewer (once in ~16 occurrences 
there is no overlap with PREB). Whereas DISCLA and PREB exist for all eight LADs, DISCSC 
(as transmitted to the ground) is summed only over those detectors which triggered on a burst. 
Therefore, only counts from the triggered detectors for the DISCLA and PREB types are summed and 
concatenated with DISCSC. Several count-summation and timing checks were made per burst to 
determine that the correct temporal correspondence was realized.  

In the earlier part of the mission when only ~4 minutes of DISCSC data was available, additional 
DISCLA data was concatenated after the end of DISCSC data to attempt to cover the whole burst 
and provide some background interval, pre and post burst. In any case, the maximum number of 64-ms samples concatenated is 8187 (524 s), save for nine exceptions for very long bursts (triggers 148, 2287, 3448, 3567, 3639, 3930, 5446, 5693, 6125) which can use up to 16379 samples.  

Infrequently, gaps occur in some portion of the data stream; gaps are filled with zeroes in 
all four channels.

---
