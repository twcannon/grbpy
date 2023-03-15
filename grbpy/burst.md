# Burst Data Documentation

## Experiments

---

### BATSE

#### 64ms Data

##### Location

Raw Data: https://heasarc.gsfc.nasa.gov/FTP/compton/data/batse/ascii_data/64ms/  
Single Download: https://gammaray.nsstc.nasa.gov/batse/grb/lightcurve/

##### File Format

trig# npts nlasc 1preb followed by 4-chan count rates (64-ms bins)

105 2496 1856 0

The first line (always the same) describes four important parameters, example values of which are listed in the second line (ASCII format = 4I6):

1st parm (trig#): unique BATSE trigger number
2nd parm (npts): total number of samples to follow, per energy channel
3rd parm (nlasc): total number of DISCLA 64-ms samples concatenated prior to PREB
4th parm (1preb): first PREB sample number after last 1.024-s DISCLA  sample

This data type is a concatenation of three standard BATSE data types, DISCLA, PREB, and DISCSC. All three data types are derived from the on-board data stream of BATSE's eight Large Area Detectors (LADs), and all three data types have four energy channels, with approximate channel boundaries: 25-55 keV, 55-110 keV, 110-320 keV, and >320 keV.

DISCLA data is a continuous stream with 1.024-s resolution, and is independent of burst occurrence. PREB data covers the interval 2.048 s just prior to a burst trigger. DISCSC nominally covers an interval of ~4 minutes starting just after trigger (early in the GRO mission, up to trigger #2099), or ~10-11 minutes (trigger #2101 and later). The adjustment to longer time was made to accommodate solar flares. Nearly all cosmic gamma-ray bursts are contained within the earlier DISCSC allotment of ~4 minutes. PREB and DISCSC have 64-ms resolution.  

To realize a uniformly binned data stream that covers a sufficient interval prior to a burst (for purpose of fitting background), we constructed the concatenated data type for all cosmic bursts where DISCLA, PREB, and DISCSC exist, and where DISCLA data overlaps PREB (no gap allowed at that juncture), as follows:  

The counts in each 1.024-s DISCLA sample were divided equally into 16 64-ms samples, with the last DISCLA sample, which can overlap the PREB data, being truncated. The truncation was accomplished by subtracting the counts in that portion of the PREB data which overlaps the last DISCLA sample, then equally dividing the remaining DISCLA counts into 16 samples or fewer (once in ~16 occurrences there is no overlap with PREB). Whereas DISCLA and PREB exist for all eight LADs, DISCSC (as transmitted to the ground) is summed only over those detectors which triggered on a burst. Therefore, only counts from the triggered detectors for the DISCLA and PREB types are summed and concatenated with DISCSC. Several count-summation and timing checks were made per burst to determine that the correct temporal correspondence was realized.  

In the earlier part of the mission when only ~4 minutes of DISCSC data was available, additional DISCLA data was concatenated after the end of DISCSC data to attempt to cover the whole burst and provide some background interval, pre and post burst. In any case, the maximum number of 64-ms samples concatenated is 8187 (524 s), save for nine exceptions for very long bursts (triggers 148, 2287, 3448, 3567, 3639, 3930, 5446, 5693, 6125) which can use up to 16379 samples.  

Infrequently, gaps occur in some portion of the data stream; gaps are filled with zeroes in all four channels.

---
