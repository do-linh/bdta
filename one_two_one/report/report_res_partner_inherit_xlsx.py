from odoo import api, fields, models, _


class ResPartnerReportXLSX(models.AbstractModel):
    _name = 'report.base.report_res_partner_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        border = workbook.add_format({'border': True, 'align': 'center', 'num_format': 'dd-mm-yyyy', 'font_size': 12})
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'border': True, 'bg_color': '#33CCCC', 'font_size': 12})
        format_red = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'red'})
        format_green = workbook.add_format({'border': True, 'align': 'center', 'bg_color': '#00CC00'})
        format_yellow = workbook.add_format({'border': True, 'align': 'center', 'bg_color': 'yellow'})

        for obj in lines:
            sheet = workbook.add_worksheet(obj.name)
            row = 0
            col = 0
            sheet_1 = obj.appointment_count
            sheet.set_column('A:C', 30)

            sheet.write(row, col, 'Name', format_1)
            sheet.write(row + 1, col, obj.name, border)

            sheet.write(row, col + 1, 'Count', format_1)
            sheet.write(row + 1, col + 1, obj.appointment_count, border)

            if sheet_1 > 2:
                sheet.write(row + 1, col + 1, sheet_1, format_green)
            elif sheet_1 == 2:
                sheet.write(row + 1, col + 1, sheet_1, format_yellow)
            else:
                sheet.write(row + 1, col + 1, sheet_1, format_red)
