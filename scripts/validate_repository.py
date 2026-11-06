"""Validación offline del repositorio; no accede a proveedores externos."""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path

import nbformat
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "CAPM_IBEX35_CSV_TR_BCE.ipynb"
CSV = ROOT / "data" / "ibex35_total_return_investing.csv"


def load_csv() -> pd.Series:
    df = pd.read_csv(CSV, encoding="utf-8-sig", sep=",", engine="python")
    df.columns = (
        df.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.replace('"', "", regex=False)
        .str.strip()
    )
    required = {"Fecha", "Último"}
    assert required <= set(df.columns), f"Faltan columnas: {required - set(df.columns)}"
    fechas = pd.to_datetime(df["Fecha"].astype(str), format="%d.%m.%Y", errors="coerce")
    valores = pd.to_numeric(
        df["Último"].astype(str)
        .str.replace("\u00a0", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False),
        errors="coerce",
    )
    prices = pd.Series(valores.to_numpy(), index=fechas, name="IBEX35_TR")
    if prices.index.hasnans or prices.isna().any():
        raise AssertionError("Fechas o precios inválidos en el CSV")
    if prices.index.has_duplicates:
        raise AssertionError("Fechas duplicadas en el CSV")
    if (prices <= 0).any():
        raise AssertionError("Hay precios no positivos")
    return prices.sort_index()


def validate() -> None:
    assert NOTEBOOK.is_file(), f"No existe el notebook {NOTEBOOK}"
    assert CSV.is_file(), f"No existe el CSV {CSV}"
    n = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(n)
    assert sum(cell.cell_type == "code" for cell in n.cells) == 8, "Faltan celdas originales de código"
    for i, cell in enumerate(n.cells):
        if cell.cell_type == "code":
            ast.parse(cell.source, filename=f"notebook_cell_{i}")
            assert not cell.outputs, f"Celda {i} contiene salidas previas"
    joined = "\n".join(c.source for c in n.cells)
    for token in ("CSV_INVESTING", "IBEX35_TR", "RF_PRESET", "Ke_rf_actual", "rolling_capm", "IBEXHeatmapExtractor", "plot_sml"):
        assert token in joined, f"Falta componente clave: {token}"
    assert 'Path("/content/Datos históricos' not in n.cells[2].source.split('CSV_CANDIDATES = [')[0], "Ruta exclusiva Colab"
    prices = load_csv()
    assert len(prices) == 3102, f"Se esperaban 3102 cotizaciones, hay {len(prices)}"
    assert prices.index.min() == pd.Timestamp("2014-10-06")
    assert prices.index.max() == pd.Timestamp("2026-11-06")
    monthly = prices.resample("ME").last()
    assert len(monthly) == 146, "Cierres mensuales esperados de octubre 2014 a noviembre 2026"
    complete = monthly.loc[monthly.index <= pd.Timestamp("2026-10-31")]
    assert len(complete) == 145
    assert complete.notna().all()
    digest = hashlib.sha256(CSV.read_bytes()).hexdigest()
    print("VALIDACIÓN OFFLINE SUPERADA")
    print(f"Notebook: {len(n.cells)} celdas ({sum(c.cell_type=='code' for c in n.cells)} de código), todas parseables")
    print(f"CSV: {len(prices)} cotizaciones, {complete.size} cierres mensuales completos hasta octubre 2026")
    print(f"CSV SHA256: {digest}")
    print("Nota: descargas Yahoo, BCE y MarketScreener NO verificadas")


if __name__ == "__main__":
    validate()
