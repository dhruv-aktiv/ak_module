odoo.define('message_note_edit_del.message_update', function(require) {
    "use strict";
 
    const { Component, useState } = owl;
    const { useRef } = owl.hooks;
    const { Message } = require('mail.message');
    class MessageWidgetU extends Message {

        static template = xml`
        <t t-inherit="mail.Message" t-inherit-mode="extension">
        <xpath expr="//div[hasclass('o_Message_header')]" position="inside">
        <span class="o_thread_edit" t-att-data-message-local-id="message and message.localId" title="Edit Message" t-on-click="_onClickEditMsg"   t-if="message.message_type !== 'notification'  and !message.is_discussion ">
                    <i t-att-class="'fa fa-pencil-square-o'"/>
        </span>

        <span class="o_thread_del" t-att-data-message-local-id="message and message.localId" title="Delete Message"  t-if="message.message_type !== 'notification' and !message.is_discussion and message.author.im_status ">
                    <i t-att-class="'fa fa-trash-o'"/>
        </span>

        </xpath>
        </t>`
        
        /**
        * @override
        */
        constructor(...args) {
            super(...args);
            console.log("init method called custom");
        }
        /**
        * @private
        * @param {MouseEvent} ev
         */
        _onClickEditMsg() {
            console.log("edit btn called...");
        }
    }

    // Object.assign(MessageEditDel, {
    //     template: 'mail.Message',
    // });


    owl.utils.whenReady().then(() => {
        const app = new MessageWidgetU();
        app.mount(document.body);
    });
   
    // return MessageWidgetU;

})