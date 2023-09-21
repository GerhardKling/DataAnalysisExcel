"""
Full financial model
"""

import xlsxwriter

class FinancialModel():
	def __init__(self, rev=5000):
		self.rev = rev

	def income_statement(self):
		#Creates Excel file
		model = xlsxwriter.Workbook('Model.xlsx')
		 
		#Add worksheet
		statement = model.add_worksheet()

		#Labels
		statement.write('A5', 'Revenue')
		statement.write('A6', 'COGS')

		#Values
		statement.write('B5', self.rev)
		statement.write_formula('B6', '=B5*0.85')

		#We need to close the file to commit changes
		model.close()






