import numpy as np

#Helper function that extracts aggregate vote tally and percentage for a given race
def find_pct(elecret, prefix):
    year = str(prefix)[-2:]
    race = str(prefix)[:3]
    rep_votes = elecret[str(prefix) + '_r'].sum()
    tot_votes = elecret[str(prefix) + '_tot'].sum()
    r_pct = 100 * rep_votes/tot_votes
    return year, race, rep_votes, tot_votes, r_pct

#Helper function that matches past electoral precinct to the new 2022 geography it falls under
def centroid_match(centroid, new_shapefile):
    for (index, geometry) in new_shapefile.iterrows():
        if centroid.within(new_shapefile['geometry'][index]):
            district = new_shapefile['district'][index]
            return district
        else:
            pass
        
        
def label_maker(n):
    if n == 0:
        return 'state'
    elif n == 1:
        return 'fed'
    else:
        return 'alr'
