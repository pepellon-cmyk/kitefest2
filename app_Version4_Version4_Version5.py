# DEBUG: adicionar para diagnosticar falha de import plotly — remover após resolver
import sys, traceback, importlib, importlib.util, os

def _debug_plotly_import():
    try:
        import plotly
        print("DEBUG: plotly import OK:", getattr(plotly, "__version__", "unknown"))
        return
    except Exception as e:
        print("DEBUG: plotly import FAILED:", repr(e))
        traceback.print_exc()

    print("DEBUG: sys.executable:", sys.executable)
    print("DEBUG: sys.path:")
    for p in sys.path:
        print("  -", p)
    spec = importlib.util.find_spec("plotly")
    print("DEBUG: plotly spec:", spec)

    # procurar ficheiros/pastas que possam causar shadowing (plotly.py, plotly/)
    try:
        for p in sys.path:
            if not p or not os.path.isdir(p):
                continue
            try:
                entries = [e for e in os.listdir(p) if e.lower().startswith("plotly")]
                if entries:
                    print(f"DEBUG: possíveis entradas 'plotly*' em {p}: {entries}")
            except Exception:
                pass
    except Exception as ex:
        print("DEBUG: erro ao procurar shadowing:", ex)

_debug_plotly_import()
# FIM DEBUG
