
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    due_date = fields.Date(string="Due Date",required=True)
    
    @api.constrains('due_date')
    def check_due_date(self):
        today = fields.Date.today()
        if self.due_date < today:
            raise ValidationError("The Due Date cannot be in the past. Please select a valid future date.")
            
                
    def send_email(self):
        today = fields.Date.today()
        purchase_orders  = self.env['purchase.order'].search([])
        
        for order in purchase_orders:
            if order.due_date:
                diff = (order.due_date - today).days
                if order.due_date and (diff == 0 or diff == 2):
                    email_template = self.env.ref('purchase_reminder_ucs.due_date_reminder_email_template')
                    followers = [follower.partner_id for follower in order.message_follower_ids]
                    for follower in followers:
                        email_template.with_context({'object': order,'today': fields.Datetime.now()}).send_mail(follower.id, force_send=True)
                            
    