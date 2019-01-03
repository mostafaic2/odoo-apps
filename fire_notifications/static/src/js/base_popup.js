odoo.define('popup_notifications.BasePopup', function (require) {
"use strict";
var bus = require('bus.bus').bus;
var core = require('web.core');
var session = require('web.session');
var WebClient = require('web.WebClient');
var web_client = require('web.web_client');
var utils = require('mail.utils');
var View = require('web.View');
var ViewManager = require('web.ViewManager');
var Widget = require('web.Widget');
var QWeb = core.qweb;
var _t = core._t;
var _lt = core._lt;

// Upgraded and modified to odoo 10 by umar aziz

WebClient.include({
    check_popup_notifications: function () {
        var self = this;

        this.rpc('/popup_notifications/notify')
        .done(
            function (notifications) {
                _.each(notifications,  function(notify) {
                    var a = {'message':'','title':''}
                    for (var i = 0; i < notify.length; i++) {
                        var found = false;
                        _.each($('.o_notification_title'),  function(element) {
                            var id = $(element).find('p#p_id').html().trim();
                            if(id == notify[i].id){
                                found = true;
                            }
                        });
                        if(found){
                            break;
                        }
                        a.title = QWeb.render('popup_title', {'title': notify[i].title,'id': notify[i].id,'model_record': notify[i].model_record,'model_name': notify[i].model_name});
                        a.message = QWeb.render('popup_footer', {'message': notify[i].message});
//                        utils.send_notification(notify.title, notify.message);
                        self.do_notify(a.title, a.message, true);
                        self.reload_notify();

                    } // #TODO check original module
                });
            }
        )
        .fail(function (err, ev) {
            if (err.code === -32098) {
                // Prevent the CrashManager to display an error
                // in case of an xhr error not due to a server error
                ev.preventDefault();
            }
        });
    },

    reload_notify: function(){
        var self = this;
        // prevent notification from showing again for the same user
        $(".link2showed").click(function() {
            $(this).parent().parent('.o_notification').find('.o_close').trigger("click");
            var id = $(this).parent().parent('.o_notification').find('p#p_id').html()
            self.rpc("/popup_notifications/notify_ack", {'notif_id': id});
        });
        $(".link2view").click(function() {
            $(this).parent().parent('.o_notification').find('.o_close').trigger("click");
            var id = $(this).parent().parent('.o_notification').find('p#p_id').html()
            var model_record = $(this).parent().parent('.o_notification').find('p#model_record').html()
            var model_name = $(this).parent().parent('.o_notification').find('p#model_name').html()
            self.rpc("/popup_notifications/notify_ack", {'notif_id': id});
            self.do_action({
                type: 'ir.actions.act_window',
                res_model: model_name,
                res_id: parseInt(model_record),
                views: [[false, 'form']],
                target: 'main',
            });
        });
    }
    ,

    start: function (parent) {
        var self = this;
        self._super(parent);
        $(document).ready(function () {
            setTimeout(function() {
                self.check_popup_notifications();
            },1500);
            setInterval( function() {
                self.check_popup_notifications();
            }, 1000*30*10); // Every 5 Minutes do check
        });

    },

})

});
