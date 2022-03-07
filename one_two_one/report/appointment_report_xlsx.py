from odoo import models
from odoo import api, fields, models, _


class AppointmentReportXLSX(models.AbstractModel):
    _name = 'report.one_two_one.report_appointment_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, lines):
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 14})
        format_2 = workbook.add_format({'align': 'center', 'font_size': 11})
        sheet = workbook.add_worksheet('Report XLSX')
        sheet.set_column('A:B', 30)
        sheet.write(0, 0, 'Name', format_1)
        sheet.write(1, 0, lines.reference, format_2)
        sheet.write(0, 1, 'Parent', format_1)
        sheet.write(1, 1, lines.inviter_id.name, format_2)
        sheet.write(0, 2, 'count', format_1)
        sheet.write(1, 2, lines.appointment_count, format_2)
