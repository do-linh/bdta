from odoo import api, fields, models, _


class ResPartnerReportwizard(models.TransientModel):
    _name = "base.report.wizard"
    _description = "Report Wizard"

    inviter_id = fields.Many2one('res.partner', string="Inviter")
    # appointment_count = fields.Integer(string="Count", related='inviter_id.appointment_count', tracking=True)

    def action_print_report(self):
        appointment = self.env['res.partner'].search_read([])
        data = {
            'appointment': appointment,
            'form_data': self.read()[0]
        }
        return self.env.ref('one_two_one.report_res_partner_xls').report_action(self, data=data)
