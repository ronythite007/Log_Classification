import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from classification import classify
import os

app = FastAPI()

# Serve templates using Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify/")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")

    try:
        # Read CSV file
        df = pd.read_csv(file.file)
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")
        
        # Perform classification
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        # Save the classified dataframe to a CSV file
        output_file = "resources/output.csv"
        df.to_csv(output_file, index=False)

        # Return classified data as JSON and the CSV file path
        return JSONResponse(content={"message": "File classified successfully", "csv_file": output_file, "data": df.to_dict(orient="records")})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()



# uvicorn server:app --reload ---> command to run the server
