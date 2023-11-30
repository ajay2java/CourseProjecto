import csv

from dict import general, business_analytics
workbook = data(filename="")

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Fall Year 1: A2
#Spring Year 1: A11

#Fall Year 2: E2
#Spring Year 2: E11

#Fall Year 3: I2
#Spring Year 3: I11

#Fall Year 4: M2
#Spring Year 4: M11

###   Analytics Concentration  ###
# def course_by_course():
    
    #while ___[each course input from the user's spreadsheet]__(recursive)
        ### will cycle through the excel for each course ###
        #if conc == "Business Analytics"
            #if header == "Data Management and Programming Concepts":
                #if Ana_DataMgmt_Prog == 1:
                    #Ana_Elec += 1
                #else:
                    #Ana_DataMgmt_Prog += 1:
            #elif header == "Advanced Data and Decision Modeling":
                #if Ana_Data_DecM == 1:
                    #Ana_Elec += 1
                #else:
                    #Ana_Data_DecM += 1:
        #if conc == "Finance":

    #if Ana_DataMgmt_Prog == 1 and Ana_Data_DecM == 1 and Ana_Elec == 2:
    ##print("You have fulfilled all the requirements for the Analytics Concentration!")


class Concentration:
    
    def __innit__(self, name, total_creds, ana_dm, ana_ad, ana_e, course_list=None):
        ###
        self.name = name
        self.total_creds = 0
        self.fMe = 0
        self.adv_lib = 0
        self.adv_libe = 0
        self.ana_dm = ana_dm
        self.ana_ad = ana_ad
        self.ana_e = ana_e
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
        
        return "\n".join(t)
            
    
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


### code that takes all courses from excel and puts them into a list##
course_list = []
#for i in range (len(excel)):
    #course_list.append(i)

pre_req = input("How many credits from pre-Babson do you have, which counts?")

Ajay = Concentration("Ajay", course_list, pre_req)
print(Ajay)

