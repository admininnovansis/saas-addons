from odoo import models


class SAASOperator(models.Model):
    _name = 'saas.operator'

    def get_db_url(self, db):
        url = super(SAASOperator, self).get_db_url(db)
        return url.format(domain=db.domain_name_id.name)
