odoo.define('message_note_edit_del.MessageEditDel', function(require) {
    "use strict";
    // const {
    //     _lt
    // } = require('web.core');
    // const {
    //     session
    // } = require('web.session');
    // var {
    //     _t
    // } = _lt._t;
    // var {
    //     QWeb
    // // } = _lt.qweb;
    const { Component, useState } = owl;
    const { useRef } = owl.hooks;
    const { Message } = require('mail.message');
    class MessageEditDel extends Message {
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

    Object.assign(MessageEditDel, {
        template: 'message_note_edit_del.MessageEditDel',
    });

    return MessageEditDel;


   

})