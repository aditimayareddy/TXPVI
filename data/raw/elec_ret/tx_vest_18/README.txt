2018 Texas precinct and election results shapefile.

## RDH Date retrieval
08/03/2021

## Sources
Election results and precinct shapefile from the Texas Legislative Council (https://data.capitol.texas.gov/). The precinct data files available for download at the TXLC Capitol Data Portal are allocated to Census VTD geography based on Voting Age Population from the 2010 Census. The unallocated precinct results and registration statistics were generously provided by TXLC staff to instead merge with the precinct boundaries.

The shapefile includes unallocated Voter Registration (VR) and Spanish Surname Voter Registration (SSVR) for the November 2018 general election. Any VR data analysis of these unallocated precinct results should utilize this unallocated VR data rather than the VR data allocated by VTD available for download at CDP. SSVR is denoted as a percentile of total VR for each precinct.

Precinct results for the following counties were replaced in whole or in part with county source files or with precinct data provided via the Secretary of State: Atascosa, Bexar, Blanco, Borden, Bowie, Brewster, Brown, Carson, Cherokee, Cochran, Comanche, Cooke, Culberson, Duval, Fort Bend, Gillespie, Hartley, Haskell, Hays, Hood, Jefferson, Jim Hogg, Johnson, Lamar, Matagorda, Midland, Nolan, Ochiltree, Robertson, Rockwall, Rusk, Starr, Terrell, Tyler.

## Fields metadata

Vote Column Label Format
------------------------
Columns reporting votes follow a standard label pattern. One example is:
G20PRERTRU
The first character is G for a general election, C for recount results, P for a primary, S for a special, and R for a runoff.
Characters 2 and 3 are the year of the election.
Characters 4-6 represent the office type (see list below).
Character 7 represents the party of the candidate.
Characters 8-10 are the first three letters of the candidate's last name.

Office Codes
A## - Ballot amendment, where ## is an identifier
AGR - Commissioner of Agriculture
ATG - Attorney General
AUD - Auditor
CFO - Chief Financial Officer
CHA - Council Chairman
COC - Corporation Commissioner
COM - Comptroller
CON - State Controller
COU - City Council Member
CSC - Clerk of the Supreme Court
DEL - Delegate to the U.S. House
GOV - Governor
H## - U.S. House, where ## is the district number. AL: at large.
HOD - House of Delegates, accompanied by a HOD_DIST column indicating district number
HOR - U.S. House, accompanied by a HOR_DIST column indicating district number
INS - Insurance Commissioner
LAB - Labor Commissioner
LAN - Commissioner of General Land Office
LND - Commissioner of Public/State Lands
LTG - Lieutenant Governor
MAY - Mayor
MNI - State Mine Inspector
PSC - Public Service Commissioner
PUC - Public Utilities Commissioner
RGT - State University Regent
RRC - Railroad Commissioner
SAC - State Appeals Court (in AL: Civil Appeals)
SBE - State Board of Education
SCC - State Court of Criminal Appeals
SOC - Secretary of Commonwealth
SOS - Secretary of State
SPI - Superintendent of Public Instruction
SPL - Commissioner of School and Public Lands
SSC - State Supreme Court
TAX - Tax Commissioner
TRE - Treasurer
UBR - University Board of Regents/Trustees/Governors
USS - U.S. Senate

Party Codes
D and R will always represent Democrat and Republican, respectively.
See the state-specific notes for the remaining codes used in a particular file; note that third-party candidates may appear on the ballot under different party labels in different states.

## Fields
G18VR - Voter registration
G18SSVR - Spanish surname voter registration

G18USSRCRU - Ted Cruz (Republican Party)
G18USSDORO - Beto O'Rourke (Democratic Party)
G18USSLDIK - Neal M. Dikeman (Libertarian Party)

G18GOVRABB - Greg Abbott (Republican Party)
G18GOVDVAL - Lupe Valdez (Democratic Party)
G18GOVLTIP - Mark Jay Tippetts (Libertarian Party)

G18LTGRPAT - Dan Patrick (Republican Party)
G18LTGDCOL - Mike Collier (Democratic Party)
G18LTGLMCK - Kerry Douglas McKennon (Libertarian Party)

G18ATGRPAX - Ken Paxton (Republican Party)
G18ATGDNEL - Justin Nelson (Democratic Party)
G18ATGLHAR - Michael Ray Harris (Libertarian Party)

G18COMRHEG - Glenn Hegar (Republican Party)
G18COMDCHE - Joi Chevalier (Democratic Party)
G18COMLSAN - Ben Sanders (Libertarian Party)

G18LANRBUS - George P. Bush (Republican Party)
G18LANDSUA - Miguel Suazo (Democratic Party)
G18LANLPIN - Matt Pina (Libertarian Party)

G18AGRRMIL - Sid Miller (Republican Party)
G18AGRDOLS - Kim Olson (Democratic Party)
G18AGRLCAR - Richard Carpenter (Libertarian Party)

G18RRCRCRA - Christi Craddick (Republican Party)
G18RRCDMCA - Roman McAllen (Democratic Party)
G18RRCLWRI - Mike Wright (Libertarian Party)

G18SSCRBLA - Jimmy Blacklock (Republican Party)
G18SSCDKIR - Stever Kirkland (Democratic Party)

G18SSCRDEV - John Devine (Republican Party)
G18SSCDSAN - R.K. Sandill (Democratic Party)

G18SSCRBRO - Jeff Brown (Republican Party)
G18SSCDCHE - Kathy Cheng (Democratic Party)

G18SCCRKEL - Sharon Keller (Republican Party)
G18SCCDJAC - Maria T. (Terri) Jackson (Democratic Party)
G18SCCLSTR - William Bryan Strange III (Libertarian Party)

G18SCCRHER - Barbara Parker Hervey (Republican Party)
G18SCCDFRA - Romana Franklin (Democratic Party)

G18SCCRSLA - Michelle Slaughter (Republican Party)
G18SCCLASH - Mark Ash (Libertarian Party)

## Processing Steps
Precinct 4/6 in Gonzales was merged prior to 2008. Gonzales 4 was the city of Nixon while Gonzales 6 was the surrounding county precinct. However, they reappear as separate line items in the 2018 general election county report. Since these are otherwise regarded as a unitary precinct and it is unclear that the separate 2018 line items correspond to the obsolete boundaries the results for Gonzales 4/6 were combined in the shapefile.

Precinct totals for the counties listed below do not add up to the Secretary of State County Canvass for one or more offices. Most commonly this is due to omission of some ballots counted after election day from either the county precinct reports or from summary results certified to the state. In some cases these involve data entry errors where numbers were transposed, dropped, or added in one or more precincts or in countywide summations. In some cases corrections to the initial precinct results were made after the certification deadline.

Armstrong, Bailey, Bandera, Baylor, Calhoun, Childress, Cochran, Collingsworth, Cottle, Culberson, Dimmit, Fayette, Galveston, Goliad, Gonzales, Hall, Hartley, Haskell, Hockley, Hudspeth, Jackson, Kent, Live Oak, Loving, McCulloch, Moore, Morris, Motley, Presidio, Reeves, Runnells, San Saba, Somervell, Starr, Stephens, Terrell, Titus, Waller, Ward, Wichita, Willacy, Winkler, Zavala.

Most of the discrepancies are in single digits or low double digits. The exceptions are an 80 vote overreport from Jackson for Ted Cruz (R) for U.S. Senate, a 2000 vote overreport from Galveston for Ken Paxton (R) for Attorney General, a 273 vote underreport from Somervell for Justin Nelson (D) for Attorney General, a 2000 vote underreport from Starr for Jimmy Blacklock (R) for Supreme Court Justice 2, an 8470 vote underreport from Wichita for Steven Kirkland (D) for Supreme Court Justice 2, a 90 vote underreport from Moore for Michelle Slaughter (R) for Criminal Appeals Judge 8, a 10229 vote underreport from Waller for Michelle Slaughter (R) for Criminal Appeals Judge 8, and a 2934 vote underreport from Waller for Mark Ash (L) for Criminal Appeals Judge 8.

Votes reported countywide were distributed by candidate to precincts based on the precinct-level reported vote. This includes all early ballots in Collingsworth, Crockett, Dawson, Hudspeth, Kent, McMullen, and Trinity. Mail ballots in Armstrong. Federal and/or limited ballots in Bexar, Brazos, Hays, Jefferson, and Rockwall. Provisional and military ballots in Bowie.

The following counties reported combined results for some precincts. As these specific precincts align with VTD boundaries the combined results were replaced with the VTD allocated precinct results from the TXLC Capitol Data Portal. Any data corrections or distributions noted above were transferred accordingly.

Bowie: 1A/4E, 1B/2A, 2B/4D/5A, 2D/4A/4C/5B, 13/30, 21/22, 24/25
Dallam: 2/8, 3/5/9
Howard: 11-16/103-105, 24-26/205, 32-35/304, 42-46/404-405, 207-208, 408/409
Kleberg: 33/34
Lamb: 7/8
Lynn: 2/8, 3/10, 4/11
McMullen: 2A/2B, 4A/4B
Newton: 11/13/21
Real: 4/7
Red River: 1/11, 17/18, 27/30
San Saba: 2A/2B, 3A/3B, 4A/4B
