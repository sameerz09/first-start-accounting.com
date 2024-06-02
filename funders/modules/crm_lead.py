from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def update_crm_tags(self):
        return {
            'name': _('Update CRM Tag'),
            'res_model': 'update.crm.tag',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {
                'crm_lead_ids': self.ids,
            }
        }

    name = fields.Char(
        'Opportunity', index='trigram', required=False,
        compute='_compute_name', readonly=False, store=True)

    probability = fields.Float(
        'Number of years', group_operator="avg", copy=False,
        compute='_compute_probabilities', readonly=False, store=True)

    grantmaking = fields.Boolean(
        string='Grantmaking',
        copy=False,
        default=False,
        readonly=False,
        store=True)

    stage_selection = fields.Selection([
        ('stage1', 'Stage 1'),
        ('stage2', 'Stage 2'),
        ('stage3', 'Stage 3'),
        ('stage4', 'Stage 4'),
        ('stage5', 'Stage 5')
    ], string='Stage', default='stage1', copy=False)

    # @api.model
    # def action_generate_future_leads(self):
    #     # Your custom logic to handle the button action
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Future Leads',
    #         'view_mode': 'tree,form',
    #         'res_model': 'crm.lead',
    #         'domain': [('type', '=', 'future')],
    #         'context': {'default_type': 'future'},
    #     }

    # @api.model
    # def action_generate_future_leads(self):
    #     # Custom logic to handle the button action
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Future Leads',
    #         'view_mode': 'tree,form',
    #         'res_model': 'crm.lead',
    #         'domain': [('type', '=', 'future')],
    #         'context': {'default_type': 'future'},
    #     }

    def action_generate_future_leads(self):
        # Check user conditions or any other pre-conditions
        if not self.env.user.has_group('sales_team.group_sale_manager'):
            raise UserError("You do not have the necessary permissions to perform this action.")

        # Logic to create a new CRM lead
        new_lead_vals = {
            'name': 'New Future Lead',
            'user_id': self.env.user.id,  # Assign to the current user
            'team_id': self.env['crm.team']._get_default_team_id(user_id=self.env.uid),
            'priority': '1',  # Set default priority
            'type': 'lead',  # Can be 'lead' or 'opportunity'
        }
        new_lead = self.env['crm.lead'].create(new_lead_vals)

        # Optionally return an action to open the newly created lead in the form view
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Lead',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'res_id': new_lead.id,
            'target': 'current',
        }