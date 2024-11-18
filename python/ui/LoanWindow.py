from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from core.Loan import Loan, LoanException
import io

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
   <string>Loan</string>
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

		}
		QTableWidget {
                background-color: #2E2E2E;
                gridline-color: #800080;        /* Цвет линий сетки */
            }
            QHeaderView::section {
                background-color: #2E2E2E;   /* Цвет заголовков столбцов */
				color: white; /* Белый цвет текста метки */
                font-weight: bold;            /* Жирный шрифт для заголовков */
                padding: 4px;                 /* Отступ для заголовков */
            }
            QTableWidget::item {
			 color: white; /* Белый цвет текста метки */
                background-color:  #2E2E2E;    /* Цвет фона ячеек */
                border: 1px solid #ccc;       /* Рамка для ячеек */
            }
            QTableWidget::item:selected {
                background-color: #800080;    /* Цвет фона выделенных ячеек */
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
    <property name="sizeConstraint">
     <enum>QLayout::SetMinimumSize</enum>
    </property>
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
         <string>Sum of loan:</string>
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
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLabel" name="label_4">
        <property name="text">
         <string>Term (months):</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QSpinBox" name="term"/>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QPushButton" name="res_btn">
      <property name="text">
       <string>Calculate</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QTableWidget" name="table">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <attribute name="horizontalHeaderCascadingSectionResizes">
       <bool>true</bool>
      </attribute>
      <attribute name="horizontalHeaderDefaultSectionSize">
       <number>180</number>
      </attribute>
      <attribute name="horizontalHeaderMinimumSectionSize">
       <number>180</number>
      </attribute>
      <attribute name="verticalHeaderCascadingSectionResizes">
       <bool>true</bool>
      </attribute>
      <attribute name="verticalHeaderDefaultSectionSize">
       <number>39</number>
      </attribute>
      <attribute name="verticalHeaderStretchLastSection">
       <bool>true</bool>
      </attribute>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_4">
      <item>
       <widget class="QLabel" name="overpayment">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Overpayment</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="mothly_payment">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>mothly_payment</string>
        </property>
       </widget>
      </item>
     </layout>
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
 <resources/>
 <connections/>
</ui>
'''

class LoanWindow(QMainWindow):
    def __init__(self, loan=None):
        super().__init__()

        self.data = None
        self.loan = loan

        f = io.StringIO(template)
        uic.loadUi(f, self)

        if self.loan:
            self.name.setText(loan.name)
            self.sum_.setText(str(loan.start_sum))
            self.percent.setValue(loan.percent)
            self.term.setValue(loan.term)

        self.res_btn.clicked.connect(self.calculate)

        self.table.hide()
        self.save_btn.hide()
        self.save_as_csv_btn.hide()
        self.overpayment.hide()
        self.mothly_payment.hide()
        self.save_btn.clicked.connect(self.save_to_db)
        self.save_as_csv_btn.clicked.connect(self.save_to_csv)

    def calculate(self):
        check_input = self.error_in_input()
        if not check_input:
            name = self.name.text()
            sum_ = float(self.sum_.text())
            percent = float(self.percent.value())
            term = int(self.term.value())
            self.loan = Loan(name, sum_, percent, term)
            self.loan.calculate()
            self.data = self.loan.get_data()
            self.table.setColumnCount(4)
            self.table.setRowCount(len(self.data))
            self.table.setHorizontalHeaderLabels(["Monthly payment", "Payment for percents",
                                                  "Payment on loan", "Sum of loan"])
            for i, month in enumerate(self.data):
                self.table.setItem(i, 0, QTableWidgetItem(str(round(month['monthly_payment'], 2))))
                self.table.setItem(i, 1, QTableWidgetItem(str(round(month['percent_payment'], 2))))
                self.table.setItem(i, 2, QTableWidgetItem(str(round(month['payment_without_percent'], 2))))
                self.table.setItem(i, 3, QTableWidgetItem(str(round(month['sum_'], 2))))
            self.table.show()
            self.overpayment.setText('Overpayment: ' + str(int(self.loan.overpayment)))
            self.mothly_payment.setText('Monthly payment: ' + str(int(self.loan.monthly_payment)))
            self.overpayment.show()
            self.mothly_payment.show()
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
                raise LoanException('Please set name!')

            if not self.sum_.text() or not is_number(str(self.sum_.text())):
                raise LoanException('Please set sum of loan!')

            if float(self.percent.value()) == 0:
                raise LoanException('Please set percent value!')

            if int(self.term.value()) == 0:
                raise LoanException('Please set term!')
            return False

        except LoanException as ex:
            return str(ex)

    def save_to_db(self):
        res = self.loan.save_to_db()
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
        if self.loan:
            self.loan.save_as_csv()
        saved_msg = QMessageBox()
        saved_msg.setWindowTitle('Saved')
        saved_msg.setText("Saved as .csv file")
        saved_msg.setIcon(QMessageBox.Icon.Information)
        saved_msg.exec()



