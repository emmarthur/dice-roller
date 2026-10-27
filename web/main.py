"""
FastAPI app — D&D-style dice roller.

Run: uvicorn main:app --reload --port 3022
"""

from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

_DEMO_ROOT = Path(__file__).resolve().parent.parent
if str(_DEMO_ROOT) not in sys.path:
    sys.path.insert(0, str(_DEMO_ROOT))

from dice_roller_core import example_notations, roll_notation  # noqa: E402

app = FastAPI(title="Dice Roller")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")


class RollRequest(BaseModel):
    notation: str = Field(..., min_length=1, max_length=32)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"examples": example_notations()},
    )


@app.get("/help", response_class=HTMLResponse)
async def help_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "help.html")


@app.post("/api/roll")
async def api_roll(body: RollRequest) -> JSONResponse:
    try:
        return JSONResponse(roll_notation(body.notation))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
