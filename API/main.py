from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data = "aaa"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name,last_name, address):
    data = "{} {} {}".format(name, last_name, address)
    return data

@app.get("/velocity")
def velocity(s, t):
    v=float(s) /float(t)
    data  = "v= {:.2f}".format(v) 
    return data 

@app.get("/resistor")
def resistor(r1, r2, r3):
    rt_series = float(r1) + float(r2) + float(r3)
    rt_pararell = ((1/float(r1)) + (1/float(r2)) + (1/float(r3))**-1)
    data = "rt series = {:.2f}".format(rt_series), "rt pararell = {:.2f}".format(rt_pararell)
    return data

print ("test")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)          