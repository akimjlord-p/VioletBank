from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from core.Contribution import Contribution, ContributionException
import io
import pyqtgraph


def is_number(str_: str) -> bool:
    try:
        float(str_)
        return True
    except ValueError:
        return False


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>770</width>
    <height>725</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Contribution</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QMainWindow {
            background-color: #1A1A1A; /* Темный фон */
        }
        QLabel {
            color: white; /* Белый цвет текста метки */
            font-size: 16px; /* Размер шрифта метки */
            margin-bottom: 10px; /* Отступ снизу */
        }
        QRadioButton {
            color: white; /* Белый цвет текста радиокнопки */
            font-size: 16px; /* Размер шрифта радиокнопки */
        }
        QRadioButton::indicator {
            background-color: #2E2E2E; /* Фон радиокнопки */
            border: 2px solid #800080; /* Граница радиокнопки */
            width: 20px; /* Ширина индикатора */
            height: 20px; /* Высота индикатора */
        }
        QRadioButton::indicator:checked {
            background-color: #800080; /* Фон радиокнопки при выборе */
        }
        QDoubleSpinBox, QSpinBox {
            background-color: #2E2E2E; /* Фон спинбоксов */
            color: white; /* Белый текст в спинбоксах */
            border: 2px solid #800080; /* Фиолетовая рамка */
            border-radius: 5px; /* Закругленные углы */
            padding: 5px; /* Отступ внутри */
            font-size: 16px; /* Размер шрифта спинбоксов */
        }
        QPushButton {
            background-color: #2E2E2E; /* Темный серый фон для кнопки */
            color: white; /* Белый текст */
            border: 2px solid #800080; /* Фиолетовая рамка */
            border-radius: 10px; /* Закругленные углы */
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #800080; /* Фиолетовый цвет при наведении */
        }
        QPushButton:pressed {
            background-color: #3A3A3A; /* Затемненная кнопка при нажатии */
        }
		QListWidget{
			color: white; /* Белый цвет текста метки */
            font-size: 16px; /* Размер шрифта метки */
            margin-bottom: 10px; /* Отступ снизу */
			 background-color: #1A1A1A; /* Темный фон */
		}</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>751</width>
     <height>711</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QLabel" name="label">
        <property name="text">
         <string>Name:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="name"/>
      </item>
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Sum of contribution:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="sum_"/>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QLabel" name="label_3">
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="text">
         <string>Percent:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QDoubleSpinBox" name="percent">
        <property name="showGroupSeparator" stdset="0">
         <bool>false</bool>
        </property>
        <property name="suffix">
         <string>%</string>
        </property>
        <property name="decimals">
         <number>3</number>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QRadioButton" name="difficult">
          <property name="text">
           <string>Difficult percent</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">percent_group</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QRadioButton" name="simple">
          <property name="text">
           <string>Simple percent</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">percent_group</string>
          </attribute>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLabel" name="label_4">
        <property name="text">
         <string>Term:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QSpinBox" name="term"/>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <item>
         <widget class="QRadioButton" name="year">
          <property name="text">
           <string>Year</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">time_group</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QRadioButton" name="month">
          <property name="text">
           <string>Month</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">time_group</string>
          </attribute>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item>
     <widget class="PlotWidget" name="plot_wdgt" native="true"/>
    </item>
    <item>
     <widget class="QPushButton" name="res_btn">
      <property name="text">
       <string>Calculate</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QListWidget" name="list_for_plot"/>
    </item>
    <item>
     <widget class="QPushButton" name="save_btn">
      <property name="text">
       <string>Save</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="save_as_csv_btn">
      <property name="text">
       <string>Save as .csv</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QWidget</extends>
   <header>pyqtgraph</header>
   <container>1</container>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="percent_group"/>
  <buttongroup name="time_group"/>
 </buttongroups>
</ui>
'''


class ContributionWindow(QMainWindow):
    def __init__(self, contribution=None):
        super().__init__()

        self.data = None
        self.contribution = contribution

        f = io.StringIO(template)
        uic.loadUi(f, self)

        if contribution:
            self.name.setText(contribution.name)
            self.sum_.setText(str(contribution.start_sum))
            self.percent.setValue(contribution.percent)
            self.term.setValue(contribution.term)
            if self.contribution.type_of_capitalization == 'dif':
                self.difficult.setChecked(True)
            else:
                self.simple.setChecked(True)
            if self.contribution.type_of_term == 'year':
                self.year.setChecked(True)
            else:
                self.month.setChecked(True)

        self.plot_wdgt.hide()

        self.list_for_plot.hide()

        self.res_btn.clicked.connect(self.calculate)

        self.save_btn.hide()
        self.save_btn.clicked.connect(self.save_to_db)

        self.save_as_csv_btn.hide()
        self.save_as_csv_btn.clicked.connect(self.save_to_csv)

    def calculate(self):
        check_input = self.error_in_input()
        if not check_input:
            name = self.name.text()
            sum_ = float(self.sum_.text())
            percent = float(self.percent.value())
            term = int(self.term.value())

            type_of_capitalization = 'dif'
            if self.simple.isChecked():
                type_of_capitalization = 'simple'

            type_of_term = 'year'
            if self.month.isChecked():
                type_of_term = 'month'

            self.contribution = Contribution(name, sum_, percent, type_of_term, term, type_of_capitalization)
            self.contribution.calculate()

            self.data = self.contribution.get_data()

            self.fill_plot()
            self.fill_list()

            self.plot_wdgt.show()
            self.list_for_plot.show()
            self.save_btn.show()
            self.save_as_csv_btn.show()
        else:
            error = QMessageBox()
            error.setWindowTitle('ERROR')
            error.setText(check_input)
            error.setIcon(QMessageBox.Icon.Warning)
            error.exec()

    def error_in_input(self):
        try:
            if not self.name.text():
                raise ContributionException('Please set name!')

            if not self.sum_.text() or not is_number(str(self.sum_.text())):
                raise ContributionException('Please set sum of deposit!')

            if float(self.percent.value()) == 0:
                raise ContributionException('Please set percent value!')

            if int(self.term.value()) == 0:
                raise ContributionException('Please set term!')

            if not (self.difficult.isChecked() or self.simple.isChecked()):
                raise ContributionException('Please set type of capitalization!')

            if not (self.year.isChecked() or self.month.isChecked()):
                raise ContributionException('Please set type of term!')

            return False

        except ContributionException as ex:
            return str(ex)

    def fill_plot(self):
        self.plot_wdgt.clear()
        self.plot_wdgt.showGrid(x=True, y=True)
        self.plot_wdgt.plot(list(range(1, len(self.data) + 1)), self.data, pen='r')

    def fill_list(self):
        self.list_for_plot.clear()
        for n, i in enumerate(self.data):
            if n != 0:
                self.list_for_plot.addItem(f'{self.contribution.type_of_term}: {n} contribution: {int(i)}')
            else:
                self.list_for_plot.addItem(f'start contribution: {i}')

    def save_to_db(self):
        res = self.contribution.save_to_db()
        saved_msg = QMessageBox()
        if res:
            saved_msg.setWindowTitle('Updated')
            saved_msg.setText("Updated into local base")
        else:
            saved_msg.setWindowTitle('Saved')
            saved_msg.setText("Saved into local base")
        saved_msg.setIcon(QMessageBox.Icon.Information)
        saved_msg.exec()

    def save_to_csv(self):
        if self.contribution:
            self.contribution.save_as_csv()
        saved_msg = QMessageBox()
        saved_msg.setWindowTitle('Saved')
        saved_msg.setText("Saved as .csv file")
        saved_msg.setIcon(QMessageBox.Icon.Information)
        saved_msg.exec()
