from django.test import TestCase
import unittest

class AbcalculatorTest(TestCase):
    def testpalue(self):
        """
            case1:
                -visit control version = 43. Conveertion control =21
                - visit variant version = 32. Conversions variant = 14

                Expected result:0.331


            """

        pvalue_case1 =pvalue(visitors_control=43, conv_control=21,
                                                        visit_var=32, conv_var=14)


        self.assertTrue(pvalue_case1 == 0.001)
    def test_mainpage(self):
        outcome = self.client.get('/')
        self.assertTemplateUsed(outcome,'calclator/index.html')

    def test_pvalue(self):
        for vc,cc,vr,cv,result in test_aginst:
            final_result = p_value(vc,cc,vr,cv)
            self.assertEqual(result,final_result)

        #we should be using unit test for p_vlaue

    def test_calculate(self):
        """
        Expected result:{pvalue:0.136,significance:"No"}

        """
        result  = self.client.post('/'{
        vcontrol : '536',
        vvariant :'600',
        ccontrol : '145',
        cvariant: '180'
        })

        response = result.json()
        self.assertTrue(response['pvalue'])
        self.assertTrue(response['significance']<0.05)
