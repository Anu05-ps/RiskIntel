try:
    import streamlit as st  # type: ignore
except Exception:
    class _DummySidebar:
        def title(self, *a, **k): pass
        def selectbox(self, *a, **k): return None
        def radio(self, *a, **k): return None
        def markdown(self, *a, **k): pass
        def image(self, *a, **k): pass

    class _DummyST:
        sidebar = _DummySidebar()
        def set_page_config(self, *a, **k): pass
        def error(self, *a, **k): print(*a)
        def stop(self): raise SystemExit
        def title(self, *a, **k): pass
        def subheader(self, *a, **k): pass
        def columns(self, n): return [self for _ in range(n)]
        def metric(self, *a, **k): pass
        def markdown(self, *a, **k): pass
        def write(self, *a, **k): print(*a)
        def selectbox(self, *a, **k): return None
        def dataframe(self, *a, **k): pass
        def plotly_chart(self, *a, **k): pass
        def number_input(self, *a, **k): return 0.0
        def slider(self, *a, **k): return 0.0
        def button(self, *a, **k): return False
        def progress(self, *a, **k): pass
        def success(self, *a, **k): pass
        def tabs(self, tabs): return [self for _ in tabs]

    st = _DummyST()

import pandas as pd
import importlib
import numpy as np
import os
from pathlib import Path

try:
    px = importlib.import_module("plotly.express")
except ImportError:
    class _DummyPX:
        def bar(self, *a, **k): return None
        def scatter(self, *a, **k): return None
    px = _DummyPX()

try:
    sqlalchemy = importlib.import_module("sqlalchemy")
    create_engine = sqlalchemy.create_engine
except ImportError:
    create_engine = None

try:
    joblib = importlib.import_module("joblib")
except ImportError:
    joblib = None


# --------------------------------------------------------------------
# Dynamic Path Auto-Discovery (Fixes OneDrive Execution Displacement)
# --------------------------------------------------------------------
# This locates the exact folder where this active script lives
CURRENT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = CURRENT_DIR.parent

# --------------------------------------------------------------------
# Page configuration
# --------------------------------------------------------------------
st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="wide",
)

# --------------------------------------------------------------------
# Core Visual Interface Framework Styling Engine
# --------------------------------------------------------------------
BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --bg-main: #0e1726;
  --bg-surface: #17223b;
  --bg-panel: #131c2d;
  --text-main: #ffffff;
  --text-muted: rgba(255, 255, 255, 0.78);
  --accent: #60a5fa;
  --accent-soft: rgba(96, 165, 250, 0.18);
  --border: rgba(148, 163, 184, 0.24);
}

body, .stApp {
  font-family: 'Inter', sans-serif;
  background: radial-gradient(circle at top left, rgba(96, 165, 250, 0.16), transparent 30%), var(--bg-main);
  color: var(--text-main);
}

.main > div {
  padding-top: 1.4rem;
}

section[data-testid="stSidebar"] {
  background: #0f172a !important;
  color: var(--text-main) !important;
}
section[data-testid="stSidebar"] * {
  color: var(--text-main) !important;
}

/* Force white text for markdown, tables, widgets, and labels */
div[data-testid="stApp"] *,
section[data-testid="stSidebar"] *,
div[data-testid="stMarkdown"] *,
div[data-testid="stMarkdown"] h1,
div[data-testid="stMarkdown"] h2,
div[data-testid="stMarkdown"] h3,
div[data-testid="stMarkdown"] h4,
div[data-testid="stMarkdown"] h5,
div[data-testid="stMarkdown"] h6,
div[data-testid="stDataFrame"] *,
div[data-testid="stDataFrame"] thead th,
div[data-testid="stDataFrame"] tbody td,
div[data-testid="stTable"] *,
div[data-testid="stTable"] thead th,
div[data-testid="stTable"] tbody td,
.table td,
.table th,
.st-bu,
.st-cs {
  color: var(--text-main) !important;
}

/* Force white text for Plotly chart titles, axis labels, and legend text */
.js-plotly-plot .main-svg text,
.js-plotly-plot .legendtext,
.js-plotly-plot .gtitle,
.js-plotly-plot .gaxis .gline,
.js-plotly-plot .gaxis .gtick text,
.js-plotly-plot .gaxis .title,
.js-plotly-plot .axistext,
.js-plotly-plot .ticktext {
  fill: #ffffff !important;
  color: #ffffff !important;
}

.js-plotly-plot .legend { color: #ffffff !important; }

div[data-testid="stDataFrame"] {
  border-color: rgba(148, 163, 184, 0.14) !important;
  background: var(--bg-panel) !important;
}

div[data-testid="stDataFrame"] table,
div[data-testid="stDataFrame"] th,
div[data-testid="stDataFrame"] td,
div[data-testid="stDataFrame"] thead th,
div[data-testid="stDataFrame"] tbody td,
div[data-testid="stTable"] table,
div[data-testid="stTable"] th,
div[data-testid="stTable"] td,
div[data-testid="stTable"] thead th,
div[data-testid="stTable"] tbody td {
  color: var(--text-main) !important;
  background: transparent !important;
  border-color: rgba(148, 163, 184, 0.18) !important;
}

div[data-testid="stTable"] {
  background: var(--bg-panel) !important;
}

/* Tab Bar Component Styling adjustments */
div[data-testid="stTabs"] button {
  font-size: 14px !important;
  font-weight: 500 !important;
  padding: 0.6rem 1.2rem !important;
  border-bottom: 2px solid transparent !important;
  color: var(--text-muted) !important;
  background: transparent !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
  color: var(--accent) !important;
  font-weight: 600 !important;
  border-bottom: 2px solid var(--accent) !important;
}

/* Premium Main Panel KPI Cards */
.kpi-card {
  background: linear-gradient(180deg, rgba(96, 165, 250, 0.14), rgba(15, 23, 42, 0.95));
  border-radius: 18px;
  padding: 24px 26px;
  border: 1px solid rgba(96, 165, 250, 0.22);
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.3);
  backdrop-filter: blur(14px);
  min-height: 172px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.kpi-card.small {
  padding: 18px 20px;
}
.metric-label {
  color: rgba(255, 255, 255, 0.68) !important;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  margin-bottom: 10px;
}
.metric-value {
  font-weight: 800;
  font-size: 34px;
  color: var(--text-main) !important;
  letter-spacing: -0.04em;
  line-height: 1.05;
  margin-bottom: 6px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.metric-note {
  color: rgba(255, 255, 255, 0.72) !important;
  font-size: 13px;
  margin-top: 4px;
}
.metric-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}
.metric-icon {
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  color: #a5b4fc;
  font-size: 16px;
}
.status-pill {
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.section-hero-note {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.78);
  margin-top: 12px;
  max-width: 820px;
  line-height: 1.65;
}
.footer-bar {
  margin-top: 28px;
  padding: 14px 18px;
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid rgba(96, 165, 250, 0.18);
  color: rgba(255, 255, 255, 0.65);
  font-size: 13px;
  text-align: center;
}

/* Structural Layout Typography Headers */
.section-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-main) !important;
  letter-spacing: -0.02em;
  margin-bottom: 2px;
}
.section-subtitle {
  font-size: 13px;
  color: var(--text-muted) !important;
  margin-bottom: 1.2rem;
}

/* Custom Predictive Alert Notification Blocks */
.assessment-card {
  padding: 18px 22px;
  border-radius: 12px;
  margin-top: 12px;
  font-weight: 500;
  font-size: 14.5px;
  line-height: 1.5;
  background: rgba(15, 23, 42, 0.65);
  border: 1px solid rgba(148, 163, 184, 0.16);
  color: var(--text-main) !important;
}
.assessment-card.danger {
  background-color: rgba(254, 226, 226, 0.16);
  border-left: 4px solid #ef4444;
  color: #f8fafc !important;
}
.assessment-card.danger * { color: #f8fafc !important; }

.assessment-card.success {
  background-color: rgba(220, 252, 231, 0.14);
  border-left: 4px solid #22c55e;
  color: #ecfccb !important;
}
.assessment-card.success * { color: #ecfccb !important; }

/* Wrapper Enclosures for Tables and Plotly Figure Assets */
.dataframe-container {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(148, 163, 184, 0.14);
  background: var(--bg-panel);
  padding: 6px;
}

.chart-card-wrapper {
  background: var(--bg-panel);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 14px;
  padding: 16px;
  margin-bottom: 1rem;
  box-shadow: 0 4px 24px rgba(15, 23, 42, 0.22);
}

div[data-baseweb="select"] > div, input[type="number"] {
  border-radius: 8px !important;
  border-color: rgba(148, 163, 184, 0.24) !important;
  background: #1f2937 !important;
  color: var(--text-main) !important;
}

.stButton>button {
  background: var(--accent);
  color: white !important;
  border-radius: 8px;
  border: none;
  padding: 0.6rem 1.6rem;
  font-weight: 600;
  box-shadow: 0 6px 16px rgba(96, 165, 250, 0.22);
}
.stButton>button:hover {
  background: #2563eb;
}
</style>
"""

st.markdown(BASE_CSS, unsafe_allow_html=True)

# --------------------------------------------------------------------
# Dynamic Core Header Block
# --------------------------------------------------------------------
st.markdown(
    """
    <div style="display:flex; align-items:center; gap:16px; padding:18px 24px; border-radius:14px; background:linear-gradient(135deg,#071528 0%,#10294b 100%); border:1px solid rgba(96,165,250,0.16); box-shadow: 0 8px 40px rgba(0, 0, 0, 0.22); backdrop-filter:blur(10px); margin-bottom:1.5rem;">
      <div style="width:44px; height:44px; border-radius:10px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color:#ffffff; font-size:22px; box-shadow:0 6px 18px rgba(37, 99, 235, 0.28);">🛡️</div>
      <div>
        <div style="font-size:22px; margin:0; color:#ffffff; font-weight:700; letter-spacing:-0.03em;">FraudShield</div>
        <div style="margin:0; color:rgba(255,255,255,0.76); font-size:13px;">Cyber Crime Intelligence • Fraud Detection • Vulnerable Population Analytics</div>
        <div class="section-hero-note">Secure risk intelligence across cybercrime, fraud detection, and vulnerable population analytics — designed for executive review and rapid decisioning.</div>
      </div>
      <div style="flex:1"></div>
      <div>
        <span class="status-pill" style="padding:4px 12px; border-radius:999px; background:rgba(255,255,255,0.08); color:#ffffff; font-size:12px; font-weight:600; border:1px solid rgba(255,255,255,0.12);">v1.4 &middot; Active Engine</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------
# Native Interface Sidebar Controls (Guarantees Text Legibility)
# --------------------------------------------------------------------
sidebar_box = st.sidebar.container()

# Dynamically checking multiple structural parent configurations for branding asset
logo_paths = [
    CURRENT_DIR / "assets" / "logo.png",
    CURRENT_DIR / "logo.png",
    PARENT_DIR / "assets" / "logo.png",
    PARENT_DIR / "logo.png"
]
for p in logo_paths:
    if p.exists():
        try:
            sidebar_box.image(str(p), width=130)
            break
        except Exception:
            pass

sidebar_box.title("FraudShield")
sidebar_box.caption("Operational Analytics Hub")
sidebar_box.markdown("---")

page = st.sidebar.radio(
    "Navigation System Matrix",
    ["Home", "Cyber Crime Intelligence", "Women & Children Safety", "Fraud Detection", "Model Performance"],
    index=0,
)

# --------------------------------------------------------------------
# Absolute Core Data Pipeline (Unaltered Backend Loading Rules)
# --------------------------------------------------------------------
def load_data():
    cyber_df = None
    if create_engine is not None:
        try:
            engine = create_engine("postgresql://postgres:Anusajeev%4028@localhost:5432/fraudshield")
            cyber_df = pd.read_sql("SELECT * FROM cybercrime_india", engine)
        except Exception:
            cyber_df = None

    # Fallback to absolute discoveries
    if cyber_df is None:
        csv_locations = [CURRENT_DIR / "data" / "top_states.csv", PARENT_DIR / "data" / "top_states.csv"]
        for p in csv_locations:
            if p.exists():
                try:
                    cyber_df = pd.read_csv(p)
                    break
                except Exception:
                    cyber_df = None

    vulnerable_df = None
    vulnerable_locations = [CURRENT_DIR / "data" / "vulnerable_population.csv", PARENT_DIR / "data" / "vulnerable_population.csv"]
    for p in vulnerable_locations:
        if p.exists():
            try:
                vulnerable_df = pd.read_csv(p)
                break
            except Exception:
                vulnerable_df = None

    model = None
    model_locations = [CURRENT_DIR / "models" / "random_forest.pkl", PARENT_DIR / "models" / "random_forest.pkl"]
    for p in model_locations:
        if p.exists() and joblib is not None:
            try:
                model = joblib.load(p)
                break
            except Exception:
                model = None

    return cyber_df, vulnerable_df, model


cyber_df, vulnerable_df, model = load_data()

if cyber_df is None:
    st.error("Cybercrime dataset fallback array unresolved. Verify folder placement of top_states.csv")
    st.stop()

def apply_chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=50, b=40),
        font=dict(family="Inter, sans-serif", size=12),
        xaxis=dict(gridcolor="#f1f5f9"),
        yaxis=dict(gridcolor="#f1f5f9")
    )
    return fig

# --------------------------------------------------------------------
# Layout Routing Architecture
# --------------------------------------------------------------------
if page == "Home":
    st.markdown(
        "<div class='section-title'>System Infrastructure Summary</div>"
        "<div class='section-subtitle'>High-level diagnostic trends calculated across state parameters.</div>",
        unsafe_allow_html=True,
    )

    total_crimes = cyber_df["crime_2020"].sum()
    avg_rate = cyber_df["crime_rate"].mean()
    highest_state = cyber_df.loc[cyber_df["crime_2020"].idxmax(), "state"]
    highest_cases = cyber_df["crime_2020"].max()

    total_women = vulnerable_df["Total Cyber Crimes against Women"].sum() if vulnerable_df is not None else 0
    total_children = vulnerable_df["Total Cyber crimes against Children"].sum() if vulnerable_df is not None else 0

    st.markdown(
        f"""
        <div style="display:grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; margin-bottom:1.5rem; align-items: stretch;">
          <div class="kpi-card">
            <div class="metric-top"><div class="metric-label">Total Cyber Crimes</div><div class="metric-icon">💼</div></div>
            <div class="metric-value">{int(total_crimes):,}</div>
            <div class="metric-note">2020 national dataset</div>
          </div>
          <div class="kpi-card">
            <div class="metric-top"><div class="metric-label">Average Crime Rate</div><div class="metric-icon">📈</div></div>
            <div class="metric-value">{avg_rate:.2f}</div>
            <div class="metric-note">Gross mean of all states</div>
          </div>
          <div class="kpi-card">
            <div class="metric-top"><div class="metric-label">Highest Risk State</div><div class="metric-icon">📍</div></div>
            <div class="metric-value">{highest_state}</div>
            <div class="metric-note">Peak absolute exposure</div>
          </div>
          <div class="kpi-card">
            <div class="metric-top"><div class="metric-label">Highest Cases</div><div class="metric-icon">🔥</div></div>
            <div class="metric-value">{int(highest_cases):,}</div>
            <div class="metric-note">Largest single-state volume</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2 = st.columns(2)
    s1.markdown(f"<div class='kpi-card'><div class='metric-label'>Women Cases</div><div class='metric-value'>{int(total_women):,}</div></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='kpi-card'><div class='metric-label'>Children Cases</div><div class='metric-value'>{int(total_children):,}</div></div>", unsafe_allow_html=True)

    st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

elif page == "Cyber Crime Intelligence":
    st.markdown(
        "<div class='section-title'>Cyber Crime Intelligence Analytics</div>"
        "<div class='section-subtitle'>Isolate distribution arrays and geographic parameter loads.</div>",
        unsafe_allow_html=True,
    )

    total_crimes = cyber_df["crime_2020"].sum()
    avg_crime_rate = cyber_df["crime_rate"].mean()
    highest_state = cyber_df.loc[cyber_df["crime_2020"].idxmax(), "state"]
    highest_cases = cyber_df["crime_2020"].max()

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f"<div class='kpi-card'><div class='metric-label'>Total Crimes</div><div class='metric-value'>{int(total_crimes):,}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='kpi-card'><div class='metric-label'>Mean Crime Rate</div><div class='metric-value'>{round(avg_crime_rate,2)}</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='kpi-card'><div class='metric-label'>Peak State Boundary</div><div class='metric-value'>{highest_state}</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='kpi-card'><div class='metric-label'>Peak Case Mass</div><div class='metric-value'>{int(highest_cases):,}</div></div>", unsafe_allow_html=True)

    st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

    tab_inspect, tab_charts = st.tabs(["🔍 Granular Territory Inspection", "📊 Structural Distribution Visuals"])

    with tab_inspect:
        st.markdown("<p style='font-size:14px; font-weight:500; margin-top:8px;'>Isolate Regional Metrics</p>", unsafe_allow_html=True)
        state = st.selectbox("Select Target State Parameter", cyber_df["state"].unique())
        selected = cyber_df[cyber_df["state"] == state]
        st.markdown("<div class='dataframe-container'>", unsafe_allow_html=True)
        st.dataframe(selected, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_charts:
        top_states = cyber_df.sort_values(by="crime_2020", ascending=False).head(10)
        
        st.markdown("<div class='chart-card-wrapper'>", unsafe_allow_html=True)
        fig1 = px.bar(top_states, x="state", y="crime_2020", title="Top 10 Regions by Absolute Case Load")
        st.plotly_chart(apply_chart_theme(fig1), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='chart-card-wrapper'>", unsafe_allow_html=True)
        fig2 = px.bar(cyber_df.sort_values(by="crime_rate", ascending=False).head(10), x="state", y="crime_rate", title="Top Regions classified by Crime Intensity Rate")
        st.plotly_chart(apply_chart_theme(fig2), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Women & Children Safety":
    st.markdown(
        "<div class='section-title'>Vulnerable Populations Risk Matrix</div>"
        "<div class='section-subtitle'>Statistical profiling prioritizing demographic tracking parameters.</div>",
        unsafe_allow_html=True,
    )

    if vulnerable_df is None:
        st.error("vulnerable_population.csv data frame missing.")
    else:
        total_women = vulnerable_df["Total Cyber Crimes against Women"].sum()
        total_children = vulnerable_df["Total Cyber crimes against Children"].sum()
        highest_state = vulnerable_df.loc[vulnerable_df["Vulnerable_Population_Index"].idxmax(), "State"]
        highest_score = vulnerable_df["Vulnerable_Population_Index"].max()

        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f"<div class='kpi-card'><div class='metric-label'>Threat Load: Women</div><div class='metric-value'>{int(total_women):,}</div></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='kpi-card'><div class='metric-label'>Threat Load: Children</div><div class='metric-value'>{int(total_children):,}</div></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='kpi-card'><div class='metric-label'>Highest Threat Index Target</div><div class='metric-value'>{highest_state}</div></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='kpi-card'><div class='metric-label'>Calculated Risk Factor Peak</div><div class='metric-value'>{int(highest_score)}</div></div>", unsafe_allow_html=True)

        st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

        tab_plots, tab_data = st.tabs(["📊 Covariance Graphic Vectors", "📋 Structural Regional Auditing"])

        with tab_plots:
            st.markdown("<div class='chart-card-wrapper'>", unsafe_allow_html=True)
            fig3 = px.bar(vulnerable_df.sort_values(by="Vulnerable_Population_Index", ascending=False).head(10), x="State", y="Vulnerable_Population_Index", title="Primary Vulnerability Interception Zones")
            st.plotly_chart(apply_chart_theme(fig3), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='chart-card-wrapper'>", unsafe_allow_html=True)
            fig4 = px.scatter(vulnerable_df, x="Total Cyber Crimes against Women", y="Total Cyber crimes against Children", hover_name="State", title="Demographic Co-variance Dispersion Graph")
            st.plotly_chart(apply_chart_theme(fig4), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with tab_data:
            state = st.selectbox("Select Target Filter Boundary", vulnerable_df["State"].unique())
            selected = vulnerable_df[vulnerable_df["State"] == state]
            st.markdown("<div class='dataframe-container'>", unsafe_allow_html=True)
            st.dataframe(selected, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif page == "Model Performance":
    st.markdown(
        "<div class='section-title'>Model Performance & Feature Importance</div>"
        "<div class='section-subtitle'>Trusted Random Forest metrics with the top predictive variables.</div>",
        unsafe_allow_html=True,
    )

    perf_col1, perf_col2 = st.columns([1.4, 1])
    with perf_col1:
        st.markdown("<div class='kpi-card'><div class='metric-label'>Random Forest</div><div class='metric-value'>Production Grade</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='kpi-card'><div class='metric-label'>Precision</div><div class='metric-value'>93%</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='kpi-card'><div class='metric-label'>Recall</div><div class='metric-value'>81%</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='kpi-card'><div class='metric-label'>ROC-AUC</div><div class='metric-value'>0.903</div></div>", unsafe_allow_html=True)

    with perf_col2:
        st.markdown("<div class='kpi-card'><div class='metric-label'>Top Features</div><div class='metric-value' style='font-size:16px; line-height:1.6; color:#ffffff;'>V17<br>V14<br>V12<br>V10<br>V16</div></div>", unsafe_allow_html=True)

    st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

elif page == "Fraud Detection":
    st.markdown(
        "<div class='section-title'>Automated Transaction Machine Learning Unit</div>"
        "<div class='section-subtitle'>Real-time inference profiling against transaction vector components.</div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='kpi-card'><div class='metric-label'>Model Precision Score</div><div class='metric-value'>93.00%</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='kpi-card'><div class='metric-label'>Model Recall Score</div><div class='metric-value'>81.00%</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='kpi-card'><div class='metric-label'>Area Under ROC Curve (AUC)</div><div class='metric-value'>0.903</div></div>", unsafe_allow_html=True)

    st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Telemetry Variable Adjustment Frame</div>", unsafe_allow_html=True)

    c_left, c_mid, c_right = st.columns([1.2, 1, 1])
    with c_left:
        amount = st.number_input("Transaction Volume Vector (Amount)", min_value=0.0, value=100.0)
    with c_mid:
        v14 = st.slider("Component Parameter V14", -20.0, 20.0, 0.0)
    with c_right:
        v17 = st.slider("Component Parameter V17", -20.0, 20.0, 0.0)

    st.markdown("")
    analyze = st.button("Execute Mathematical Threat Scan")

    if analyze:
        if model is None:
            st.error("Model engine file path resolving error.")
        else:
            sample = np.zeros((1, 30))
            sample[0, 28] = amount
            sample[0, 13] = v14
            sample[0, 16] = v17

            prediction = model.predict(sample)[0]
            probability = model.predict_proba(sample)[0][1]

            st.markdown('<hr class="app-section-divider" />', unsafe_allow_html=True)

            st.markdown(
                "<div class='section-title'>Inference Engine Output Analysis</div>"
                "<div class='section-subtitle'>Statistical anomaly evaluation mapping from provided parameters.</div>",
                unsafe_allow_html=True,
            )

            st.metric("Calculated Structural Anomaly Probability", f"{probability*100:.2f}%")
            st.progress(float(probability))

            if prediction == 1:
                st.markdown(
                    "<div class='assessment-card danger'><strong>🚨 SEC_ALERT_HIGH:</strong> Anomalous Anomaly Flag Triggered. Parameters line up within critical threat matrix deviations. Immediate hold suggested.</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div class='assessment-card success'><strong>🛡️ STATUS_OK:</strong> Transaction features fit cleanly within typical variance models. No risk vector detected.</div>",
                    unsafe_allow_html=True
                )

st.markdown(
    "<div class='footer-bar'>FraudShield • v1.4 • Data: 2020 national dataset • Secure analytics dashboard</div>",
    unsafe_allow_html=True,
)
