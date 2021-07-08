# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

from odoo import _, api, fields, models, modules, tools
from odoo.exceptions import UserError, AccessError


class MailMessageUpdate(models.Model):
    _inherit = "mail.message"

    msg_parent_id =  fields.Many2one(
        'mail.message', 'Parent Message Id')
    msg_history_ids =   fields.One2many(
        'mail.message', 'msg_parent_id')

    def write(self, vals):
        if self._context.get("edit_message"):
            for rec in self:
                mail_message_vals = {
                    'msg_parent_id': rec.id,
                    'res_id': False,
                    'author_id': rec.author_id.id,
                    'parent_id': rec.id,
                    'subtype_id': rec.subtype_id.id,
                    'body': rec.body,
                }
                mail_message_new = self.create(mail_message_vals)
        return super(MailMessageUpdate,self).write(vals)

       

    def confirm_msg(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


    @api.model
    def delete_msg(self,messageId):
        message = self.browse([messageId])
        child_messages = self.search([('msg_parent_id','=',messageId)])
        message.unlink()
        child_messages.sudo().unlink()





