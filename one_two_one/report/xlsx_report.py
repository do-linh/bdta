from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.module_name.report_name1'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        # for obj in partners:
        # report_name = obj.name
        # One sheet by partner
        sheet = workbook.add_worksheet('test')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'test', bold)