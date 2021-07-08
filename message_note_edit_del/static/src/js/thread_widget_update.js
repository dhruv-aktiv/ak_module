odoo.define('message_note_edit.thread_widget_update', function(require) {
    "use strict";


    var session = require('web.session');
    var ThreadWidget = require('mail.widget.Thread');
    var core = require('web.core');
    var _t = core._t;
    var QWeb = core.qweb;
 
    ThreadWidget.include({
        events: _.extend({}, ThreadWidget.prototype.events, {
            'click .o_thread_edit': '_onClickEditMsg',
            'click .o_thread_del': '_onClickDelMsg',

        }),
        init: function() {
            this._super.apply(this, arguments);
            console.log("init called...")
        },
        render: function(thread, options) {
            this._super.apply(this, arguments);
            console.log("render called...");
            session.user_has_group('message_note_edit_del.group_message_note_edit').then(function(has_group) {
                if (!has_group) {
                    $('.o_thread_edit').hide();
                }
            });
            session.user_has_group('message_note_edit_del.group_message_note_del').then(function(has_group) {
                if (!has_group) {
                    $('.o_thread_del').hide();
                }
            });
            console.log("render called...")

        },
        _onClickEditMsg: function(ev) {
            var messageID = $(ev.currentTarget).data('message-id');

            var self = this;

            self._rpc({
                model: 'ir.model.data',
                method: 'get_object_reference',
                args: ['message_note_edit_del', 'message_note_edit_view_message_form'],
            }).then(function(data) {
                return self.do_action({
                    name: _t('Edit Message'),
                    type: 'ir.actions.act_window',
                    res_model: "mail.message",
                    res_id: messageID,
                    views: [
                        [data[1] || false, 'form']
                    ],
                    view_mode: 'form',
                    target: 'new',
                    context: {
                        'edit_message': true
                    }
                });

            });
        },

        _onClickDelMsg: function(ev) {
            var messageID = $(ev.currentTarget).data('message-id');
            var self = this;
            console.log(`Msg ID : ${messageID}`)
            if (confirm("Do you want to delete this message?") == true) {
                self._rpc({
                    model: 'mail.message',
                    method: 'delete_msg',
                    args: [messageID],
                }).then(function() {
                    // self.consumed_tours.push(tour_name);
                    window.location.reload()
                    console.log("message deleted successfully...")
                })
            }
        }

    });

});