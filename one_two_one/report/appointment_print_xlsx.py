from odoo import api, fields, models, _


class AppointmentPrintXLSX(models.AbstractModel):
    _name = 'report.one_two_one.print_appointment_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        border = workbook.add_format({'border': True, 'align': 'center', 'num_format': 'dd-mm-yyyy', 'font_size': 12})
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format(
            {'bold': True, 'align': 'center', 'border': True, 'bg_color': '#33CCCC', 'font_size': 12})
        format_red = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'red'})
        format_green = workbook.add_format({'border': True, 'align': 'center', 'bg_color': '#00CC00'})
        format_yellow = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'yellow'})

        for obj in lines:
            sheet = workbook.add_worksheet(obj.reference)
            row = 0
            col = 0
            sheet_1 = obj.appointment_count
            sheet.set_column('A:B', 30)
            sheet.set_column('C:D', 30)

            sheet.write(row, col, 'Inviter', format_1)
            sheet.write(row + 1, col, obj.inviter_id.name, border)

            sheet.write(row, col + 1, 'Count', format_1)
            sheet.write(row + 1, col + 1, obj.appointment_count, border)

            if sheet_1 > 2:
                sheet.write(row + 1, col + 1, sheet_1, format_green)
            elif sheet_1 == 2:
                sheet.write(row + 1, col + 1, sheet_1, format_yellow)
            else:
                sheet.write(row + 1, col + 1, sheet_1, format_red)

            sheet.write(row, col + 2, 'Date', format_1)
            sheet.write(row + 1, col + 2, obj.date, border)
