from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (you can restrict to specific origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can change it to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
app = FastAPI()

# Load student data from JSON file
students =[{"name":"e0liRoERS","marks":95},{"name":"UI","marks":27},{"name":"xdk","marks":50},{"name":"MoTGkQDI","marks":29},{"name":"ZWn45mh","marks":43},{"name":"j","marks":72},{"name":"TBu5224","marks":6},{"name":"iVS87O2","marks":97},{"name":"ywG","marks":50},{"name":"hs2bpukb","marks":1},{"name":"W4O7bAJZHi","marks":67},{"name":"As6u8","marks":16},{"name":"qxPAqF","marks":62},{"name":"0o","marks":2},{"name":"UCPsqN","marks":41},{"name":"y6z","marks":54},{"name":"Rl4UE","marks":86},{"name":"Fn9TKmu","marks":91},{"name":"UGfD4QR","marks":37},{"name":"Hlro","marks":92},{"name":"p","marks":96},{"name":"xColj6En","marks":33},{"name":"LbkSh2ar","marks":83},{"name":"tI8jD56z","marks":29},{"name":"p3TcfdUFPR","marks":6},{"name":"BakNi0iA","marks":8},{"name":"YPDRr9","marks":48},{"name":"Mktj8U","marks":40},{"name":"8z4F","marks":34},{"name":"dLoOr","marks":69},{"name":"Tyd","marks":60},{"name":"SMSV","marks":97},{"name":"rUCy7T8uY","marks":36},{"name":"qCqLW5","marks":65},{"name":"jrJjrpobR","marks":93},{"name":"602mAmrNML","marks":41},{"name":"6vnbvU","marks":84},{"name":"LQd","marks":13},{"name":"H","marks":26},{"name":"VojuzgrQ","marks":53},{"name":"C3kz","marks":67},{"name":"W7E","marks":65},{"name":"a6EQ","marks":4},{"name":"guFi5","marks":42},{"name":"Ro7CLt8jb","marks":58},{"name":"LgTpQ","marks":96},{"name":"y","marks":2},{"name":"bSAkqHb1T","marks":51},{"name":"7uleB6","marks":67},{"name":"Oc","marks":2},{"name":"wwlQlTZ","marks":71},{"name":"pDlPzy","marks":88},{"name":"h","marks":35},{"name":"RrKHlL2zQ2","marks":82},{"name":"Bq","marks":26},{"name":"f8zfm5zq","marks":6},{"name":"awSQo","marks":31},{"name":"eN3MSeVrti","marks":41},{"name":"JbXgAp2J88","marks":58},{"name":"2C0Kn","marks":84},{"name":"D","marks":2},{"name":"d","marks":84},{"name":"D1","marks":76},{"name":"wPwsshvCm","marks":1},{"name":"co75o9ry","marks":67},{"name":"PrHrm","marks":19},{"name":"IQKRL","marks":64},{"name":"u","marks":77},{"name":"xh68twQT8","marks":65},{"name":"0pvPcoB4","marks":54},{"name":"auOLzTxIiu","marks":31},{"name":"5jVwlK","marks":98},{"name":"mWWsGLJ","marks":58},{"name":"Zco","marks":11},{"name":"up5xb5xPr","marks":51},{"name":"ugKXJuFZ5","marks":51},{"name":"Srn","marks":29},{"name":"S","marks":89},{"name":"Zn","marks":68},{"name":"A7","marks":58},{"name":"GNQw8NU","marks":99},{"name":"4CAIe","marks":83},{"name":"uvx","marks":73},{"name":"Nj6kz","marks":49},{"name":"atarlGDOu","marks":54},{"name":"wwl3","marks":54},{"name":"CIWIs","marks":35},{"name":"n","marks":31},{"name":"qNe0","marks":4},{"name":"Qh8AkIH","marks":52},{"name":"c8HEv7","marks":55},{"name":"mP","marks":78},{"name":"aggO1Mru","marks":93},{"name":"byK7TBY7","marks":14},{"name":"zKcn","marks":91},{"name":"7Bsk","marks":91},{"name":"8LSA","marks":66},{"name":"dFN0kdCcQC","marks":93},{"name":"metqioVIsR","marks":4},{"name":"7vLxEl","marks":77}]
name_to_marks = {item["name"]: item["marks"] for item in students}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """
    Endpoint to retrieve marks for multiple names in order
    """
    result = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
