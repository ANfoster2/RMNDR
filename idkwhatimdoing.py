# import dialog_addnew
# class load(object):
#  #load data into SQLite
#     def loadData(self, weekday):
#         dateSelected = self.dateEdit_task.date().toPyDate()
#         weekday =dateSelected.isoweekday() #returns weekday as number (1-7)
#         if weekday == 1:
#             self.weekday = 'Monday'
#         elif weekday ==2:
#             self.weekday = 'Tuesday'
#         elif weekday ==3:
#             self.weekday = 'Wednesday'
#         elif weekday ==4:
#             self.weekday = 'Thursday'
#         elif weekday ==5:
#             self.weekday = 'Friday'
#         elif weekday ==6:
#             self.weekday = 'Saturday'
#         elif weekday ==7:
#             self.weekday = 'Sunday'
#         return weekday
        
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

#         import ui_mainwindow
#         if weekday == 'Monday':
#             self.loadMonday()
#         elif weekday == 'Tuesday':
#             self.loadTuesday()
#         elif weekday == 'Wednesday':
#             self.loadWednesday()
#         elif weekday == 'Thursday':
#             self.loadThursday()
#         elif weekday == 'Friday':
#             self.loadFriday()
#         elif weekday == 'Saturday':
#             self.loadSaturday()
#         elif weekday == 'Sunday':
#             self.loadSunday()

         
#         #load SQL data into table based on weekday
# def loadSunday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Sunday';"

#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_sunday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadMonday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Monday';"
       
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_monday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadTuesday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Tuesday';"
       
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_tuesday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadWednesday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Wednesday';"
        
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_wednesday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadThursday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Thursday';"
        
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_thursday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadFriday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Friday';"
        
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_friday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
# def loadSaturday(self):
#         connection = sqlite3.connect("tasks.db")
#         cur = connection.cursor()
#         sqlquery = "Select Task_Name FROM task_info WHERE Weekday = 'Saturday';"
        
#         tablerow = 0
#         for row in cur.execute(sqlquery):
#                 self.tbl_saturday.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
#                 tablerow +=1
      