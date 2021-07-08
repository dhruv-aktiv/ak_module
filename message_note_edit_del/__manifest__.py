# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software PVT. LTD.
# mail: odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
# Aktiv Software:
# - Burhan Vakharia
# - Dhruv Suthar
# - Saurabh Yadav

{
    'name': "Editable messeges in Chatter/Discuss",
    'category': 'Discuss',
    'summary': """This module is allow user to edit/delete messages/notes in Chatter/Discuss.
    """,

    'description': """
    Title: Signup With Mobile Number \n
    Author: Aktiv Software PVT. LTD. \n
    mail: odoo@aktivsoftware.com \n
    Copyright (C) 2015-Present Aktiv Software PVt. LTD. \n
    Contributions: Aktiv Software \n
                     - Burhan Vakharia
                     - Dhruv Suthar
                     - Saurabh Yadav
    This module is allow user to edit/delete messages/notes in Chatter/Discuss.


    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'version': '14.0.1.0.0',
    'depends': ['base', 'mail'],
    'license': 'AGPL-3',
    'data': [
        'security/message_security.xml',
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/mail_message_edit_view.xml',
    ],
    "application": False,
    "installable": True,
    'qweb': [
        # 'static/src/components/messege/MessageEditDel.xml',
        # 'static/src/xml/thread_update.xml',
        # 'static/src/components/messege/Message.xml',
    ],
    'images': ['static/description/banner.jpg'],
}
