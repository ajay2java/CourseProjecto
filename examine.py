from dict import general, accounting, business_analytics, comp_math_fin, econ, entre, enviro_sust, finance, global_reg_studies, hist_pol, iden_diver, info_tech, int_business, jcs, leadership, legal_studies, lit_visual, man_fin_pl, marketing, operations_mgmt, quant_m, real_estate, retail_scm, social_culture, strat_cult, tech_entr, tech_entr_des


from openpyxl import load_workbook


### This list is CRUCIAL --> It allows us to identify where the number part of the course id is:

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ex input: 'OIM3640' --> the code below will go letter by letter till it finds one that's in the 'num' list (In this case, 3). From there, it will start from 3 and go through the rest of the string, and store it in a variable.
# Here: 3640 will be stored in a variable to be checked against requirements.


class Concentration:
    
    def __init__(self, name, pre_req, course_list=None):
        ###

        # self.name take person's name from provided excel template
        self.name = name

        # self.total_creds is the cummulative number of credits taken from all courses added together. This variable is preset to the number of existing credits a student had before coming to Babson (from previous AP courses in high school)
        self.total_creds = int(pre_req)
        #self.fMe is the variable that counts for both FME courses taken at Babson
        self.fMe = 0
        #self.std is the variable that counts the required courses students take; it's preset to the number of AP credits a student has, that overrides some of the requirements
        self.std = int(pre_req)
        #self.adv_exp counts Advance Experiential Courses
        self.adv_exp = 0
        #self.adv_lib counts Advance Liberal Arts Courses
        self.adv_lib = 0
        #self.adv_libe counts Advanced Liberal Arts Elective Course
        self.adv_libe = 0
        #self.gen_e counts
        self.gen_e = 0

        #self.acc_req is self.acc_ele are for the Accounting Concentration (requirements & electives)
        self.acc_req = 0
        self.acc_ele = 0

        # The three below are for the Business Analytics Concentration [_dm is for the Data Management Part; _ad is for the Advanced Data Part; _e is for the electives]
        self.ana_dm = 0
        self.ana_ad = 0
        self.ana_e = 0

        #The three below are for the Computational and Mathematical Finance Concentration
        self.compr = 0
        self.compe1 = 0
        self.compe2 = 0

        # The two below are for the Economics Concentration
        self.econr = 0
        self.econe = 0

        # The two below are for the Entrepreneurship Concentration
        self.entr = 0
        self.ente = 0

        # This is for the Environmental Sustainability Concentration
        self.env = 0

        # This is for the Finance Concentration
        self.fin = 0

        # This is for the Global and Regional Studies Concentration
        self.grs1 = 0
        self.grs2 = 0

        # This is for the Historical and Political Studies Concentration
        self.hist = 0
        self.pol = 0

        # This is for the Identity and Diversity Concentration
        self.idr = 0
        self.ide = 0

        # This is for the Information Technology Management Concentration
        self.itm_c = 0
        self.itm_e = 0

        # This is for the International Business Environment Concentration
        self.ibe_r = 0
        self.ibe_e = 0

        # This is for the Justice, Citizenship, and Social Responsibility Concentration
        self.jcs_phil = 0
        self.jcs_e = 0

        # These three are for the Leadership Concentration
        self.lead_r = 0
        self.lead_r1 = 0
        self.lead_r2 = 0

        # This is for the Legal Studies Concentration
        self.ls1 = 0
        self.ls2 = 0

        # This is for the Literary and Visual Arts Concentration
        self.lva_r = 0

        # These three are for the Managerial Financial Planning and Analysis Concentration
        self.mf_r = 0
        self.mf_e1 = 0
        self.mf_e2 = 0

        # These three are for the Marketing Concentration
        self.mkr = 0
        self.mke1 = 0
        self.mke2 = 0

        #These two are for the Operations Management Concentration
        self.omr = 0
        self.ome = 0

        # This is for the Quantitative Methods Concentration
        self.qm = 0

        # This is for the Real Estate Concentration
        self.re = 0

        # This is for the Retail Supply Chain Management Concentration
        self.rscr = 0
        self.rsce = 0

        # These two are for the Social and Cultural Studies Concentration
        self.sci = 0
        self.sca = 0

        # These two are for the Strategy & Consulting Concentration
        self.sc_r = 0
        self.sc_e = 0

        # These two are for the Tech Entrepreneurship Concentration
        self.ter = 0
        self.tee = 0

        # These three are for the Technology, Entrepreneurship & Design Concentration
        self.ted_r1 = 0
        self.ted_r2 = 0
        self.ted_r3 = 0

        # This populates self.course, which has the full list of courses a student will take throughout their 4 years of college
        if course_list is None:
            self.courses = []
        else:
            self.courses = course_list
    
    def __str__(self):
        """This is the method that checks each self. variable for each requirement & concentration, and returns a list stating whether the user has met the requirements.
        The key here, is that it only returns the concentration name, which the student has fulfilled."""

        t = [f"{self.name} College Course Status:"]
        if self.total_creds >= 128:
            s = "Total Credits Status: ✅"
            t.append(s)
        else:
            s = "Total Credits Status: ❌"
            t.append(s)
        
        if self.fMe >= 2:
            s = "FME/EPS Requirement: ✅"
            t.append(s)
        else:
            s = "FME/EPS Requirements: ❌"
            t.append(s)

        if self.std >= 20:
            s = "Standard Requirements: ✅"
            t.append(s)
        else:
            s = "Standard Requirements: ❌"
            t.append(s)

        if self.adv_exp >= 1:
            s = "Advanced Experiential: ✅"
            t.append(s)
        else:
            s = "Advanced Experiential: ❌"
            t.append(s)

        if self.adv_lib >= 4: # num in credits
            s = "Advanced Liberal Arts: ✅"
            t.append(s)
        else:
            s = "Advanced Liberal Arts: ❌"
            t.append(s)
        
        if self.adv_libe >= 12:
            s = "Advanced Liberal Arts Elective: ✅"
            t.append(s)
        else:
            s = "Advanced Liberal Arts Elective: ❌"
            t.append(s)
        
        if self.gen_e >= 20:
            s = "General Elective: ✅"
            t.append(s)
        else:
            s = "General Elective: ❌"
            t.append(s)
        
        if self.acc_req == 3 and self.acc_ele >= 1:
            s = "Accounting Concentration: ✅"
            t.append(s)

        if self.ana_dm >= 1 and self.ana_ad >= 1 and self.ana_e >= 2:
            s = "Business Analytics Concentration: ✅"
            t.append(s)
        
        if self.compr == 1 and self.compe1 >= 2 and self.compe2 >= 1:
            s = "Computational and Mathematical Finance Concentration: ✅"
            t.append(s)

        if self.econr >= 1 and self.econe >= 3:
            s = "Economics Concentration: ✅"
            t.append(s)

        if self.entr == 1 and self.ente >= 3:
            s = "Entrepreneurship Concentration: ✅"
            t.append(s)

        if self.env >= 4:
            s = "Environmental Sustainability Concentration: ✅"
            t.append(s)
        
        if self.fin >= 4:
            s = "Finance Concentration: ✅"
            t.append(s)

        if self.grs1 >= 1 and self.grs2 >= 1 and self.grs1 + self.grs2 >= 4:
            s = "Global and Regional Studies Concentration: ✅"
            t.append(s)

        if self.hist >= 1 and self.pol >= 1 and self.hist + self.pol >= 4:
            s = "Historical and Political Studies Concentration: ✅"
            t.append(s)

        if self.idr >= 2 and self.idr + self.ide >= 4:
            s = "Identity and Diversity Concentration: ✅"
            t.append(s)
        
        if self.itm_c >= 4 and self.itm_c + self.itm_e >= 16:
            s = "Information Technology Management Concentration: ✅"
            t.append(s)
        
        if self.ibe_r >= 3 and self.ibe_e >= 1:
            s = "International Business Environment Concentration: ✅"
            t.append(s)
        
        if self.jcs_phil + self.jcs_e >= 4:
            s = "Justice, Citizenship, and Social Responsibility Concentration: ✅"
            t.append(s)

        if self.lead_r == 1 and self.lead_r1 >= 2 and self.lead_r2 >= 1:
            s = "Leadership Concentration: ✅"
            t.append(s)

        if self.ls1 >= 3 and self.ls1 + self.ls2 >= 4:
            s = "Legal Studies Concentration: ✅"
            t.append(s)

        if self.lva_r >= 16:
            s = "Literary and Visual Arts Concentration: ✅"
            t.append(s)

        if self.mf_r == 2 and self.mf_e1 >= 1 and self.mf_e2 >= 1:
            s = "Managerial Financial Planning and Analysis Concentration: ✅"
            t.append(s)

        if self.mkr == 1 and self.mke1 >= 1 and self.mke2 >= 2:
            s = "Marketing Concentration: ✅"
            t.append(s)

        if self.omr == 1 and self.ome >= 3:
            s = "Operations Management Concentration: ✅"
            t.append(s)
        
        if self.qm >= 4:
            s = "Quantitative Methods Concentration: ✅"
            t.append(s)

        if self.re >= 4:
            s = "Real Estate Concentration: ✅"
            t.append(s)

        if self.rscr == 2 and self.rsce >= 2:
            s = "Retail Supply Chain Management Concentration: ✅"
            t.append(s)

        if self.sci >= 2 and self.sca >= 2:
            s = "Social and Cultural Studies Concentration: ✅"
            t.append(s)

        if self.sc_r >= 2 and self.sc_e >= 2:
            s = "Strategy & Consulting Concentration: ✅"
            t.append(s)

        if self.ter >= 2 and self.tee >= 2:
            s = "Tech Entrepreneurship Concentration: ✅"
            t.append(s)

        if self.ted_r1 == 1 and self.ted_r2 >= 1 and self.ted_r3 >= 2:
            s = "Technology, Entrepreneurship, and Design Concentration: ✅"
            t.append(s)
        
        return t
            
    
    def num_credits(self):
        """This method checks in the 'general' dictionary from 'dict.py' under the credi headers to see if a course is in a certain list.
        These numbers populate the self.total_creds variable."""
        for a in self.courses:
            if a in general['One Credit']:
                self.total_creds += 1
            elif a in general['Two Credit']:
                self.total_creds += 2
            elif a in general['Three Credit']:
                self.total_creds += 3
            elif a in general['Six Credit']:
                self.total_creds += 6
            elif a in general['Seventeen Credit']:
                self.total_creds += 17
            else:
                self.total_creds += 4
    
    
    def get_num_creds(self, course):
        """This method will be called by certain concentration methods below, by which the requirements are based off the # of credits rather than the # of courses (As not all courses are 4 credits)."""
        if course in general['One Credit']:
            return 1
        elif course in general['Two Credit']:
            return 2
        elif course in general['Three Credit']:
            return 3
        elif course in general['Six Credit']:
            return 6
        elif course in general['Seventeen Credit']:
            return 17
        else:
            return 4

    def FME(self):
        """This method checks to see if the student has the FME courses, which populate the self.fMe variable"""
        for a in self.courses:
            if a in general['FME']:
                self.fMe += 1

    def standard(self):
        """This method checks with the 'Standard category in the 'general' dictionary to count the number of standard requirements a person meets."""
        for a in self.courses:
            if a in general['Standard']:
                self.std += 1

    def adv_exper(self):
        """This method checks with the Adv_Experiential section in the 'general' dictionary to count the number of Advanced experiential credits a user has met."""
        for a in self.courses:
            if a in general['Adv_Experiential']:
                self.adv_exp += 1

    def adv_libarts(self):
        """This checks for any courses with 46xx number and adds the requisite credits to the self.adv_lib variable."""
        store = ""
        for a in self.courses:
            #store variable will only store the number part of the course id; that's why we check if a[i] in num
            for i in range(len(a)):
                if a[i] in num:
                    store += a[i]
            if len(store) == 4 and '46' == store[0:2]:
                self.adv_lib += self.get_num_creds(a)
            store = ""

    def adv_libarts_elec(self):
        """This method checks if a course includes a 6 as the second digit in the number part of the id - X6XX"""
        store = ""
        for a in self.courses:
            # print(a)
            for i in range(len(a)):
                # same strategy as above, in using store to only keep the number part of the course id.
                if a[i] in num:
                    store += a[i]
            if len(store) == 4 and store[1] == '6':
                self.adv_libe += self.get_num_creds(a)
            store = ""

    def gen_elective(self):
        """This method checks for if certain course have X1XX, X2XX, X5XX, X6XX"""
        store = ""
        for a in self.courses:
            # print(a)
            for i in range(len(a)):
                if a[i] in num:
                    store += a[i]
            if len(store) == 4 and (store[1] == '1' or store[1] == '2' or store[1] == '5' or store[1] == '6'):
                self.gen_e += self.get_num_creds(a)
            store = ""

    def accounting(self):
        """This course cheks i certain courses meet the Accounting concentration Requirements and Electives."""
        for a in self.courses:
            if a in accounting['Required']:
                self.acc_req += 1
            elif a in accounting['Elective']:
                self.acc_ele += 1



    def analytics(self):
        """This method populates the analytics concentration variables if a certain course(s) meets any one of the  three analytics categories."""
        for a in self.courses:
            if a in business_analytics['Data Management and Programming Concepts']:
                if self.ana_dm == 1:
                    self.ana_e += self.get_num_creds(a)
                else:
                    self.ana_dm += 1
            elif a in business_analytics['Advanced Data and Decision Modeling']:
                if self.ana_ad == 1:
                    self.ana_e += self.get_num_creds(a)
                else:
                    self.ana_ad += 1
            elif a in business_analytics['Electives']:
                self.ana_e += self.get_num_creds(a)
            else:
                continue

    def computational(self):
        """This method checks to see if any courses meet the Computational Math and Finance requirements, and populate the necessary variables depending on the category the course is in."""
        for a in self.courses:
            if a in comp_math_fin['Required']:
                self.compr += 1
            elif a in comp_math_fin['Elective_1']:
                self.compe1 += 1
            elif a in comp_math_fin['Elective_2']:
                self.compe2 += 1

    def economics(self):
        """This method checks to see if any courses meet the Economics Concentration, and populate the necessary variables depending on the category the course is in."""
        for a in self.courses:
            if a in econ['Required']:
                self.econr += 1
            elif a in econ['Elective']:
                self.econe += 1

    def entrepren(self):
        """This method checks to see if any courses meet the Entrepreneurship Concentration, and populate the necessary variables depending on the category the course is in."""
        for a in self.courses:
            if a in entre['Required']:
                self.entr += 1
            elif a in entre['Elective']:
                self.ente += 1
    
    def enviro_sustainability(self):
        """This method checks to see if any courses meet the Environmental Sustainability Concentration, and populates the self.env variable."""
        for a in self.courses:
            if a in enviro_sust['General']:
                self.env += 1

    def financee(self):
        """This method checks to see if any courses meet the Finance Concentration, and populates the self.fin variable."""
        for a in self.courses:
            if a in finance['General']:
                self.fin += 1
        
    def global_regional_studies(self):
        """This method checks to see if any courses meet the Global and Regional Studies Concentration, and populates the self.grs1 or grs2 variable depending on the category the course is matched to."""
        for a in self.courses:
            if a in global_reg_studies['Global']:
                self.grs1 += 1
            elif a in global_reg_studies['Regional']:
                self.grs2 += 1

    def historical_political(self):
        """This method checks to see if any courses meet the Historical and Political Studies Concentration, and populates the self.hist and pol variable."""
        for a in self.courses:
            if a in hist_pol['Historical']:
                if self.hist == 1:
                    # if someone has already previously taken a course in this category, the code only adds an additional 1 if the course has 3XXX or 4XXX in the id.
                    if a[3] in num:
                        if int(a[3]) >= 3:
                           self.hist += 1 
                else:
                    self.hist += 1
            elif a in hist_pol['Political']:
                if self.pol == 1:
                    # if someone has already previously taken a course in this category, the code only adds an additional 1 if the course has 3XXX or 4XXX in the id.
                    if a[3] in num:
                        if int(a[3]) >= 3:
                           self.pol += 1 
                else:
                    self.pol += 1
    
    def identity_diversity(self):
        """This method checks to see if any courses meet the Identity and Diversity Concentration, and populates the self.idr and ide variable."""
        for a in self.courses:
            if a in iden_diver['Required']:
                self.idr += 1
            elif a in iden_diver['Elective']:
                self.ide += 1
    
    def info_tech_management(self):
        """This method checks to see if any courses meet the Information Technology Management Concentration, and populates the self.itm_c and itm_e variables."""
        for a in self.courses:
            if a in info_tech['Creator']:
                self.itm_c += self.get_num_creds(a)
            elif a in info_tech['Elective']:
                self.itm_e += self.get_num_creds(a)

    def inter_business_enviro(self):
        """This method checks to see if any courses meet the International Business Environment Concentration, and populates the self.ibe_r and ibe_e variables."""
        for a in self.courses:
            if a in int_business['Required']:
                self.ibe_r += 1
            elif a in int_business['Elective']:
                self.ibe_e += 1

    def just_citi_sr(self):
        """This method checks to see if any courses meet the Justice, Citizenship, Social Responsibility Concentration, and populates the self.jsc_phil and jcs_e variables."""
        for a in self.courses:
            if a in jcs['Philosophy']:
                self.jcs_phil += 1
            elif a in jcs['Elective']:
                self.jcs_e += 1

    def lead(self):
        """This method checks to see if any courses meet the Leadership Concentration, and populates the self.lead_r, lead_r1, and lead_r2 variables."""
        for a in self.courses:
            if a in leadership['Required']:
                self.lead_r += 1
            elif a in leadership['Req2']:
                self.lead_r1 += 1
            elif a in leadership['Req3']:
                self.lead_r2 += 1

    def legal_study(self):
        """This method checks to see if any courses meet the Legal Studies Concentration, and populates the self.ls1 and ls2 variables."""
        for a in self.courses:
            if a in legal_studies['Part1']:
                self.ls1 += 1
            elif a in legal_studies['Part2']:
                self.ls2 += 1

    def lva(self):
        """This method checks to see if any courses meet the Literary and Visual Arts Concentration, and populates the self.lva_r variable."""
        for a in self.courses:
            if a in lit_visual['Required']:
                self.lva_r += self.get_num_creds(a)

    def mfpa(self):
        """This method checks to see if any courses meet the Managerial Financial Planning and Analysis Concentration, and populates the self.mf_r, mf_e1, and mf_e2 variables."""
        for a in self.courses:
            if a in man_fin_pl['Required']:
                self.mf_r += 1
            elif a in man_fin_pl['Elective1']:
                self.mf_e1 += 1
            elif a in man_fin_pl['Elective2']:
                self.mf_e2 += 1

    def market(self):
        """This method checks to see if any courses meet the Marketing Concentration, and populates the self.mkr, mke1, and mke2 variables."""
        for a in self.courses:
            if a in marketing['Required']:
                self.mkr += 1
            elif a in marketing['Elective1']:
                if self.mke1 == 1:
                    self.mke2 += 1
                else:
                    self.mke1 += 1
            elif a in marketing['Elective2']:
                self.mke2 += 1
    
    def operations_management(self):
        """This method checks to see if any courses meet the Operations Management Concentration, and populates the self.omr and ome variables."""
        for a in self.courses:
            if a in operations_mgmt['Required']:
                self.omr += 1
            elif a in operations_mgmt['Elective']:
                self.ome += 1

    def quant_methods(self):
        """This method checks to see if any courses meet the Quantitative Methods Concentration, and populates the self.qm variable."""
        for a in self.courses:
            if a in quant_m['Required']:
                self.qm += 1
    
    def real_e(self):
        """This method checks to see if any courses meet the Real Estate Concentration, and populates the self.re variable."""
        for a in self.courses:
            if a in real_estate['Required']:
                self.re += 1

    def retail_supplychain(self):
        """This method checks to see if any courses meet the Retail Supply Chain Management Concentration, and populates the self.rscr and rsce variables."""
        for a in self.courses:
            if a in retail_scm['Required']:
                self.rscr += 1
            elif a in retail_scm['Elective']:
                self.rsce += 1

    def social_cultural_studies(self):
        """This method checks to see if any courses meet the Social and Cultural Studies Concentration, and populates the self.sci and sca variables depending on if the met course is in the intermediate or advance category."""
        for a in self.courses:
            if a in social_culture['Intermediate']:
                self.sci += 1
            elif a in social_culture['Advanced']:
                self.sca += 1
    
    def strategy_consulting(self):
        """This method checks to see if any courses meet the Strategy & Consulting Concentration, and populates the self.sc_r and sc_e variables."""
        for a in self.courses:
            if a in strat_cult['Required']:
                self.sc_r += 1
            elif a in strat_cult['Elective']:
                self.sc_e += 1
    
    def tech_entrepreneurship(self):
        """This method checks to see if any courses meet the Tech Entrepreneurship Concentration, and populates the self.ter and tee variables."""
        for a in self.courses:
            if a in tech_entr['Required']:
                self.ter += 1
            elif a in tech_entr['Elective']:
                self.tee += 1
    
    def tech_entre_design(self):
        """This method checks for if certain courses meet the Technology, Entrepreneurship and Design Concentration Categories, and populates the below variables based on which categories are being met."""
        for a in self.courses:
            if a in tech_entr_des['Required']:
                self.ted_r1 += 1
            elif a in tech_entr_des['Req2']:
                self.ted_r2 += 1
            elif a in tech_entr_des['Elective']:
                self.ted_r3 += 1


def store1(workbook):
    """This method will be called by app.py"""

    workbook.sheetnames

    sheet = workbook.active

    ### code that takes all courses from excel and puts them into a list##
    course_list = [sheet["A2"].value, sheet["A3"].value, sheet["A4"].value, sheet["A5"].value, sheet["A6"].value,
                sheet["A11"].value, sheet["A12"].value, sheet["A13"].value, sheet["A14"].value, sheet["A15"].value,

                sheet["E2"].value, sheet["E3"].value, sheet["E4"].value, sheet["E5"].value, sheet["E6"].value,
                sheet["E11"].value, sheet["E12"].value, sheet["E13"].value, sheet["E14"].value, sheet["E15"].value,

                sheet["I2"].value, sheet["I3"].value, sheet["I4"].value, sheet["I5"].value, sheet["I6"].value,
                sheet["I11"].value, sheet["I12"].value, sheet["I13"].value, sheet["I14"].value, sheet["I15"].value,
                
                sheet["M2"].value, sheet["M3"].value, sheet["M4"].value, sheet["M5"].value, sheet["M6"].value,
                sheet["M11"].value, sheet["M12"].value, sheet["M13"].value, sheet["M14"].value, sheet["M15"].value]



# KEY: sheet["B3"].value is EMPTY --- so we use that comparison to essentially see if certain cells are EMPTY.

# for this one, we remove empty cells from the list to prevent errors.
    for z in course_list:
        if z == sheet["B3"].value:
            course_list.remove(z)

# If a student doesn't put their name on the template, we just label them as "Student" ##
    if sheet["C18"].value == sheet["B3"].value:
        id = "Student"  
    else:
        id = sheet["C18"].value

# If a student doesn't list the number of pre-requisites on their excel, we just set it to 0.
    if sheet["H18"].value == sheet["B3"].value:
        pre_req = 0
    else:
        pre_req = int(sheet["H18"].value)

# Here, we just call all the methods to populate the self. variables above

    Object1 = Concentration(id, pre_req, course_list)
    Object1.num_credits()
    Object1.FME()
    Object1.standard()
    Object1.adv_exper()
    Object1.adv_libarts()
    Object1.adv_libarts_elec()
    Object1.gen_elective()
    
    Object1.accounting()
    Object1.analytics()
    Object1.computational()
    Object1.economics()
    Object1.entrepren()
    Object1.enviro_sustainability()
    Object1.financee()
    Object1.global_regional_studies()
    Object1.historical_political()
    Object1.identity_diversity()
    Object1.info_tech_management()
    Object1.inter_business_enviro()
    Object1.just_citi_sr()
    Object1.lead()
    Object1.legal_study()
    Object1.lva()
    Object1.mfpa()
    Object1.market()
    Object1.operations_management()
    Object1.quant_methods()
    Object1.real_e()
    Object1.retail_supplychain()
    Object1.social_cultural_studies()
    Object1.strategy_consulting()
    Object1.tech_entrepreneurship()
    Object1.tech_entre_design()


   # Finally, we return it to 'app.py'
    return(Object1.__str__())


# store1("data/Course_template.xlsx")

