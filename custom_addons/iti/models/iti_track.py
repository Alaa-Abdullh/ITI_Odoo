from odoo import models,fields

class  ITITrack(models.Model):
     _name="iti.track"

     name=fields.Char()
     is_append=fields.Boolean()
     capacity=fields.Integer()

     student_ids=fields.One2many("iti.student","track_id")