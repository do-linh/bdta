from odoo import api, fields, models, _


class BaseReportXLSX(models.AbstractModel):
    _name = 'report.base.report_res_partner_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Appointment Count")
        border = workbook.add_format({'border': True, 'align': 'center', 'font_size': 12})
        format_1 = workbook.add_format(
            {'bold': True, 'align': 'center', 'border': True, 'bg_color': '#33CCCC', 'font_size': 14})
        format_red = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'red'})
        format_green = workbook.add_format({'border': True, 'align': 'center', 'bg_color': '#00CC00'})
        format_yellow = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'yellow'})

        row = 0
        col = 0

        sheet.write(row, col, "Inviter", format_1)
        sheet.write(row, col + 1, "Count", format_1)

        for appointment in data['appointment']:
            sheet.set_column('A:A', 20)
            sheet.set_column('B:B', 15)

            row += 1
            sheet.write(row, col, appointment['inviter_id'][1], border)
            sheet.write(row, col + 1, appointment['appointment_count'], border)
