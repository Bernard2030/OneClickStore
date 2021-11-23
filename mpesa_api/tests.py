from django.test import TestCase


# from mpesa_api.models import MpesaPayments,MpesaCallbacks,BaseModel,MpesaCalls

# from mpesa_api.models import MpesaPayments,MpesaCallbacks,BaseModel,MpesaCalls

# Create your tests here.
"""
class MpesaPaymentsTest(TestCase):
    def setUp(self):
        self.mpesa_payments = MpesaPayments(
            transaction_type='CustomerPayBillOnline',
            transaction_id='LN0123456789',
            amount='100',
            phone_number='254712345678',
            first_name='John',
            middle_name='M',
            last_name='Doe',)

    def test_create_mpesa_payments(self):
        self.assertEqual(self.mpesa_payments.transaction_type, 'CustomerPayBillOnline')
        self.assertEqual(self.mpesa_payments.transaction_id, 'LN0123456789')
        self.assertEqual(self.mpesa_payments.amount, '100')
        self.assertEqual(self.mpesa_payments.phone_number, '254712345678')
        self.assertEqual(self.mpesa_payments.first_name, 'John')
        self.assertEqual(self.mpesa_payments.middle_name, 'M')
        self.assertEqual(self.mpesa_payments.last_name, 'Doe')

    def test_str(self):
        self.assertEqual(str(self.mpesa_payments), 'CustomerPayBillOnline')  


    def test_get_absolute_url(self):
        self.assertEqual(self.mpesa_payments.get_absolute_url(), '/mpesa_api/mpesa_payments/1') 

    def test_get_update_url(self):
        self.assertEqual(self.mpesa_payments.get_update_url(), '/mpesa_api/mpesa_payments/1/update')
        
class MpesaCallbacksTest(TestCase):
    def setUp(self):
        self.mpesa_callbacks = MpesaCallbacks(
            transaction_type='CustomerPayBillOnline',
            transaction_id='LN0123456789',
            amount='100',
            phone_number='254712345678',
            first_name='John',)

    def test_create_mpesa_callbacks(self):
        self.assertEqual(self.mpesa_callbacks.transaction_type, 'CustomerPayBillOnline')
        self.assertEqual(self.mpesa_callbacks.transaction_id, 'LN0123456789')
        self.assertEqual(self.mpesa_callbacks.amount, '100')
        self.assertEqual(self.mpesa_callbacks.phone_number, '254712345678')
        self.assertEqual(self.mpesa_callbacks.first_name, 'John')


    def test_str(self):
        self.assertEqual(str(self.mpesa_callbacks), 'CustomerPayBillOnline')

class BaseModelTest(TestCase):
    def setUp(self):
        self.base_model = BaseModel(
            transaction_type='CustomerPayBillOnline',
            transaction_id='LN0123456789',
            amount='100',
            phone_number='254712345678',
            first_name='John',)

    def test_create_base_model(self):
        self.assertEqual(self.base_model.transaction_type, 'CustomerPayBillOnline')
        self.assertEqual(self.base_model.transaction_id, 'LN0123456789')
        self.assertEqual(self.base_model.amount, '100')
        self.assertEqual(self.base_model.phone_number, '254712345678')
        self.assertEqual(self.base_model.first_name, 'John')


    def test_str(self):
        self.assertEqual(str(self.base_model), 'CustomerPayBillOnline')

class MpesaCallsTest(TestCase):
    def setUp(self):
        self.mpesa_calls = MpesaCalls(
            transaction_type='CustomerPayBillOnline',
            transaction_id='LN0123456789',
            amount='100',
            phone_number='254712345678',
            first_name='John',)

    def test_create_mpesa_calls(self):
        self.assertEqual(self.mpesa_calls.transaction_type, 'CustomerPayBillOnline')
        self.assertEqual(self.mpesa_calls.transaction_id, 'LN0123456789')
        self.assertEqual(self.mpesa_calls.amount, '100')
        self.assertEqual(self.mpesa_calls.phone_number, '254712345678')
        self.assertEqual(self.mpesa_calls.first_name, 'John')


    def test_str(self):
        self.assertEqual(str(self.mpesa_calls), 'CustomerPayBillOnline')                                                   
"""
