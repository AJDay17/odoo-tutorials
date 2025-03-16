from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default= fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'), 
            ('offer received', 'Offer Received'), 
            ('offer accepted', 'Offer Accepted'), 
            ('sold', 'Sold'), 
            ('canceled', 'Canceled')
            ], 
        default='new',
        copy=False,
        required=True
        )
    property_type_id = fields.Many2one('estate.property.type')
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    
    # is it convention to use _ids sufix for many2many fields
    tag_ids = fields.Many2many('estate.property.tag')

    offer_ids = fields.One2many('estate.property.offer', 'property_id')