{
    'name': 'estate',
    # data files are always loaded when the module is installed or updated and are loaded in the order they are listed
    # in other words if data files have foreign key realationships, they should be in the order of dependencies
    'data': [
        'security/ir.model.access.csv',
    ],
}