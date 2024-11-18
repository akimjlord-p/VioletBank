from PyQt6.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QMessageBox
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from ui.ContributionWindow import ContributionWindow
from ui.LoanWindow import LoanWindow
from core.db_func import get_projects, get_contribution_by_name, get_loan_by_name
from core.csv_func import get_type_of_project, get_contribution_from_csv, get_loan_from_csv
from core.Contribution import Contribution
from core.Loan import Loan
import io


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>VioletBank</class>
 <widget class="QWidget" name="VioletBank">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>953</width>
    <height>814</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>VioletBank</string>
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
		QInputDialog{
			 background-color: #1A1A1A; /* Темный фон */
		}</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>951</width>
     <height>811</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLabel" name="logo">
        <property name="minimumSize">
         <size>
          <width>0</width>
          <height>0</height>
         </size>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="app_name">
        <property name="enabled">
         <bool>true</bool>
        </property>
        <property name="sizePolicy">
         <sizepolicy hsizetype="MinimumExpanding" vsizetype="Fixed">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>VioletBank - Application for bank calculations</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <property name="sizeConstraint">
       <enum>QLayout::SetFixedSize</enum>
      </property>
      <item>
       <widget class="QPushButton" name="deposit_btn">
        <property name="text">
         <string>New contribution</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="credit_btn">
        <property name="text">
         <string>New loan</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <property name="sizeConstraint">
       <enum>QLayout::SetFixedSize</enum>
      </property>
      <item>
       <widget class="QPushButton" name="from_csv_btn">
        <property name="text">
         <string>Open from .csv file</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="from_db_btn">
        <property name="text">
         <string>Open from current base</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.deposit_btn.clicked.connect(self.open_new_contribution)
        self.contribution_window = None
        self.loan_window = None
        self.from_csv_btn.clicked.connect(self.open_project_from_csv)
        self.from_db_btn.clicked.connect(self.open_project_from_db)
        self.credit_btn.clicked.connect(self.open_new_loan)
        pixmap = QPixmap('ui/logo.png')
        pixmap.scaled(50, 50)
        self.logo.setPixmap(pixmap)


    def open_new_contribution(self):
        self.contribution_window = ContributionWindow()
        self.contribution_window.show()

    def open_new_loan(self):
        self.loan_window = LoanWindow()
        self.loan_window.show()

    def open_project_from_csv(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать csv файл', '',
            'csv файл (*.csv);;')[0]
        if get_type_of_project(fname) == 'contribution':
            self.get_contribution_window_from_dict(get_contribution_from_csv(fname))
        else:
            self.get_loan_window_from_dict(get_loan_from_csv(fname))

    def open_project_from_db(self):
        names_list = get_projects()
        if len(names_list) != 0:
            project, ok_pressed = QInputDialog.getItem(
                None, "Select your project", "project:",
                names_list, 1, False)
            if project.split()[0] == 'contribution':
                self.get_contribution_window_from_dict(get_contribution_by_name(project.split()[1]))
            else:
                self.get_loan_window_from_dict(get_loan_by_name(project.split()[1]))

        else:
            saved_msg = QMessageBox()
            saved_msg.setWindowTitle('No projects')
            saved_msg.setText("No projects in local base")
            saved_msg.setIcon(QMessageBox.Icon.Information)
            saved_msg.exec()

    def get_contribution_window_from_dict(self, contribution_data):
        self.contribution_window = ContributionWindow(Contribution(
            name=contribution_data['name'],
            start_sum=float(contribution_data['start_sum']),
            percent=float(contribution_data['percent']),
            type_of_term=contribution_data['type_of_term'],
            term=int(contribution_data['term']),
            type_of_capitalization=contribution_data['type_of_capitalization']))
        self.contribution_window.show()

    def get_loan_window_from_dict(self, loan_data):
        self.loan_window = LoanWindow(Loan(
            name=loan_data['name'],
            start_sum=loan_data['start_sum'],
            percent=loan_data['percent'],
            term=loan_data['term'],
        ))
        self.loan_window.show()



