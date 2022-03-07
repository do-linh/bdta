from odoo import api, fields, models, _
import base64
import io


class AppointmentReportXLSX(models.AbstractModel):
    _name = 'report.one_two_one.report_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Appointment Count")
        border = workbook.add_format({'border': True, 'font_size': 12})
        format_1 = workbook.add_format(
            {'bold': True, 'align': 'center', 'border': True, 'bg_color': '#33CCCC', 'font_size': 14})
        format_red = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'red'})
        format_green = workbook.add_format({'border': True, 'bg_color': '#00CC00'})
        format_yellow = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'yellow'})

        row = 0
        col = 0

        sheet.write(row, col, "Inviter", format_1)
        sheet.write(row, col + 1, "Count", format_1)

        for appointment in data['appointments']:
            sheet.set_column('A:A', 25)
            sheet.set_column('B:B', 15)
            # sheet_1 = appointment['appointment_count']
            # if sheet_1 >= 3:
            #     sheet.write(row + 1, col + 1, sheet_1, format_green)
            # elif sheet_1 == 2:
            #     sheet.write(row, col + 1, sheet_1, format_yellow)
            # else:
            #     sheet.write(row, col + 1, sheet_1, format_red)

            row += 1
            sheet.write(row, col, appointment['inviter_id'][1], border)
            # sheet.write(row, col + 1, appointment['appointment_count'], border)
