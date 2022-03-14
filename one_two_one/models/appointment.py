from odoo import api, fields, models, _
import datetime


class ApointmentCustom(models.Model):
    _name = 'appointment.custom'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment Custom'
    _rec_name = 'inviter_id'
    _order = "id desc"

    reference = fields.Char(string="Order Reference", required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    inviter_id = fields.Many2one('res.partner', string="Inviter", required=True)
    customer_id = fields.Many2one('res.partner', string="Invitee", required=True)
    date = fields.Datetime(string="Appointment Schedule", default=fields.Datetime.now, tracking=True)
    active = fields.Boolean(string="Active", default=True)
    formality = fields.Selection(string='Formality', default='online',
                                 selection=[('online', 'Online'), ('offline', 'Offline')])
    location = fields.Selection(string="Location", default='on',
                                selection=[('on', 'In the office'), ('out', 'Outside the office')])
    note = fields.Char(string="Note")
    number_type = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], string="Referrals")

    appointment_count = fields.Integer(string="Count", related='inviter_id.appointment_count', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('appointment.custom') or _('New')
        return super(ApointmentCustom, self).create(vals)

    # Duplicate
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('inviter_id', 'customer_id'):
            default['inviter_id', 'customer_id'] = _("%s (Copy)", self.inviter_id)
        default['note'] = "Copied Record"
        return super(ApointmentCustom, self).copy(default)


