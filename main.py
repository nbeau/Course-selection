class CourseOption:
    def __init__(self, name, day, start_hour, start_min, length, second_class=None, list_discussion_groups=None, list_labs=None):
        self.name = name
        self.day = day
        self.start_hour = start_hour
        self.start_min = start_min
        self.length = length
        self.second_class = second_class
        self.list_discussion_groups = list_discussion_groups
        self.list_labs = list_labs
    
    def get_second_class(self):
        return self.second_class

    def __repr__(self):
        out_str = ""
        out_str += self.name + " Starts: " + str(self.start_hour) + ":" + str(self.start_min) + " Len: " + str(self.length)
        return out_str
        
    def __lt__(self, other):
        if self.day < other.day: 
            return True
        elif self.day == other.day:
            if self.start_hour < other.start_hour: 
                return True
        return False
            
    def getTimeSlots(self):
        timeSlotList = []
        minute = self.start_min
        hour = self.start_hour
        for i in range(int(self.length / 30)):
            if minute == 0:
                strSlot = str(self.day) + "_" + str(hour) + "00"
                timeSlotList.append(strSlot)
                minute = 30
            elif minute == 30:
                strSlot = str(self.day) + "_" + str(hour) + "30"
                timeSlotList.append(strSlot)
                minute = 0
                hour += 1
        if self.second_class != None:
            secondTS = self.second_class.getTimeSlots()
            for TS in secondTS:
                timeSlotList.append(TS)
        return timeSlotList
     
 

eng1dg1 = CourseOption("ENGD", 3, 14, 30, 90)
eng1dg = []
eng1dg.append(eng1dg1)

eng2dg1 = CourseOption("ENGD", 5, 10, 0, 90)
eng2dg = []
eng2dg.append(eng2dg1)

eng3dg1 = CourseOption("ENGD", 5, 19, 0, 90)
eng3dg = []
eng3dg.append(eng3dg1)

eng4dg1 = CourseOption("ENGD", 4, 8, 30, 90)
eng4dg = []
eng4dg.append(eng4dg1)

eng5dg1 = CourseOption("ENGD", 2, 14, 30, 90)
eng5dg = []
eng5dg.append(eng5dg1)

eng6dg1  = CourseOption("ENGD", 1, 10, 0, 90)
eng6dg = []
eng6dg.append(eng6dg1)

eng7dg1 = CourseOption("ENGD", 5, 8, 30, 90)
eng7dg = []
eng7dg.append(eng7dg1)

eng1 = CourseOption("ENG1112", 1, 16, 0, 90, None, eng1dg)
eng2 = CourseOption("ENG1112", 2, 8, 30, 90, None, eng2dg)
eng3 = CourseOption("ENG1112", 5, 17, 30, 90, None, eng3dg)
eng4 = CourseOption("ENG1112", 2, 10, 0, 90, None, eng4dg)
eng5 = CourseOption("ENG1112", 5, 16, 0, 90, None, eng5dg)
eng6 = CourseOption("ENG1112", 3, 8, 30, 90, None, eng6dg)
eng7 = CourseOption("ENG1112", 3, 10, 0, 90, None, eng7dg)
eng = []
eng.append(eng1)
eng.append(eng2)
eng.append(eng3)
eng.append(eng4)
eng.append(eng5)
eng.append(eng6)
eng.append(eng7)



iti1lab1 = CourseOption("ITILAB", 3, 16, 0, 180)
iti1lab2 = CourseOption("ITILAB", 4, 8, 30, 180)
iti1lab3 = CourseOption("ITILAB", 4, 16, 0, 180)
iti1lab4 = CourseOption("ITILAB", 5, 14, 30, 180)
iti1lab = []
iti1lab.append(iti1lab1)
iti1lab.append(iti1lab2)
iti1lab.append(iti1lab3)
iti1lab.append(iti1lab4)

iti2lab1 = CourseOption("ITILAB", 2, 10, 0, 180)
iti2lab2 = CourseOption("ITILAB", 3, 19, 0, 180)
iti2lab3 = CourseOption("ITILAB", 4, 16, 0, 180)
iti2lab4 = CourseOption("ITILAB", 5, 17, 30, 180)
iti2lab = []
iti2lab.append(iti2lab1)
iti2lab.append(iti2lab2)
iti2lab.append(iti2lab3)
iti2lab.append(iti2lab4)

iti3lab1 = CourseOption("ITILAB", 1, 8, 30, 180)
iti3lab2 = CourseOption("ITILAB", 1, 14, 30, 180)
iti3lab3 = CourseOption("ITILAB", 3, 8, 30, 180)
iti3lab4 = CourseOption("ITILAB", 5, 8, 30, 180)
iti3lab = []
iti3lab.append(iti3lab1)
iti3lab.append(iti3lab2)
iti3lab.append(iti3lab3)
iti3lab.append(iti3lab4)

iti1sc = CourseOption("ITI1120", 1, 13, 0, 90)
iti2sc = CourseOption("ITI1120", 1, 16, 0, 90)
iti3sc = CourseOption("ITI1120", 2, 14, 30, 90)

iti1 = CourseOption("ITI1120", 3, 11, 30, 90, iti1sc, None, iti1lab)
iti2 = CourseOption("ITI1120", 3, 14, 30, 90, iti2sc, None, iti2lab)
iti3 = CourseOption("ITI1120", 5, 16, 0, 90, iti3sc, None, iti3lab)
iti = []
iti.append(iti1)
iti.append(iti2)
iti.append(iti3)



mat1dg1 = CourseOption("MATD", 5, 8, 30, 90)
mat1dg2 = CourseOption("MATD", 5, 10, 0, 90)
mat1dg3 = CourseOption("MATD", 5, 11, 30, 90)
mat1dg4 = CourseOption("MATD", 5, 13, 0, 90)
mat1dg5 = CourseOption("MATD", 5, 14, 30, 90)
mat1dg = []
mat1dg.append(mat1dg1)
mat1dg.append(mat1dg2)
mat1dg.append(mat1dg3)
mat1dg.append(mat1dg4)
mat1dg.append(mat1dg5)

mat2dg1 = CourseOption("MATD", 5, 10, 0, 90)
mat2dg2 = CourseOption("MATD", 5, 11, 30, 90)
mat2dg3 = CourseOption("MATD", 5, 13, 0, 90)
mat2dg4 = CourseOption("MATD", 5, 14, 30, 90)
mat2dg5 = CourseOption("MATD", 5, 16, 0, 90)
mat2dg = []
mat2dg.append(mat2dg1)
mat2dg.append(mat2dg2)
mat2dg.append(mat2dg3)
mat2dg.append(mat2dg4)
mat2dg.append(mat2dg5)

mat3dg1 = CourseOption("MATD", 5, 10, 0, 90)
mat3dg2 = CourseOption("MATD", 5, 11, 30, 90)
mat3dg3 = CourseOption("MATD", 5, 13, 0, 90)
mat3dg = []
mat3dg.append(mat3dg1)
mat3dg.append(mat3dg2)
mat3dg.append(mat3dg3)

mat4dg1 = CourseOption("MATD", 5, 8, 30, 90)
mat4dg2 = CourseOption("MATD", 5, 10, 0, 90)
mat4dg3 = CourseOption("MATD", 5, 11, 30, 90)
mat4dg4 = CourseOption("MATD", 5, 13, 30, 90)
mat4dg = []
mat4dg.append(mat4dg1)
mat4dg.append(mat4dg2)
mat4dg.append(mat4dg3)
mat4dg.append(mat4dg4)

mat5dg1 = CourseOption("MATD", 5, 8, 30, 90)
mat5dg2 = CourseOption("MATD", 5, 10, 0, 90)
mat5dg3 = CourseOption("MATD", 5, 11, 30, 90)
mat5dg4 = CourseOption("MATD", 5, 13, 0, 90)
mat5dg = []
mat5dg.append(mat5dg1)
mat5dg.append(mat5dg2)
mat5dg.append(mat5dg3)
mat5dg.append(mat5dg4)

mat1sc = CourseOption("MAT1320", 1, 10, 0, 90)
mat2sc = CourseOption("MAT1320", 1, 13, 0, 90)
mat3sc = CourseOption("MAT1320", 1, 17, 30, 90)
mat4sc = CourseOption("MAT1320", 1, 13, 0, 90)
mat5sc = CourseOption("MAT1320", 1, 10, 0, 90)

mat1 = CourseOption("MAT1320", 3, 8, 30, 90, mat1sc, mat1dg)
mat2 = CourseOption("MAT1320", 3, 11, 30, 90, mat2sc, mat2dg)
mat3 = CourseOption("MAT1320", 3, 17, 30, 90, mat3sc, mat3dg)
mat4 = CourseOption("MAT1320", 3, 11, 30, 90, mat4sc, mat4dg)
mat5 = CourseOption("MAT1320", 3, 8, 30, 90, mat5sc, mat5dg)
mat = []
mat.append(mat1)
mat.append(mat2)
mat.append(mat3)
mat.append(mat4)
mat.append(mat5)



phydg1 = CourseOption("PHYD", 2, 10, 0, 90)
phydg2 = CourseOption("PHYD", 3, 10, 0, 90)
phydg3 = CourseOption("PHYD", 1, 14, 30, 90)
phydg4 = CourseOption("PHYD", 5, 13, 0, 90)
phydg = []
phydg.append(phydg1)
phydg.append(phydg2)
phydg.append(phydg3)
phydg.append(phydg4)

phylab1 = CourseOption("PHYLAB", 2, 14, 30, 180)
phylab2 = CourseOption("PHYLAB", 3, 14, 30, 180)
phylab3 = CourseOption("PHYLAB", 4, 14, 30, 180)
phylab4 = CourseOption("PHYLAB", 5, 14, 30, 180)
phylab = []
phylab.append(phylab1)
phylab.append(phylab2)
phylab.append(phylab3)
phylab.append(phylab4)

phy1sc = CourseOption("PHY1321", 1, 13, 0, 90)
phy2sc = CourseOption("PHY1321", 2, 8, 30, 90)

phy1 = CourseOption("PHY1321", 3, 11, 30, 90, phy1sc, phydg, phylab)
phy2 = CourseOption("PHY1321", 5, 10, 0, 90, phy2sc, phydg, phylab)
phy = []
phy.append(phy1)
phy.append(phy2)



seg1dg1 = CourseOption("SEGTUT", 2, 19, 0, 90)
seg1dg = []
seg1dg.append(seg1dg1)

seg1sc = CourseOption("SEG2900", 2, 17, 30, 90)
 
seg1 = CourseOption("SEG2900", 4, 13, 0, 90, seg1sc, seg1dg)
seg = []
seg.append(seg1)


counter = 0
counter2 = 0
for e in eng:
    for i in iti:
        for s in seg:
            for m in mat:
                for p in phy:
                    for edg in e.list_discussion_groups:
                        for sdg in s.list_discussion_groups:
                            for mdg in m.list_discussion_groups:
                                for pdg in p.list_discussion_groups:
                                    for ilab in i.list_labs:
                                        for plab in p.list_labs:
                                            counter2 += 1
                                            eList = e.getTimeSlots()
                                            iList = i.getTimeSlots()
                                            sList = s.getTimeSlots()
                                            mList = m.getTimeSlots()
                                            pList = p.getTimeSlots()
                                            edgList = edg.getTimeSlots()
                                            sdgList = sdg.getTimeSlots()
                                            mdgList = mdg.getTimeSlots()
                                            pdgList = pdg.getTimeSlots()
                                            ilabList = ilab.getTimeSlots()
                                            plabList = plab.getTimeSlots()
                                            timeSlotList = eList + iList + sList + mList + pList + edgList + sdgList + mdgList + pdgList + ilabList + plabList
                                            if any(int(slot[2::]) > 1130 and slot[0] == "5" for slot in timeSlotList):
                                                continue
                                            if any(int(slot[2::]) > 1130 and int(slot[2::]) < 1300 for slot in timeSlotList):
                                                continue
                                            if len(timeSlotList) != len(set(timeSlotList)): 
                                                continue
                                            print("\n\n\nfound one: ", counter)
                                            courseList = [e, i, i.get_second_class(), s, s.get_second_class(), m, m.get_second_class(), p, p.get_second_class(), edg, sdg, mdg, pdg, ilab, plab]
                                            courseList.sort()
                                            monday = False
                                            tuesday = False
                                            wednesday = False
                                            thursday = False
                                            friday = False
                                            for x in courseList:
                                                if x.day == 1:
                                                    if monday == False: 
                                                        print("Monday:")
                                                        monday = True
                                                if x.day == 2:
                                                    if tuesday == False:
                                                        print("\nTuesday:")
                                                        tuesday = True
                                                if x.day == 3:
                                                    if wednesday == False:
                                                        print("\nWednesday:")
                                                        wednesday = True
                                                if x.day == 4:
                                                    if thursday == False:
                                                        print("\nThursday:")
                                                        thursday = True
                                                if x.day == 5:
                                                    if friday == False:
                                                        print("\nFriday:")
                                                        friday = True
                                                print(x)
                                            counter += 1
                      
print(counter, "out of", counter2, "possible combinations were valid")