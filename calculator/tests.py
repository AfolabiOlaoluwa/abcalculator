from django.test import TestCase
import unittest

class AbcalculatorTest(TestCase):
    test_against =((322,45,34,321,04.03),
    )

    def test_mainpage(self):
        outcome = self.client.get('/')
        self.assertTemplateUsed(outcome,'calclator/index.html')

    def test_pvalue(self):
        for vc,cc,vr,cv,result in test_aginst:
            final_result = p_value(vc,cc,vr,cv)
            self.assertEqual(result,final_result)

        #we should be using unit test for p_vlaue

    def test_calculate(self):
        result  = self.client.post('/'{
        vcontrol : '536',
        vvariant :'600',
        ccontrol : '145',
        cvariant: '180'
        })

        response = result.json()
        self.assertTrue(response['pvalue'])
        self.assertTrue(response['significance']<0.05)
