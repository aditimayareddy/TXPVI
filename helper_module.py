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
        
#Helper function that labels election returns            
def label_maker(n):
    if n == 0:
        return 'state'
    elif n == 1:
        return 'fed'
    else:
        return 'alr'

#helper function that extracts republican vote percentage for each legislative district    
def find_rpct(data, cols):
    SD = data.groupby('SD').sum()
    HD = data.groupby('HD').sum()
    start = (len(cols)*2) + 1
    for item in cols:
        r = str(item) + '_r'
        tot = str(item) + '_tot'
        rpct = str(item) + '_rpct'
        SD[rpct] = SD[r]/SD[tot]
        HD[rpct] = HD[r]/HD[tot]
    SD = SD.iloc[:,start:]
    HD = HD.iloc[:,start:]
    print('done')
    return SD, HD

#Helper function to compress republican vote percentage across multiple years
def compress_rpct(item):
    div = len(item.columns)
    label = 'alr' + item.columns[1][4:6]
    item[label] = item.mean(axis=1)
    item = item[[label]]
    print(label, 'done')
    return item

#Helper function that creates 'bins' for raw PVI numbers
def to_bin(item): 
    if item <= -20:
        bin_ = 'Solid D'
    elif item > -20 and item <= - 5:
        bin_ = 'Likely D'
    elif item > -5 and item < 5:
        bin_ = 'Competitive'
    elif item > 5 and item < 20:
        bin_ = 'Likely R'
    elif item > 20:
        bin_ = 'Solid R'
    else:
        bin_ = 'Unknown'
    return bin_