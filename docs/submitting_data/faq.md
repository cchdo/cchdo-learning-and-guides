# Frequently Asked Questions (FAQ)
Find answers to commonly asked questions related to data submission.

## Where can I find quality control flag definitions?
The CCHDO uses WOCE quality flags that can be found in our [detailed submission guidelines](../submitting_data/detailed_guide.md#data-quality-evaluation-and-data-quality-flags). 
```{caution}
There are three distinct sets of flag definitions: one for CTD data, one for discrete bottle samples, and one for the bottle itself. 
```


---

 ## What do I do with replicates?
The CCHDO asks for one value to be reported per sample, and for this value to be determined by the data originator following whatever method they would prefer. The CCHDO requests that any mathematical operations on values, such as averaging, be performed by the data originator. Values that result from averaging should be flagged `6` and detailed in the cruise report.

If there is any reason that multiple values for one sample must be reported, please contact [cchdo@ucsd.edu](mailto:cchdo@ucsd.edu) before submission.

---

## Should I submit my data to NCEI as well?
No. The CCHDO archives all core data at NCEI, so please do not submit there. If your data are not in the core dataset (and fall under "ancillary data"), then you can submit these data to NCEI. 

---

## Where can I find the GO-SHIP submission schedule requirements?
- **US GO-SHIP**: [https://usgoship.ucsd.edu/cruise-data-submit-download/](https://usgoship.ucsd.edu/cruise-data-submit-download/)  
- **Non-US GO-SHIP**: [http://www.go-ship.org/DatReq.html](http://www.go-ship.org/DatReq.html)

---

## Can I submit underway data to CCHDO?
CCHDO accepts only discrete CTD and bottle data from repeat hydrography cruises, such as those conducted under GO-SHIP. Underway data — including continuous surface measurements, meteorological observations, or navigation data — are not managed by CCHDO, even if collected during a GO-SHIP cruise.

If you have underway data to archive, we suggest you work with your funding agency and national oceanographic data center(s) to identify an appropriate repository. In the US, raw underway data are managed by the [Rolling Deck to Repository program](http://www.rvdata.us) for the [US Academic Research Fleet](https://www.unols.org/ships-facilities/unols-vessels/unols-designated-vessels/unols-designated-vessels). If you have a post-processed product from a US vessel, we recommend submitting to NOAA's National Centers for Environmental Information (NCEI), via their [submission tool](https://www.ncei.noaa.gov/archive/send2ncei/).

```{note}
Discrete surface measurements collected via the underway system that correspond to specific station locations may be submitted to CCHDO for integration into the bottle data file (i.e., added as rows representing 0 dbar).
```
