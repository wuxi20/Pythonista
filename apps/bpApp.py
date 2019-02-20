# 您可以在此处粘贴Pythonista脚本。
#
# 要更改应用程序的图标，您可以修改Icon76.png（iPad非视网膜),
# Icon120.png (iPhone) 和 Icon152.png (iPad retina).
#
# 如果您不希望脚本在后台运行，请打开Info.plist，
#并将“应用程序不在后台运行”设置为是
# 要在主屏幕上更改应用程序的名称，请打开Info.plist，然后
#更改“Bundle display name”。

# 要减小应用程序的大小，您可以从纹理中删除未使用的图像
# 文件夹.
#
# 请注意，独立应用程序目前不支持matplotlib.

# coding: utf-8

import ui
import os
import pickle as pickle
import datetime
import re
import console

@ui.in_background
def empty():
   console.alert('empty')

class bloodAppView(object):
   def __init__(self):
      self.file = "app.dat"
      self.loadData()
      self.v = ui.View(name="bloodApp")
      self.v.background_color = 'white'
      self.v.left_button_items = ui.ButtonItem(title='sugar',action=self.switchBs),ui.ButtonItem(title='BP',action=self.switchBp)
      self.v.right_button_items = ui.ButtonItem(title='save', action=self.save),

      self.timePick = ui.DatePicker(name = "timePick")
      self.timePick.mode = ui.DATE_PICKER_MODE_DATE_AND_TIME
      
      self.table = ui.TableView(name = "Table")
      self.table.data_source = self
      self.table.background_color = (1,1,1,1)
      self.table.border_color = (0,0,0,1)
      self.table.row_height = 30
      self.table.flex = "WH"
      self.table.border_width = 1
      self.table.corner_radius = 1
      self.table.frame = (0,200,320,272)
      
      self.value = ui.TextField(name = "value")
      self.value.keyboard_type = ui.KEYBOARD_PHONE_PAD
      self.value.clear_button_mode ='always'
      self.value.x = 0;
      self.value.y = 0
      self.value.width = 120
      self.value.height = 38.5
      self.value.background_color = (1,1,1,1)
      self.value.border_color = (0,0,0,1)
      self.value.border_width = 1
      self.value.corner_radius = 2
      self.value.alignment = ui.ALIGN_LEFT
      self.value.enabled = 1
      self.value.placeholder ='blood sugar'
      
      self.v.add_subview(self.timePick)
      self.v.add_subview(self.table)
      self.v.add_subview(self.value)
      
      self.state = "bs"
      self.switch()
      self.table.reload()

      self.v.present("fullscreen")

      
   def switchBs(self,sender):
      if self.state != "bs":
         self.state = "bs"
         self.switch()

   def switchBp(self,sender):
      if self.state != "bp":
         self.state = "bp"
         self.switch()

   def switch(self):
      if self.state == "bs":
         self.value.placeholder ='blood sugar'
      else:
         self.value.placeholder ='blood pressure'

      self.value.text = ''
      self.table.reload()
      self.v.set_needs_display()

   def eraseData(self):
       self.bsData = {}
       self.bpData = {}
       saveData()
                             
   def loadData(self):
       if os.path.exists(self.file):
          data = pickle.load(open(self.file,'rb'))
          self.bpData = data["bp"]
          self.bsData = data["bs"]
       else:
          self.bsData = {}
          self.bpData = {}

   def saveData(self):
      data = {}
      data["bs"] = self.bsData
      data["bp"] = self.bpData
      pickle.dump(data,open(self.file,'wb'))

   def clear(self, sender):
       self.eraseData()

   def save(self, sender):
      t = self.timePick.date.isoformat()
      self.timePick.date = datetime.datetime.now()

      val = self.value.text
      self.value.text = ''
      self.value.end_editing()
      
      if val == '':
         empty()
         self.value.end_editing()
         return

      if self.state == "bs":
         self.bsData[t] = str(val)
      else:
         self.bpData[t] = re.sub('[+*#]', ':', val)

      self.saveData()
      self.table.reload()

   def tableview_number_of_rows(self, tv, s):
      if self.state == "bs":
         return len(self.bsData)
      else:
         return len(self.bpData)

   def tableview_title_for_header(self, tableview, section):
      if self.state == "bs":
         return 'Blood sugars'
      else:
         return 'Blood pressure readings'
     
   def tableview_cell_for_row(self, tv, s, r):
      cell = ui.TableViewCell()
      if self.state == "bs":
         ks = sorted(self.bsData.keys())
      else:
         ks = sorted(self.bpData.keys())

      ks.reverse()
      date = ks[r]

      if self.state == "bs":
         val = self.bsData[date]
      else:
         val = self.bpData[date]
      
      z = ui.Label()
      z.text = re.sub('T',' ',date)
      z.center = (70,20)
      z.width = 200
      z.alignment = ui.ALIGN_LEFT
      cell.content_view.add_subview(z)

      label = ui.Label()
      label.text = val
      label.center = (310,20)
      label.width = 50
      label.alignment = ui.ALIGN_RIGHT
      cell.content_view.add_subview(label)

      return cell

bloodAppView()

