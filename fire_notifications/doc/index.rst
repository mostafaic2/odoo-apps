PopUp Notifications
===================
* For each popup Odoo would generate a special instance of 'popup.notification'
* The field popup_handler_ids - is a many2many relation to res.users object
* Each popup notification handler has a status. Possible values: 'draft', 'shown'. By default: 'draft'
* As soon as you pressed 'View' or 'Close', the status is changed to 'shown'. The notification would not be shown again

Example of use:
=====================

.. code:: python

        values = {
            'title': 'Title of your message',
            'message': 'Your message',
            'model_name': self._name,  # the the model that will be shown by the popup view button
            'model_record': self.id,  # the specific row or record related to the model name
            'popup_handler_ids': [(0, 0, {'status': 'draft', 'user_id': 1})],  # the list of user_id or ids to notify
        }
        self.env['popup.notification'].create(values)