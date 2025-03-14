{
    'name': 'estate',
    # data files are always loaded when the module is installed or updated and are loaded in the order they are listed
    # in other words if data files have foreign key realationships, they should be in the order of dependencies
    # menus and views should be loaded in order too, menu, action, view
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
    ],
}