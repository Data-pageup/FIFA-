<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>World Cup 2026 Predictor</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0C0C0C;
    --surface: #141414;
    --surface2: #1C1C1C;
    --border: rgba(255,255,255,0.08);
    --border-hover: rgba(255,255,255,0.16);
    --text: #F0F0F0;
    --text-muted: #888;
    --text-dim: #555;
    --green: #1D9E75;
    --green-light: #5DCAA5;
    --green-glow: rgba(29,158,117,0.15);
    --blue: #3D7EF0;
    --amber: #F0A030;
    --red: #E24B4A;
    --purple: #8B7EDD;
    --mono: 'JetBrains Mono', monospace;
    --sans: 'Inter', sans-serif;
  }

  body {
    font-family: var(--sans);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    min-height: 100vh;
  }

  /* ── LAYOUT ── */
  .page { max-width: 1100px; margin: 0 auto; padding: 0 2rem 5rem; }

  /* ── HERO ── */
  .hero {
    padding: 5rem 0 4rem;
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -60px; left: -60px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(29,158,117,0.12) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-eyebrow {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--green-light);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: var(--green-light);
  }
  .hero h1 {
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 300;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: var(--text);
    margin-bottom: 1.2rem;
  }
  .hero h1 strong { font-weight: 600; color: #fff; }
  .hero-desc {
    font-size: 1.05rem;
    color: var(--text-muted);
    max-width: 560px;
    font-weight: 300;
    margin-bottom: 2.5rem;
    line-height: 1.7;
  }
  .hero-stats {
    display: flex;
    gap: 2.5rem;
    flex-wrap: wrap;
  }
  .stat-item { }
  .stat-num {
    font-family: var(--mono);
    font-size: 1.8rem;
    font-weight: 500;
    color: #fff;
    line-height: 1;
  }
  .stat-lbl {
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 0.5px;
    margin-top: 4px;
    text-transform: uppercase;
  }

  /* ── SECTION ── */
  section { padding: 4rem 0; border-bottom: 1px solid var(--border); }
  section:last-child { border-bottom: none; }
  .sec-label {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-dim);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .sec-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }
  .sec-title {
    font-size: 1.6rem;
    font-weight: 400;
    letter-spacing: -0.5px;
    color: #fff;
    margin-bottom: 0.6rem;
  }
  .sec-sub {
    color: var(--text-muted);
    font-size: 0.95rem;
    font-weight: 300;
    margin-bottom: 2.5rem;
    max-width: 540px;
  }

  /* ── WINNER BAND ── */
  .winner-band {
    background: linear-gradient(135deg, #0d2f24 0%, #0f3d2c 50%, #092820 100%);
    border: 1px solid rgba(29,158,117,0.3);
    border-radius: 16px;
    padding: 2.5rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
  }
  .winner-band::before {
    content: '';
    position: absolute;
    top: -30px; right: -30px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(29,158,117,0.2) 0%, transparent 70%);
  }
  .trophy-icon { font-size: 3rem; flex-shrink: 0; }
  .winner-info { flex: 1; }
  .winner-tag {
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--green-light);
    margin-bottom: 6px;
    display: block;
  }
  .winner-name { font-size: 2rem; font-weight: 500; color: #fff; letter-spacing: -0.5px; margin-bottom: 6px; }
  .winner-meta { font-size: 13px; color: rgba(93,202,165,0.7); }
  .winner-prob {
    font-family: var(--mono);
    font-size: 3rem;
    font-weight: 500;
    color: var(--green-light);
    flex-shrink: 0;
  }
  .winner-prob span { font-size: 1rem; color: var(--green); margin-left: 2px; }

  /* ── TEAM BARS ── */
  .team-list { display: flex; flex-direction: column; gap: 8px; }
  .team-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    transition: border-color 0.2s, background 0.2s;
    cursor: default;
  }
  .team-row:hover { border-color: var(--border-hover); background: var(--surface2); }
  .rank { font-family: var(--mono); font-size: 12px; color: var(--text-dim); width: 20px; text-align: right; flex-shrink: 0; }
  .team-flag { font-size: 20px; flex-shrink: 0; }
  .team-name { font-size: 14px; font-weight: 500; color: var(--text); width: 110px; flex-shrink: 0; }
  .conf-pill {
    font-size: 9px;
    padding: 2px 8px;
    border-radius: 20px;
    font-family: var(--mono);
    letter-spacing: 0.5px;
    flex-shrink: 0;
  }
  .bar-track { flex: 1; height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
  .bar-fill { height: 100%; border-radius: 2px; transition: width 0.8s ease; }
  .prob-val { font-family: var(--mono); font-size: 13px; font-weight: 500; color: var(--text); width: 42px; text-align: right; flex-shrink: 0; }

  /* ── METHODOLOGY STEPS ── */
  .steps { display: flex; flex-direction: column; gap: 0; }
  .step {
    display: flex;
    gap: 20px;
    align-items: flex-start;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--border);
    position: relative;
  }
  .step:last-child { border-bottom: none; }
  .step-icon-wrap {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }
  .step-num-badge {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-dim);
    position: absolute;
    left: -24px;
    top: 1.75rem;
    display: none;
  }
  .step-body { flex: 1; }
  .step-title { font-size: 15px; font-weight: 500; color: #fff; margin-bottom: 4px; }
  .step-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; }
  .step-tag {
    display: inline-block;
    font-family: var(--mono);
    font-size: 9px;
    padding: 2px 7px;
    border-radius: 4px;
    margin-top: 8px;
    border: 1px solid;
  }

  /* ── PIPELINE CARDS ── */
  .pipeline { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
  .pipe-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
    transition: border-color 0.2s, transform 0.2s;
  }
  .pipe-card:hover { border-color: var(--border-hover); transform: translateY(-2px); }
  .pipe-icon { font-size: 22px; margin-bottom: 12px; display: block; }
  .pipe-title { font-size: 13px; font-weight: 500; color: #fff; margin-bottom: 5px; }
  .pipe-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

  /* ── FEATURES ── */
  .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; }
  .feat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.25rem 1.5rem;
    transition: border-color 0.2s;
  }
  .feat-card:hover { border-color: var(--border-hover); }
  .feat-icon { font-size: 20px; margin-bottom: 12px; display: block; }
  .feat-title { font-size: 14px; font-weight: 500; color: #fff; margin-bottom: 6px; }
  .feat-desc { font-size: 12px; color: var(--text-muted); line-height: 1.6; }

  /* ── TECH TAGS ── */
  .tech-wrap { display: flex; flex-wrap: wrap; gap: 8px; }
  .tech-chip {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text-muted);
    transition: border-color 0.2s, color 0.2s;
  }
  .tech-chip:hover { border-color: var(--border-hover); color: var(--text); }
  .tech-chip i { font-size: 14px; }

  /* ── FILES TREE ── */
  .tree {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--text-muted);
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    line-height: 2;
  }
  .tree .dir { color: var(--blue); }
  .tree .file { color: var(--text-muted); }
  .tree .highlight { color: var(--green-light); }
  .tree .indent1 { padding-left: 1.2rem; }
  .tree .indent2 { padding-left: 2.4rem; }

  /* ── FOOTER ── */
  .footer {
    padding: 3rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    border-top: 1px solid var(--border);
  }
  .footer-left { font-size: 12px; color: var(--text-dim); }
  .footer-badge {
    font-family: var(--mono);
    font-size: 11px;
    padding: 5px 12px;
    border-radius: 6px;
    border: 1px solid rgba(29,158,117,0.3);
    color: var(--green-light);
    background: rgba(29,158,117,0.06);
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .animate { animation: fadeInUp 0.5s ease both; }
  .delay1 { animation-delay: 0.1s; }
  .delay2 { animation-delay: 0.2s; }
  .delay3 { animation-delay: 0.3s; }

  @media (max-width: 640px) {
    .hero { padding: 3rem 0 2.5rem; }
    .winner-band { flex-direction: column; text-align: center; }
    .winner-prob { font-size: 2rem; }
    .team-name { width: 80px; }
  }
</style>
</head>
<body>

<div class="page">

  <!-- HERO -->
  <div class="hero animate">
    <div class="hero-eyebrow">FIFA World Cup 2026 — Forecasting Project</div>
    <h1>Predicting the<br><strong>World Cup winner</strong><br>with data.</h1>
    <p class="hero-desc">
      Poisson regression trained on historical international match data, combined with Elo ratings and Monte Carlo simulation to forecast every stage of the 2026 tournament across 1,000 full simulations.
    </p>
    <div class="hero-stats">
      <div class="stat-item">
        <div class="stat-num">1,000</div>
        <div class="stat-lbl">Simulated tournaments</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">48</div>
        <div class="stat-lbl">Teams modeled</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">2</div>
        <div class="stat-lbl">Poisson models</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">6</div>
        <div class="stat-lbl">Tournament stages</div>
      </div>
    </div>
  </div>

  <!-- WINNER -->
  <section class="animate delay1">
    <div class="sec-label">Simulation output</div>
    <h2 class="sec-title">Who wins the World Cup?</h2>
    <p class="sec-sub">Based on 1,000 full Monte Carlo tournament runs. Win probability = fraction of simulations where each team lifts the trophy.</p>

    <div class="winner-band">
      <div class="trophy-icon">🏆</div>
      <div class="winner-info">
        <span class="winner-tag">Predicted champion</span>
        <div class="winner-name">🇫🇷 France</div>
        <div class="winner-meta">UEFA · Elo rank #1 · Consistent semi-final performer</div>
      </div>
      <div class="winner-prob">~21%<span>win prob</span></div>
    </div>

    <div class="team-list" id="teamList"></div>
  </section>

  <!-- METHODOLOGY -->
  <section>
    <div class="sec-label">Methodology</div>
    <h2 class="sec-title">How the model works</h2>
    <p class="sec-sub">A six-stage pipeline from raw match data to tournament probability estimates.</p>
    <div class="steps" id="steps"></div>
  </section>

  <!-- PIPELINE -->
  <section>
    <div class="sec-label">Prediction pipeline</div>
    <h2 class="sec-title">Core components</h2>
    <p class="sec-sub">Each component feeds directly into the next, forming a coherent forecasting chain.</p>
    <div class="pipeline" id="pipeline"></div>
  </section>

  <!-- APP FEATURES -->
  <section>
    <div class="sec-label">Streamlit app</div>
    <h2 class="sec-title">Interactive dashboard</h2>
    <p class="sec-sub">Three separate views let you explore, simulate, and compare teams from any angle.</p>
    <div class="features" id="features"></div>
  </section>

  <!-- PROJECT STRUCTURE -->
  <section>
    <div class="sec-label">Project structure</div>
    <h2 class="sec-title">Codebase layout</h2>
    <div class="tree">
      <div><span class="dir">football_wc2026/</span></div>
      <div class="indent1"><span class="dir">data/</span></div>
      <div class="indent2"><span class="file">raw/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> historical match results</div>
      <div class="indent2"><span class="file">processed/ &nbsp;</span> <span class="highlight">wc2026_tournament_probabilities.csv</span></div>
      <div class="indent2"><span class="file">reference/ &nbsp;</span> fixtures, groups, brackets</div>
      <div class="indent1"><span class="dir">models/</span></div>
      <div class="indent2"><span class="highlight">poisson_home.pkl</span></div>
      <div class="indent2"><span class="highlight">poisson_away.pkl</span></div>
      <div class="indent2"><span class="file">feature_columns.pkl</span></div>
      <div class="indent1"><span class="dir">notebooks/</span></div>
      <div class="indent2"><span class="file">0-data_fetch.ipynb</span></div>
      <div class="indent2"><span class="file">1-data_cleaning.ipynb</span></div>
      <div class="indent2"><span class="file">2-feature_engineering_ELO.ipynb</span></div>
      <div class="indent2"><span class="file">3-feature_engineering_match_metadata.ipynb</span></div>
      <div class="indent2"><span class="file">4-model_training.ipynb</span></div>
      <div class="indent2"><span class="highlight">5-tournament_simulation.ipynb</span></div>
      <div class="indent1"><span class="dir">src/</span></div>
      <div class="indent2"><span class="file">data_loader.py &nbsp; prediction.py &nbsp; tournament.py</span></div>
      <div class="indent2"><span class="file">group_stage.py &nbsp; bracket.py &nbsp; knockout.py</span></div>
      <div class="indent1"><span class="highlight">simulation_app.py</span> &nbsp; <span class="file">← Streamlit entry point</span></div>
    </div>
  </section>

  <!-- TECH -->
  <section>
    <div class="sec-label">Technologies</div>
    <h2 class="sec-title">Stack</h2>
    <div class="tech-wrap" id="techWrap"></div>
  </section>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-left">FIFA World Cup 2026 Predictor &nbsp;·&nbsp; Monte Carlo + Poisson Regression</div>
    <div class="footer-badge">⚽ 48 teams · 1,000 simulations</div>
  </div>

</div>

<script>
/* ── TEAM DATA ── */
const teams = [
  { flag: "🇫🇷", name: "France",    conf: "UEFA",     prob: 21, color: "#3D7EF0" },
  { flag: "🇧🇷", name: "Brazil",    conf: "CONMEBOL", prob: 17, color: "#1D9E75" },
  { flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿", name: "England",   conf: "UEFA",     prob: 14, color: "#E24B4A" },
  { flag: "🇦🇷", name: "Argentina", conf: "CONMEBOL", prob: 13, color: "#8B7EDD" },
  { flag: "🇪🇸", name: "Spain",     conf: "UEFA",     prob: 11, color: "#F0A030" },
  { flag: "🇩🇪", name: "Germany",   conf: "UEFA",     prob:  8, color: "#888" },
  { flag: "🇵🇹", name: "Portugal",  conf: "UEFA",     prob:  6, color: "#1D9E75" },
  { flag: "🇧🇪", name: "Belgium",   conf: "UEFA",     prob:  4, color: "#E24B4A" },
];

const confStyle = {
  UEFA:     { bg: "rgba(61,126,240,0.12)", color: "#3D7EF0" },
  CONMEBOL: { bg: "rgba(29,158,117,0.12)", color: "#1D9E75" },
};

const tl = document.getElementById("teamList");
teams.forEach((t, i) => {
  const s = confStyle[t.conf];
  const pct = Math.round((t.prob / 21) * 100);
  tl.innerHTML += `
    <div class="team-row">
      <span class="rank">${i + 1}</span>
      <span class="team-flag">${t.flag}</span>
      <span class="team-name">${t.name}</span>
      <span class="conf-pill" style="background:${s.bg}; color:${s.color}; border-color:${s.color}30;">${t.conf}</span>
      <div class="bar-track"><div class="bar-fill" style="width:0%; background:${t.color};" data-w="${pct}"></div></div>
      <span class="prob-val">${t.prob}%</span>
    </div>`;
});

/* ── METHODOLOGY ── */
const steps = [
  { icon: "ti-database", color: "#3D7EF0", bg: "rgba(61,126,240,0.12)",
    title: "Data collection & cleaning",
    desc: "Historical international match results gathered and cleaned — normalizing team names, handling neutral venues, filtering meaningless friendlies.",
    tag: "FOUNDATION" },
  { icon: "ti-chart-line", color: "#8B7EDD", bg: "rgba(139,126,221,0.12)",
    title: "Elo rating engine",
    desc: "Custom Elo pipeline built on all historical results with recency weighting and tournament-type adjustments. Gives every team a dynamic strength score before each match.",
    tag: "TEAM STRENGTH" },
  { icon: "ti-settings-cog", color: "#F0A030", bg: "rgba(240,160,48,0.12)",
    title: "Feature engineering",
    desc: "Match-level features constructed: home/away Elo, Elo delta, neutral venue flag, tournament importance weight, confederation encoding. These become model inputs.",
    tag: "INPUT FEATURES" },
  { icon: "ti-math-function", color: "#1D9E75", bg: "rgba(29,158,117,0.12)",
    title: "Poisson regression (xG models)",
    desc: "Two separate Poisson regression models trained — one for home goals, one for away goals. Poisson is the right choice because goals are count events with low expected values per match.",
    tag: "STATISTICAL MODEL" },
  { icon: "ti-calculator", color: "#E24B4A", bg: "rgba(226,75,74,0.12)",
    title: "Match outcome probabilities",
    desc: "Expected goals from both models are convolved over the Poisson distribution to compute win, draw, and loss probabilities for every possible matchup.",
    tag: "PROBABILITY ENGINE" },
  { icon: "ti-rotate-clockwise", color: "#5DCAA5", bg: "rgba(93,202,165,0.12)",
    title: "Monte Carlo simulation ×1,000",
    desc: "The entire 48-team World Cup — group stage, best third-place rules, Round of 32, R16, QF, SF, Final — simulated 1,000 times. Stage-by-stage probabilities are aggregated across all runs.",
    tag: "MONTE CARLO" },
];

const stepsEl = document.getElementById("steps");
steps.forEach(s => {
  stepsEl.innerHTML += `
    <div class="step">
      <div class="step-icon-wrap" style="background:${s.bg};">
        <i class="ti ${s.icon}" style="color:${s.color};" aria-hidden="true"></i>
      </div>
      <div class="step-body">
        <div class="step-title">${s.title}</div>
        <div class="step-desc">${s.desc}</div>
        <span class="step-tag" style="color:${s.color}; border-color:${s.color}40; background:${s.bg};">${s.tag}</span>
      </div>
    </div>`;
});

/* ── PIPELINE ── */
const pipes = [
  { icon: "ti-file-spreadsheet", color: "#3D7EF0", title: "Historical match data", desc: "Cleaned CSV of international results going back decades" },
  { icon: "ti-activity", color: "#8B7EDD", title: "Elo ratings", desc: "Pre-match team strength scores updated after every result" },
  { icon: "ti-binary-tree", color: "#F0A030", title: "Feature matrix", desc: "Elo, venue, confederation, importance — engineered per match" },
  { icon: "ti-math-function", color: "#1D9E75", title: "xG Poisson models", desc: "Trained home + away goal expectation models" },
  { icon: "ti-arrows-split", color: "#E24B4A", title: "Outcome probabilities", desc: "Win / draw / loss odds for any head-to-head" },
  { icon: "ti-trophy", color: "#5DCAA5", title: "Tournament probabilities", desc: "Monte Carlo win rates per stage, per team" },
];

const pipeEl = document.getElementById("pipeline");
pipes.forEach(p => {
  pipeEl.innerHTML += `
    <div class="pipe-card">
      <i class="ti ${p.icon} pipe-icon" style="color:${p.color};" aria-hidden="true"></i>
      <div class="pipe-title">${p.title}</div>
      <div class="pipe-desc">${p.desc}</div>
    </div>`;
});

/* ── FEATURES ── */
const feats = [
  { icon: "ti-chart-bar", color: "#3D7EF0", title: "Probability explorer", desc: "Full 48-team ranking with win, final, SF, QF, R16, and R32 probabilities. Sortable and filterable." },
  { icon: "ti-player-play", color: "#1D9E75", title: "Live simulation", desc: "Run a single full World Cup with live score reveals — group matches, standings, knockout bracket, champion." },
  { icon: "ti-vs", color: "#8B7EDD", title: "Match explorer", desc: "Pick any two teams. See win/draw/loss odds, xG, Elo, form, H2H score, and top 12 predicted scorelines." },
  { icon: "ti-table", color: "#F0A030", title: "Group standings", desc: "Simulated group tables with points, GD, and qualification status highlighted." },
];

const featEl = document.getElementById("features");
feats.forEach(f => {
  featEl.innerHTML += `
    <div class="feat-card">
      <i class="ti ${f.icon} feat-icon" style="color:${f.color};" aria-hidden="true"></i>
      <div class="feat-title">${f.title}</div>
      <div class="feat-desc">${f.desc}</div>
    </div>`;
});

/* ── TECH ── */
const techs = [
  { icon: "ti-brand-python", name: "Python" },
  { icon: "ti-chart-dots", name: "Statsmodels (Poisson)" },
  { icon: "ti-table", name: "Pandas" },
  { icon: "ti-math", name: "NumPy / SciPy" },
  { icon: "ti-chart-bar", name: "Plotly" },
  { icon: "ti-device-desktop", name: "Streamlit" },
  { icon: "ti-notebook", name: "Jupyter" },
  { icon: "ti-package", name: "UV package manager" },
];

const techEl = document.getElementById("techWrap");
techs.forEach(t => {
  techEl.innerHTML += `
    <div class="tech-chip">
      <i class="ti ${t.icon}" aria-hidden="true"></i>
      ${t.name}
    </div>`;
});

/* ── ANIMATE BARS ON LOAD ── */
setTimeout(() => {
  document.querySelectorAll(".bar-fill[data-w]").forEach(el => {
    el.style.width = el.dataset.w + "%";
  });
}, 300);
</script>
</body>
</html>
