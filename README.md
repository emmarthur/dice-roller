# Dice Roller (catalog #456)

Al Sweigart — *The Big Book of Small Python Projects*, Project #18.

| Artifact | Path |
|----------|------|
| Book steps | [`BOOK_DIRECTIONS.md`](./BOOK_DIRECTIONS.md) |
| Upstream script | [`reference/diceroller.py`](./reference/diceroller.py) |
| CLI | [`reference/run_cli.py`](./reference/run_cli.py) |
| Shared logic | [`dice_roller_core.py`](./dice_roller_core.py) |
| Web (FastAPI) | [`web/`](./web/) — port **3022** |

## Run the web demo

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\dice-roller\web"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 3022
```

Open [http://127.0.0.1:3022/](http://127.0.0.1:3022/).

## Run the CLI

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\dice-roller"
python reference\run_cli.py
```

Portfolio: [`PORTFOLIO_INTEGRATION.md`](./PORTFOLIO_INTEGRATION.md).
