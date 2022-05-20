# Partisan Voter Index for Texas State Legislatures in 2022
## Exploratory Data Analysis and Visualization for Predicting Relative Political Lean for 2022 State Legislative districts

This project aims to produce Partisan Voter Index(PVI) metrics for the upper and lower Texas State Legislatures, and see if there is meaningful difference in metrics calculated using national election data vs state-wide election data.

Presentation Slides for this project can be found [here](https://www.beautiful.ai/player/-N2Y7vN4NqLSnLvunjGI).

### What is Partisan Voter Index?

The Cook Political Report's Partisan Voter Index (CPVI) is a measure of how strongly a state or congressional district leans towards the Republican or Democratic party, compared to the country as a whole.

It is a *relative* measure of lean for answering the question "How does this district vote?"

Traditionally, PVI for a congressional district has been calculated by comparing how that congressional district voted in a given election, to a 'baseline' of how the country as a whole voted in the last two presidential elections.

This project aims to produce PVI metrics for *state legislative districts*. The 'baseline' will be adapted to factor in state-wide executive office election returns, as well as presidential election returns from that state for last two presidential elections.

### How to Calculate Partisan Voter Index for a State Legislature after Redistricting

Texas Enacted new state legislative district boundaries after the 2020 census.
Calculating the PVI in a redistricting year requires matching vote tallies from previous elections to the *new* geographic boundaries of legislative districts.

This project uses precint-level election returns for 2016, 2018 and 2020, and will match voting precint geographies for each year of election returns to the 2022 state legislative district they fall under.

## Data Sources

Many thanks to the [Voting Science and Elections Team (VEST)](https://dataverse.harvard.edu/dataverse/electionscience) for their painstaking compilation and validation of election returns by precinct! Shapefiles for 2022 and 2012-2021 legislative districts were downloaded from [Texas's Capital Data Portal](https://data.capitol.texas.gov/)


<font size="2">Voting and Election Science Team, 2018, "2016 Precinct-Level Election Results", https://doi.org/10.7910/DVN/NH5S2I, Harvard Dataverse, V83 </font>

Voting and Election Science Team, 2019, "2018 Precinct-Level Election Results", https://doi.org/10.7910/DVN/UBKYRU, Harvard Dataverse, V59

Voting and Election Science Team, 2020, "2020 Precinct-Level Election Results", https://doi.org/10.7910/DVN/K7760H, Harvard Dataverse, V35

Texas Legislative Council, 2022, "PLANH2316", Retrieved from https://data.capitol.texas.gov/dataset/planh2316, Texas Capital Data Portal

Texas Legislative Council, 2022, "PLANS2168", Retrieved from https://data.capitol.texas.gov/dataset/plans2168, Texas Capital Data Portal

Texas Legislative Council, 2021, "PLANH283", Retrieved from https://data.capitol.texas.gov/dataset/planplanh283, Texas Capital Data Portal

Texas Legislative Council, 2021, "PLANS148", Retrieved from https://data.capitol.texas.gov/dataset/plans148, Texas Capital Data Portal