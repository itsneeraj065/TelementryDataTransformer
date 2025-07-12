import json, unittest, datetime


with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def iso_to_milliseconds(ts):
    if isinstance(ts, int):
        return ts  
    dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def convertFromFormat1(jsonObject):
    return {
        "deviceID": "dh28dslkja",
        "deviceType": "LaserCutter",
        "timestamp": iso_to_milliseconds(jsonObject["timestamp"]),
        "location": {
            "country": "japan",
            "city": "tokyo",
            "area": "keiyō-industrial-zone",
            "factory": "daikibo-factory-meiyo",
            "section": "section-1"
        },
        "data": {
            "status": "healthy",
            "temperature": 22
        }
    }


def convertFromFormat2(jsonObject):
    jsonObject["timestamp"] = iso_to_milliseconds(jsonObject["timestamp"])

   
    device_info = jsonObject.pop("device", {})
    jsonObject["deviceID"] = device_info.get("id")
    jsonObject["deviceType"] = device_info.get("type")

  
    location_fields = ["country", "city", "area", "factory", "section"]
    location = {field: jsonObject.pop(field) for field in location_fields if field in jsonObject}
    jsonObject["location"] = location

    return jsonObject


def main(jsonObject):
    if isinstance(jsonObject, list):
        return [main(item) for item in jsonObject]
    elif jsonObject.get('device') is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 1 failed')

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 2 failed')

if __name__ == '__main__':
    unittest.main()