from requests import get
from math import log, floor

#File with sensitive information needed for the script
import credentials

#Function for making pretty tables
from tabulate import tabulate

def hiveos_requests():

    #"Logging in" to the API so to say, with personal API key
    headers = { 
        "Content-Type": "application/json",
        "Authorization": "Bearer " + credentials.hiveos_key }

    #The base URL for the API, which we use as a base to navigate to different endpoints
    base_url = "https://api2.hiveos.farm/api/v2"

    #The endpoints for farm and worker(s) related data 
    endpoint_worker_1 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_1_id)
    endpoint_worker_2 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_2_id)
    endpoint_farm = base_url + "/farms/{0}".format(credentials.farm_id)

    #Request for the said endpoints
    hiveos_api_worker_1 = get(endpoint_worker_1, headers=headers)
    hiveos_api_worker_2 = get(endpoint_worker_2, headers=headers)
    hiveos_api_farm = get(endpoint_farm, headers=headers)

    #Extracting keys from the API
    hiveos_api_keys_worker_1 = hiveos_api_worker_1.json()
    hiveos_api_keys_worker_2 = hiveos_api_worker_2.json()
    hiveos_api_keys_farm = hiveos_api_farm.json()
   

    #Function for changing large numbers to Kilos, Megas etc.
    def hashrate_format(number):
        units = ['', ' MH', ' GH', ' TH', ' PH']
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k**magnitude, units[magnitude])



    #---------- WORKER 1 ----------#

    try:
        #Worker 1 GPU 0 data"
        worker_1_gpu_0_name = "RX 5700 XT MSI"
        worker_1_gpu_0_index = "0:"
        worker_1_gpu_0_hashrate = hiveos_api_keys_worker_1["gpu_stats"][0]["hash"]
        worker_1_gpu_0_power = str(hiveos_api_keys_worker_1["gpu_stats"][0]["power"]) + " W"
        worker_1_gpu_0_fan = str(hiveos_api_keys_worker_1["gpu_stats"][0]["fan"]) + " %"
        worker_1_gpu_0_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["temp"]) + " °C"
        
        #Color changes depending on temperatures
        if hiveos_api_keys_worker_1["gpu_stats"][0]["temp"] >= 60:
            worker_1_gpu_0_coretemp = f"""
            <a style="color: red">{worker_1_gpu_0_coretemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][0]["temp"] < 60 and hiveos_api_keys_worker_1["gpu_stats"][0]["temp"] >= 55:
            worker_1_gpu_0_coretemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_0_coretemp}</a>
            """            
        else:
            worker_1_gpu_0_coretemp = f"""
            <a style="color: green;">{worker_1_gpu_0_coretemp}</a>
            """
            
        worker_1_gpu_0_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"] >= 86:
            worker_1_gpu_0_memtemp = f"""
            <a style="color: red">{worker_1_gpu_0_memtemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"] < 86 and hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"] >= 81:
            worker_1_gpu_0_memtemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_0_memtemp}</a>
            """            
        else:
            worker_1_gpu_0_memtemp = f"""
            <a style="color: green;">{worker_1_gpu_0_memtemp}</a>
            """

        #Worker 1 GPU 1 data
        worker_1_gpu_1_name = "RX 5700 XT Gigabyte"
        worker_1_gpu_1_index = "1:"
        worker_1_gpu_1_hashrate = hiveos_api_keys_worker_1["gpu_stats"][1]["hash"]
        worker_1_gpu_1_power = str(hiveos_api_keys_worker_1["gpu_stats"][1]["power"]) + " W"
        worker_1_gpu_1_fan = str(hiveos_api_keys_worker_1["gpu_stats"][1]["fan"]) + " %"
        worker_1_gpu_1_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["temp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][1]["temp"] >= 60:
            worker_1_gpu_1_coretemp = f"""
            <a style="color: red">{worker_1_gpu_1_coretemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][1]["temp"] < 60 and hiveos_api_keys_worker_1["gpu_stats"][1]["temp"] >= 55:
            worker_1_gpu_1_coretemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_1_coretemp}</a>
            """  
        else:
            worker_1_gpu_1_coretemp = f"""
            <a style="color: green">{worker_1_gpu_1_coretemp}</a>
            """
                    
        worker_1_gpu_1_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"] >= 82:
            worker_1_gpu_1_memtemp = f"""
            <a style="color: red">{worker_1_gpu_1_memtemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"] < 86 and hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"] >= 81:
            worker_1_gpu_1_memtemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_1_memtemp}</a>
            """ 
        else:
            worker_1_gpu_1_memtemp = f"""
            <a style="color: green">{worker_1_gpu_1_memtemp}</a>
            """

        #Worker 1 GPU 2 data
        worker_1_gpu_2_name = "RX 5700 XT PowerColor"
        worker_1_gpu_2_index = "2:"
        worker_1_gpu_2_hashrate = hiveos_api_keys_worker_1["gpu_stats"][2]["hash"]
        worker_1_gpu_2_power = str(hiveos_api_keys_worker_1["gpu_stats"][2]["power"]) + " W"
        worker_1_gpu_2_fan = str(hiveos_api_keys_worker_1["gpu_stats"][2]["fan"]) + " %"
        worker_1_gpu_2_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["temp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][2]["temp"] >= 60:
            worker_1_gpu_2_coretemp = f"""
            <a style="color: red">{worker_1_gpu_2_coretemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][2]["temp"] < 60 and hiveos_api_keys_worker_1["gpu_stats"][2]["temp"] >= 55:
            worker_1_gpu_2_coretemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_2_coretemp}</a>
            """              
        else:
            worker_1_gpu_2_coretemp = f"""
            <a style="color: green">{worker_1_gpu_2_coretemp}</a>
            """
            
        worker_1_gpu_2_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"] >= 82:
            worker_1_gpu_2_memtemp = f"""
            <a style="color: red">{worker_1_gpu_2_memtemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"] < 86 and hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"] >= 81:
            worker_1_gpu_2_memtemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_2_memtemp}</a>
            """ 
        else:
            worker_1_gpu_2_memtemp = f"""
            <a style="color: green">{worker_1_gpu_2_memtemp}</a>
            """
            
        #Worker 1 GPU 3 data
        worker_1_gpu_3_name = "RX 5700 XT Asus"
        worker_1_gpu_3_index = "3:"
        worker_1_gpu_3_hashrate = hiveos_api_keys_worker_1["gpu_stats"][3]["hash"]
        worker_1_gpu_3_power = str(hiveos_api_keys_worker_1["gpu_stats"][3]["power"]) + " W"
        worker_1_gpu_3_fan = str(hiveos_api_keys_worker_1["gpu_stats"][3]["fan"]) + " %"
        worker_1_gpu_3_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["temp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][3]["temp"] >= 60:
            worker_1_gpu_3_coretemp = f"""
            <a style="color: red">{worker_1_gpu_3_coretemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][3]["temp"] < 60 and hiveos_api_keys_worker_1["gpu_stats"][3]["temp"] >= 55:
            worker_1_gpu_3_coretemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_3_coretemp}</a>
            """              
        else:
            worker_1_gpu_3_coretemp = f"""
            <a style="color: green">{worker_1_gpu_3_coretemp}</a>
            """        
            
        worker_1_gpu_3_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"] >= 82:
            worker_1_gpu_3_memtemp = f"""
            <a style="color: red">{worker_1_gpu_3_memtemp}</a>
            """
        elif hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"] < 86 and hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"] >= 81:
            worker_1_gpu_3_memtemp = f"""
            <a style="color: rgb(255, 179, 128);">{worker_1_gpu_3_memtemp}</a>
            """ 
        else:
            worker_1_gpu_3_memtemp = f"""
            <a style="color: green">{worker_1_gpu_3_memtemp}</a>
            """        

        #Create a HTML table from all worker GPUs
        worker_1_table = f"""
        <div>
            <table style="width: 96%; max-width: 700px; height: 165px; border: 2px solid rgb(255, 133, 51); background-color: black;">
            <tbody>
            <tr style="height: 33.0469px; text-align: center; background-color: grey;">
            <td style="width: 91px; height: 33.0469px;">GPU</td>
            <td style="width: 91px; height: 36px;">Hashrate</td>
            <td style="width: 91px; height: 33.0469px;">Core Temp</td>
            <td style="width: 91px; height: 33.0469px;">Mem Temp</td>
            <td style="width: 59px; height: 33.0469px;">Fan</td>
            <td style="width: 110px; height: 33.0469px;">Power</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216)">
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_0_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_1_gpu_0_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_1_gpu_0_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_0_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_1_gpu_0_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_1_gpu_0_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_1_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_1_gpu_1_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_1_gpu_1_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_1_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_1_gpu_1_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_1_gpu_1_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216">
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_2_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_1_gpu_2_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_1_gpu_2_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_2_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_1_gpu_2_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_1_gpu_2_power}</td>
            </tr>
            <tr style="height: 33px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_3_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_1_gpu_3_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_1_gpu_3_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_1_gpu_3_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_1_gpu_3_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_1_gpu_3_power}</td>
            </tr>
            </tbody>
            </table>
        <div>
        """
        with open("/var/www/html/hiveos_output_worker_1.html", "w", encoding="utf-8") as hiveos_output_file_worker_1:
            hiveos_output_file_worker_1.write(f"{worker_1_table}")
                
    
    #In case of an error
       
    except IndexError:
        worker_1_table = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 1 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div>
            <a style="color: red;">Index error. Please Check script.<br><br></a>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_worker_1.html", "w", encoding="utf-8") as hiveos_output_file_worker_1:
            hiveos_output_file_worker_1.write(f"{worker_1_table}")
            
    except KeyError or Exception:
        worker_1_table = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 1 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div>
            <h1 style="color: red;">OFFLINE!<br><br></h1>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_worker_1.html", "w", encoding="utf-8") as hiveos_output_file_worker_1:
            hiveos_output_file_worker_1.write(f"{worker_1_table}")
        
       
       



    #---------- WORKER 2 ----------#
    
    try:    
        #Worker 2 GPU 0 data
        worker_2_gpu_0_name = "RTX 3070 Ti ASUS"
        worker_2_gpu_0_index = "0:"
        worker_2_gpu_0_hashrate = hiveos_api_keys_worker_2["gpu_stats"][0]["hash"]
        worker_2_gpu_0_power = str(hiveos_api_keys_worker_2["gpu_stats"][0]["power"]) + " W"
        worker_2_gpu_0_fan = str(hiveos_api_keys_worker_2["gpu_stats"][0]["fan"]) + " %"
        worker_2_gpu_0_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][0]["temp"] >= 60:
            worker_2_gpu_0_coretemp = f"""
            <a style="color: red">{worker_2_gpu_0_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][0]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][0]["temp"] >= 55:
            worker_2_gpu_0_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_0_coretemp}</a>
            """              
        else:
            worker_2_gpu_0_coretemp = f"""
            <a style="color: green">{worker_2_gpu_0_coretemp}</a>
            """          
        worker_2_gpu_0_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"] >= 86:
            worker_2_gpu_0_memtemp = f"""
            <a style="color: red">{worker_2_gpu_0_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"] >= 81:
            worker_2_gpu_0_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_0_memtemp}</a>
            """            
        else:
            worker_2_gpu_0_memtemp = f"""
            <a style="color: green">{worker_2_gpu_0_memtemp}</a>
            """        

        #Worker 2 GPU 1 data
        worker_2_gpu_1_name = "GTX 1660 Super MSI"
        worker_2_gpu_1_index = "1:"
        worker_2_gpu_1_hashrate = hiveos_api_keys_worker_2["gpu_stats"][1]["hash"]
        worker_2_gpu_1_power = str(hiveos_api_keys_worker_2["gpu_stats"][1]["power"]) + " W"
        worker_2_gpu_1_fan = str(hiveos_api_keys_worker_2["gpu_stats"][1]["fan"]) + " %"
        worker_2_gpu_1_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][1]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][1]["temp"] >= 60:
            worker_2_gpu_1_coretemp = f"""
            <a style="color: red">{worker_2_gpu_1_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][1]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][1]["temp"] >= 55:
            worker_2_gpu_1_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_1_coretemp}</a>
            """              
        else:
            worker_2_gpu_1_coretemp = f"""
            <a style="color: green">{worker_2_gpu_1_coretemp}</a>
            """                  
        worker_2_gpu_1_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"] >= 86:
            worker_2_gpu_1_memtemp = f"""
            <a style="color: red">{worker_2_gpu_1_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"] >= 81:
            worker_2_gpu_1_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_1_memtemp}</a>
            """            
        else:
            worker_2_gpu_1_memtemp = f"""
            <a style="color: green">{worker_2_gpu_1_memtemp}</a>
            """            

        #Worker 2 GPU 2 data    
        worker_2_gpu_2_name = "RTX 3070 Ti ASUS TUF"
        worker_2_gpu_2_index = "2:"
        worker_2_gpu_2_hashrate = hiveos_api_keys_worker_2["gpu_stats"][2]["hash"]
        worker_2_gpu_2_power = str(hiveos_api_keys_worker_2["gpu_stats"][2]["power"]) + " W"
        worker_2_gpu_2_fan = str(hiveos_api_keys_worker_2["gpu_stats"][2]["fan"]) + " %"
        worker_2_gpu_2_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][2]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][2]["temp"] >= 60:
            worker_2_gpu_2_coretemp = f"""
            <a style="color: red">{worker_2_gpu_2_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][2]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][2]["temp"] >= 55:
            worker_2_gpu_2_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_2_coretemp}</a>
            """              
        else:
            worker_2_gpu_2_coretemp = f"""
            <a style="color: green">{worker_2_gpu_2_coretemp}</a>
            """           
        worker_2_gpu_2_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"] >= 86:
            worker_2_gpu_2_memtemp = f"""
            <a style="color: red">{worker_2_gpu_2_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"] >= 81:
            worker_2_gpu_2_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_2_memtemp}</a>
            """            
        else:
            worker_2_gpu_2_memtemp = f"""
            <a style="color: green">{worker_2_gpu_2_memtemp}</a>
            """          

        #Worker 2 GPU 3 data
        worker_2_gpu_3_name = "GTX 1660 Super MSI"
        worker_2_gpu_3_index = "3:"
        worker_2_gpu_3_hashrate = hiveos_api_keys_worker_2["gpu_stats"][3]["hash"]
        worker_2_gpu_3_power = str(hiveos_api_keys_worker_2["gpu_stats"][3]["power"]) + " W"
        worker_2_gpu_3_fan = str(hiveos_api_keys_worker_2["gpu_stats"][3]["fan"]) + " %"
        worker_2_gpu_3_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][3]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][3]["temp"] >= 60:
            worker_2_gpu_3_coretemp = f"""
            <a style="color: red">{worker_2_gpu_3_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][3]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][3]["temp"] >= 55:
            worker_2_gpu_3_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_3_coretemp}</a>
            """              
        else:
            worker_2_gpu_3_coretemp = f"""
            <a style="color: green">{worker_2_gpu_3_coretemp}</a>
            """              
        worker_2_gpu_3_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"] >= 86:
            worker_2_gpu_3_memtemp = f"""
            <a style="color: red">{worker_2_gpu_3_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"] >= 81:
            worker_2_gpu_3_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_3_memtemp}</a>
            """            
        else:
            worker_2_gpu_3_memtemp = f"""
            <a style="color: green">{worker_2_gpu_3_memtemp}</a>
            """          

        #Worker 2 GPU 4 data
        worker_2_gpu_4_name = "GTX 1660 Super HP OEM"
        worker_2_gpu_4_index = "4:"
        worker_2_gpu_4_hashrate = hiveos_api_keys_worker_2["gpu_stats"][4]["hash"]
        worker_2_gpu_4_power = str(hiveos_api_keys_worker_2["gpu_stats"][4]["power"]) + " W"
        worker_2_gpu_4_fan = str(hiveos_api_keys_worker_2["gpu_stats"][4]["fan"]) + " %"
        worker_2_gpu_4_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][4]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][4]["temp"] >= 60:
            worker_2_gpu_4_coretemp = f"""
            <a style="color: red">{worker_2_gpu_4_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][4]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][4]["temp"] >= 55:
            worker_2_gpu_4_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_4_coretemp}</a>
            """              
        else:
            worker_2_gpu_4_coretemp = f"""
            <a style="color: green">{worker_2_gpu_4_coretemp}</a>
            """              
        worker_2_gpu_4_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"] >= 86:
            worker_2_gpu_4_memtemp = f"""
            <a style="color: red">{worker_2_gpu_4_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"] >= 81:
            worker_2_gpu_4_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_4_memtemp}</a>
            """            
        else:
            worker_2_gpu_4_memtemp = f"""
            <a style="color: green">{worker_2_gpu_4_memtemp}</a>
            """          

        #Worker 2 GPU 5 data
        worker_2_gpu_5_name = "GTX 1660 Super ASUS"
        worker_2_gpu_5_index = "5:"
        worker_2_gpu_5_hashrate = hiveos_api_keys_worker_2["gpu_stats"][5]["hash"]
        worker_2_gpu_5_power = str(hiveos_api_keys_worker_2["gpu_stats"][5]["power"]) + " W"
        worker_2_gpu_5_fan = str(hiveos_api_keys_worker_2["gpu_stats"][5]["fan"]) + " %"
        worker_2_gpu_5_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][5]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][5]["temp"] >= 60:
            worker_2_gpu_5_coretemp = f"""
            <a style="color: red">{worker_2_gpu_5_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][5]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][5]["temp"] >= 55:
            worker_2_gpu_5_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_5_coretemp}</a>
            """              
        else:
            worker_2_gpu_5_coretemp = f"""
            <a style="color: green">{worker_2_gpu_5_coretemp}</a>
            """                      
        worker_2_gpu_5_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"] >= 86:
            worker_2_gpu_5_memtemp = f"""
            <a style="color: red">{worker_2_gpu_5_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"] >= 81:
            worker_2_gpu_5_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_5_memtemp}</a>
            """            
        else:
            worker_2_gpu_5_memtemp = f"""
            <a style="color: green">{worker_2_gpu_5_memtemp}</a>
            """           

        #Worker 2 GPU 6 data
        worker_2_gpu_6_name = "GTX 1660 Super ASUS"
        worker_2_gpu_6_index = "6:"
        worker_2_gpu_6_hashrate = hiveos_api_keys_worker_2["gpu_stats"][6]["hash"]
        worker_2_gpu_6_power = str(hiveos_api_keys_worker_2["gpu_stats"][6]["power"]) + " W"
        worker_2_gpu_6_fan = str(hiveos_api_keys_worker_2["gpu_stats"][6]["fan"]) + " %"
        worker_2_gpu_6_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][6]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][6]["temp"] >= 60:
            worker_2_gpu_5_coretemp = f"""
            <a style="color: red">{worker_2_gpu_6_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][6]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][6]["temp"] >= 55:
            worker_2_gpu_6_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_6_coretemp}</a>
            """              
        else:
            worker_2_gpu_6_coretemp = f"""
            <a style="color: green">{worker_2_gpu_6_coretemp}</a>
            """             
        worker_2_gpu_6_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"] >= 86:
            worker_2_gpu_6_memtemp = f"""
            <a style="color: red">{worker_2_gpu_6_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"] >= 81:
            worker_2_gpu_6_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_6_memtemp}</a>
            """            
        else:
            worker_2_gpu_6_memtemp = f"""
            <a style="color: green">{worker_2_gpu_6_memtemp}</a>
            """           

        #Worker 2 GPU 7 data
        worker_2_gpu_7_name = "GTX 1660 Super ASUS"
        worker_2_gpu_7_index = "7:"
        worker_2_gpu_7_hashrate = hiveos_api_keys_worker_2["gpu_stats"][7]["hash"]
        worker_2_gpu_7_power = str(hiveos_api_keys_worker_2["gpu_stats"][7]["power"]) + " W"
        worker_2_gpu_7_fan = str(hiveos_api_keys_worker_2["gpu_stats"][7]["fan"]) + " %"
        worker_2_gpu_7_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][7]["temp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][7]["temp"] >= 60:
            worker_2_gpu_7_coretemp = f"""
            <a style="color: red">{worker_2_gpu_7_coretemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][7]["temp"] < 60 and hiveos_api_keys_worker_2["gpu_stats"][7]["temp"] >= 55:
            worker_2_gpu_7_coretemp = f"""
            <a style="color: yellow">{worker_2_gpu_7_coretemp}</a>
            """              
        else:
            worker_2_gpu_7_coretemp = f"""
            <a style="color: green">{worker_2_gpu_7_coretemp}</a>
            """              
        worker_2_gpu_7_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"]) + " °C"
        if hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"] >= 86:
            worker_2_gpu_7_memtemp = f"""
            <a style="color: red">{worker_2_gpu_7_memtemp}</a>
            """
        elif hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"] < 86 and hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"] >= 81:
            worker_2_gpu_7_memtemp = f"""
            <a style="color: yellow">{worker_2_gpu_7_memtemp}</a>
            """            
        else:
            worker_2_gpu_7_memtemp = f"""
            <a style="color: green">{worker_2_gpu_7_memtemp}</a>
            """         

        #Create a HTML table from all worker GPUs
        worker_2_table = f"""
        <div>
            <table style="width: 96%; max-width: 700px; height: 165px; border: 2px solid rgb(255, 133, 51); background-color: black;">
            <tbody>
            <tr style="height: 33.0469px; text-align: center; background-color: grey;">
            <td style="width: 91px; height: 33.0469px;">GPU</td>
            <td style="width: 91px; height: 36px;">Hashrate</td>
            <td style="width: 91px; height: 33.0469px;">Core Temp</td>
            <td style="width: 91px; height: 33.0469px;">Mem Temp</td>
            <td style="width: 59px; height: 33.0469px;">Fan</td>
            <td style="width: 110px; height: 33.0469px;">Power</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216)">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_0_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_0_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_0_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_0_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_0_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_0_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_1_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_1_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_1_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_1_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_1_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_1_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_2_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_2_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_2_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_2_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_2_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_2_power}</td>
            </tr>
            <tr style="height: 33px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_3_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_3_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_3_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_3_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_3_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_3_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_4_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_4_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_4_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_4_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_4_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_4_power}</td>
            </tr>
            <tr style="height: 33px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_5_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_5_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_5_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_5_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_5_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_5_power}</td>
            </tr>
            <tr style="height: 32px; text-align: center; background-color: rgb(216, 216, 216">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_6_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_6_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_6_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_6_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_6_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_6_power}</td>
            </tr>
            <tr style="height: 33px; text-align: center; background-color: #f1f1f1;">
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_7_name}</td>
            <td style="width: 91.5625px; height: 32px;">{hashrate_format(worker_2_gpu_7_hashrate)}</td>
            <td style="width: 75.3281px; height: 32px;">{worker_2_gpu_7_coretemp}</td>
            <td style="width: 91.4219px; height: 32px;">{worker_2_gpu_7_memtemp}</td>
            <td style="width: 59.1406px; height: 32px;">{worker_2_gpu_7_fan}</td>
            <td style="width: 129.125px; height: 32px;">{worker_2_gpu_7_power}</td>
            </tr>
            </tbody>
            </table>
        </div>
        """
        with open("/var/www/html/hiveos_output_worker_2.html", "w", encoding="utf-8") as hiveos_output_file_worker_2:
            hiveos_output_file_worker_2.write(f"{worker_2_table}")
        

    #In case of an error
    except IndexError:
        worker_2_table = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 2 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div>
            <a style="color: red;">Index error. Please Check script.<br><br></a>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_worker_2.html", "w", encoding="utf-8") as hiveos_output_file_worker_2:
            hiveos_output_file_worker_2.write(f"{worker_2_table}")
            
    except KeyError or Exception:
        worker_2_table = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 2 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div>
            <h1 style="color: red;">OFFLINE!<br><br></h1>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_worker_2.html", "w", encoding="utf-8") as hiveos_output_file_worker_2:
            hiveos_output_file_worker_2.write(f"{worker_2_table}")
        
        


    #---------- Farm Total Stats ----------#
    try:
        total_gpus = str(hiveos_api_keys_farm["stats"]["gpus_online"])
        if hiveos_api_keys_farm["stats"]["gpus_online"] == 12:
            total_gpus = f"""
            <a style="color: green">{total_gpus}</a>
            """
        else:
            total_gpus = f"""
            <a style="color: yellow">{total_gpus}</a>
            """

        total_gpus_offline = str(hiveos_api_keys_farm["stats"]["gpus_offline"])
        if hiveos_api_keys_farm["stats"]["gpus_offline"] > 0:
            total_gpus_offline = f"""
            <a style="color: red">{total_gpus_offline}!!</a>
            """            
        total_hash = str(hashrate_format(hiveos_api_keys_farm["hashrates"][0]["hashrate"]))
        total_power = str(hiveos_api_keys_farm["stats"]["power_draw"]) + " W"
        
        
        
        total_stats = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 2 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div style="font-size: 18px; margin-top: 10px; margin-bottom: 20px;">
            <a>GPUs online: {total_gpus}<br>
            GPUs offline: {total_gpus_offline}<br>
            Hashrate: {total_hash}<br>
            Power: {total_power}<br><br>
            </a>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_total.html", "w", encoding="utf-8") as hiveos_output_file_total:
            hiveos_output_file_total.write(f"{total_stats}")  
            
    except Exception:
        total_stats = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Worker 2 Table</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
        </head>
        <div>
            <a>Error getting data.</a>
        <div>
        </html>
        """
        with open("/var/www/html/hiveos_output_total.html", "w", encoding="utf-8") as hiveos_output_file_total:
            hiveos_output_file_total.write(f"{total_stats}")    
        
        
if __name__ == '__main__':
    hiveos_requests()
