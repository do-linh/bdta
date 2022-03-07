from odoo import api, fields, models, _


class AppointmentReportwizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"

    inviter_id = fields.Many2one('appointment.custom', string="Inviter")
    # appointment_count = fields.Integer(string="Count", related='inviter_id.appointment_count', tracking=True)

    def action_print_report(self):
        domain = []
        inviter_id = self.inviter_id
        if inviter_id:
            domain += [('inviter_id', '=', self.inviter_id.id)]
        print("Domain", domain)

        appointments = self.env['appointment.custom'].search_read(domain)
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('one_two_one.report_appointment_xls').report_action(self, data=data)
