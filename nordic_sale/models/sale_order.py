# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('pending', 'To Approve'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    @api.model
    def _default_note(self):
        return self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_terms') and self.env.company.invoice_terms or ''

    quotation_ref = fields.Char(string='Quotation Reference', copy=False)
    note = fields.Html('Terms and conditions', default=_default_note)
    approver_ids = fields.One2many('sale.order.approver', 'order_id', string="Approvers", check_company=True)
    user_status = fields.Selection([
        ('draft', 'New'),
        ('pending', 'To Approve'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancel', 'Cancel')], string="Status",compute="_compute_user_status")

    @api.depends('approver_ids.status')
    def _compute_user_status(self):
        user = self.env.user
        for order in self:
            order.user_status = order.approver_ids.filtered(lambda r: r.user_id == user).status


    def action_submit(self):
        if len(self.approver_ids) < 1:
            raise UserError(_("You have to add at least one approver to confirm your request.") % self.approval_minimum)

        approvers = self.mapped('approver_ids').filtered(lambda approver: approver.status == 'draft')
        approvers._create_activity()
        approvers.write({'status': 'pending'})
        self.write({'state': 'pending'})



    def _get_user_approval_activities(self, user):
        domain = [
            ('res_model', '=', 'sale.order'),
            ('res_id', 'in', self.ids),
            ('activity_type_id', '=', self.env.ref('nordic_sale.mail_activity_data_approval').id),
            ('user_id', '=', user.id)
        ]
        activities = self.env['mail.activity'].search(domain)
        return activities


    def action_approve(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'approved'})
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()

        status_lst = self.mapped('approver_ids.status')
        approvers = len(status_lst)
        result = {}
        if status_lst.count('approved') == approvers:
            result = super(SaleOrder, self).action_confirm()
        return result


    def action_refuse(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'refused'})
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()


class SaleOrderApprovalApprover(models.Model):
    _name = 'sale.order.approver'
    _description = 'Approver'

    user_id = fields.Many2one('res.users', string="User", required=True, )
    name = fields.Char(related='user_id.name')

    status = fields.Selection([
        ('draft', 'New'),
        ('pending', 'To Approve'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancel', 'Cancel')], string="Status", default="draft", readonly=True)
    order_id = fields.Many2one('sale.order', string="Sale Order",
        ondelete='cascade', check_company=True)
    company_id = fields.Many2one(
        string='Company', related='order_id.company_id',
        store=True, readonly=True, index=True)

    def action_approve(self):
        self.order_id.action_approve(self)

    def action_refuse(self):
        self.order_id.action_refuse(self)

    def _create_activity(self):
        for approver in self:
            approver.order_id.activity_schedule(
                'nordic_sale.mail_activity_data_approval',
                user_id=approver.user_id.id)



class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    note = fields.Html('Terms and conditions', translate=True)


