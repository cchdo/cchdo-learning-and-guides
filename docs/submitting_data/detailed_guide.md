# A Guide to Submitting Data and Associated Documentation to the CCHDO

:version: V1 2024-08-08

## Overview
This guide gives recommendations for scientists and groups submitting data to the CLIVAR and Carbon Hydrographic Data Office (CCHDO) at the University of California - San Diego (UCSD) Scripps Institution of Oceanography.
The CCHDO is a Data Assembly Center for high-quality hydrographic data - meaning vertical profile data from CTD, CTD/rosette, and bottle casts covering physical and chemical parameters - from GO-SHIP and related programs.
Any vertical profile data from CTD instruments and bottles may be submitted from any oceanographic region.
Additional GO-SHIP measurements, such as underway data and ADCP data, are not managed by CCHDO. 

These guidelines are recommendations and not requirements.
CCHDO has always and will continue to accept data as provided.
However, when resources are limited, data meeting submission guidelines will have priority for assembly into standard products.
Standardizing heterogeneous data is the time-limiting step of providing our standardized product and the CCHDO can be at its most efficient when incoming data meet standards.
For an abridged version of data submission guidelines, please refer to the following [document][submission_summary].

For further information about the CCHDO and its holdings, please see: <https://cchdo.ucsd.edu/>. 

More information on the CCHDO data license policy, CCHDO use of DOIs and attribution can be found here: [](../policies_and_procedures/data_license).

For more information on the CCHDO data citation policy, please see: [](../policies_and_procedures/how_to_cite)

The CCHDO highly encourages anyone, especially first time submitters, to send us an email if they have any questions. We are very happy to help! Email us at [cchdo@ucsd.edu][cchdo_email]

### Overview of  Steps for Data Submission

1. **Send a cruise plan to the CCHDO (Optional)**

   Before a CTD/hydrographic cruise takes place, it is useful for the scientists planning the cruise to contact the CCHDO (via email to [cchdo@ucsd.edu][cchdo_email]) to provide a cruise plan and discuss data timing and any special considerations.
   Data licensing should be considered before the cruise takes place. 
1. **Apply and document appropriate sampling and analytic protocols at sea (Essential)**

   The core of reference-quality CTD/hydrographic/tracer work lies in the application *and documentation* of appropriate methodology. Review recommendations on creating unique identifiers for cruise, station, cast, and samples (see {ref}`number_scheme`) in advance, to implement while at sea.

1. Submit data and documentation to the CCHDO (Essential).

   The CCHDO *strongly* recommends that data originators submit their data using one of three formats: WHP-Exchange, CSV with suggested information, or NetCDF with suggested information; see the {ref}`formats` section for more details.

   The following minimum required ancillary information is requested in the data submission portal:

   1. Name and email address of person submitting the data
   2. Whether or not the data are public. CCHDO is intended as an open, public archive.
      Non-public data are only accepted under special circumstances and should be discussed in advance. 

   While programs such as GO-SHIP have specific timelines for data submission after a cruise (e.g. <https://usgoship.ucsd.edu/>), CCHDO accepts data at any time.
   Bottle data parameters from different measurement groups may be submitted together in a single file that has been compiled by the scientific team, or in separate files that will be combined by the CCHDO.
   Data updates that are submitted to the CCHDO following the same protocol as initial data submissions will be combined by the CCHDO into the dataset.

## Data Format and Content Guidance

### General Guidelines

(parameter-naming)=
#### Parameter Naming

*The CCHDO strongly requests that all parameters used in a CTD or bottle data file come from:*
<https://exchange-format.readthedocs.io/en/latest/parameters.html>
This list describes the parameter, how it should be named, and the expected units.
If parameters are submitted that are not in the list, the CCHDO requests the data provider send [cchdo@ucsd.edu][cchdo_email] the parameters they are requesting to be added with corresponding methods papers, if available. 

While CCHDO does not accept data outside of CTD and bottle data, we ask that contact information for the group(s) responsible for the various data should be included in the cruise report sent to the CCHDO.

#### Units

Units must be clearly stated and must match the reported data upon submission.
Data providers are encouraged to report data in the standard units given in the parameters table for consistency and ease of comparison between cruises. 

#### Data quality evaluation and data quality flags
To monitor, evaluate, maintain, and later access the data, it is advisable to keep individual records for the quality of each measurement. 
We recommend that data originators provide a quality flag for each measured value when feasible, preferably using WOCE quality flags (see {numref}`ctd_qc_flags`, {numref}`bottle_qc_flags`, and {numref}`param_qc_flags` for specific applications).
We also accept the flagging systems that are mapped in the following document and request that the alternative flagging schema used is documented in the submission notes:
<https://odv.awi.de/fileadmin/user_upload/odv/misc/ODV_QualityFlagSets.pdf>

For more information on quality assurance and documentation procedures see "[Reference-Quality Water Sample Data, Notes on Acquisition, Record Keeping, and Evaluation][swift_2018]"

(ctd-data)=
### CTD Data
Typically submitted as a directory of _ct1.csv data files or a zipped _ct1.zip directory of _ct1.csv data files of CTD profiles (described in <https://exchange-format.readthedocs.io/en/latest/ctd.html>).
Quality flags for CTD data are optional but highly recommended and should accompany every measured parameter ({numref}`ctd_qc_flags`). If flags are used, CCHDO recommends the WOCE quality flags.

```{table} WOCE Quality flag definitions for CTD data
:name: ctd_qc_flags

| Flag Value | Definition |
|---|---|
| 1 | Not calibrated |
| 2 | Acceptable measurement  |
| 3 | Questionable measurement |
| 4 | Bad measurement |
| 5 | Not reported |
| 6 | Interpolated over a pressure interval larger than 2 dbar |
| 7 | Despiked |
| 8 | (Not used for CTD data) |
| 9 | Not sampled |
```

(bottle-data)=
### Bottle Data

A submitted bottle data file, preferably a _hy1.csv file (i.e., in WHP-Exchange format, see <https://exchange-format.readthedocs.io/en/latest/bottle.html> for more details), contains the results from all small volume water sample measurements made during the cruise.
Each row should be a complete record of a sample containing cruise, station, cast, and sample/bottle number (described in depth in {ref}`number_scheme`).

The _hy1.csv file should contain columns and associated quality flags (when applicable) for every parameter measured, whether or not data values are being submitted.
Empty columns should be included for parameters intended to be submitted later to indicate to the CCHDO that additional data should be expected.
The CCHDO will merge the additional parameters into the dataset when they are received.
WOCE quality flags for the bottle ({numref}`bottle_qc_flags`) and each measured parameter ({numref}`param_qc_flags`) are optional but highly recommended.

After the initial submission of a bottle file, updated values and flags for parameters can be submitted individually as they become available.

Note that each rosette bottle has its own unique quality flag ({numref}`bottle_qc_flags`) to indicate problems associated with the sampling device that were noted either at the time the samples were drawn or found later during quality control. The combination of BTLNBR and its quality flag allows ‘problem’ bottles to be identified and tracked.

```{table} "WOCE" Quality code definitions for water **bottles**. This is a quality code in case issues arrive with the bottles on a rosette water sampler.
:name: bottle_qc_flags 

| Flag Value | Definition |
|---|---|
| 1 | Bottle information unavailable |
| 2 | No problems noted |
| 3 | Leaking |
| 4 | Did not trip correctly |
| 5 | Not reported |
| 6[^1] | Significant discrepancy in measured values between Gerard and Niskin bottles |
| 7[^1] | Unknown problem |
| 8[^1] | Pair did not trip correctly. Note that the Niskin bottle can trip at an unplanned depth while the Gerard trips correctly and vice versa |
| 9 | Sample not drawn for this bottle |
```

[^1]: These flags apply primarily to large volume samplers, which are not currently in use

```{table} "WOCE" Quality code definitions for water sample measurements 
:name: param_qc_flags 

| Flag Value | Definition |
|---|---|
| 1 | Sample for this measurement was drawn from water bottle analysis not received. This sample is expected to be sent in when analysis is complete |
| 2 | Acceptable measurement  |
| 3 | Questionable measurement |
| 4 | Bad measurement |
| 5 | Not reported |
| 6 | Mean of replicate measurements (Number of replicates should be specified in the cruise report and the replicate data tabulated there, however only one value should be reported in the data file) |
| 7 | Manual chromatographic peak measurement |
| 8 | Irregular digital chromatographic peak integration |
| 9 | Sample not drawn for this measurement from this bottle |
```

### Station summary file (Optional)
The WOCE Hydrographic Program created a station summary file format intended to gather the most critical station information into a compact ASCII file.
This is optional but useful; data providers submitting summary files are asked to follow this guidance: <https://cchdo.github.io/hdo-assets/documentation/manuals/pdf/90_1/chap4.pdf>.
If a summary file is not submitted, the CCHDO will generate a rudimentary summary file from the information in the CF-NetCDF CTD and bottle data files.


## Cruise Report - from the Chief Scientist and measurement groups (Essential)
The CCHDO requests a cruise report to accompany all cruise data.
A cruise report conveys to eventual data users all the information needed to understand the context and content of the reported data.
The CCHDO strongly prefers that cruise documentation and data reports be in English.
Reports sent in another language will be distributed as received, and will not be translated by the CCHDO. PDF and .docx (Microsoft Word) files are recommended formats for cruise reports.

Cruise reports should document the measurements made and methods used to make them, describe the contents of the data files (headers, parameters, units, quality flags, etc.), and provide complete contact information for each data provider.
This comprehensive document is typically prepared by the Chief Scientist with the help of the various data originators and is best done at sea while the teams are together and memories are fresh. 
Any needed changes to a cruise report after submission should be reported to the Chief Scientist, who can then communicate with the CCHDO to update the cruise report.

The following content is valuable to include in cruise reports. For a complete example template of a comprehensive cruise report, see {ref}`outline_cruise_report`.

* Linked table of contents
* Highlights section including general cruise information such as start and end dates, ports of call, expocode, etc.
* Cruise summary
    * A general summary of the cruise, its main goals, number of stations completed including detailed information about each station and parameters sampled, floats and drifters deployed, moorings deployed or recovered, etc.
* Table of all parameters sampled and the contact information for their respective PIs
    * Name and/or persistent unique identifier (ORCid)
    * Institution
    * Measurement/s responsible for
    * Contact information (email preferred)
* A section for every measured parameter (underway and hydrographic measurements) that includes:
    * Methods
        * Instrumentation (including manufacturer and model), chemicals used, calibration information, referenced protocols, etc.
    * At-sea sampling notes
    * Data analysis
    * Relevant figures

The CCHDO may reformat a cruise report for consistency or add additional materials received from other data originators, data quality experts, or data users.
The original materials are retained and archived by the CCHDO.

Note that each measurement group - for example, CTD, nutrients, CFCs, helium, etc. - should provide sufficient detail to establish how their data were created and to help assess the data quality. 
References to the analytical methods used should be supplied, and variations from these techniques described.
Techniques should be described in detail if no published reference exists. 

It is extremely helpful if each measurement group’s report includes an assessment of the uncertainty of the measurements and notes of any problems peculiar to the data gathered during the cruise. 

(formats)=
## Formats
In an effort to ensure a diverse community can easily exchange data and the CCHDO can streamline data processing, the CCHDO strongly recommends standard formats, consistent naming conventions, and common units for data reporting, as described below.
Standardizing heterogeneous data is intensively time consuming, and the CCHDO can best serve the community when incoming data meet standards and can be assembled efficiently.

Specifically, the CCHDO requests that, when possible, all CTD and bottle data be submitted in one of three formats.
The CCHDO encourages submitters to choose the format best fitting their current workflow.
If the user does not yet have a data workflow, the .csv option is generally easiest to set up. 

### Exchange
* The Exchange guidelines can be found here: <https://exchange-format.readthedocs.io/en/latest/common.html>
* Example {download}`Exchange Template <templates/Exchange_Template.csv>`
    * For a CTD file, replace ‘BOTTLE’ from the stamp with ‘CTD’

### A .csv that contains the following information; in the data file, please use the parameter name in parentheses, with no variations:
* If this is the first time data is submitted for a cruise:  
    * Expocode (EXPOCODE)
    * Station Number (STNNBR)
    * Cast Number (CASTNO)
    * Sample Number (SAMPNO)
    * Date (DATE)
    * Time (TIME)
    * Latitude (LATITUDE)
    * Longitude (LONGITUDE)
    * CTD pressure (CTDPRS)
* If this is a data update: 
    * Station Number (STNNBR)
    * Cast Number (CASTNO)
    * Sample Number (SAMPNO)
* Example {download}`CSV Template <templates/CSV_Template.csv>`

### NetCDF
* We recommend following the guidelines from NCEI - <https://www.ncei.noaa.gov/data/oceans/ncei/formats/netcdf/v2.0/index.html>.
  Specifically, we recommend the profile template found on the NCEI page. It is most likely that the ‘profile’ template is most relevant 
* Use netCDF names and attributes as listed in our [parameter table][parameter_table]
    * The same parameters required in the .csv format (Expocode, station, cast, sample, etc.) are required in this format
* We recommend details to be in the attributes rather than highly descriptive/assumptive variable names

<!-- 
The original souce did something that is not structually valid by "dedenting" from sections 4.1 to 4.3 back to the top level (section 4). This is impossible to repsent in HTML so I made up this new heading.
-->

### General Recomendations
As described more fully in other sections, the CCHDO also requests that all parameters within the data file should be found using our [parameter table][parameter_table] (see section {ref}`parameter-naming` for more information).
Additionally, a WOCE quality flag should be included for each measured parameter (see Sections {ref}`ctd-data` or {ref}`bottle-data` for further information).

The CCHDO does not have recommendations on header comments.
However, if there is information that should be retained with the data and is valuable in the long-term, data submitters can add header comments, preceded by # (hash sign).

For each expedition, the data submitted to the CCHDO should include the following files: 

```{table} Requested documents for every cruise

| Suffix for file type | Description of file |
|---|---|
| do.pdf do.txt | Cruise Report (e.g., cruise and data documentation in MS Word, PDF, or ASCII) |
| _hy1.csv | Bottle data file (if any water sampling took place and is being reported) |
| _ct1.csv or _ct1.zip | CTD data file(s) |
| su.txt (optional) | Station/cast summary file in original WOCE format (see <https://cchdo.ucsd.edu/manuals/pdf/90_1/chap4.pdf> for format description) |

```


(number_scheme)=
## Cruise/Station/Cast/Sample Numbering Scheme
A unique identifier is required for each CTD/hydrographic profile and each water sample from a rosette sample bottle, as well as for the station and cruise.
These identifiers are critical to accurately assembling data across files from an expedition.

*For discrete water sample data, it is essential that the intended sample depth **never** be used to index water samples.*
There are many good reasons for not using sample depth to index water samples, such as discovering later (sometimes months or years later) that the rosette bottle did not close at (or sometimes even near) the intended sample depth.

The following **cruise/station/cast/sample** numbering scheme is suggested to provide unique, traceable identifiers. 

### Cruise (EXPOCODE)
Each cruise in the data set is given a unique identifier that appears in every file.
The CCHDO uses EXPOCODE as cruise identifiers composed of NODCShipCodeYearMonthDay, for example, a Roger Revelle Cruise starting March 29, 2009 would have the EXPOCODE 33RR20090329.
NODC Ship Codes can be found here: <https://vocab.nerc.ac.uk/collection/C17/current/>.

### Station (STNNBR)
Each station on a cruise must be given a unique (alphanumeric) identifier as the STNNBR.
Repeat and time series cruises may use the same station number on sequential cruises and that presents no difficulties as long as each cruise is given a unique EXPOCODE.

### Cast (CASTNO)
Each over-the-side operation at a station should be given a separate cast number.
If a station is reoccupied later during the same cruise, and the same station number is used, the cast numbers should increment upward in some sensible manner.
In no case should a data file contain at different points the same pair of STNNBR and CASTNO on the same cruise.
STNNBR and CASTNO appear in all su.txt, _hy1.csv, and _ct1.csv files submitted to the WHPO and must be used consistently in each file in which they appear.

### Sample id (SAMPNO) [or bottle id (BTLNBR)]
Many groups use the sample number to identify the rosette position of the bottle from which water samples are drawn while on deck.
Whatever scheme is used, it is critical that either (1) the same numbering scheme be used by all participants on the cruise, or (2) the bottle data file contains both identifiers.
Great confusion arises if one group uses one sample numbering scheme and another group uses a different one on the same cruise, but with the bottle data file containing only one of the two schemes (which has occurred several times in the CCHDO records).

For WHP-Exchange format bottle data files (_hy1.csv) the bottle number (BTLNBR) is also needed in order to uniquely identify the particular device used to collect the water sample.
The bottle number is defined as: (1) the permanent, unique serial number (alphanumeric) stamped or engraved on the barrel of the bottle from which the water samples are drawn or, alternatively, (2) as a unique alphanumeric identifier assigned to only that device over the duration of the expedition.
If, for example, bottles 11 and 12 are removed during the cruise to mount another instrument on the rosette, the bottle in the 13th position should remain BTLNBR 13, even though the sample from that bottle would now be SAMPNO 11. 

## References
```{eval-rst}

.. [Hood2010] Hood, E. M. (2010). Introduction to the collection of expert reports and guidelines. The GO-SHIP Repeat Hydrography Manual: A Collection of Expert Reports and Guidelines. Hood, EM, CL Sabine, and BM Sloyan, eds. IOCCP Report, (14). https://doi.org/10.25607/OBP-1351

.. [Joyce1994] Joyce, T. and C. Corry (1994), Requirements for WOCE Hydrographic Programme Data Reporting, WHPO Publication 90-1 Revision 2, WOCE Report 67/91, Woods Hole, Mass., USA

.. [Swift2008] Swift, J. H. (2008), A Guide to Submitting CTD/Hydrographic/Tracer Data and Associated Documentation to the CLIVAR and Carbon Hydrographic Data Office, https://cchdo.github.io/hdo-assets/documentation/policies/CCHDO_DataSubmitGuide.pdf, San Diego, CA., USA

.. [Swift2010] Swift, J. H. (2010) Reference-Quality Water Sample Data: Notes on Acquisition, Record Keeping, and Evaluation. In, The GO-SHIP Repeat Hydrography Manual: A Collection of Expert Reports and Guidelines. Version 1, (eds Hood, E.M., C.L. Sabine, and B.M. Sloyan), 38pp. (IOCCP Report Number 14; ICPO Publication Series Number 134). DOI: https://doi.org/10.25607/OBP-1346

```


(outline_cruise_report)=
## Appendix A - Outline of a Cruise Report
{style=upper-alpha}
1. **Cruise narrative**
    1. **Highlights**

        {style=lower-alpha}
        1. Cruise designation (cruise name) (e.g., "AIS01" for Amery Ice Shelf 1) [or, for a repeated WOCE-era section, the section designation(s), for example A11, IR04, etc. Include all sections covered on cruise]
        1. EXPOCODE 
        1. Chief scientist for each leg, including contact information (email preferred)
        1. Ship name
        1. Ports of call. Port(s) where cruise begins and ends plus any stops during the cruise
        1. Cruise dates (Official ship's log date of departure & return for each leg)

    1. **Cruise Summary Information**

        {style=lower-alpha}
        1. Written description of the survey's geographic boundaries
        1. Total number of stations occupied for each section, broken down by type of station and parameters sampled at each station
        1. Detailed list of each and every parameter measured on the cruise
        1. Floats and drifters deployed (type, identification number, location, and time)
        1. Moorings deployed or recovered (type, identification, location, and time)

     1. **List of Principal Investigators for All Measurements**

        {style=lower-alpha}
        1. Name (first and last) and/or persistent unique identifier (ORCid)
        1. Measurement responsibility
        1. Institution or affiliation (abbreviations should be defined)
        1. Contact information, email preferred

    1. **Scientific Program and Methods**

        {style=lower-alpha}
        1. Narrative
        1. Interlaboratory comparisons made (if any) or comparisons with previous cruise data
        1. (Optional) Vertical sections along the ship's track showing the bottle depth distributions, and plots of property vs. property relationships
    
    1. **Major Problems and Goals Not Achieved**
    1. **Other Incidents of Note**

1. **Underway Measurements**
    1. Navigation and bathymetry
    1. Acoustic Doppler Current Profiler (ADCP)
    1. Thermosalinograph and underway dissolved oxygen, fluorometer, etc.
    1. XBT and XCTD
    1. Meteorological observations
    1. Atmospheric chemistry
1. **Hydrographic Measurements - Descriptions, Techniques, and Calibrations**

    A discussion of each measurement type, including the following sub-headings as they apply:

    1.  Measurement name(s), section author's name(s) (date, or revision date)

        {style=lower-alpha}
        1. Description of equipment and technique or published reference.
        1. Sampling and data processing techniques followed or published reference for these techniques.
        1. Calibration data, including dates and laboratory where calibrations were done.
        1. Error estimates and noise sources, including:
           * effect of noise on samples and
           * comparisons with historical data or test stations.
        1. Laboratory and sample temperatures where required.
        1. Replicate analyses (tables).
        1. Standards used (for example, standard sea water batch number and ampoule number of standard sea water for each station).
        1. Reagents: purity and concentrations of stock solutions, where applicable.
        1. Values for blanks, where applicable (blank values should be subtracted from the data).
        1. Atmospheric values for tracers, where applicable.
1. **Acknowledgments**

   Funding sources, contract numbers, contributors, etc. 
1. **References**
1. **Appendices**

   Deck logs, water sample quality assessment notes, etc.



[submission_summary]: quick_guide
[cchdo_email]: mailto:cchdo@ucsd.edu
[swift_2018]: https://cchdo.github.io/hdo-assets/documentation/policies/Data_Evaluation_reference.pdf
[parameter_table]: https://exchange-format.readthedocs.io/en/latest/parameters.html#