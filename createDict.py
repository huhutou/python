import urllib.request  
import urllib.parse
import json

#the url
prefix="http://10.11.4.239:30382"
suffix_add_dict="/iot-dict/iot/api/dict/add"
suffix_add_dict_detail="/iot-dict/iot/api/dictDetail/add"
suffix_login="/iot-api/iot/api/auth/login"

#login params
user="sysadmin@cmict.chinamobile.com"
password="sysadmin"

#header
headers: dict={
    "Content-Type":"application/json" 
}

# Get cookie
req=urllib.request.Request(url=prefix+suffix_login,
        data=json.dumps({
            "username":user,
            "password":password
        }).encode(),
        headers={
            "Content-Type":"application/json"
        }
        )
with urllib.request.urlopen(url=req) as response:
    res=json.loads(s=response.read().decode())
    X_Authorization:str="Bearer "+res.get("token")
    headers.update(X_Authorization=X_Authorization)

# add a new dict
req=urllib.request.Request(url=prefix+suffix_add_dict,
                           data=json.dumps(
                               obj={"isEdit":0,"isDelete":0,"name":"attribute_unit","description":"物模型业务属性计量单位"}
                           ).encode(),
                           headers=headers,
                           method="POST")
# urllib.request.urlopen(url=req)

# dict id
dictid=574

# dict details
dict_details=[{"name":"百分比/%","type":1}, 
                                    {"name":"次/count","type":2}, 
                                    {"name":"转每分钟/r/min","type":3}, 
                                    {"name":"纳米/nm","type":4}, 
                                    {"name":"微米/μm","type":5}, 
                                    {"name":"毫米/mm","type":6}, 
                                    {"name":"厘米/cm","type":7}, 
                                    {"name":"米/m","type":8}, 
                                    {"name":"千米/km","type":9}, 
                                    {"name":"平方毫米/mm²","type":10}, 
                                    {"name":"平方厘米/cm²","type":11}, 
                                    {"name":"平方米/m²","type":12}, 
                                    {"name":"平方千米/km²","type":13}, 
                                    {"name":"公顷/hm²","type":14}, 
                                    {"name":"天/d","type":15}, 
                                    {"name":"小时/h","type":16}, 
                                    {"name":"分钟/min","type":17}, 
                                    {"name":"秒/s","type":18}, 
                                    {"name":"毫秒/ms","type":19}, 
                                    {"name":"微秒/μs","type":20}, 
                                    {"name":"纳秒/ns","type":21}, 
                                    {"name":"立方毫米/mm³","type":22}, 
                                    {"name":"立方厘米/cm³","type":23}, 
                                    {"name":"立方米/m³","type":24}, 
                                    {"name":"立方千米/km³","type":25}, 
                                    {"name":"立方米每秒/m³/s","type":26}, 
                                    {"name":"立方千米每秒/km³/s","type":27}, 
                                    {"name":"立方厘米每秒/cm³/s","type":28}, 
                                    {"name":"升每秒/l/s","type":29}, 
                                    {"name":"立方米每小时/m³/h","type":30}, 
                                    {"name":"立方千米每小时/km³/h","type":31}, 
                                    {"name":"立方厘米每小时/cm³/h","type":32}, 
                                    {"name":"升每小时/l/h","type":33}, 
                                    {"name":"毫升/mL","type":34}, 
                                    {"name":"升/L","type":35}, 
                                    {"name":"毫克/mg","type":36}, 
                                    {"name":"克/g","type":37}, 
                                    {"name":"千克/kg","type":38}, 
                                    {"name":"吨/t","type":39}, 
                                    {"name":"帕斯卡/Pa","type":40}, 
                                    {"name":"千帕斯卡/kPa","type":41}, 
                                    {"name":"牛顿/N","type":42}, 
                                    {"name":"牛·米/N.m","type":43}, 
                                    {"name":"开尔文/K","type":44}, 
                                    {"name":"摄氏度/℃","type":45}, 
                                    {"name":"华氏度/℉","type":46}, 
                                    {"name":"焦耳/J","type":47}, 
                                    {"name":"卡/cal","type":48}, 
                                    {"name":"瓦特/W","type":49}, 
                                    {"name":"千瓦特/kW","type":50}, 
                                    {"name":"弧度/rad","type":51}, 
                                    {"name":"度/°","type":52}, 
                                    {"name":"[角]分/′","type":53}, 
                                    {"name":"[角]秒/″","type":54}, 
                                    {"name":"赫兹/Hz","type":55}, 
                                    {"name":"兆赫兹/MHz","type":56}, 
                                    {"name":"G赫兹/GHz","type":57}, 
                                    {"name":"米每秒/m/s","type":58}, 
                                    {"name":"千米每小时/km/h","type":59}, 
                                    {"name":"节/kn","type":60}, 
                                    {"name":"伏特/V","type":61}, 
                                    {"name":"千伏/kV","type":62}, 
                                    {"name":"毫伏/mV","type":63}, 
                                    {"name":"微伏/μV","type":64}, 
                                    {"name":"安培/A","type":65}, 
                                    {"name":"毫安/mA","type":67}, 
                                    {"name":"微安/μA","type":68}, 
                                    {"name":"纳安/nA","type":69}, 
                                    {"name":"欧姆/Ω","type":70}, 
                                    {"name":"千欧/KΩ","type":71}, 
                                    {"name":"兆欧/MΩ","type":72}, 
                                    {"name":"电子伏/eV","type":73}, 
                                    {"name":"千瓦·时/kW·h","type":74}, 
                                    {"name":"Kg标准煤/kgce","type":75}]

# add dict details
for i in dict_details:
    req=urllib.request.Request(prefix+suffix_add_dict_detail,
                               data=json.dumps({"isEdit":1,"isDelete":1,"label":i.get("name"),"value":i.get("type"),"dictSort":i.get("type"),"dictId":574}).encode(),
                               headers=headers,
                               method="POST")
    urllib.request.urlopen(req)