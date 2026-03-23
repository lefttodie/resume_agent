# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import StreamingResponse
# import asyncio
# import uuid
# import pandas as pd
# import io

# from agents.job_agent import run_agent
# from enum import Enum

# app = FastAPI(title="Linkedin Recent Job Finder")


# class OutputFormat(str, Enum):
#     csv = "csv"
#     json = "json"


# @app.post("/search-jobs")
# async def search_jobs_api(
#     resume: UploadFile = File(...),
#     output_format: OutputFormat = Form(...)
# ):

#     # Save resume temporarily
#     file_id = str(uuid.uuid4())
#     file_path = f"temp_resume_{file_id}.pdf"

#     with open(file_path, "wb") as f:
#         f.write(await resume.read())

#     # Only LinkedIn jobs now
#     website = {
#         "site": "linkedin"
#     }

#     # Run LangGraph agent
#     jobs = await asyncio.to_thread(run_agent, file_path, website)

#     df = pd.DataFrame(jobs)

#     # Ensure required columns exist
#     columns = [
#         "source",
#         "title",
#         "company",
#         "location",
#         "date_posted",
#         "job_type",
#         "url",
#         "about"
#     ]

#     df = df[columns]

#     buffer = io.StringIO()

#     if output_format == OutputFormat.csv:

#         df.to_csv(buffer, index=False)
#         buffer.seek(0)

#         return StreamingResponse(
#             iter([buffer.getvalue()]),
#             media_type="text/csv",
#             headers={
#                 "Content-Disposition": "attachment; filename=jobs.csv"
#             }
#         )

#     else:

#         df.to_json(buffer, orient="records")
#         buffer.seek(0)

#         return StreamingResponse(
#             iter([buffer.getvalue()]),
#             media_type="application/json",
#             headers={
#                 "Content-Disposition": "attachment; filename=jobs.json"
#             }
#         )





from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
import asyncio
import uuid
import pandas as pd
import io
import os

from agents.job_agent import run_agent
from enum import Enum

app = FastAPI(title="Linkedin Recent Job Finder")


class OutputFormat(str, Enum):
    csv = "csv"
    json = "json"


@app.post("/search-jobs")
async def search_jobs_api(
    resume: UploadFile = File(...),
    output_format: OutputFormat = Form(...)
):

    file_id = str(uuid.uuid4())
    file_path = f"temp_resume_{file_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(await resume.read())

    website = {
        "site": "linkedin",
        "job_type": "job"
    }

    jobs = await asyncio.to_thread(run_agent, file_path, website)

    columns = [
        "source",
        "title",
        "company",
        "location",
        "date_posted",
        "job_type",
        "url",
        "about"
    ]

    df = pd.DataFrame(jobs)

    # SAFE HANDLING (fixes your crash)
    if df.empty:
        df = pd.DataFrame(columns=columns)

    for col in columns:
        if col not in df.columns:
            df[col] = ""

    df = df[columns]

    buffer = io.StringIO()

    if output_format == OutputFormat.csv:

        df.to_csv(buffer, index=False)
        buffer.seek(0)

        return StreamingResponse(
            iter([buffer.getvalue()]),
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=jobs.csv"
            }
        )

    else:

        df.to_json(buffer, orient="records")
        buffer.seek(0)

        return StreamingResponse(
            iter([buffer.getvalue()]),
            media_type="application/json",
            headers={
                "Content-Disposition": "attachment; filename=jobs.json"
            }
        )