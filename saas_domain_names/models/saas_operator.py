from odoo import models


class SAASOperator(models.Model):
    _inherit = 'saas.operator'

    def get_db_url(self, db):
        return self.db_url_template.format(domain=db.domain_name_id.name)
