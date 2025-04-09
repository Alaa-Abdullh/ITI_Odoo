

from odoo import models,fields,api

class  ITIStudent(models.Model):
     _name="iti.student"

     name = fields.Char()
     age = fields.Integer()
     info = fields.Text()
     is_accepted = fields.Boolean()
     birth_date = fields.Date()
     image =fields.Binary()
     gender =fields.Selection([('male','m'),('female','f')])
     salary = fields.Float()

     #ddata base
     track_id=fields.Many2one("iti.track")
     track_capacity=fields.Integer(related="track_id.capacity")


     level=fields.Selection([('level1','level1'),('level2','level2'),('level3','level3')])
     @api.onchange('field_name')
     def _onchange_field_name(self):
              self.is_accepted = True

     def approve_action(self):
        for rec in self:
            rec.level = 'level3'