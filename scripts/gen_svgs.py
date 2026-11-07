"""Generate the profile README SVG assets (banner, stats card, AtliQ architecture).

Writes a dark and a light variant of each SVG; the README picks one with
<picture> + prefers-color-scheme so the cards match the viewer's GitHub theme.

Usage: python scripts/gen_svgs.py assets
"""
import sys
from pathlib import Path

FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
BG0, BG1 = "#0d1117", "#161b22"
BORDER = "#30363d"
TEXT, MUTED = "#e6edf3", "#8b949e"
ACCENT = "#3ecf8e"

W = 1000
MARGIN = 48
COLS = 6
NODE_W = 118
STEP = (W - 2 * MARGIN - NODE_W) / (COLS - 1)  # 154.8


def col_x(i: int) -> float:
    return MARGIN + i * STEP


def defs(extra: str = "") -> str:
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
  </linearGradient>
  <radialGradient id="glow" cx="85%" cy="0%" r="60%">
    <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.18"/>
    <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="1.5" cy="1.5" r="1" fill="{DOT}" fill-opacity="0.05"/>
  </pattern>
  <linearGradient id="flow" gradientUnits="userSpaceOnUse" x1="{MARGIN}" y1="0" x2="{W - MARGIN}" y2="0">
    <stop offset="0%" stop-color="#58a6ff"/>
    <stop offset="35%" stop-color="#cd7f32"/>
    <stop offset="55%" stop-color="#c9d1d9"/>
    <stop offset="75%" stop-color="#e3b341"/>
    <stop offset="100%" stop-color="{ACCENT}"/>
  </linearGradient>
  {extra}
</defs>"""


def frame(h: int) -> str:
    return (
        f'<rect width="{W}" height="{h}" rx="16" fill="url(#bg)"/>\n'
        f'<rect width="{W}" height="{h}" rx="16" fill="url(#dots)"/>\n'
        f'<rect width="{W}" height="{h}" rx="16" fill="url(#glow)"/>\n'
        f'<rect x="0.75" y="0.75" width="{W-1.5}" height="{h-1.5}" rx="15.5" fill="none" stroke="{BORDER}" stroke-width="1.5"/>'
    )


def pipeline(y: float, nodes, h: int = 56, dots: int = 3, dur: float = 6.0, line_id: str = "p") -> str:
    """A row of nodes on a shared line, with animated dots flowing left to right."""
    cy = y + h / 2
    x0, x1 = col_x(0) + 10, col_x(COLS - 1) + NODE_W - 10
    out = [
        f'<path id="{line_id}" d="M{x0},{cy} L{x1},{cy}" stroke="url(#flow)" stroke-width="2.5" stroke-dasharray="5 4" opacity="0.9" fill="none"/>'
    ]
    for k in range(dots):
        begin = -k * dur / dots
        out.append(
            f'<circle r="4" fill="{ACCENT}"><animateMotion dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite">'
            f'<mpath href="#{line_id}" xlink:href="#{line_id}"/></animateMotion></circle>'
        )
    for i, (title, sub, color) in enumerate(nodes):
        x = col_x(i)
        out.append(
            f'<rect x="{x:.1f}" y="{y}" width="{NODE_W}" height="{h}" rx="10" fill="{BG0}" stroke="{color}" stroke-width="1.5"/>'
            f'<text x="{x + NODE_W/2:.1f}" y="{y + h/2 - 3:.1f}" font-family="{FONT}" font-size="14" font-weight="700" fill="{color}" text-anchor="middle">{title}</text>'
            f'<text x="{x + NODE_W/2:.1f}" y="{y + h/2 + 15:.1f}" font-family="{FONT}" font-size="11" fill="{MUTED}" text-anchor="middle">{sub}</text>'
        )
    return "\n".join(out)


BLUE, BRONZE, SILVER, GOLD, PURPLE = "#58a6ff", "#cd7f32", "#c9d1d9", "#e3b341", "#bc8cff"
DOT = "#ffffff"


def banner() -> str:
    h = 290
    nodes = [
        ("Sources", "Azure SQL · CSV", BLUE),
        ("Ingest", "ADF · Kafka", PURPLE),
        ("Bronze", "raw Delta", BRONZE),
        ("Silver", "Databricks · Spark", SILVER),
        ("Gold", "dbt · tested", GOLD),
        ("Insight", "Tableau · Power BI", ACCENT),
    ]
    pill_text = "Open to Tableau Developer &amp; Analytics Engineer roles"
    pill_w = 48 + int(len(pill_text.replace("&amp;", "&")) * 7.3)
    pill_x = W - MARGIN - pill_w
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="t d">
<title id="t">Jaideep Gupta: Tableau Developer, Analytics &amp; Data Engineering</title>
<desc id="d">Animated data pipeline from sources through ingestion, bronze, silver and gold layers to Tableau and Power BI dashboards.</desc>
{defs()}
{frame(h)}
<text x="{MARGIN}" y="72" font-family="{FONT}" font-size="15" fill="{MUTED}">Hi, I'm</text>
<text x="{MARGIN}" y="114" font-family="{FONT}" font-size="40" font-weight="800" fill="{TEXT}">Jaideep Gupta</text>
<text x="{MARGIN}" y="146" font-family="{FONT}" font-size="19" font-weight="600" fill="{ACCENT}">Tableau Developer <tspan fill="{MUTED}">·</tspan> Analytics Engineering</text>
<text x="{MARGIN}" y="174" font-family="{FONT}" font-size="14" fill="{MUTED}">4+ years of BI · now building the pipelines that feed the dashboards.</text>

<rect x="{pill_x}" y="46" width="{pill_w}" height="32" rx="16" fill="{ACCENT}" fill-opacity="0.08" stroke="{ACCENT}" stroke-opacity="0.6"/>
<circle cx="{pill_x + 20}" cy="62" r="4.5" fill="{ACCENT}"/>
<circle cx="{pill_x + 20}" cy="62" r="4.5" fill="none" stroke="{ACCENT}">
  <animate attributeName="r" values="4.5;10" dur="1.8s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.8;0" dur="1.8s" repeatCount="indefinite"/>
</circle>
<text x="{pill_x + 34}" y="67" font-family="{FONT}" font-size="13" font-weight="600" fill="{TEXT}">{pill_text}</text>

{pipeline(204, nodes, line_id="bannerflow")}
</svg>
"""


def stats() -> str:
    h = 116
    tiles = [
        ("4+ yrs", "BI &amp; analytics"),
        ("50+", "dashboards shipped"),
        ("40+", "stakeholders served"),
        ("8 → 3 min", "report generation time"),
    ]
    gap = 16
    tw = (W - gap * (len(tiles) - 1)) / len(tiles)
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="4+ years in BI and analytics; 50+ dashboards shipped; 40+ stakeholders served; report generation cut from 8 to 3 minutes">',
        defs(),
    ]
    for i, (big, label) in enumerate(tiles):
        x = i * (tw + gap)
        out.append(
            f'<rect x="{x + 0.75:.1f}" y="0.75" width="{tw - 1.5:.1f}" height="{h - 1.5}" rx="14" fill="url(#bg)" stroke="{BORDER}" stroke-width="1.5"/>'
            f'<rect x="{x + 24:.1f}" y="24" width="28" height="4" rx="2" fill="{ACCENT}"/>'
            f'<text x="{x + 24:.1f}" y="68" font-family="{FONT}" font-size="30" font-weight="800" fill="{TEXT}">{big}</text>'
            f'<text x="{x + 24:.1f}" y="94" font-family="{FONT}" font-size="13" fill="{MUTED}">{label}</text>'
        )
    out.append("</svg>")
    return "\n".join(out)


def atliq() -> str:
    h = 400
    batch = [
        ("Azure SQL", "OLTP · CSV", BLUE),
        ("ADF", "metadata-driven", PURPLE),
        ("Bronze", "ADLS Gen2", BRONZE),
        ("Silver", "Spark MERGE", SILVER),
        ("Gold", "dbt star schema", GOLD),
        ("Power BI", "Microsoft Fabric", ACCENT),
    ]
    stream = [
        ("Producer", "order events", BLUE),
        ("Kafka", "topic", PURPLE),
        ("Bronze", "stream ingest", BRONZE),
        ("Silver", "watermark · dedup", SILVER),
        ("Gold", "streaming aggs", GOLD),
        ("Airflow", "DAG ops", ACCENT),
    ]
    foot_y = 330
    chips = ["GitHub Actions CI", "13 dbt models · 18 tests", "Unity Catalog", "idempotent re-runs", "revenue reconciliation"]
    chip_out = []
    cx = MARGIN
    for c in chips:
        w = 16 + len(c) * 7.1
        chip_out.append(
            f'<rect x="{cx:.1f}" y="{foot_y}" width="{w:.1f}" height="28" rx="14" fill="{BG0}" stroke="{BORDER}"/>'
            f'<text x="{cx + w/2:.1f}" y="{foot_y + 18.5}" font-family="{FONT}" font-size="12" fill="{TEXT}" text-anchor="middle">{c}</text>'
        )
        cx += w + 10
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="t d">
<title id="t">AtliQ Commerce architecture</title>
<desc id="d">Batch lane: Azure SQL to Azure Data Factory to Bronze on ADLS Gen2, Silver on Databricks, Gold in dbt, served in Power BI on Microsoft Fabric. Streaming lane: Kafka producer and topic to Structured Streaming bronze, silver and gold, operated by Airflow. CI with GitHub Actions gated on dbt tests.</desc>
{defs()}
{frame(h)}
<text x="{MARGIN}" y="44" font-family="{FONT}" font-size="18" font-weight="700" fill="{TEXT}">AtliQ Commerce <tspan fill="{MUTED}" font-weight="400">· end-to-end data platform</tspan></text>

<text x="{MARGIN}" y="88" font-family="{MONO}" font-size="12" font-weight="700" fill="{BLUE}">BATCH · nightly</text>
{pipeline(100, batch, line_id="batch", dur=7)}

<text x="{MARGIN}" y="208" font-family="{MONO}" font-size="12" font-weight="700" fill="{ACCENT}">STREAMING · real-time</text>
{pipeline(220, stream, line_id="stream", dur=3.5, dots=4)}

<line x1="{MARGIN}" y1="306" x2="{W - MARGIN}" y2="306" stroke="{BORDER}"/>
{"".join(chip_out)}
</svg>
"""


THEMES = {
    "dark": dict(BG0="#0d1117", BG1="#161b22", BORDER="#30363d", TEXT="#e6edf3", MUTED="#8b949e",
                 ACCENT="#3ecf8e", BLUE="#58a6ff", BRONZE="#cd7f32", SILVER="#c9d1d9",
                 GOLD="#e3b341", PURPLE="#bc8cff", DOT="#ffffff"),
    "light": dict(BG0="#ffffff", BG1="#f6f8fa", BORDER="#d0d7de", TEXT="#1f2328", MUTED="#59636e",
                  ACCENT="#1a7f37", BLUE="#0969da", BRONZE="#a0522d", SILVER="#57606a",
                  GOLD="#9a6700", PURPLE="#8250df", DOT="#000000"),
}


def apply_theme(name: str) -> None:
    globals().update(THEMES[name])


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for theme, suffix in (("dark", ""), ("light", "-light")):
        apply_theme(theme)
        for name, fn in (("profile-banner", banner), ("stats", stats), ("atliq-architecture", atliq)):
            (out / f"{name}{suffix}.svg").write_text(fn(), encoding="utf-8")
    print("wrote", sorted(p.name for p in out.iterdir()))
