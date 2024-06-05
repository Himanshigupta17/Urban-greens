from flask import Flask,render_template,request
from getTestData import getTreeData,getCoord
from pyswip import Prolog
from TreePred import getPred
import json
app=Flask(__name__)
prolog = Prolog()
prolog.consult('KB.pl')
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

@app.route('/',methods=["GET"])
def homeP():
    return render_template('home.html')
@app.route('/map')
def show_map():
    return render_template('map.html')
@app.route('/form', methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html',str="Please Select A City From DropDown",coordinates=[])
    else:
        measures_string=''
        selected = request.form['city']
        if selected == 'SouthDelhi':
            getTreeData("SouthDelhi")
            measures_string = (
            "1. Road Traffic Management\n"
            "2. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "3. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
            "4. Repair roads where there are potholes.\n"
            "5. Maintenance of trees.\n"
            "6. Water Sprinkling.\n"
            "7. Smog Towers (Already present but not operational)"
            )
            getPred(AQI=60,LAND=250,LAT=28.47,LONG=77.1830,TEMP=30,HUM=37,POP=9000,PERCP=164,TRAFFIC=3)
        elif selected == 'SouthWestDelhi':
            getTreeData("SouthWestDelhi")
            measures_string = (
            "1. Use of smog guns on a regular basis.\n"
            "2. Smog Towers (Already present but not operational).\n"
            "3. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid, and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "4. Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
            "5. Road Traffic Management.\n"
            "6. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
            "7. Water Sprinkling.\n"
            "8. Construction sites must be covered and netted properly and also inspected strictly.\n"
            "9. Waste Management System.\n"
            "10. Control on Crop stubble burning by the government. Following steps can be followed:\n"
            "    - Incentives sowing of Kharif crops instead of paddy.\n"
            "    - Include straw as input in coal power plants.\n"
            "11. Improve machineries or manufacturing processes to reduce emissions from factories.\n"
            "12. Proper maintenance of boilers e.g. blowing dust from the surface, reducing excess air can reduce air pollution from industries.\n"
            "13. Maintenance of trees.\n"
            "14. Control on solid waste burning:\n"
            "15. Setting up new waste to energy plants with the latest technology.\n"
            "16. Segregation of waste.\n"
            "17. Maintain and ensure 100% capacity utilization of all plants in affected and surrounding areas."
            )
            getPred(AQI=60,LAND=420,LAT=28.40,LONG=77.50,TEMP=29,HUM=42,POP=5445,PERCP=105,TRAFFIC=4)
        elif selected == 'NorthDelhi':
            getTreeData("NorthDelhi")
            measures_string = (
            "1. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
            "2. Use of smog guns on a regular basis.\n"
            "3. Smog Towers (Already present but not operational).\n"
            "4. Waste Management.\n"
            "5. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "6. Water Sprinkling.\n"
            "7. Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
            "8. Repair roads where there are potholes.\n"
            "9. Maintenance of trees.\n"
            "10. Control on solid waste burning:\n"
            "11. Setting up new waste to energy plants with the latest technology.\n"
            "12. Segregation of waste.\n"
            "13. Maintain and ensure 100% capacity utilization of all plants in affected and surrounding areas."
            )
            getPred(AQI=60,LAND=291,LAT=28.6775,LONG=77.2224,TEMP=30,HUM=47,POP=3100,PERCP=33,TRAFFIC=4)
        elif selected == 'EastDelhi':
            getTreeData("EastDelhi")
            measures_string = (
            "1.USE OF SMOG GUNS ON REGULAR BASIS.\n"
            "2.Smog Towers (Already present but not operational)\n"
            "3.Emissions from nearby industrial areas at Patparganj and Sahibabad should be controlled to bring the level of particulate matter down. THIS CAN BE DONE BY IMPLEMENTING AND REGULAR CHECK OF USE OF CHIMNEYS BY INDUSTRIES.\n"
            "4.Water sprinkling\n"
            "5.Covering loose soil and construction waste with netting.\n"
            "6.Paving and cleaning approach roads near the bus terminal to control dust pollution and reduce exposure.\n"
            "7.Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "8.Construction sites must be covered and netted properly.\n"
            "9.Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
            "10.The large power plants and refineries in Delhi emit pollutants like sulphur dioxide (SO2) and nitrogen oxides (NOx). In a bid to limit them, these plants and refineries need to install De-SOx-ing and De-NOx-ing systems that remove SO2 and NOx respectively.\n"
            "11.Waste management system.\n"
            "12.Perforated high-density polyethylene pipes to be installed to prevent the accumulation of the highly flammable gas and a dedicated surveillance squad to keep a strict vigil over the activities going on at the dumping sites.\n"
            "13.Maintenance of trees"
             )
            getPred(AQI=60,LAND=181,LAT=28.6425,LONG=77.2975,TEMP=30,HUM=41,POP=23614,PERCP=-30,TRAFFIC=5)
        elif selected == 'SouthEastDelhi':
            getTreeData("SouthEastDelhi")
            measures_string = (
                "1. Water Sprinkling\n"
                "2. Use of smog guns on a regular basis.\n"
                "3. Smog Towers (Already present but not operational).\n"
                "4. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid, and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
                "5. Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
                "6. Road Traffic Management\n"
                "7. Waste Management System\n"
                "8. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
                "9. Regular check of use of chimneys by industries.\n"
                "10. Maintenance of trees.\n"
                "11. Control on Crop stubble burning by the government. Following steps can be followed:\n"
                "    - Incentives sowing of Kharif crops instead of paddy.\n"
                "    - Include straw as input in coal power plants.\n"
                "12. Use wet scrubbers and electric precipitators in all coal using industrial plants.\n"
                "13. Control on solid waste burning:\n"
                "14. Setting up new waste to energy plants with the latest technology.\n"
                "15. Segregation of waste.\n"
                "16. Maintain and ensure 100% capacity utilization of all plants in affected and surrounding areas."
            )
            getPred(AQI=60,LAND=132,LAT=28.47,LONG=77.1830,TEMP=30,HUM=40,POP=15000,PERCP=100,TRAFFIC=4)
        elif selected == 'NorthWestDelhi':
            getTreeData("NorthWestDelhi")
            measures_string = (
                "1. Control on Crop stubble burning by government. Following steps can be followed:\n"
                "   - Incentives sowing of Kharif crops instead of paddy.\n"
                "   - Include straw as input in coal power plants.\n\n"
                
                "2. Controlling Vehicular pollution. Following steps can be undertaken by government:\n"
                "   - Import low sulphur petrol and diesel.\n"
                "   - Accurate conversion of public sector refineries to low sulphur.\n"
                "   - Introduce pollution cess on high sulphur fuel.\n"
                "   - Double metro capacity.\n"
                "   - Funding fuel-efficient two-wheelers.\n"
                "   - Advance emission surveillance of on-road vehicles with remote sensing devices.\n\n"
                
                "3. Clean fuels and electric mobility.\n\n"
                
                "4. Proper road traffic management.\n\n"
                
                "5. Control on solid waste burning:\n"
                "   - Setting up new waste to energy plants with the latest technology.\n"
                "   - Segregation of waste.\n"
                "   - Maintain and ensure 100% capacity utilization of all plants in affected and surrounding areas.\n\n"
                
                "6. Installation of solar panels should be encouraged at homes, multi-storey buildings, and commercial establishments so that decentralized power is generated with suitable subsidies to make it financially viable for all households. The cost of solar panels has come down considerably. This should help retire all coal-based thermal power plants which are adding a lot to Delhi’s air pollution problems and adversely affecting climate change.\n\n"
                
                "7. Control on soil and road dust:\n"
                "   - Repair roads where bitumen is loose or there are potholes.\n"
                "   - Ensure quick completion of digging work.\n"
                "   - Convert all roads to surfaced category.\n\n"
                
                "8. Monitoring and check on emissions from industries 24×7.\n\n"
                
                "9. Use wet scrubbers and electric precipitators in all coal-using industrial plants.\n\n"
                
                "10. Changes in coal and thermal plants:\n"
                "    - Use superior quality coal for plants.\n"
                "    - Subsidize gas power with a high pollution cess on coal.\n"
                "    - Stop small thermal plants and increase the capacity of gas-based power plants."
            )
            getPred(AQI=60,LAND=442,LAT=28.7306,LONG=77.0219,TEMP=30,HUM=47,POP=8300,PERCP=98,TRAFFIC=5)
        elif selected == 'WestDelhi':
            getTreeData("WestDelhi")
            measures_string = (
            "1. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
            "2. Construction sites must be covered.\n"
            "3. Water Sprinkling.\n"
            "4. Strict inspection of construction sites.\n"
            "5. Waste Management System.\n"
            "6. Use of smog guns on a regular basis.\n"
            "7. Smog Towers (Already present but not operational).\n"
            "8. Road Traffic Management.\n"
            "9. Monitoring emissions and maintenance 24*7.\n"
            "10. Repair roads where there are potholes.\n"
            "11. Abatement of air pollution caused by crop residue burning.\n"
            "12. Maintenance of trees.\n"
            "13. Control on Crop stubble burning by the government. Following steps can be followed:\n"
            "    - Incentives sowing of Kharif crops instead of paddy.\n"
            "    - Include straw as input in coal power plants.\n"
            "14. Control on soil and road dust:\n"
            "15. Repair roads where bitumen is loose or there are potholes.\n"
            "16. Ensure quick completion of digging work.\n"
            "17. Convert all roads to surfaced category."
            )
            getPred(AQI=60,LAND=129,LAT=28.6663,LONG=77.0680,TEMP=30,HUM=48,POP=19600,PERCP=89,TRAFFIC=5)
        elif selected == 'NewDelhi':
            getTreeData("NewDelhi")
            measures_string = (
            "1. Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
            "2. Water Sprinkling on roads.\n"
            "3. Use of smog guns on a regular basis.\n"
            "4. Smog Towers (Already present but not operational).\n"
            "5. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "6. Road Traffic Management.\n"
            "7. Maintenance of trees.\n"
            "8. Control on Crop stubble burning by the government. Following steps can be followed:\n"
            "   - Incentives sowing of Kharif crops instead of paddy.\n"
            "   - Include straw as input in coal power plants."
            )
            getPred(AQI=60,LAND=42,LAT=28.6139,LONG=77.2090,TEMP=30,HUM=49,POP=3381,PERCP=47,TRAFFIC=4)
        elif selected == 'CentralDelhi':
            getTreeData("CentralDelhi")
            measures_string = (
            "1. Paving and cleaning approach roads near the bus terminal and metro stations to control dust pollution and reduce exposure.\n"
            "2. Use of smog guns on a regular basis.\n"
            "3. Smog Towers (Already present but not operational).\n"
            "4. Waste Management.\n"
            "5. Encourage the use of Hydro electric vehicles. The introduction of more electric, hybrid and BS-VI vehicles can also help. Improvement of public transport is also necessary.\n"
            "6. Water Sprinkling.\n"
            "7. Diesel Particulate Filter (DPF) can significantly reduce emissions from diesel vehicles.\n"
            "8. Repair roads where there are potholes.\n"
            "9. Maintenance of trees.\n"
            "10. Control on solid waste burning:\n"
            "11. Setting up new waste to energy plants with the latest technology.\n"
            "12. Segregation of waste.\n"
            "13. Maintain and ensure 100% capacity utilization of all plants in affected and surrounding areas."
            )
            getPred(AQI=60,LAND=25,LAT=28.6145,LONG=77.2000,TEMP=30,HUM=51,POP=20000,PERCP=203,TRAFFIC=4)
        query= "check_result('output.txt')."
        list(prolog.query(query))
        str1= read_text_file('output2.txt')
        coord= getCoord(selected)
    return render_template('form.html', str=str1,coordinates=coord,sol=measures_string)
if __name__=="__main__":
    app.run(debug=True)