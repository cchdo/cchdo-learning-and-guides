# CCHDO Summary Data Submission Guidelines

:version: 2024-08-08

Thank you for submitting your data to the CCHDO!
While we still accept submissions in any format, we *strongly encourage* data submitters to follow these guidelines.
Submissions following these guidelines will be prioritized for processing.
This document provides a summary of our guidance; an in-depth manual with more information can be found [here][in_depth].
If you have any questions, especially if you are a first time submitter, please don’t hesitate to reach out to the CCHDO at [cchdo@ucsd.edu][cchdo_email].

## Data Submission
**All submissions** should follow these guidelines:

* All parameters within the data file should be found using our [parameter table][parameter_table]
  * The parameter name must match exactly as it appears in the parameter table
  * If your parameter can not be found here:
    * Send [cchdo@ucsd.edu][cchdo_email] the parameter(s) you’d like added with a corresponding methods papers
* A quality flag for each measured parameter
  * We recommend WOCE quality flags. For more information on WOCE quality flags, please refer to our [manual][in_depth]
     * If WOCE quality flags are not used, we accept flagging systems that are included in the following document and request that the flagging schema used is named in the submission notes: [https://odv.awi.de/fileadmin/user_upload/odv/misc/ODV_QualityFlagSets.pdf](https://odv.awi.de/fileadmin/user_upload/odv/misc/ODV_QualityFlagSets.pdf)

We prefer if data are submitted in one of the following three formats.
The CCHDO encourages submitters to choose whatever format best fits their current workflow.
If the user does not yet have a data workflow, the .csv option is generally easiest to set up.

1. **Exchange**

    {style=lower-alpha}
    1. The Exchange guidelines can be found here: [https://exchange-format.readthedocs.io/en/latest/common.html](https://exchange-format.readthedocs.io/en/latest/common.html)
    1. Example {download}`Exchange Template <templates/Exchange_Template.csv>`

        {style=lower-roman}
        1. For a CTD file, replace ‘BOTTLE’ from the stamp with ‘CTD’
1. **A .csv that contains the following information; in the data file, please use the parameter name in parentheses, with no variations:**

    {style=lower-alpha}
    1. If this is the first time data is submitted for a cruise:

        {style=lower-roman}
        1. Expocode (EXPOCODE)
        1. Station Number (STNNBR)
        1. Cast Number (CASTNO)
        1. Sample Number (SAMPNO)
        1. Date (DATE)
        1. Time (TIME)
        1. Latitude (LATITUDE)
        1. Longitude (LONGITUDE)
        1. CTD pressure (CTDPRS)

    1. If this is a data update:

        {style=lower-roman}
        1. Station Number (STNNBR)
        1. Cast Number (CASTNO)
        1. Sample Number (SAMPNO)

    1. Example CSV [Template][csv_template]
1. **NetCDF**

    {style=lower-alpha}
    1. We recommend following the guidelines from NCEI - [https://www.ncei.noaa.gov/data/oceans/ncei/formats/netcdf/v2.0/index.html](https://www.ncei.noaa.gov/data/oceans/ncei/formats/netcdf/v2.0/index.html).
       Specifically, we recommend the profile template found on the NCEI page.
    1. Use netCDF names and attributes as listed in our [parameter table][parameter_table]

        {style=lower-roman}
        1. The same parameters required in the .csv format (Expocode, station, cast, sample, etc.) are required in this format

    1. We recommend details to be in the attributes rather than highly descriptive/assumptive variable names

## Cruise Report Submission
Every cruise should have a corresponding cruise report that conveys to data users the information needed to understand the context and content of the reported data.
PDF and .docx (Microsoft Word) formats are recommended.
An abridged recommendation on content is provided below, but a comprehensive outline is available in our full [manual][in_depth] (Appendix A):

* Linked table of contents
* Highlights section including general cruise information such as start and end dates, ports of call, expocode, etc.
* Cruise summary
    * A general summary of the cruise, its main goals, number of stations completed including detailed information about each station and parameters sampled, floats and drifters deployed, moorings deployed or recovered, etc.
* Table of all parameters sampled and the contact information for their respective PIs
    * Name and/or persistent unique identifier ([ORCID](https://orcid.org/))
    * Institution
    * Measurement/s responsible for
    * Contact information (email preferred)
* A section for every measured parameter (underway and hydrographic measurements) that includes:
    * Methods
        * Instrumentation (including manufacturer and model), chemicals used, calibration information, referenced protocols, etc.
    * At-sea sampling notes
    * Data analysis
    * Relevant figures

[cchdo_email]: mailto:cchdo@ucsd.edu
[parameter_table]: https://exchange-format.readthedocs.io/en/latest/parameters.html
[in_depth]: submission_detailed
[csv_template]: broken_link_fix_me_2