
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class MessageNoteEdit(models.TransientModel):
    _name = 'message.note.edit'
    _description = 'Message/Note Edit Wizard'

    author_id = fields.Many2one('res.partner', 'Author')
    email_from = fields.Char('From')
    message_id = fields.Many2one('mail.message')
    date = fields.Datetime(default=fields.Datetime.now)
    related_document_model = fields.Char('Related Document')
    related_document_id = fields.Many2oneReference(
        'Related Document ID', index=True, model_field='related_document_model')
    body = fields.Html()
    subject = fields.Char('Subject')
    msg_parent_id =  fields.Many2one(
        'mail.message', 'Parent Message Id')
    msg_history_ids =   fields.One2many(
        'mail.message', 'msg_parent_id')


    @api.model
    def default_get(self, fields):
        result = super(MessageNoteEdit, self).default_get(fields)
        message_id = self._context.get('mail_message_id')
        if message_id:
            mail_message_id = self.env['mail.message'].browse(message_id)
            author_id = mail_message_id.author_id.id
            email_from = mail_message_id.email_from
            date = mail_message_id.date
            related_document_model =  mail_message_id.model
            related_document_id = mail_message_id.res_id
            body = mail_message_id.body
            subject = mail_message_id.subject
            result.update({
                    'author_id' : author_id,
                    'email_from' : email_from,
                    'message_id' : mail_message_id.id,
                    'date' : date,
                    'related_document_id' : related_document_id,
                    'related_document_model' : related_document_model,
                    'body' : body,
                    'subject' : subject,
                })
            return result

    
    def confirm_msg(self):
        
        print("\n\n\n confirm message called. \n\n\n")
      




