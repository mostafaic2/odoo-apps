# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class popup_notification(models.Model):
    _name = "popup.notification"

    title = fields.Char()
    message = fields.Text()
    popup_handler_ids = fields.One2many(comodel_name='popup.notification.handler', inverse_name='popup_id', string="Users" )
    model_record = fields.Integer(string="Product", required=False, )
    model_name = fields.Char(string="Model", required=False, )

    @api.multi
    def get_notifications(self):
        result = []
        for obj in self:
            result.append({
                'title': obj.title,
                'message': obj.message,
                'id': obj.id,
                'model_record': obj.model_record,
                'model_name': obj.model_name,
            })
        return result


class popup_notification_handler(models.Model):
    _name = "popup.notification.handler"

    status = fields.Selection([('shown', 'shown'), ('draft', 'draft')], defaul='draft')
    user_id = fields.Many2one(comodel_name="res.users", string="User")
    popup_id = fields.Many2one(comodel_name="popup.notification", string="Popup", required=False)
