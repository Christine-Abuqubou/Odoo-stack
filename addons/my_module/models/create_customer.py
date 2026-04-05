import xmlrpc.client
from odoo import models, fields, api
from odoo.exceptions import UserError

class ExternalCustomerSync(models.Model):
    _name = 'external.sync'
    _description = 'Sync Customers via XML-RPC'

    # أضف هذا السطر لحل مشكلة الـ XML
    name = fields.Char(string="Operation Name", default="Sync Customers", readonly=True)

    def action_create_external_customer(self):
        url = 'https://odoo.com' 
        db = 'my_database'
        username = 'admin'
        password = 'admin'

        try:
            common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
            uid = common.authenticate(db, username, password, {})

            if uid:
                models_proxy = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
                new_partner = {
                    'name': 'first name',
                    'is_company': True,
                    'email': 'test@example.com',
                }

                partner_id = models_proxy.execute_kw(db, uid, password, 'res.partner', 'create', [new_partner])
                
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'message': f"🚀 تم إنشاء العميل بنجاح ID: {partner_id}",
                        'type': 'rainbow_man',
                    }
                }
            else:
                raise UserError("❌ فشل الاتصال.. تأكد من البيانات.")

        except Exception as e:
            raise UserError(f"حدث خطأ أثناء الاتصال: {str(e)}")
        
        
    def action_update_external_customer(self):
        url = 'https://odoo.com' 
        db = 'my_database'
        username = 'admin'
        password = 'admin'

        try:
            common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
            uid = common.authenticate(db, username, password, {})

            if uid:
                models_proxy = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
                partner_id = 1  # ID العميل الذي تريد تحديثه
                updated_data = {
                    'name': 'updated name',
                    'email': 'updated@example.com',
                }

                models_proxy.execute_kw(db, uid, password, 'res.partner', 'write', [partner_id, updated_data])

                return {
                    'effect': {
                        'fadeout': 'slow',
                        'message': f"🚀 تم تحديث العميل بنجاح ID: {partner_id}",
                        'type': 'rainbow_man',
                    }
                }
            else:
                raise UserError("❌ فشل الاتصال.. تأكد من البيانات.")

        except Exception as e:
            raise UserError(f"حدث خطأ أثناء الاتصال: {str(e)}")