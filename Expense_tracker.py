import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout
import pymysql


class FinanceWithPython(QWidget):
    def __init__(self):
        super().__init__()  # it is used to inherit the __init__ from QWidget class.
        self.connection = pymysql.connect(
            host='financewithpython.csjz51eskfab.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='admincreate',
            db='FinanceWithPython',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        #intializing button on layout
        weekly_button = QPushButton('View weekly Transcation')
        monthly_button = QPushButton('View Monthly Transaction')
        yearly_button = QPushButton('View yearly Transaction')

        #adding buttons to layout
        layout.addWidget(weekly_button)
        layout.addWidget(monthly_button)
        layout.addWidget(yearly_button)

        #defin action of the buttons and attching them with methods
        weekly_button.clicked.connect(self.view_weekly)
        monthly_button.clicked.connect(self.view_monthly)
        yearly_button.clicked.connect(self.view_yearly)

        #intalizing form fields to the layout
        self.expense_form_layout = QFormLayout()
        self.amount_input = QLineEdit()
        self.description_input = QLineEdit()
        add_expense_button = QPushButton('Add Expenses')

        #adding rows to the forms
        self.expense_form_layout.addRow('Amount', self.amount_input)
        self.expense_form_layout.addRow('Description', self.description_input)
        self.expense_form_layout.addWidget(add_expense_button)

        add_expense_button.clicked.connect(self.add_expense)

        # adding form layout to the Box layout
        layout.addLayout(self.expense_form_layout)

        self.setLayout(layout)
        self.setWindowTitle('Finance Tracker')
        self.show()

    def view_weekly(self):
        query = "select * from transactions where week(date_column)=week(now())"
        result = self.execute_query(query)
        print("Weekly transaction:", result)

    def view_monthly(self):
        query = "select * from transactions where month(date_column)=month(now())"
        result = self.execute_query(query)
        print("monthly transcatiobs", result)

    def view_yearly(self):
        query = "select * from transactions where year(date_column)=year(now())"
        result = self.execute_query(query)
        print("yearly transcation", result)

    def add_expense(self):
        # get input from form amount_input
        amount = float(self.amount_input.text())
        description = self.description_input.text()
        date = datetime.now()

        # insert expenses into database
        query = "insert into transaction(amount,description,date_column) values(%s,%s,%s)"
        params = (amount, description, date)
        print("Expenses added successfully")

    def execute_query(self, query, params=None):
        "If adding expenses we will have params if not we will just query"
        "for adding expenes we need params"
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        self.connection.commit()
        return result

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = FinanceWithPython()
    sys.exit(app.exec_())