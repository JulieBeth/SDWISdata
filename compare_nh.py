# this file will be used to compare NH systems from the EFC database to those downloaded from the SDWIS API
# I will use outer joins to identify if any EFC systems are no longer active in the NH SDWIS database

import numpy
import pandas

# read in files to dataframes
efc_nh = pandas.read_csv('data-1608239424981.csv', sep = ',')
sdwis_nh = pandas.read_csv('downloaded.csv', sep = ',')

# print dataframes to make sure columns are correct
print(efc_nh)
print(sdwis_nh)

# set pwsid as index to efc_nh then outer join to sdwis_nh
efc_nh.set_index('pwsid')
compare_nh = efc_nh.join(sdwis_nh.set_index('water_system.PWSID'),on='pwsid', how='left')

# output to csv
compare_nh.to_csv(r'nh_comparison.csv')
