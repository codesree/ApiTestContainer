import unittest
import pprint
from .test_gate import test_rating_db, Asset_stack, gateway_process
import logging
import uuid
from pymongo import MongoClient
import time, datetime
import os, json
from .test_gate import All_safe, log_builder, report_builder
from .asset_manager import Asset_endtoend


class asset_homecontent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_homecontent"
        testdb = test_rating_db("rate_home_contents")

        # Intializing the report builder

        rlog = report_builder('asset_homecontent')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('Assetapi_homecontent')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    # @unittest.skip('done')
    # def test_content_asset_with_ControlledAccess(self):
    #     caseval = "ControlledAccess"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - ControlledAccess'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)

    def test_content_asset_with_Alarm(self):
        caseval = "Alarm"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - Alarm'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("/* Test cases for Asset api - rating factors Home Contents */")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    # def test_content_asset_with_HighWallCode(self):
    #     caseval = "HighWallCode"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - HighWallCode'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_ApplianceBreakdown(self):
    #     caseval = "ApplianceBreakdown"
    #     tinfo = "rate_keys"
    #
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - ApplianceBreakdown'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_BurglarBarType(self):
    #     caseval = "BurglarBarType"
    #     tinfo = "rate_keys"
    #
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - BurglarBarType'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_NCB(self):
    #     caseval = "NCB"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - NCB'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_RoofType(self):
    #     caseval = "RoofType"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - RoofType'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_WallType(self):
    #     caseval = "WallType"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - WallType'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_HomeArea(self):
    #     caseval = "HomeArea"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - HomeArea'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_HomeType(self):
    #     caseval = "HomeType"
    #     tinfo = "rate_keys"
    #
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - HomeType'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_policyFrequency(self):
    #     caseval = "policyFrequency"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - policyFrequency'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_itemStatus(self):
    #     caseval = "itemStatus"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - itemStatus'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_BuildingUsage(self):
    #     caseval = "BuildingUsage"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - BuildingUsage'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_IsCommune(self):
    #     caseval = "IsCommune"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - IsCommune'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_RentedBuilding(self):
    #     caseval = "RentedBuilding"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - RentedBuilding'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_HasElectricGates(self):
    #     caseval = "HasElectricGates"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - HasElectricGates'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_HasAccessControl(self):
    #     caseval = "HasAccessControl"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - HasAccessControl'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_Legal(self):
    #     caseval = "Legal"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - Legal'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_Dwell100Water(self):
    #     caseval = "Dwell100Water"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - Dwell100Water'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_content_asset_with_ContentsFullyFurnished(self):
    #     caseval = "ContentsFullyFurnished"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_HomeContents_rating_factor - ContentsFullyFurnished'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Home Contents")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        print(logdat)

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class asset_building(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_building"
        testdb = test_rating_db("rate_buildings")

        # Intializing the report builder

        rlog = report_builder('asset_building')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_building')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    @unittest.skip('done')
    def test_building_asset_with_electricalMotor(self):
        caseval = "electricalMotor"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-electricalMotor'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_RoofType(self):
        caseval = "roofConstrCode"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-roofConstrCode'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_ppolFrequency(self):
        caseval = "policyFrequency"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-policyFrequency'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_wallConstrCode(self):
        caseval = "wallConstrCode"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-wallConstrCode'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_typeOfDwellingCode(self):
        caseval = "typeOfDwellingCode"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-typeOfDwellingCode'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        logger.info("-----------}")

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_unoccupiedDays(self):
        caseval = "unoccupiedDays"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-unoccupiedDays'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_landSlip(self):
        caseval = "landSlip"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-landSlip'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_wallConstrCode(self):
        caseval = "wallConstrCode"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-wallConstrCode'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_itemStatus(self):
        caseval = "itemStatus"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-itemStatus'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_building_asset_with_useOfResidence(self):
        caseval = "useOfResidence"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_building_rating_factor-useOfResidence'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api- rating_factors_Building")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        print(logdat)

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class asset_vehicle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_vehicle"
        testdb = test_rating_db("rate_vehicles")

        # Intializing the report builder

        rlog = report_builder('asset_vehicle')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_vehicle')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    def test_vehicle_asset_with_CARS(self):
        caseval = "CARS_MMcode"
        tinfo = "CARS_MMcode"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - CARS'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)


    # def test_vehicle_asset_with_Usage(self):
    #     caseval = "Usage"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - Usage'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_ExcessWaiver(self):
    #     caseval = "ExcessWaiver"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - ExcessWaiver'}
    #
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_Cover(self):
    #     caseval = "Cover"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - Cover'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_policyFrequency(self):
    #     caseval = "policyFrequency"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - policyFrequency'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_CommodityCarrying(self):
    #     caseval = "CommodityCarrying"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - CommodityCarrying'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_CrossBorder(self):
    #     caseval = "CrossBorder"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - CrossBorder'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_BusinessNature(self):
    #     caseval = "BusinessNature"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - BusinessNature'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_VehicleRebuilt(self):
    #     caseval = "VehicleRebuilt"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - VehicleRebuilt'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_hasImmobiliser(self):
    #     caseval = "hasImmobiliser"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - hasImmobiliser'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_AlarmType(self):
    #     caseval = "AlarmType"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - AlarmType'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_Financed(self):
    #     caseval = "Financed"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - Financed'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_CarHireOption(self):
    #     caseval = "CarHireOption"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - CarHireOption'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_NewVehicle(self):
    #     caseval = "NewVehicle"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - NewVehicle'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)
    #
    # def test_vehicle_asset_with_ParkedOvernight(self):
    #     caseval = "ParkedOvernight"
    #     tinfo = "rate_keys"
    #     tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - ParkedOvernight'}
    #     logger = tlog.set_log('INFO', 'noformat')
    #     logger.info("Test cases for Asset api - rating factors Motor vehicle")
    #
    #     logger.info(tclist['testcase'])
    #
    #     logger.info("{----------")
    #     testdb.get_rating_factors(caseval, test_case, tinfo)
    #
    #     goky = All_safe()
    #
    #     getresp = Asset_stack()
    #     asset_resp = getresp.asset_resp_handover()
    #
    #     logger.info("-----------}")
    #
    #     itemc = goky.checkoutput(asset_resp)
    #
    #     tclist['status'] = itemc
    #
    #     logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class asset_allrisks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_allrisks"
        testdb = test_rating_db("rate_allrisks")

        # Intializing the report builder

        rlog = report_builder('asset_allrisks')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_allrisks')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    @unittest.skip('bypass test method')
    def test_allrisks_asset_with_subsection(self):
        caseval = "subsection"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - subsection'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_allrisks_asset_with_policyFrequency(self):
        caseval = "policyFrequency"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - policyFrequency'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_allrisks_asset_with_discountType(self):
        caseval = "discountType"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - discountType'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_allrisks_asset_with_discountLoading(self):
        caseval = "discountLoading"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - discountLoading'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_allrisks_asset_with_itemStatus(self):
        caseval = "itemStatus"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - itemStatus'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @unittest.skip('bypass test method')
    def test_allrisks_asset_with_storageLocation(self):
        caseval = "storageLocation"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - storageLocation'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class asset_personal_liability(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_allrisks"
        testdb = test_rating_db("rate_allrisks")

        # Intializing the report builder

        rlog = report_builder('asset_allrisks')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_allrisks')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    # @unittest.skip('bypass test method')
    def test_personal_liability_asset_with_ppolFrequency(self):
        caseval = "ppolFrequency"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - ppolFrequency'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    # @unittest.skip('bypass test method')
    def test_personal_liability_asset_with_discountType(self):
        caseval = "discountType"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - discountType'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_personal_liability_asset_with_itemStatus(self):
        caseval = "itemStatus"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - itemStatus'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class ratingEngineBuild(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog
        test_case = "asset_allrisks"
        testdb = test_rating_db("rate_allrisks")

        # Intializing the report builder

        rlog = report_builder('asset_allrisks')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('asset_allrisks')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    @unittest.skip('bypass test method')
    def testRatingEngineGenderfactor(self):
        caseval = "subsection"
        tinfo = "rate_keys"
        tclist = {'testcase': 'test_assetapi_with_Vehicle_rating_factor - subsection'}
        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test cases for Asset api - rating factors Motor vehicle")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        testdb.get_rating_factors(caseval, test_case, tinfo)

        goky = All_safe()

        getresp = Asset_stack()
        asset_resp = getresp.asset_resp_handover()

        logger.info("-----------}")

        itemc = goky.checkoutput(asset_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)



    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')

class asset_api_process(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global testdb, test_case, rlog, logdat, stsec, start_time, dof, tlog, quote_n
        test_case = "ASSET API PROCESS LIFECYCLE - INSURANCE QUOTING AND POLICY"

        # Intializing the report builder

        rlog = report_builder('quote_to_policy')
        logdat = {
            'testc': [],
            'time_taken': '',
            'start_time': '',
            'end_time': ''
        }
        stsec = time.time()
        start_time = time.asctime(time.localtime(time.time()))

        logdat['start_time'] = start_time

        # Intializing the log builder

        tlog = log_builder('quote_to_policy')

        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """

    # @unittest.skip('bypass test method')
    def test_a_create_quote(self):
        global quote_n

        tclist = {'testcase': 'Create quote from asset api for liberty sti'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test case:--")

        logger.info(tclist['testcase'])

        logger.info("{----------")
        qop = Asset_endtoend()
        asset_req = qop.create_quote()
        logger.info("API request.......")
        logger.info(asset_req)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(asset_req)

        logger.info("API response......")
        # check
        logger.info(asset_resp[0])

        logger.info("-----------}")

        # validate response
        itemc = qop.create_quote_check(asset_resp)

        tclist['status'] = itemc

        asset_resp_dat = asset_resp[0]
        quote_n = asset_resp_dat['quoteNumber']
        print('quote number from test create quote is', quote_n)

        # golog = All_safe()
        # golog.test_all_safe("quote_no",quote_n)

        logdat['testc'].append(tclist)

    def test_b_view_quote(self):
        global amend_quote

        golog = All_safe()
        quote_n = golog.test_all_safe("get_quote_n", '')
        print("quote number..test view quote..", quote_n)

        tclist = {'testcase': 'View quote from Asset api'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        qop = Asset_endtoend()
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(quote_n)

        tgate = gateway_process("amend_quote")

        asset_resp = tgate.view_quote(quote_n)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        # check
        logger.info(asset_resp[0])

        logger.info("-----------}")

        # validate response
        itemc = qop.view_quote_check(asset_resp)

        tclist['status'] = itemc

        amend_quote = asset_resp[0]

        print("amend quote...", amend_quote)

        golog = All_safe()
        golog.test_all_safe("amend_quote", amend_quote)

        logdat['testc'].append(tclist)

    def test_c_amend_quote(self):
        golog = All_safe()
        amend_quote = golog.test_all_safe("get_amend_quote", '')

        tclist = {'testcase': 'Amend quote from Asset api'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        qop = Asset_endtoend()
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(amend_quote)

        tgate = gateway_process("asset_api")

        asset_resp = tgate.api_exec(amend_quote)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        # check
        logger.info(asset_resp[0])

        logger.info("-----------}")

        # validate response
        itemc = qop.create_quote_check(asset_resp)

        tclist['status'] = itemc

        asset_resp_dat = asset_resp[0]
        quote_n = asset_resp_dat['quoteNumber']

        logdat['testc'].append(tclist)

    # @unittest.skip('bypass test method')
    def test_d_accept_quote(self):
        tclist = {'testcase': 'Accept and Calulate prorata from Asset api for the create quote'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test case:--")

        logger.info(tclist['testcase'])

        logger.info("{----------")

        # golog = All_safe()
        # quote_n = golog.test_all_safe("get_quote_n",'')

        qop = Asset_endtoend()
        acc_req = qop.calculate_prorata(quote_n)
        logger.info("API request........")
        logger.info(acc_req)

        tgate = gateway_process("calculate_prorata")

        acc_resp = tgate.api_exec(acc_req)

        logger.info("API response........")
        logger.info(acc_resp)

        logger.info("-----------}")

        # validate response
        itemc = qop.create_quote_check(acc_req)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_e_convert_quote_to_policy(self):
        tclist = {'testcase': 'Convert quote to Policy from Asset API'}

        logger = tlog.set_log('INFO', 'noformat')
        logger.info("Test case:--")

        logger.info(tclist['testcase'])

        logger.info("{----------")

        # golog = All_safe()
        # quote_n = golog.test_all_safe("get_quote_n", '')

        qop = Asset_endtoend()
        logger.info("API request.........")
        logger.info(quote_n)

        tgate = gateway_process("convert_to_policy")

        conv_resp = tgate.convtop_exec(quote_n)

        logger.info("API response........")
        logger.info(conv_resp)

        logger.info("-----------}")

        # validate response
        itemc = qop.create_quote_check(conv_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    def test_f_view_policy(self):
        global policy_n,policy_detail

        golog = All_safe()
        quote_n = golog.test_all_safe("get_quote_n", '')

        policy_n = quote_n

        tclist = {'testcase': 'View policy from Asset api test'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        pop = Asset_endtoend()
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(policy_n)

        tgate = gateway_process("view_policy")

        viewp_resp = tgate.view_policy(policy_n)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(viewp_resp)

        logger.info("-----------}")

        # validate response
        itemc = pop.view_policy_check(viewp_resp)

        policy_detail = viewp_resp[0]

        golog = All_safe()
        golog.test_all_safe("policy_detail",policy_detail)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)
    #
    def test_g_amend_policy(self):

        tclist = {'testcase': 'Amend Policy from Asset API '}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")

        golog = All_safe()
        policy_detail = golog.test_all_safe("get_policy_detail", '')

        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(policy_detail)

        tgate = gateway_process("process_policy")

        policy_resp = tgate.api_exec(policy_detail)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(policy_resp)

        logger.info("-----------}")

        pop = Asset_endtoend()

        itemc = pop.amendpolicy_check(policy_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)
    #
    def test_g_accept_policy_amendment(self):

        golog = All_safe()
        quote_n = golog.test_all_safe("get_quote_n", '')
        print(quote_n)

        policy_n = quote_n

        tclist = {'testcase': 'Accept / Decline policy amendment for Endorsement'}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")

        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info("Decison: True")

        tgate = gateway_process("accept_policy")

        acdpol_resp = tgate.accept_policyendorse(policy_n,"True")

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(acdpol_resp)

        logger.info("-----------}")

        # validate response

        pop = Asset_endtoend()

        itemc = pop.acdpol_check(acdpol_resp)

        tclist['status'] = itemc

        logdat['testc'].append(tclist)
    #
    def test_h_view_policy_after_endorsement(self):

        golog = All_safe()
        quote_n = golog.test_all_safe("get_quote_n", '')

        policy_n = quote_n

        tclist = {'testcase': 'View policy from Asset API  after endorsement '}

        logger = tlog.set_log('INFO', 'format')
        logger.info("Test case:--")
        logger = tlog.set_log('INFO', 'noformat')

        logger.info(tclist['testcase'])

        logger.info("{----------")
        pop = Asset_endtoend()
        logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
        logger.info(policy_n)

        tgate = gateway_process("view_policy")

        viewp_resp = tgate.view_policy(policy_n)

        logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
        logger.info(viewp_resp)

        logger.info("-----------}")

        # validate response
        itemc = pop.view_policy_check(viewp_resp)

        policy_detail = viewp_resp[0]

        tclist['status'] = itemc

        logdat['testc'].append(tclist)

    @classmethod
    def tearDownClass(cls):
        etsec = time.time()
        end_time = time.asctime(time.localtime(time.time()))

        print('start time:', start_time)
        print('end time:  ', end_time)
        print("--- %s seconds ---" % (etsec - stsec))

        logdat['end_time'] = end_time
        logdat['time_taken'] = (etsec - stsec)

        rlog.log_repdata(logdat, 'testsuite')

        rlog.report_handover('handover')
        tlog.file_handover('handover')





# class asset_api_process(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         global testdb,test_case,rlog,logdat,stsec,start_time,dof,tlog
#         test_case = "PROCESS QUOTE - ASSET API"
#
#         #Intializing the report builder
#
#         rlog = report_builder('quote_to_policy')
#         logdat = {
#                     'testc':[],
#                     'time_taken':'',
#                     'start_time':'',
#                     'end_time':''
#                  }
#         stsec = time.time()
#         start_time = time.asctime(time.localtime(time.time()))
#
#         logdat['start_time'] = start_time
#
#         #Intializing the log builder
#
#         tlog = log_builder('quote_to_policy')
#
#         """
#         logger.debug('debug message')
#         logger.info('info message')
#         logger.warning('warn message')
#         logger.error('error message')
#         logger.critical('critical message')
#         """
#
#     #@unittest.skip('bypass test method')
#     def test_quote_to_policy(self):
#         global quote_n
#
#         tclist = {'testcase': 'Create quote from asset api for liberty sti'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#         qop = Asset_endtoend()
#         asset_req = qop.create_quote()
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(asset_req)
#
#         tgate = gateway_process("asset_api")
#
#         asset_resp = tgate.api_exec(asset_req)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         #check
#         logger.info(asset_resp[0])
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = qop.create_quote_check(asset_resp)
#
#         tclist['status'] = itemc
#
#         asset_resp_dat = asset_resp[0]
#
#         quote_n = asset_resp_dat['quoteNumber']
#         print('quote number from test create quote is..',quote_n)
#
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'View quote from Asset api'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#         qop = Asset_endtoend()
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(quote_n)
#
#         tgate = gateway_process("amend_quote")
#
#         asset_resp = tgate.view_quote(quote_n)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         #check
#         logger.info(asset_resp[0])
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = qop.view_quote_check(asset_resp)
#
#         tclist['status'] = itemc
#
#         amend_quote = asset_resp[0]
#
#         print("amend quote...",amend_quote)
#
#
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'Amend quote from Asset api'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#         qop = Asset_endtoend()
#
#         tgate = gateway_process("asset_api")
#
#         amend_quote = json.dumps(amend_quote,indent=5)
#
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(amend_quote)
#
#         asset_resp = tgate.api_exec(amend_quote)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         #check
#         asset_resp[0] = json.dumps(amend_quote,indent=5)
#         logger.info(asset_resp[0])
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = qop.create_quote_check(asset_resp)
#
#         tclist['status'] = itemc
#
#         asset_resp_dat = asset_resp[0]
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'Accept and Calulate prorata from Asset api for the create quote'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#
#         qop = Asset_endtoend()
#         acc_req = qop.calculate_prorata(quote_n)
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(acc_req)
#
#         tgate = gateway_process("calculate_prorata")
#
#         acc_resp = tgate.api_exec(acc_req)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(acc_resp)
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = qop.create_quote_check(acc_req)
#
#         tclist['status'] = itemc
#
#
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'Convert quote to Policy from Asset API'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#
#
#         qop = Asset_endtoend()
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(quote_n)
#
#         tgate = gateway_process("convert_to_policy")
#
#         conv_resp = tgate.convtop_exec(quote_n)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(conv_resp)
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = qop.create_quote_check(conv_resp)
#
#         tclist['status'] = itemc
#
#         logdat['testc'].append(tclist)
#
#         policy_n = quote_n
#
#         tclist = {'testcase': 'View policy from Asset api test'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#         pop = Asset_endtoend()
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(policy_n)
#
#         tgate = gateway_process("view_policy")
#
#         viewp_resp = tgate.view_policy(policy_n)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(viewp_resp)
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = pop.view_policy_check(viewp_resp)
#
#         policy_detail = viewp_resp[0]
#
#
#         tclist['status'] = itemc
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'Amend Policy from Asset API '}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(policy_detail)
#
#         tgate = gateway_process("process_policy")
#
#         policy_resp = tgate.api_exec(policy_detail)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(policy_resp)
#
#         logger.info("-----------}")
#
#         pop = Asset_endtoend()
#
#         itemc = pop.amendpolicy_check(policy_resp)
#
#         tclist['status'] = itemc
#
#         logdat['testc'].append(tclist)
#
#
#         tclist = {'testcase': 'Accept / Decline policy amendment for Endorsement'}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info("Decison: True")
#
#         tgate = gateway_process("accept_policy")
#
#         acdpol_resp = tgate.accept_policyendorse(policy_n,"True")
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(acdpol_resp)
#
#         logger.info("-----------}")
#
#         # validate response
#
#         pop = Asset_endtoend()
#
#         itemc = pop.acdpol_check(acdpol_resp)
#
#         tclist['status'] = itemc
#
#         logdat['testc'].append(tclist)
#
#
#         policy_n = quote_n
#
#         tclist = {'testcase': 'View policy from Asset API  after endorsement '}
#
#         logger = tlog.set_log('INFO', 'format')
#         logger.info("Test case:--")
#         logger = tlog.set_log('INFO', 'noformat')
#
#         logger.info(tclist['testcase'])
#
#         logger.info("{----------")
#         pop = Asset_endtoend()
#         logger.info("<<<<<<<< api-gateway-request >>>>>>>>>>")
#         logger.info(policy_n)
#
#         tgate = gateway_process("view_policy")
#
#         viewp_resp = tgate.view_policy(policy_n)
#
#         logger.info("<<<<<<<< api-gateway-response >>>>>>>>>>")
#         logger.info(viewp_resp)
#
#         logger.info("-----------}")
#
#         # validate response
#         itemc = pop.view_policy_check(viewp_resp)
#
#         policy_detail = viewp_resp[0]
#
#         tclist['status'] = itemc
#
#         logdat['testc'].append(tclist)
#
#
#
#     @classmethod
#     def tearDownClass(cls):
#         etsec = time.time()
#         end_time = time.asctime(time.localtime(time.time()))
#
#         print('start time:', start_time)
#         print('end time:  ', end_time)
#         print("--- %s seconds ---" % (etsec - stsec))
#
#         logdat['end_time'] = end_time
#         logdat['time_taken'] = (etsec - stsec)
#
#         rlog.log_repdata(logdat, 'testsuite')
#
#         rlog.report_handover('handover')
#         tlog.file_handover('handover')










