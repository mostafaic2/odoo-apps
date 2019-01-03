from odoo import http, _
from odoo.http import request


class PopupController(http.Controller):

    @http.route('/popup_notifications/notify', type='json', auth="none")
    def notify(self):
        user_id = request.session.get('uid')
        datas = []
        popup_handler_obj = request.env['popup.notification.handler'].sudo().search(
            [('user_id', '=', user_id), ('status', '!=', 'shown')])
        for obj in popup_handler_obj:
            datas.append(obj.popup_id.get_notifications())
        return datas

    @http.route('/popup_notifications/notify_ack', type='json', auth="none")
    def notify_ack(self, notif_id, type='json'):
        user_id = request.session.get('uid')
        notif_obj = request.env['popup.notification.handler'].sudo().search([('popup_id', '=', int(notif_id.strip())), ('user_id', '=', user_id)])
        if notif_obj:
            notif_obj.status = 'shown'
