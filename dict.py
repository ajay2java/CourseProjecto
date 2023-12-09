# This file has dictionaries with all the list of courses for the various categories (# of credits, standard requirements, Advanced Experiential).

# Also included are the list of courses for each type of concentration.

# Key: There are no lists for Advanced liberal arts or Advanced liberal arts Elective or General Electives, a those encompass courses w/ specific digits in the course name (ex: 46XX, X1XX, X5XX).

general = {
    'One Credit': ['MOB2322','FYS1001','IMH25', 'IMH26'],
    'Two Credit': ['PRF1200', 'EPS3514', 'MOB3531', 'COM3511', 'COM3521', 'ECN3664', 'OIM3615', 'LIB3603', 'EPS3553', 'EPS3552', 'ENG4615', 'OIM3508', 'IND3612', 'IND3602', 'OIM4520', 'MOB3513', 'OIM2645', 'EPS3534', 'LIT4607', 'OIM3610', 'PRF1120', 'OIM3635'],
    'Three Credit': ['IND3603', 'IND2503', 'SME2001', 'SME2012', 'SME2002', 'SME2021', 'SME2031'],
    'Six Credit': ['SME2010', 'SME2000'],
    'Seventeen Credit': ['EXC3000'],
    'FME': ['FME1000', 'FME1001', 'EPS1000', 'MOB1010'], 
    'Standard': ['ACC1000', 'LAW1000', 'AQM1000', 'AQM2000', 'WRT1001', 'WRT2000', 'FCI1000', 'NST10', 'ACC2002', 'OIM2001', 'OIM2000', 'MKT2000', 'FIN2000', 'ECN2002', 'ECN2000', 'HSS20', 'CVA20', 'LVA20', 'SES2000', 'STR3000'],
    'Adv_Experiential': ['COM3504', 'COM3522', 'ECN3600', 'ECN3601', 'ECN3664', 'EPS3534', 'EPS3551', 'EPS4515', 'FIN3560', 'FIN4520', 'LAW3504', 'LIT4682', 'MFE3534', 'MKT3502', 'MKT3540', 'MKT3575', 'MKT4505', 'MKT4515', 'MKT4520', 'OIM3501', 'OIM3517', 'OIM3536', 'QTM3635', 'SCN3602', 'STR3500', 'STR3508'],
}


accounting = {
    'Required': ['ACC3500', 'ACC3501', 'ACC4530'],
    'Elective': ['TAX3500', 'TAX3650', 'ACC3510', 'ACC3546', 'ACC4520']
}

business_analytics = {
    'Data Management and Programming Concepts': ['OIM3545', 'OIM3640', 'ENG2510'],
    'Advanced Data and Decision Modeling': ['QTM3635', 'QTM3605'],
    'Electives': ['ACC3546', 'ECN3620', 'FIN4510', 'FIN4530', 'FIN4535', 'OIM3545', 'OIM3525', 'OIM3640', 'OIM3536', 'OIM3580', 'OIM3690', 'OIM3573', 'MKT3510' 'MKT4506', 'MKT4530', 'QTM2600', 'QTM2622', 'QTM2623', 'QTM3605', 'QTM3610', 'QTM3615', 'QTM3620', 'QTM3625', 'QTM3635', 'QTM3675', 'ENGR2510']
}

comp_math_fin = {
    'Required': ['QTM3625'],
    'Elective_1': ['FIN3520', 'FIN4505', 'FIN4510', 'FIN4530', 'FIN4560'],
    'Elective_2': ['QTM2623', 'QTM3610', 'QTM3615', 'QTM3620', 'QTM3635', 'QTM3675']
}

econ = {
    'Required': ['ECN3615', 'ECN3655'],
    'Elective': ['ECN3606', 'ECN3620', 'ECN3625', 'ECN3630', 'ECN3645', 'ECN3650', 'ECN3660', 'ECN3662', 'ECN3663', 'ECN3665', 'ECN3667', 'ECN3671', 'ECN3675', 'ECN3677']
}

entre = {
    'Required': ['EPS3501', 'EPS3502', 'EPS3503', 'EPS3508', 'EPS4520'],
    'Elective': ['EPS3504', 'EPS3505', 'EPS3508', 'EPS3509', 'EPS3513', 'EPS3514', 'EPS3518', 'EPS3520', 'EPS3524', 'EPS3529', 'EPS3531', 'EPS3532', 'EPS3534', 'EPS3536', 'EPS3538', 'EPS3540', 'EPS3541', 'EPS3542', 'EPS3543', 'EPS3551', 'EPS4510', 'EPS4515', 'EPS4521', 'EPS4530', 'OIM3525', 'OIM3610', 'MOB3503', 'MOB3526']
}

enviro_sust = {
    'General': ['NST2020', 'NST2040', 'NST2080', 'HSS2080', 'NST2090', 'HSS2090', 'NST2011', 'ECN2611', 'NST2012', 'HSS2012', 'CVA2003', 'CVA2036', 'CVA2057', 'ECN3675', 'ENV4600', 'ENV4605', 'ENV4610', 'EPS4515', 'EPS4527', 'FIN3535', 'HSS2040', 'LIT4676', 'LIT4682', 'LVA2030', 'LVA2062', 'MDS4620', 'MKT4525', 'OIM3522', 'PHL4609', 'POL4630', 'SCN3600', 'SCN3630', 'SCN3615', 'SCN3665']
}

finance = {
    'General': ['FIN3502', 'FIN3515', 'FIN3520', 'FIN3535', 'FIN3555', 'FIN3560', 'FIN3565', 'FIN4504', 'FIN4505', 'FIN4507', 'FIN4510', 'FIN4520', 'FIN4521', 'FIN4530', 'FIN4535', 'FIN4540', 'FIN4545', 'FIN4560', 'FIN4570', 'FIN4571']
}

global_reg_studies = {
    'Global': ['HSS2010', 'HSS2025', 'HSS2028', 'HSS2033', 'ENV4605', 'GDR4605', 'HIS4626', 'HUM4612', 'LIT4682', 'POL4640', 'ECN3650', 'ECN3660', 'ECN3665', 'LAW3601'],
    'Regional': ['CVA2009', 'CSP2009', 'CVA2011', 'CSP2011', 'CSP2026', 'CVA2035', 'CSP2035', 'CVA2055', 'CSP2055', 'CVA2058', 'CSP2058', 'HSS2003', 'HSS2006', 'HSS2013', 'HSS2030', 'HSS2032', 'HSS2034', 'HSS2038', 'HSS2039', 'HSS2042', 'AMS4672', 'ANT4606', 'HIS4610', 'HIS4616', 'HIS4620', 'HIS4682', 'HUM4611', 'HUM4615', 'POL4601', 'POL4635', 'ECN3625', 'ECN3645', 'ECN3662', 'ECN3677']
}

hist_pol = {
    'Historical': ['AMS4672', 'CVA2002', 'CVA2026', 'CVA2055', 'HIS4606', 'HIS4612', 'HIS4616', 'HIS4619', 'HIS4626', 'HIS4670', 'HIS4682', 'HSS2000', 'HSS2003', 'HSS2006', 'HSS2010', 'HSS2013', 'HSS2019', 'HSS2025', 'HSS2032', 'HSS2034', 'HSS2038', 'HSS2039', 'HSS2041', 'HSS2058', 'LVA2006', 'VSA4615'],
    'Political': ['CVA2015', 'CVA2033', 'ECN3662', 'ENV4605', 'GDR4605', 'HSS2028', 'HSS2030', 'HSS2033', 'HSS2040', 'LAW3601', 'LIT4682', 'POL4604', 'POL4630', 'POL4635', 'POL4645']
}

iden_diver = {
    'Required': ['AMS4672', 'ENV ', 'GDR4605', 'HIS4640', 'HIS4682', 'HUM4611', 'HUM4630', 'LIT4682', 'POL4602', 'POL4630'],
    'Elective': ['CVA2003', 'CVA2010', 'CVA2008', 'CVA2030', 'CVA2033', 'CVA2025', 'CVA2026', 'HIS4619', 'HSS2000', 'HSS2032', 'HSS2039', 'HSS2058', 'HSS2018', 'HUM4605', 'HUM4615', 'ECN3671', 'LIT4661', 'LVA2010', 'LVA2032', 'LVA2061', 'LVA2062', 'LVA2073', 'LVA2074', 'MUS4620', 'QTM3605', 'SOC4620']
}

info_tech = {
    'Creator': ['OIM3640', 'ENGR2510', 'CS111', 'OIM3690', 'CS230', 'ENGR3520', 'ENGR3525'],
    'Elective': ['OIM3640', 'ENGR2510', 'CS111', 'OIM3690', 'CS230', 'ENGR3520', 'ENGR3525', 'OIM3525', 'OIM3560', 'OIM3610', 'OIM3615', 'OIM3565', 'OIM3580', 'OIM2645', 'OIM3525', 'OIM3545', 'MKT3515', 'MKT4530', 'QTM2601', 'OIM3620', 'OIM3635', 'OIM3650', 'QTM3674', 'CS232', 'ENGR3220']
}

int_business = {
    'Required': ['ECN3660', 'ECN3665', 'ECN3645', 'LAW3601', 'ECN3625', 'ECN3662'],
    'Elective': ['MOB3560', 'LAW3560', 'ECN3650']
}

jcs = {
    'Philosophy': ['CVA2001', 'CVA2007', 'CVA2015', 'PHL4607', 'PHL4609'],
    'Elective': ['AMS4672', 'CVA2005', 'CVA2006', 'CVA2008', 'CVA2010', 'CVA2036', 'CVA2057', 'CVA2058', 'ENV4605', 'FRN4615', 'GDR4605', 'HIS4610', 'HIS4640', 'HIS4670', 'HSS2018', 'HSS2025', 'HSS2058', 'HUM4611', 'HUM4630', 'LAW3601', 'LAW3605', 'LIT4862', 'LIT4676', 'MDS4620', 'MUS4620', 'POL4630', 'QTM3506']
}

leadership = {
    'Required': ['MOB3512'],
    'Req2': ['MOB3514', 'MOB3515', 'MOB3580', 'MOB3582', 'MOB4572', 'MFE3534'],
    'Req3': ['MOB4510', 'OIM3509', 'MOB3560', 'MKT4505', 'EPS3520']
}

legal_studies = {
    'Part1': ['LAW3504', 'LAW3515', 'LAW3525', 'LAW3560', 'LAW3573', 'LAW3601', 'LAW3602', 'LAW3603', 'LAW3604', 'LAW3605', 'LAW3615', 'LAW3661', 'LAW3662', 'LAW3675', 'MKT3525', 'TAX3500', 'TAX3650'],
    'Part2': ['FIN3512', 'LIT4682', 'ANT4605']
}

lit_visual = {
    'Required': ['ARB4640', 'ART4610', 'CSP2058', 'ENG4604', 'ENG4605', 'ENG4620', 'ENV4610', 'FLM4610', 'FLM4691', 'FRN4640', 'HUM4611', 'HUM4615', 'LIT4600', 'LIT4610', 'LIT4611', 'LIT4661', 'LIT4676', 'LIT4682', 'LIT4689', 'LIT4693', 'LTA2003', 'LTA2004', 'LTA2005', 'LTA2006', 'LTA2009', 'LTA2010', 'LTA2013', 'LTA2022', 'LTA2030', 'LTA2031', 'LTA2032', 'LTA2039', 'LTA2045', 'LTA2049', 'LTA2061', 'LTA2062', 'LTA2067', 'LTA2069', 'LTA2072', 'LTA2074', 'LTA2075', 'LTA2078', 'LTA2079', 'LTA2080', 'LTA2090', 'SPN4640', 'THR4600']
}

man_fin_pl = {
    'Required': ['ACC3510', 'FIN3515'],
    'Elective1': ['ACC3502', 'ACC3501'],
    'Elective2': ['ECN3655', 'EPS4510', 'FIN3535', 'FIN4510', 'FIN4540', 'FIN4570']
}

marketing = {
    'Required': ['MKT4505'],
    'Elective1': ['MKT3510', 'MKT4506', 'MKT4530'],
    'Elective2': ['MKT3500', 'MKT3501', 'MKT3515', 'MKT3540', 'MKT3550', 'MKT3574', 'MKT3575', 'EPS3580', 'MKT4510', 'MKT4515', 'MKT4520', 'MKT4525', 'MKT4560']
}

operations_mgmt = {
    'Required': ['OIM3573'],
    'Elective': ['OIM3501', 'OIM3503', 'OIM3509', 'OIM3517', 'OIM3519', 'OIM3522', 'OIM3536', 'OIM3578', 'OIM4520', 'MKT3540', 'DES3600', 'OIM2645', 'QTM3630']
}

quant_m = {
    'Required': ['QTM2600', 'QTM2601', 'QTM2622', 'QTM2623', 'QTM3605', 'QTM3610', 'QTM3615', 'QTM3620', 'QTM3625', 'QTM3635', 'QTM3674', 'QTM3675']
}

real_estate = {
    'Required': ['FIN3511', 'FIN3512', 'FIN3555', 'FIN3565', 'FIN4571']
}

retail_scm = {
    'Required': ['MKT3540', 'OIM3573'],
    'Elective': ['COM3522', 'MKT3510', 'MKT3550', 'MKT3574', 'MKT4505', 'MKT4506', 'MKT4515', 'MKT4520', 'MKT4530', 'MKT4560', 'MOB3515', 'OIM3522', 'OIM3545', 'OIM3525', 'MOB3560', 'MOB3580', 'QTM3610', 'QTM3615', 'QTM3620', 'ECN3630', 'ECN3655', 'ECN3660', 'EPS3580', 'EPS3501', 'LAW3560']
}

social_culture = {
    'Intermediate': ['ARB2200', 'CHN2200', 'CVA2002', 'CVA2004', 'CVA2005', 'CVA2007', 'CVA2008', 'CVA2009', 'CVA2010', 'CVA2026', 'CVA2030', 'CVA2032', 'CVA2035', 'CVA2055', 'CVA2058', 'CVA2090', 'FRN2200', 'HSS2000', 'HSS2003', 'HSS2006', 'HSS2018', 'HSS2020', 'HSS2025', 'HSS2039', 'HSS2058', 'HSS2060', 'JPN2200', 'LVA2005', 'LVA2006', 'LVA2009', 'LVA2032', 'LVA2073', 'LVA2075', 'SPN2200'],
    'Advanced': ['AMS4672', 'ARB4610', 'ARB4640', 'ARB4650', 'ART4610', 'ART4615', 'CHN4610', 'ECN3662', 'ECN3677', 'FRN4610', 'FRN4615', 'FRN4620', 'FRN4640', 'HIS4606', 'HIS4610', 'HIS4612', 'HIS4616', 'HIS4619', 'HIS4640', 'HUM4611', 'JPN4610', 'LIT4611', 'LIT4676', 'MDS4620', 'MOB3518', 'MUS4620', 'POL4630', 'SPN4610', 'SPN4615', 'SPN4620', 'SPN4640']
}

strat_cult = {
    'Required': ['STR3500', 'STR3506', 'STR3508', 'STR3510', 'STR3540', 'STR3560', 'STR4510', 'STR4572', 'MOB3534'],
    'Elective': ['MOB3507', 'MOB3512', 'MOB3514', 'MOB3515', 'MOB3523', 'MOB3524', 'MOB3580', 'COM3504', 'ECN3630', 'ECN3655', 'ECN3667', 'ECN3671', 'EPS3529', 'MKT4505', 'OIM3501', 'OIM3509', 'OIM3517', 'OIM3522', 'OIM3536', 'OIM3545']
}

tech_entr = {
    'Required': ['EPS3501', 'OIM3690', 'OIM3640'],
    'Elective': ['EPS3504', 'EPS4515', 'EPS3536', 'EPS3518', 'OIM2645', 'OIM3501', 'OIM3503', 'OIM3517', 'OIM3525', 'OIM3536', 'OIM3545', 'OIM3580', 'OIM3560', 'OIM3610', 'OIM3620', 'OIM3640', 'OIM3650', 'OIM3565', 'OIM3690', 'SCN3600', 'SCN3601']
}

tech_entr_des = {
    'Required': ['EPS3501'],
    'Req2': ['EPS3536', 'EPS4515', 'ENGR2250'],
    'Elective': ['DES3600', 'ECN3675', 'ENGR1200', 'ENGR2141', 'AHSE2141', 'ENGR3210', 'ENGR3220', 'EPS3504', 'EPS3509', 'EPS3513', 'EPS3531', 'EPS3537', 'LAW3675', 'LVA2075', 'OIM3517', 'OIM3522', 'OIM3578', 'OIM3635', 'SCN3655']
}



