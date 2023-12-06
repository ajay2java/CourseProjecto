# import csv

from dict import general, business_analytics
# from app import f 

from openpyxl import load_workbook

# workbook = load_workbook(filename="data/Course_template.xlsx")


# workbook = load_workbook(filename=f)


# workbook.sheetnames

# sheet = workbook.active

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Concentration:
    
    def __init__(self, name, pre_req, course_list=None):
        ###
        self.name = name
        self.total_creds = int(pre_req)
        self.fMe = 0
        self.std = int(pre_req)
        self.adv_exp = 0
        self.adv_lib = 0
        self.adv_libe = 0
        self.ana_dm = 0
        self.ana_ad = 0
        self.ana_e = 0
        if course_list is None:
            self.courses = []
        else:
            self.courses = course_list
    
    def __str__(self):
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
        
        if self.ana_dm >= 1 and self.ana_ad >= 1 and self.ana_e >= 2:
            s = "Business Analytics Concentration: ✅"
            t.append(s)
        # repeat for other concentrations
        
        # return "\n".join(t)
        return t
            
    
    def num_credits(self):
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
        for a in self.courses:
            if a in general['FME']:
                self.fMe += 1

    def standard(self):
        for a in self.courses:
            if a in general['Standard']:
                self.std += 1

    def adv_exper(self):
        for a in self.courses:
            if a in general['Adv_Experiential']:
                self.adv_exp += 1

    def adv_libarts(self):
        store = ""
        for a in self.courses:
            for i in range(len(a)):
                if a[i] in num:
                    store += a[i]
            if int(store) >= 4600:
                self.adv_lib += self.get_num_creds(a)
            store = ""

    def adv_libarts_elec(self):
        store = ""
        for a in self.courses:
            # print(a)
            for i in range(len(a)):
                if a[i] in num:
                    store += a[i]
            if int(store) >= 3600:
                self.adv_libe += self.get_num_creds(a)
            store = ""

    def analytics(self):
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




def store1(workbook):

    # workbook = load_workbook(filename="data/{f}")
    # workbook = load_workbook(filename=f)

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




    for z in course_list:
        if z == sheet["B3"].value:
            course_list.remove(z)


        

    #Put an int check on this!
    # pre_req = input("How many credits from pre-Babson do you have, which counts? ")

    pre_req = 0

    Object1 = Concentration("Ajay", pre_req, course_list)
    Object1.num_credits()
    Object1.FME()
    Object1.standard()
    Object1.adv_libarts()
    Object1.adv_libarts_elec()
    Object1.analytics()

    # print(Ajay)
    # return(str(Object1))
    return(Object1.__str__())


# store1("data/Course_template.xlsx")
