from pymongo import MongoClient
from .test_gate import log_builder,gateway_process
import json



class prorata_calculator():

    def __init__(self):
        global con
        db = MongoClient('mongodb://prbk-pa001sap4v:27017')
        con = db['ApiTestContainer']

    def prorata_calc_log(self):
        global logger
        tlog = log_builder('prorata_process')
        logger = tlog.set_log('INFO', 'noformat')

    def prorata_main(self,date_rfact):

        col = con['prorata_base']

        rfact = date_rfact
        prdisp = []

        for point in rfact:

            col.update({"ItemType": "MOT"},
                       {
                           "$set": {
                               "Effective_Date": "" + point['Effective_Date'] + "",
                               "Debit_Date": "" + point['Debit_Date'] + "",
                           }
                       })

            procal_api = col.find_one({"ItemType": "MOT"})

            del procal_api['_id']
            procal_api = json.dumps(procal_api, indent=5)

            # log_builder("API Request:----------------------")
            # logger.info(procal_api)
            print("API request----------------")
            print(procal_api)

            tgate = gateway_process("prorata_process")

            asset_resp = tgate.process_prorata(procal_api)

            amount = asset_resp['Amount']
            point.update({"Amount":amount,"Premium":1000})
            prdisp.append(point)
            asset_resp = json.dumps(asset_resp, indent=5)



            print("API response----------------")

            print(asset_resp)

            # logger.info("API Response:---------------------")
            # logger.info(asset_resp)
        return prdisp

    def getdate(self):
        db = MongoClient()
        col = con['prorata_factors']
        prodate_dict = col.find_one({"runtype": "testfact_2018"})

        del prodate_dict['_id']

        rfact = prodate_dict['rating_factors']

        return rfact


if __name__ == '__main__':

    pcalc = prorata_calculator()

    date_fact = pcalc.getdate()

    #pcalc.prorata_calc_log()

    prdata = pcalc.prorata_main(date_fact)
    print(prdata)

    print(len(prdata))
