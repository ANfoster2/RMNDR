# from ui_mainwindow import *
# from dialog_addnew import *
# import sqlite3
    
#class LoadData(object):
#    def loadData(self):
#         dateSelected = self.dateEdit_task.date().toPyDate()
#         weekday =dateSelected.isoweekday()
#         if weekday == 1:
#             weekday = 'Monday'
#         elif weekday ==2:
#             weekday = 'Tuesday'
#         elif weekday ==3:
#             weekday = 'Wednesday'
#         elif weekday ==4:
#             weekday = 'Thursday'
#         elif weekday ==5:
#             weekday = 'Friday'
#         elif weekday ==6:
#             weekday = 'Saturday'
#         elif weekday ==7:
#             weekday = 'Sunday'
#         taskName = self.txt_task_name.text()
#         taskDescription = self.txt_task_description.toPlainText()
#         estimatedTime = str(self.cb_estimated_time.currentText())

#         conn = sqlite3.connect("tasks.db")
#         cur = conn.cursor()
#         user_info = [weekday, taskName, taskDescription, estimatedTime, dateSelected,]
#         cur.execute('INSERT INTO task_info(Weekday, Task_Name, Task_Description, Estimated_Time, Date) VALUES(?, ?, ?, ?, ?)', user_info)

#         conn.commit()
#         print('Record inserted successfully')
#         conn.close()
#         self.function_loadData.chooseLoadDay()

#     def chooseLoadDay(self, weekday):
#         weekday = dialog_addnew.loadData(weekday)
#         if weekday == 'Monday':
#             self.loadMonday
#         elif weekday == 'Tuesday':
#             self.loadTuesday
#         elif weekday == 'Wednesday':
#             self.loadWednesday
#         elif weekday == 'Thursday':
#             self.loadThursday
#         elif weekday == 'Friday':
#             self.loadFriday
#         elif weekday == 'Saturday':
#             self.loadSaturday
#         elif weekday == 'Sunday':
#             self.loadSunday

#     def loadSunday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Sunday';"

#         self.tbl_sunday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_sunday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadMonday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Monday';"
#         self.tbl_monday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_monday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadTuesday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Tuesday';"
#         self.tbl_tuesday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_tuesday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadWednesday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Wednesday';"
#         self.tbl_wednesday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_wednesday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadThursday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Thursday';"
#         self.tbl_thursday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_thursday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadFriday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Friday';"
#         self.tbl_friday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_friday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
#     def loadSaturday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Saturday';"
#         self.tbl_saturday.setRowCount(7)
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_saturday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1

