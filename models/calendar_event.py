# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Meeting(models.Model):
    _inherit = 'calendar.event'

    is_employe_id = fields.Many2one('hr.employee', 'Employé', index=True)
    is_partner_id = fields.Many2one('res.partner', 'Client' , index=True)


    @api.model
    def _get_public_fields(self):
        return self._get_recurrent_fields() | self._get_time_fields() | {
            'id', 'active', 'allday',
            'duration', 'user_id', 'interval',
            'count', 'rrule', 'recurrence_id', 'show_as','is_employe_id','is_partner_id'}

