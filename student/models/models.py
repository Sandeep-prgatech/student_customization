# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'student.students'
    _description = 'student.students'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    classes = fields.Char(string='Class')
