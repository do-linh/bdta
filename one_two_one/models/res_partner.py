from odoo import api, fields, models, _


class ApointmentCustom(models.Model):
    _inherit = 'res.partner'

    date = fields.Datetime(string="Appointment Schedule", tracking=True)
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count", tracking=True)

    def _compute_appointment_count(self):
        for rec in self:
            count = self.env['appointment.custom'].search_count([('inviter_id', '=', rec.id)])
            rec.appointment_count = count

    def action_open_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'appointment.custom',
            'view_mode': 'tree,form',
            'domain': [('inviter_id', '=', self.id)],
            'context': {'default_patient_id': self.id},
            'target': 'current'
        }
