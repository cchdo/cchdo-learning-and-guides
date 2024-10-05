### File Formats

Several file formats are available from the CCHDO:

#### CF/netCDF
A netCDF 4 format following the Climate and Forecast (CF) Conventions version 1.8.  
**The conventions are described at:**  
[http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html)

We are using a [profile](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#profile-data) discrete sampling geometry with an incomplete multidimensional array representation described in [section 9.3.2](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#_incomplete_multidimensional_array_representation). Also informative is [Appendix H](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html#profile-data), which provides examples of the features described in Section 9. A rigorous format description for our specific data files is in process.

#### Exchange
The WHP Exchange format is a text-based format for bottle and CTD data.  
**The format is described at:**  
[https://exchange-format.readthedocs.io/en/latest/index.html](https://exchange-format.readthedocs.io/en/latest/index.html)

The source code for the format description is [available on GitHub](https://github.com/cchdo/exchange); we invite pull requests and the opening of issues.  
The legacy format description [is also available](https://cchdo.github.io/hdo-assets/documentation/WHP_Exchange_Description.pdf).

#### netCDF (WHP)
The (WHP) netCDF files are COARDS compliant, one station per file.  
A [primer is available](https://cchdo.github.io/hdo-assets/documentation/netcdf_primer/index.html).  
The variable names inside WHP netCDF files will be the parameter names as described by the [parameters section](#parameters).

#### WOCE
The legacy WOCE formats are still provided by the CCHDO.  
The summary file format is described by [chapter 3 of the WOCE manual](https://cchdo.github.io/hdo-assets/documentation/manuals/pdf/90_1/chap3.pdf).  
The bottle, CTD, and quality flag descriptions are described by [chapter 4 of the WOCE manual](https://cchdo.github.io/hdo-assets/documentation/manuals/pdf/90_1/chap4.pdf).
