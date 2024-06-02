from odoo import models, fields, api


class UpdateCrmTag(models.TransientModel):
    _name = "update.crm.tag"

    update_type = fields.Selection([("replace", "Replace"), ("keep", "Add New")], default="replace")
    tag_ids = fields.Many2many("crm.tag", string="Tags")
    crm_lead_ids = fields.Many2many("crm.lead", string="Leads")

    @api.model
    def default_get(self, fields):
        res = super(UpdateCrmTag, self).default_get(fields)
        if 'crm_lead_ids' in self._context:
            res['crm_lead_ids'] = [(6, 0, self._context['crm_lead_ids'])]
        return res

    def update_tags(self):
        if self.update_type == "replace":
            for lead_id in self.crm_lead_ids:
                lead_id.write({
                    'tag_ids': [(6, 0, self.tag_ids.ids)]
                })
        else:
            for lead_id in self.crm_lead_ids:
                for tag_id in self.tag_ids:
                    lead_id.write({
                        'tag_ids': [(4, tag_id.id)]
                    })
