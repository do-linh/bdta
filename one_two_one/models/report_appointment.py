from odoo import api, fields, models, _, tools


# class ReportAppointment(models.AbstractModel):
#     _name = 'report.appointment'
#     _description = 'Report Appointment'

#     partner_id = fields.Many2one('res.partner', string="Partner", required=True)
#     date = fields.Datetime(string="Date")
#     id = fields.Integer()

#     def init(self):
#         tools.drop_view_if_exists(self.env.cr, self._table)
#         self.env.cr.execute('''
#                 CREATE OR REPLACE VIEW %s AS (
#                 select id,date,inviter_id as partner_id from appointment_custom
#                 UNION
#                 select id,date,customer_id as partner_id from appointment_custom)''' % (self._table,))


class ReportAppointmentWeek(models.AbstractModel):
    _name = 'report.appointment.weeky'
    _description = 'Report Appointment'

    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    date_week = fields.Date(string="Date")
    id = fields.Integer()
    count = fields.Integer()

    # def init(self):
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     self.env.cr.execute('''
    #             CREATE OR REPLACE VIEW %s AS (
    #             SELECT row_number() OVER ()  AS id, count("report_appointment".id) AS "count" , "report_appointment"."partner_id" as "partner_id" ,date_trunc('week', timezone('Singapore', timezone('UTC',"report_appointment"."date"))::timestamp) as "date_week"
    #             FROM "report_appointment" LEFT JOIN "res_partner" AS "report_appointment__partner_id" ON ("report_appointment"."partner_id" = "report_appointment__partner_id"."id")
    #             GROUP BY "report_appointment"."partner_id",date_trunc('week', timezone('Singapore', timezone('UTC',"report_appointment"."date"))::timestamp)
    #             )
    #             ''' % (self._table,))
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
         CREATE OR REPLACE VIEW %s AS (
         with r_a as (
         select id,date,inviter_id as partner_id from appointment_custom
         UNION
         select id,date,customer_id as partner_id from appointment_custom)
         SELECT row_number() OVER ()  AS id, count("r_a".id) AS "count" , "r_a"."partner_id" as "partner_id" ,date_trunc('week', timezone('Singapore', timezone('UTC',"r_a"."date"))::timestamp) as "date_week"
         FROM "r_a" LEFT JOIN "res_partner" AS "r_a__partner_id" ON ("r_a"."partner_id" = "r_a__partner_id"."id")
         GROUP BY "r_a"."partner_id",date_trunc('week', timezone('Singapore', timezone('UTC',"r_a"."date"))::timestamp))''' % (
            self._table,))
