# -*- coding: utf-8 -*-
"""
Generator script to build the perfected index.html.
No timer, 17 slides (slide 18 removed), dynamic per-slide glossary,
rich pedagogical notes, clear explanations of charts and examples,
and full mobile remote synchronization.
"""

import sys
import json
from notes_and_glossary_data import SLIDE_GLOSSARIES, PRESENTER_NOTES

sys.stdout.reconfigure(encoding='utf-8')

def generate_index_html():
    # Convert glossaries and notes to JSON for safe injection into JS
    glossaries_json = json.dumps(SLIDE_GLOSSARIES, ensure_ascii=False)
    notes_json = json.dumps(PRESENTER_NOTES, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Defensa Metodológica: Puntos 6.4 al 6.7 | UPDS</title>
  <meta name="description" content="Presentación interactiva doctoral para defensa de informe metodológico de investigación científica en la Universidad Privada Domingo Savio.">
  <style>
    :root {{
      --bg-dark: #0f172a;
      --bg-darker: #090d16;
      --bg-surface: #1e293b;
      --bg-surface-elevated: #283548;
      --bg-card: rgba(30, 41, 59, 0.75);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(37, 99, 235, 0.4);
      --primary: #2563eb;
      --primary-light: #3b82f6;
      --primary-glow: rgba(37, 99, 235, 0.35);
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #8b5cf6;
      --text-white: #f8fafc;
      --text-body: #cbd5e1;
      --text-muted: #94a3b8;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
      --shadow-glow: 0 0 25px rgba(37, 99, 235, 0.25);
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-body);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.5;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
      user-select: none;
    }}

    /* TOP BAR PERSISTENTE (SIN TEMPORIZADOR) */
    .top-bar {{
      height: 60px;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
      flex-shrink: 0;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .institution-badge {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(37, 99, 235, 0.15);
      border: 1px solid var(--border-accent);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-white);
      letter-spacing: 0.5px;
    }}

    .speaker-pill {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      padding: 6px 14px;
      border-radius: 24px;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--accent-cyan);
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }}

    .speaker-pill .speaker-num {{
      background: var(--primary);
      color: var(--text-white);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 800;
    }}

    .speaker-pill .subtopic {{
      color: var(--text-muted);
      font-weight: 400;
    }}

    .top-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .remote-live-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-emerald);
      box-shadow: 0 0 10px var(--accent-emerald);
      display: inline-block;
    }}

    .remote-live-dot.waiting {{
      background: var(--accent-amber);
      box-shadow: 0 0 10px var(--accent-amber);
    }}

    /* MAIN STAGE (SLIDE CONTAINER) */
    .stage-container {{
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px 24px;
    }}

    .slide-deck {{
      width: 100%;
      height: 100%;
      max-width: 1440px;
      position: relative;
    }}

    .slide {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.98) translateY(8px);
      transition: opacity 0.35s cubic-bezier(0.4, 0, 0.2, 1), transform 0.35s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.35s;
      pointer-events: none;
    }}

    .slide.active {{
      opacity: 1;
      visibility: visible;
      transform: scale(1) translateY(0);
      pointer-events: auto;
    }}

    /* SLIDE HEADER */
    .slide-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
      flex-shrink: 0;
    }}

    .slide-pretitle {{
      font-size: 0.76rem;
      font-weight: 800;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--accent-cyan);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .slide-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.3px;
      line-height: 1.25;
    }}

    .slide-meta-badge {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 2px;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .slide-meta-badge strong {{
      color: var(--accent-emerald);
      font-size: 0.82rem;
    }}

    /* SLIDE CONTENT (GRID 2 COLUMNS) */
    .slide-content {{
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      min-height: 0;
      overflow-y: auto;
      padding-bottom: 6px;
    }}

    .slide-content.full-width {{
      grid-template-columns: 1fr;
    }}

    /* GLASS CARDS */
    .glass-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      backdrop-filter: blur(10px);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: var(--transition);
    }}

    .glass-card:hover {{
      border-color: rgba(37, 99, 235, 0.3);
      box-shadow: var(--shadow-md);
    }}

    .card-title {{
      font-size: 0.98rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .card-title .icon {{
      font-size: 1.15rem;
    }}

    p, ul, ol {{
      font-size: 0.88rem;
      color: var(--text-body);
      line-height: 1.5;
    }}

    ul, ol {{
      padding-left: 20px;
      margin-bottom: 10px;
    }}

    li {{
      margin-bottom: 6px;
    }}

    /* RECUADROS EXPLICATIVOS DIDÁCTICOS */
    .didactic-box {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(6, 182, 212, 0.3);
      border-left: 4px solid var(--accent-cyan);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      margin-top: 10px;
      font-size: 0.84rem;
      color: #e2e8f0;
      line-height: 1.45;
    }}

    .didactic-box strong {{
      color: var(--accent-cyan);
    }}

    .alert-box {{
      background: rgba(245, 158, 11, 0.1);
      border-left: 4px solid var(--accent-amber);
      padding: 10px 14px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-top: 10px;
      font-size: 0.84rem;
      color: #fde68a;
    }}

    .alert-box.success {{
      background: rgba(16, 185, 129, 0.1);
      border-left-color: var(--accent-emerald);
      color: #a7f3d0;
    }}

    .alert-box.danger {{
      background: rgba(244, 63, 94, 0.1);
      border-left-color: var(--accent-rose);
      color: #fecdd3;
    }}

    .alert-box.info {{
      background: rgba(37, 99, 235, 0.15);
      border-left-color: var(--primary-light);
      color: #bfdbfe;
    }}

    /* BARRA DINÁMICA DE GLOSARIO DE LA DIAPOSITIVA (FOOTER DE CADA SLIDE) */
    .slide-glossary-bar {{
      margin-top: 10px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }}

    .glossary-bar-label {{
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--accent-amber);
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}

    .glossary-pills-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      flex: 1;
    }}

    .glossary-term-chip {{
      background: var(--bg-surface);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 0.78rem;
      color: var(--text-white);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
    }}

    .glossary-term-chip:hover {{
      border-color: var(--accent-amber);
      background: rgba(245, 158, 11, 0.15);
      transform: translateY(-1px);
    }}

    .glossary-term-chip strong {{
      color: var(--accent-amber);
    }}

    /* BOTTOM CONTROL BAR */
    .bottom-bar {{
      height: 56px;
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
      flex-shrink: 0;
    }}

    .controls-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-nav {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-white);
      padding: 7px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
      user-select: none;
    }}

    .btn-nav:hover {{
      background: var(--bg-surface-elevated);
      border-color: var(--border-accent);
      transform: translateY(-1px);
    }}

    .btn-nav.primary {{
      background: var(--primary);
      border-color: var(--primary-light);
      box-shadow: 0 2px 8px var(--primary-glow);
    }}

    .slide-counter {{
      font-size: 0.84rem;
      color: var(--text-muted);
      font-weight: 500;
      padding: 0 8px;
    }}

    .slide-counter span {{
      color: var(--text-white);
      font-weight: 700;
    }}

    .shortcuts-hint {{
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .kbd {{
      background: var(--bg-surface);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 0.7rem;
      color: var(--text-white);
      font-family: monospace;
    }}

    /* MODAL OVERLAYS */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
    }}

    .modal-overlay.open {{
      opacity: 1;
      visibility: visible;
    }}

    .modal-window {{
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 900px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      transform: scale(0.96);
      transition: var(--transition);
      overflow: hidden;
    }}

    .modal-overlay.open .modal-window {{
      transform: scale(1);
    }}

    .modal-header {{
      padding: 16px 22px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.7);
    }}

    .modal-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-white);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .modal-close {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.4rem;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
      transition: var(--transition);
    }}

    .modal-close:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-white);
    }}

    .modal-body {{
      padding: 20px 24px;
      overflow-y: auto;
      flex: 1;
    }}

    /* SECCIONES EN EL MODAL DE NOTAS */
    .note-section {{
      margin-bottom: 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 14px 18px;
    }}

    .note-section-title {{
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .note-section-title.goal {{ color: var(--accent-cyan); }}
    .note-section-title.script {{ color: var(--accent-emerald); }}
    .note-section-title.metaphor {{ color: var(--accent-amber); }}
    .note-section-title.faq {{ color: var(--accent-purple); }}
    .note-section-title.glossary {{ color: #38bdf8; }}
    .note-section-title.pass {{ color: #f43f5e; }}

    .note-content {{
      font-size: 0.92rem;
      line-height: 1.6;
      color: var(--text-white);
    }}

    /* QR MODAL BOX */
    .qr-box-container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 16px;
      padding: 10px;
    }}

    .qr-svg-holder {{
      background: white;
      padding: 14px;
      border-radius: var(--radius-md);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .room-code-tag {{
      background: var(--primary);
      color: white;
      padding: 4px 14px;
      border-radius: 20px;
      font-weight: 800;
      font-size: 1.1rem;
      letter-spacing: 1px;
    }}

    .action-btn {{
      background: var(--primary);
      border: 1px solid var(--primary-light);
      color: white;
      padding: 9px 18px;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.88rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
    }}

    .action-btn:hover {{
      background: var(--primary-light);
      transform: translateY(-1px);
    }}

    .action-btn.secondary {{
      background: var(--bg-surface-elevated);
      border-color: var(--border-subtle);
    }}

    /* OVERVIEW THUMBNAILS GRID (17 SLIDES) */
    .overview-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 14px;
      padding: 4px;
    }}

    .overview-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
    }}

    .overview-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}

    .overview-card.current {{
      border-color: var(--accent-cyan);
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
    }}

    .overview-num {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }}

    .overview-title {{
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 6px;
      line-height: 1.3;
    }}

    .overview-speaker {{
      font-size: 0.74rem;
      color: var(--text-muted);
      margin-top: auto;
    }}

    /* ======================================================== */
    /* MODO CONSOLA MÓVIL (ACTIVADO MEDIANTE ?remote=1)         */
    /* ======================================================== */
    .mobile-remote-container {{
      display: none;
      position: fixed;
      inset: 0;
      background: var(--bg-dark);
      z-index: 9999;
      flex-direction: column;
      overflow-y: auto;
      padding: 16px;
    }}

    body.remote-mode .top-bar,
    body.remote-mode .stage-container,
    body.remote-mode .bottom-bar {{
      display: none !important;
    }}

    body.remote-mode .mobile-remote-container {{
      display: flex !important;
    }}

    .mobile-header-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-md);
      padding: 14px;
      margin-bottom: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .mobile-status-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.78rem;
    }}

    .mobile-slide-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text-white);
      line-height: 1.25;
    }}

    .mobile-speaker-badge {{
      background: rgba(37, 99, 235, 0.2);
      border: 1px solid var(--border-accent);
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--accent-cyan);
      display: inline-block;
      align-self: flex-start;
    }}

    /* BOTONES GIGANTES TÁCTILES DEL CELULAR */
    .mobile-touch-controls {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 14px;
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg-dark);
      padding: 6px 0;
    }}

    .btn-mobile-touch {{
      background: var(--bg-surface-elevated);
      border: 2px solid var(--border-accent);
      color: var(--text-white);
      padding: 16px;
      border-radius: var(--radius-md);
      font-size: 1.05rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      -webkit-tap-highlight-color: transparent;
    }}

    .btn-mobile-touch.primary {{
      background: var(--primary);
      border-color: var(--primary-light);
      box-shadow: 0 4px 15px var(--primary-glow);
    }}

    .btn-mobile-touch:active {{
      transform: scale(0.96);
    }}

    /* TARJETA DE GLOSARIO DINÁMICO EN EL CELULAR */
    .mobile-glossary-card {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-md);
      padding: 14px;
      margin-bottom: 14px;
    }}

    .mobile-glossary-title {{
      font-size: 0.82rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--accent-amber);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .mobile-glossary-item {{
      font-size: 0.86rem;
      line-height: 1.45;
      color: #fef3c7;
      margin-bottom: 8px;
    }}

    .mobile-glossary-item strong {{
      color: #fff;
    }}

    /* TABLAS Y ELEMENTOS GRÁFICOS PERSONALIZADOS */
    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      margin-top: 8px;
      background: rgba(15, 23, 42, 0.6);
      border-radius: var(--radius-sm);
      overflow: hidden;
    }}

    .matrix-table th, .matrix-table td {{
      padding: 8px 10px;
      text-align: center;
      border: 1px solid var(--border-subtle);
    }}

    .matrix-table th {{
      background: rgba(30, 41, 59, 0.9);
      color: var(--accent-cyan);
      font-weight: 700;
    }}

    .matrix-table tr:hover {{
      background: rgba(37, 99, 235, 0.15);
    }}

    .interactive-btn {{
      background: rgba(37, 99, 235, 0.15);
      border: 1px solid var(--border-accent);
      color: var(--text-white);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      margin: 2px;
    }}

    .interactive-btn:hover, .interactive-btn.active {{
      background: var(--primary);
      border-color: var(--primary-light);
    }}
  </style>
</head>
<body>

  <!-- ======================================================== -->
  <!-- BARRA SUPERIOR PERSISTENTE (SIN CRONÓMETRO)               -->
  <!-- ======================================================== -->
  <header class="top-bar">
    <div class="brand-group">
      <div class="institution-badge">
        <span>🏛️</span>
        <span>UPDS • SEDE SANTA CRUZ</span>
      </div>
      <div class="speaker-pill" id="currentSpeakerPill">
        <span class="speaker-num" id="speakerPillNum">EXP 1</span>
        <span id="speakerPillName">Deivy Melgar Perez</span>
        <span class="subtopic" id="speakerPillSubtopic">• 6.4 Tabulación de Datos</span>
      </div>
    </div>

    <div class="top-actions">
      <button class="btn-nav" onclick="openSlideGlossaryModal()" style="border-color: var(--accent-amber); color: var(--accent-amber);" title="Ver palabras difíciles de esta diapositiva explicadas fácil">
        <span>💡 Palabras Clave</span>
      </button>

      <button class="btn-nav" onclick="openRemoteModal()" style="border-color: var(--accent-cyan); color: var(--accent-cyan);" title="Escanear QR para controlar desde el celular">
        <span class="remote-live-dot" id="remoteStatusIndicator"></span>
        <span>📱 Conectar Celular</span>
      </button>

      <button class="btn-nav" onclick="toggleNotesModal()" title="Ver notas del presentador (Tecla N)">
        <span>🎙️ Notas</span>
      </button>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- ESCENARIO PRINCIPAL (17 DIAPOSITIVAS)                     -->
  <!-- ======================================================== -->
  <main class="stage-container">
    <div class="slide-deck" id="slideDeck">

      <!-- SLIDE 1: APERTURA FORMAL -->
      <section class="slide active" id="slide-1" data-speaker="EQUIPO DE INVESTIGACIÓN" data-role="Apertura Formal" data-subtopic="Defensa Metodológica (6.4 - 6.7)">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🏛️</span> UNIVERSIDAD PRIVADA DOMINGO SAVIO • FACULTAD DE CIENCIAS EMPRESARIALES Y SOCIALES</div>
            <h1 class="slide-title">Defensa de Informe Metodológico de Investigación Científica</h1>
          </div>
          <div class="slide-meta-badge">
            <span>Docente Evaluador:</span>
            <strong>Lic. Marcial Villarroel Siles</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card" style="justify-content: center;">
            <div style="display: inline-block; background: rgba(37,99,235,0.15); border: 1px solid var(--border-accent); padding: 4px 12px; border-radius: 14px; font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan); margin-bottom: 12px;">
              Puntos Metodológicos 6.4 al 6.7
            </div>
            <h2 style="font-size: 1.45rem; color: #fff; margin-bottom: 10px; line-height: 1.3;">
              El Viaje Científico: De la Recolección de Datos a la Construcción de Teoría
            </h2>
            <p style="margin-bottom: 14px;">
              Presentación formal de la metodología aplicada: ordenamiento sistemático, modelos predictivos cuantitativos (SPSS) y análisis hermenéutico cualitativo (ATLAS.ti).
            </p>
            <div class="didactic-box">
              <strong>💡 En palabras sencillas:</strong> La investigación no es amontonar números ni transcribir charlas; es seguir un camino claro y con reglas para responder preguntas reales y resolver problemas de nuestra sociedad con evidencia comprobable.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">👥</span> Equipo Defensor (8 Expositores)</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.82rem;">
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">1. Deivy Melgar Perez</strong><br>
                <span style="color: var(--text-muted);">6.4 Tabulación de Datos</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">2. María Teresa Paco Flores</strong><br>
                <span style="color: var(--text-muted);">6.4 Codificación y Missing Data</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">3. José Maria Peredo Barba</strong><br>
                <span style="color: var(--text-muted);">6.5 Sistematización e Intervalos</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">4. Mishel Alcázar Valdez</strong><br>
                <span style="color: var(--text-muted);">6.5 Gráficos y Detección Outliers</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">5. Carlos Alberto Choque</strong><br>
                <span style="color: var(--text-muted);">6.6 Análisis Cuantitativo y Regresión</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">6. Dapne Scarlet Salvatierra</strong><br>
                <span style="color: var(--text-muted);">6.6 Minería KDD y Causalidad</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">7. Yord Gember Rojas Rocha</strong><br>
                <span style="color: var(--text-muted);">6.7 IBM SPSS y Lectura p-valor</span>
              </div>
              <div style="background: rgba(15,23,42,0.5); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
                <strong style="color: var(--accent-cyan);">8. Rodrigo Arauz Mercado</strong><br>
                <span style="color: var(--text-muted);">6.7 ATLAS.ti y Redes Semánticas</span>
              </div>
            </div>
            <div class="alert-box success" style="margin-top: 10px; font-size: 0.8rem;">
              ✓ Presentación sincronizada para proyección en aula y control remoto móvil.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-1"></div>
        </div>
      </section>

      <!-- SLIDE 2: DEIVY - 6.4 TABULACIÓN -->
      <section class="slide" id="slide-2" data-speaker="Deivy Melgar Perez" data-role="Expositor 1" data-subtopic="6.4 Tabulación: Fundamentos y Rol">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1 • PUNTO 6.4 TABULACIÓN DE DATOS</div>
            <h2 class="slide-title">Concepto, Finalidad y Rol Metodológico de la Tabulación</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 1:</span>
            <strong>Deivy Melgar Perez</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📋</span> ¿Qué es la Tabulación y para qué sirve?</h3>
            <p>
              Cuando salimos a encuestar a la calle o a las aulas, lo que tenemos al final del día es una montaña de cuestionarios en papel o formularios desordenados.
            </p>
            <ul>
              <li><strong>Concepto formal:</strong> La tabulación es la operación técnica que cuenta, clasifica y resume las respuestas de cada encuestado en tablas organizadas.</li>
              <li><strong>Objetivo clave:</strong> Pasar del caos de hojas sueltas a un sistema numérico limpio donde podamos ver qué respondió el grupo en general.</li>
              <li><strong>Importancia:</strong> Si tabulamos mal, todos los gráficos, porcentajes y conclusiones posteriores estarán completamente equivocados ("Basura entra, basura sale").</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Analogía sencilla:</strong> Tabular es como clasificar las compras del supermercado al llegar a casa: separas frutas, verduras y lácteos en sus gavetas correspondientes antes de empezar a cocinar.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔍</span> Ejemplo Práctico: De la Encuesta a la Tabla</h3>
            <p style="font-size: 0.84rem; margin-bottom: 6px;">
              Supongamos que aplicamos un cuestionario corto a 5 docentes de la UPDS sobre su uso del aula virtual:
            </p>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th>Encuesta</th>
                  <th>Docente</th>
                  <th>¿Usa Aula Virtual?</th>
                  <th>Nivel de Satisfacción</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>#001</td><td>Docente A</td><td>Sí (1)</td><td>Alto (3)</td></tr>
                <tr><td>#002</td><td>Docente B</td><td>Sí (1)</td><td>Medio (2)</td></tr>
                <tr><td>#003</td><td>Docente C</td><td>No (0)</td><td>Bajo (1)</td></tr>
                <tr><td>#004</td><td>Docente D</td><td>Sí (1)</td><td>Alto (3)</td></tr>
                <tr><td>#005</td><td>Docente E</td><td>Sí (1)</td><td>Alto (3)</td></tr>
              </tbody>
            </table>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>Resultado de la Tabulación:</strong> De 5 docentes evaluados, 4 usan aula virtual (80%) y 3 están altamente satisfechos (60%). ¡En dos segundos convertimos 5 hojas sueltas en conocimiento claro!
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-2"></div>
        </div>
      </section>

      <!-- SLIDE 3: MARÍA TERESA - 6.4 CODIFICACIÓN Y MATRIZ N x K -->
      <section class="slide" id="slide-3" data-speaker="María Teresa Paco Flores" data-role="Expositor 2" data-subtopic="6.4 Codificación y Matriz N×K">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1 • PUNTO 6.4 CODIFICACIÓN TÉCNICA</div>
            <h2 class="slide-title">Codificación Técnica, Libro de Códigos y la Matriz (N × K)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 2:</span>
            <strong>María Teresa Paco Flores</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🏷️</span> ¿Cómo traducimos palabras en números?</h3>
            <p>
              Las computadoras y programas como SPSS no entienden opiniones en texto libre; necesitan números bien definidos.
            </p>
            <ul>
              <li><strong>Pre-codificación:</strong> Asignar números a las opciones antes de imprimir la encuesta (ej. 1 = Masculino, 2 = Femenino, o escala de satisfacción del 1 al 5).</li>
              <li><strong>Post-codificación:</strong> Leer respuestas de preguntas abiertas de texto, agrupar las ideas parecidas y ponerles un número a cada grupo después de encuestar.</li>
              <li><strong>El Libro de Códigos (Codebook):</strong> Es el diccionario oficial de la investigación. Dice exactamente: la variable <code>GEN</code> significa Género y el 1 es Varón y el 2 es Mujer.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 En palabras sencillas:</strong> El Libro de Códigos evita confusiones. Si otro investigador revisa tu base de datos el próximo año, gracias al Libro de Códigos sabrá exactamente qué significa cada número.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📊</span> Inspector de la Matriz de Datos Rectangular (N × K)</h3>
            <p style="font-size: 0.84rem;">
              Estructura formal: <strong>N Filas</strong> (Personas encuestadas) × <strong>K Columnas</strong> (Preguntas o Variables):
            </p>
            <table class="matrix-table" id="matrixInspectorTable">
              <thead>
                <tr>
                  <th>Fila (Sujeto N)</th>
                  <th>ID_PART</th>
                  <th>EDAD</th>
                  <th>SEXO (1=M, 2=F)</th>
                  <th>SATISF (1 al 5)</th>
                </tr>
              </thead>
              <tbody>
                <tr id="mat-row-1" onclick="highlightMatrixRow(1)"><td>Fila 1</td><td>#101</td><td>28</td><td>1</td><td>4</td></tr>
                <tr id="mat-row-2" onclick="highlightMatrixRow(2)"><td>Fila 2</td><td>#102</td><td>34</td><td>2</td><td>5</td></tr>
                <tr id="mat-row-3" onclick="highlightMatrixRow(3)"><td>Fila 3</td><td>#103</td><td>22</td><td>2</td><td>3</td></tr>
                <tr id="mat-row-4" onclick="highlightMatrixRow(4)"><td>Fila 4</td><td>#104</td><td>41</td><td>1</td><td>5</td></tr>
              </tbody>
            </table>
            <div class="didactic-box" id="matrixInspectorFeedback" style="margin-top: 8px;">
              <strong>Haga clic en una fila:</strong> Cada casilla individual (Xᵢⱼ) representa la respuesta exacta de ese participante en esa pregunta.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-3"></div>
        </div>
      </section>

      <!-- SLIDE 4: MARÍA TERESA - 6.4 MISSING DATA Y CONTINGENCIA 2x2 -->
      <section class="slide" id="slide-4" data-speaker="María Teresa Paco Flores" data-role="Expositor 2 (Cont.)" data-subtopic="6.4 Missing Data y Contingencia 2×2">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1 • PUNTO 6.4 CONTROL DE CALIDAD</div>
            <h2 class="slide-title">Tratamiento del Missing Data y Tabulación Cruzada (2 × 2)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 2 (Cont.):</span>
            <strong>María Teresa Paco Flores</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚠️</span> El Gran Peligro de los Datos Faltantes (Missing)</h3>
            <p>
              ¿Qué pasa si alguien dejó una pregunta en blanco o no quiso responder?
            </p>
            <ul>
              <li><strong>Jamás dejes la casilla vacía:</strong> Si dejas un hueco en blanco, programas como SPSS aplican la "eliminación listwise", es decir, ¡tiran a la basura a toda la persona encuestada!</li>
              <li><strong>La solución metodológica:</strong> Asignar códigos de usuario explícitos:
                <code>8 = No aplica</code>, <code>9 = No sabe / No responde</code>.
              </li>
              <li>De esta forma, la computadora sabe que la persona sí participó, pero no contestó esa pregunta específica.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Metáfora clara:</strong> Si vas al médico y no recuerdas cuándo fue tu última gripe, el doctor no te echa del consultorio; anota "no recuerda" y sigue revisando tu corazón y presión.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔀</span> Tabla de Contingencia (2 × 2) con Porcentajes de Fila</h3>
            <p style="font-size: 0.84rem; margin-bottom: 6px;">
              Cruce de 150 docentes de la UPDS: Género vs. Uso del Aula Virtual:
            </p>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th>Género</th>
                  <th>Usa Aula Virtual (Sí)</th>
                  <th>No Usa Aula (No)</th>
                  <th>Total Fila</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Mujeres</strong></td>
                  <td>67 <span style="color: var(--accent-emerald); font-weight: 700;">(74.4%)</span></td>
                  <td>23 (25.6%)</td>
                  <td><strong>90 (100%)</strong></td>
                </tr>
                <tr>
                  <td><strong>Varones</strong></td>
                  <td>34 <span style="color: var(--accent-amber); font-weight: 700;">(56.7%)</span></td>
                  <td>26 (43.3%)</td>
                  <td><strong>60 (100%)</strong></td>
                </tr>
                <tr style="background: rgba(30,41,59,0.9); font-weight: 700;">
                  <td>Total Muestra</td>
                  <td>101 (67.3%)</td>
                  <td>49 (32.7%)</td>
                  <td>150 (100%)</td>
                </tr>
              </tbody>
            </table>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>🔍 ¿Cómo se interpreta?</strong> Miramos los porcentajes de fila: el 74.4% de las profesoras usa el aula virtual frente al 56.7% de los profesores varones. ¡Esta diferencia se prueba luego con Chi-cuadrado!
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-4"></div>
        </div>
      </section>

      <!-- SLIDE 5: JOSÉ MARÍA - 6.5 SISTEMATIZACIÓN Y FRECUENCIAS -->
      <section class="slide" id="slide-5" data-speaker="José Maria Peredo Barba" data-role="Expositor 3" data-subtopic="6.5 Sistematización y Frecuencias">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2 • PUNTO 6.5 SISTEMATIZACIÓN DE DATOS</div>
            <h2 class="slide-title">Sistematización y los 5 Componentes de la Tabla de Frecuencias</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 3:</span>
            <strong>José Maria Peredo Barba</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📐</span> Las 5 Columnas Canónicas de una Tabla Formal</h3>
            <p>
              Sistematizar es resumir ordenadamente las respuestas para que cualquier persona las entienda al instante mediante 5 elementos:
            </p>
            <ol>
              <li><strong>Categoría:</strong> Cada una de las opciones posibles (ej. Satisfecho, Regular, Insatisfecho).</li>
              <li><strong>Frecuencia Absoluta (fᵢ):</strong> La cantidad exacta de personas que eligió esa opción.</li>
              <li><strong>Porcentaje Total:</strong> El porcentaje calculado sobre el total de encuestas, incluyendo las que quedaron vacías.</li>
              <li><strong>Porcentaje Válido:</strong> ¡El más importante! El porcentaje calculado únicamente sobre las personas que sí respondieron.</li>
              <li><strong>Porcentaje Acumulado:</strong> La suma corrida hacia abajo para saber cuánto porcentaje se acumula hasta cierto punto.</li>
            </ol>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">💡</span> Ejemplo Interactivo: ¿Por qué el % Válido es vital?</h3>
            <p style="font-size: 0.84rem;">
              Caso real de 10 encuestados donde 2 dejaron la pregunta en blanco:
            </p>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th>Nivel</th>
                  <th>Personas (fᵢ)</th>
                  <th>% Total (Base 10)</th>
                  <th>% Válido (Base 8)</th>
                  <th>% Acumulado</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>Satisfecho</td><td>5</td><td>50.0%</td><td style="color: var(--accent-emerald); font-weight:700;">62.5%</td><td>62.5%</td></tr>
                <tr><td>Regular</td><td>2</td><td>20.0%</td><td>25.0%</td><td>87.5%</td></tr>
                <tr><td>Insatisfecho</td><td>1</td><td>10.0%</td><td>12.5%</td><td>100.0%</td></tr>
                <tr style="color: var(--accent-rose);"><td>No Respondió</td><td>2</td><td>20.0%</td><td>Perdido</td><td>—</td></tr>
              </tbody>
            </table>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>⚠️ Conclusión fundamental para el jurado:</strong> Si usamos el porcentaje total parece que solo el 50% está satisfecho; pero entre los que sí opinaron, ¡la satisfacción real es del 62.5%! Usar el % total falsearía los resultados.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-5"></div>
        </div>
      </section>

      <!-- SLIDE 6: JOSÉ MARÍA - 6.5 INTERVALOS Y MARCA DE CLASE -->
      <section class="slide" id="slide-6" data-speaker="José Maria Peredo Barba" data-role="Expositor 3 (Cont.)" data-subtopic="6.5 Intervalos y Marca de Clase">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2 • PUNTO 6.5 AGRUPACIÓN DE DATOS</div>
            <h2 class="slide-title">Agrupación en Intervalos de Clase y Marca de Clase</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 3 (Cont.):</span>
            <strong>José Maria Peredo Barba</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📏</span> ¿Cuándo y cómo agrupamos números continuos?</h3>
            <p>
              Si evaluamos un examen de 0 a 100 puntos y 63 alumnos tienen notas diferentes, hacer una fila por cada nota crearía una tabla de 100 filas incomprensible.
            </p>
            <ul>
              <li><strong>Rango (R):</strong> La distancia total entre la nota más alta y la más baja: <code>R = Máximo − Mínimo</code>.</li>
              <li><strong>Intervalos (k):</strong> La cantidad de grupos que formaremos (ej. 5 a 7 grupos).</li>
              <li><strong>Amplitud (c):</strong> El ancho o tamaño de cada grupo: <code>c = R / k</code>.</li>
              <li><strong>Marca de Clase (Xᵢ):</strong> El punto medio exacto de cada grupo: <code>Xᵢ = (Límite Inferior + Superior) / 2</code>. Es el número embajador que representa a todo el grupo en fórmulas matemáticas.</li>
            </ul>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📊</span> Tabla Real de 63 Docentes Evaluados (Puntajes 51 a 85)</h3>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th>Intervalo de Notas</th>
                  <th>Marca Clase (Xᵢ)</th>
                  <th>Docentes (fᵢ)</th>
                  <th>% Válido</th>
                  <th>% Acumulado</th>
                </tr>
              </thead>
              <tbody>
                <tr id="row-int-1" onclick="highlightInterval(1)"><td>[51 a 55]</td><td>53</td><td>8</td><td>12.7%</td><td>12.7%</td></tr>
                <tr id="row-int-2" onclick="highlightInterval(2)" style="background: rgba(37,99,235,0.2); font-weight:700;"><td>[56 a 60] ⭐ Modal</td><td>58</td><td>16</td><td>25.4%</td><td>38.1%</td></tr>
                <tr id="row-int-3" onclick="highlightInterval(3)"><td>[61 a 65]</td><td>63</td><td>11</td><td>17.5%</td><td>55.6%</td></tr>
                <tr id="row-int-4" onclick="highlightInterval(4)"><td>[66 a 70]</td><td>68</td><td>14</td><td>22.2%</td><td>77.8%</td></tr>
                <tr id="row-int-5" onclick="highlightInterval(5)"><td>[71 a 75]</td><td>73</td><td>9</td><td>14.3%</td><td>92.1%</td></tr>
                <tr id="row-int-6" onclick="highlightInterval(6)"><td>[76 a 85]</td><td>80.5</td><td>5</td><td>7.9%</td><td>100.0%</td></tr>
              </tbody>
            </table>
            <div class="didactic-box" id="intervalExplanationBox" style="margin-top: 8px;">
              <strong>🔍 Lectura inmediata de la tabla:</strong> La mayor cantidad de docentes (clase modal con 16 docentes) sacó entre 56 y 60 puntos, y más del 77% obtuvo 70 puntos o menos.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-6"></div>
        </div>
      </section>

      <!-- SLIDE 7: MISHEL - 6.5 SELECCIÓN GRÁFICA -->
      <section class="slide" id="slide-7" data-speaker="Mishel Alcázar Valdez" data-role="Expositor 4" data-subtopic="6.5 Visualización y Gráficos">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2 • PUNTO 6.5 VISUALIZACIÓN CIENTÍFICA</div>
            <h2 class="slide-title">Criterios de Selección Gráfica según la Escala de Medición</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 4:</span>
            <strong>Mishel Alcázar Valdez</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🚫</span> El Error Típico en las Tesis</h3>
            <p>
              Muchos estudiantes eligen gráficos solo porque "se ven bonitos" o usan efectos 3D llamativos de Excel. En ciencia esto es un error metodológico grave:
            </p>
            <div style="background: rgba(244,63,94,0.1); border: 1px solid var(--accent-rose); padding: 12px; border-radius: 8px; margin-top: 8px;">
              <strong style="color: var(--accent-rose);">❌ El Grave Error:</strong> Poner una variable numérica continua (como notas de 0 a 100) en un gráfico de torta con 25 rebanadas microscópicas. ¡Es ilegible e induce al error visual!
            </div>
            <div style="background: rgba(16,185,129,0.1); border: 1px solid var(--accent-emerald); padding: 12px; border-radius: 8px; margin-top: 8px;">
              <strong style="color: var(--accent-emerald);">✓ El Acierto Científico:</strong> Usar gráficos de barras separadas solo para categorías (ej. Carreras), y un <strong>Histograma (barras unidas)</strong> para notas numéricas continuas.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🎯</span> Guía Rápida: ¿Qué gráfico usar siempre?</h3>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th>Tipo de Variable</th>
                  <th>Ejemplo en la UPDS</th>
                  <th>Gráfico Obligatorio</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Nominal</strong> (Nombres sin orden)</td>
                  <td>Carrera (Sistemas, Derecho, Marketing)</td>
                  <td><strong>Barras con separación</strong> o Torta (máx 4 clases)</td>
                </tr>
                <tr>
                  <td><strong>Ordinal</strong> (Con jerarquía)</td>
                  <td>Nivel de satisfacción (Bajo, Medio, Alto)</td>
                  <td><strong>Barras ordenadas</strong> de menor a mayor</td>
                </tr>
                <tr>
                  <td><strong>Continua</strong> (Números corridos)</td>
                  <td>Calificación final (0 a 100 puntos)</td>
                  <td><strong>Histograma</strong> (barras completamente unidas)</td>
                </tr>
                <tr>
                  <td><strong>Distribución y Outliers</strong></td>
                  <td>Dispersión general de notas del curso</td>
                  <td><strong>Boxplot</strong> (Diagrama de Caja y Bigotes)</td>
                </tr>
              </tbody>
            </table>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>💡 Regla de oro visual:</strong> Las barras del histograma van pegadas porque los números continuos no tienen saltos en el espacio; las barras categóricas van separadas porque las carreras son independientes.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-7"></div>
        </div>
      </section>

      <!-- SLIDE 8: MISHEL - 6.5 BOXPLOT Y OUTLIERS -->
      <section class="slide" id="slide-8" data-speaker="Mishel Alcázar Valdez" data-role="Expositor 4 (Cont.)" data-subtopic="6.5 Boxplot y Detección de Outliers">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2 • PUNTO 6.5 DETECCIÓN DE ANOMALÍAS</div>
            <h2 class="slide-title">Diagrama de Caja y Bigotes (Boxplot) y Detección de Outliers</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 4 (Cont.):</span>
            <strong>Mishel Alcázar Valdez</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📦</span> La Radiografía de un Solo Vistazo</h3>
            <p>
              El Boxplot es el gráfico más completo porque resume a todo un curso en 5 números estratégicos:
            </p>
            <ul>
              <li><strong>La Caja Central:</strong> Encierra exactamente al 50% de los estudiantes del medio (entre el Cuartil 1 y el Cuartil 3). Su altura es el Rango Intercuartílico (IQR).</li>
              <li><strong>La Raya Adentro:</strong> Es la <strong>Mediana</strong> (la nota exacta que divide al curso en dos mitades).</li>
              <li><strong>Los Bigotes:</strong> Líneas que se extienden hasta la nota más baja y más alta que se consideran normales.</li>
              <li><strong>Los Puntos Sueltos (Outliers):</strong> Alumnos con notas extraordinariamente raras o extremas fuera de los bigotes.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 ¿Por qué es crucial detectarlos?</strong> Si un estudiante sacó 99 y el resto sacó 40, el promedio subirá artificialmente. Detectar el outlier evita engañarnos.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔍</span> Ejemplo Interactivo del Boxplot (Curso con Outlier)</h3>
            <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 14px; text-align: center;">
              <!-- Simulación visual simple de Boxplot SVG -->
              <svg width="100%" height="110" viewBox="0 0 400 110">
                <!-- Bigote inferior -->
                <line x1="60" y1="55" x2="130" y2="55" stroke="#94a3b8" stroke-width="2"/>
                <line x1="60" y1="40" x2="60" y2="70" stroke="#94a3b8" stroke-width="2"/>
                <!-- Caja IQR -->
                <rect x="130" y="30" width="140" height="50" rx="4" fill="rgba(37,99,235,0.3)" stroke="#3b82f6" stroke-width="2"/>
                <!-- Mediana -->
                <line x1="190" y1="30" x2="190" y2="80" stroke="#06b6d4" stroke-width="3"/>
                <!-- Bigote superior -->
                <line x1="270" y1="55" x2="330" y2="55" stroke="#94a3b8" stroke-width="2"/>
                <line x1="330" y1="40" x2="330" y2="70" stroke="#94a3b8" stroke-width="2"/>
                <!-- Outlier Sujeto 42 -->
                <circle cx="375" cy="55" r="7" fill="#f43f5e" stroke="#fff" stroke-width="1.5" style="cursor: pointer;" onclick="alert('Sujeto 42: Nota 99 puntos. Es un Outlier Extremo.')"/>
                <!-- Etiquetas -->
                <text x="50" y="95" fill="#94a3b8" font-size="11">Mín: 42</text>
                <text x="120" y="22" fill="#3b82f6" font-size="11">Q1: 54</text>
                <text x="175" y="100" fill="#06b6d4" font-size="11" font-weight="700">Mediana: 62</text>
                <text x="260" y="22" fill="#3b82f6" font-size="11">Q3: 73</text>
                <text x="320" y="95" fill="#94a3b8" font-size="11">Máx: 82</text>
                <text x="355" y="42" fill="#f43f5e" font-size="11" font-weight="700">★ Outlier: 99</text>
              </svg>
            </div>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>🔍 En este gráfico:</strong> El 50% central de los alumnos está entre 54 y 73 puntos. Pero el Sujeto 42 sacó 99 puntos (punto rojo), superando el límite superior de Q₃ + 1.5 · IQR = 82. ¡Es un caso atípico que debe auditarse!
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-8"></div>
        </div>
      </section>

      <!-- SLIDE 9: CARLOS ALBERTO - 6.6 ANÁLISIS CUANTITATIVO Y FASES -->
      <section class="slide" id="slide-9" data-speaker="Carlos Alberto Choque Serrano" data-role="Expositor 5" data-subtopic="6.6 Análisis Cuantitativo y Fases">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3 • PUNTO 6.6 ANÁLISIS CUANTITATIVO</div>
            <h2 class="slide-title">Propósito del Análisis Cuantitativo y las 4 Fases Secuenciales</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 5:</span>
            <strong>Carlos Alberto Choque Serrano</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🎯</span> ¿Cuál es el Fin del Análisis Cuantitativo?</h3>
            <p>
              El análisis cuantitativo no consiste en calcular fórmulas por calcular; su propósito científico es <strong>validar o rechazar hipótesis</strong> usando datos numéricos para sacar conclusiones con respaldo matemático.
            </p>
            <div class="didactic-box">
              <strong>💡 La diferencia clave:</strong>
              <br>• <em>Estadística Descriptiva:</em> Te cuenta lo que pasó con los 100 alumnos que encuestaste.
              <br>• <em>Estadística Inferencial:</em> Te permite afirmar con seguridad matemática que lo mismo ocurrirá con los 5,000 alumnos de toda la universidad.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔄</span> Las 4 Fases Secuenciales Obligatorias</h3>
            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-cyan);">
                <strong style="color: var(--accent-cyan);">Fase 1: Limpieza y Depuración</strong><br>
                <span style="font-size: 0.82rem;">Revisar casillas vacías, corregir errores de dedo y verificar que los códigos estén bien asignados.</span>
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-emerald);">
                <strong style="color: var(--accent-emerald);">Fase 2: Exploración Descriptiva</strong><br>
                <span style="font-size: 0.82rem;">Calcular promedios, porcentajes y dibujar gráficos para conocer el comportamiento de la muestra.</span>
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-amber);">
                <strong style="color: var(--accent-amber);">Fase 3: Verificación de Supuestos</strong><br>
                <span style="font-size: 0.82rem;">Comprobar si los datos siguen una distribución normal (campana de Gauss) antes de elegir la prueba.</span>
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--primary-light);">
                <strong style="color: var(--primary-light);">Fase 4: Inferencia y Prueba de Hipótesis</strong><br>
                <span style="font-size: 0.82rem;">Calcular la correlación, la regresión y el pp-valor para dictar la conclusión final de la tesis.</span>
              </div>
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-9"></div>
        </div>
      </section>

      <!-- SLIDE 10: CARLOS ALBERTO - 6.6 CORRELACIÓN Y REGRESIÓN -->
      <section class="slide" id="slide-10" data-speaker="Carlos Alberto Choque Serrano" data-role="Expositor 5 (Cont.)" data-subtopic="6.6 Correlación y Regresión Lineal">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3 • PUNTO 6.6 MODELOS ESTADÍSTICOS</div>
            <h2 class="slide-title">Modelos Estadísticos Clásicos: Correlación (r) y Regresión Lineal</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 5 (Cont.):</span>
            <strong>Carlos Alberto Choque Serrano</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📈</span> Correlación de Pearson (r): ¿Van de la mano?</h3>
            <p>
              El coeficiente de Pearson mide si dos variables numéricas suben o bajan juntas:
            </p>
            <ul>
              <li><strong>Rango de valores:</strong> Siempre da un número entre -1 y +1.</li>
              <li><strong>Cerca de 0:</strong> No hay relación (ej. color de zapatos y nota del examen).</li>
              <li><strong>Positivo alto (r = .68):</strong> Significa que a mayor tiempo de estudio semanal, mayor es la nota obtenida.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Varianza Explicada (r²):</strong> Si elevamos .68² = 0.468, descubrimos que casi el <strong>47% de las buenas notas</strong> de los estudiantes se debe a las horas que dedican al estudio.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔮</span> Regresión Lineal: Prediciendo el Futuro</h3>
            <p style="font-size: 0.84rem;">
              La regresión convierte los datos en una fórmula matemática predictiva:
            </p>
            <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-accent); padding: 12px; border-radius: 8px; text-align: center; margin: 8px 0;">
              <span style="font-size: 1.15rem; font-weight: 800; color: #fff;">Nota Estimada = 42.5 + 1.45 · (Horas de Estudio)</span>
            </div>
            <div class="didactic-box">
              <strong>🔍 ¿Cómo se usa esta fórmula en la vida real?</strong>
              <br>• Si un estudiante estudia <strong>0 horas</strong>: su nota base esperada es <strong>42.5 puntos</strong>.
              <br>• Por <strong>cada hora adicional</strong> de estudio: suma <strong>+1.45 puntos</strong>.
              <br>• Si estudia <strong>20 horas</strong>: 42.5 + 1.45 · (20) = <strong>71.5 puntos</strong>.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-10"></div>
        </div>
      </section>

      <!-- SLIDE 11: DAPNE - 6.6 MINERÍA KDD Y PATRONES -->
      <section class="slide" id="slide-11" data-speaker="Dapne Scarlet Salvatierra Nina" data-role="Expositor 6" data-subtopic="6.6 Minería KDD y Patrones">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3 • PUNTO 6.6 MINERÍA DE DATOS</div>
            <h2 class="slide-title">Minería de Datos y el Proceso KDD (*Knowledge Discovery*)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 6:</span>
            <strong>Dapne Scarlet Salvatierra Nina</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⛏️</span> Descubriendo Tesoros en Mares de Datos</h3>
            <p>
              Hoy las universidades y empresas tienen miles de datos guardados (asistencia digital, clics en Moodle, biblioteca). Los humanos no podemos ver patrones revisando miles de filas.
            </p>
            <ul>
              <li><strong>Minería de Datos:</strong> Es usar algoritmos computacionales para encontrar patrones ocultos y relaciones que nadie sospechaba.</li>
              <li><strong>El Proceso KDD:</strong> Son las siglas de *Knowledge Discovery in Databases* (Descubrimiento de Conocimiento en Bases de Datos). Es el camino científico ordenado para convertir datos crudos en decisiones inteligentes.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Metáfora sencilla:</strong> La minería de datos es como usar un detector de metales en una playa gigante: te avisa exactamente dónde cavar para encontrar lo valioso sin perder tiempo buscando a ciegas.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚙️</span> Los 5 Pasos del Embudo KDD</h3>
            <div style="font-size: 0.82rem; display: flex; flex-direction: column; gap: 6px;">
              <div style="background: rgba(15,23,42,0.5); padding: 6px 10px; border-radius: 4px;"><strong>1. Selección:</strong> Elegir qué datos nos sirven de la base universitaria.</div>
              <div style="background: rgba(15,23,42,0.5); padding: 6px 10px; border-radius: 4px;"><strong>2. Preprocesamiento:</strong> Limpiar duplicados y corregir faltantes.</div>
              <div style="background: rgba(15,23,42,0.5); padding: 6px 10px; border-radius: 4px;"><strong>3. Transformación:</strong> Estandarizar variables para que la máquina las lea.</div>
              <div style="background: rgba(15,23,42,0.5); padding: 6px 10px; border-radius: 4px;"><strong>4. Minería de Datos:</strong> Correr algoritmos de agrupamiento y árboles de decisión.</div>
              <div style="background: rgba(15,23,42,0.5); padding: 6px 10px; border-radius: 4px; border-left: 3px solid var(--accent-emerald);"><strong>5. Interpretación:</strong> Convertir el hallazgo en acciones reales.</div>
            </div>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>Ejemplo Real en Educación:</strong> El sistema descubre que los estudiantes que no entran al aula virtual las primeras dos semanas tienen un 80% de riesgo de abandonar. La universidad puede llamarlos a tiempo y ayudarlos.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-11"></div>
        </div>
      </section>

      <!-- SLIDE 12: DAPNE - 6.6 MODELOS Y ADVERTENCIA CAUSAL -->
      <section class="slide" id="slide-12" data-speaker="Dapne Scarlet Salvatierra Nina" data-role="Expositor 6 (Cont.)" data-subtopic="6.6 Modelos y Advertencia Causal">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3 • PUNTO 6.6 RIGOR METODOLÓGICO</div>
            <h2 class="slide-title">Selección de Modelos y la Advertencia: Correlación ≠ Causalidad</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 6 (Cont.):</span>
            <strong>Dapne Scarlet Salvatierra Nina</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🍦</span> El Ejemplo Clásico de los Helados y el Calor</h3>
            <p>
              El error más vergonzoso que puede cometer un investigador es decir que porque dos cosas pasan al mismo tiempo, una es la causa de la otra:
            </p>
            <div style="background: rgba(244,63,94,0.1); border: 1px solid var(--accent-rose); padding: 12px; border-radius: 8px; margin-top: 8px;">
              <strong style="color: var(--accent-rose);">Ejemplo Inolvidable:</strong> En verano aumentan las ventas de helados y también aumentan los ahogamientos en piscinas. ¿Comer helado hace que la gente se ahogue? ¡Por supuesto que no! La causa real es una tercera variable oculta: <strong>el calor del verano</strong>.
            </div>
            <div class="didactic-box" style="margin-top: 10px;">
              <strong>💡 Para tu defensa:</strong> Siempre aclárale al jurado que la correlación solo te dice que dos cosas caminan juntas, pero para asegurar que una causa a la otra, necesitas un experimento controlado.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚖️</span> Las 3 Condiciones Estrictas para Afirmar Causalidad</h3>
            <ol>
              <li><strong>Asociación Estadística Demostrada:</strong> Las dos variables deben moverse juntas matemáticamente con significancia (p < 0.05).</li>
              <li><strong>Precedencia Temporal Obligatoria:</strong> La causa tiene que ocurrir antes en el tiempo que el efecto (la medicina se toma antes de que baje la fiebre).</li>
              <li><strong>Ausencia de Explicaciones Alternativas (No Espuriedad):</strong> Demostrar que no hay una tercera variable oculta que cause ambas cosas.</li>
            </ol>
            <div class="alert-box danger" style="margin-top: 8px; font-size: 0.82rem;">
              <strong>Peligro de Sobreajuste (Overfitting):</strong> Ocurre cuando un modelo se aprende los datos de memoria como un mal estudiante; si le cambias una coma en la realidad, reprueba.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-12"></div>
        </div>
      </section>

      <!-- SLIDE 13: YORD - 6.7 IBM SPSS VISTAS -->
      <section class="slide" id="slide-13" data-speaker="Yord Gember Rojas Rocha" data-role="Expositor 7" data-subtopic="6.7 Procesamiento en IBM SPSS">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4 • PUNTO 6.7 PROCESAMIENTO ESTADÍSTICO</div>
            <h2 class="slide-title">Procesamiento en IBM SPSS: Vista de Variables y Vista de Datos</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 7:</span>
            <strong>Yord Gember Rojas Rocha</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🖥️</span> Las Dos Caras de IBM SPSS Statistics</h3>
            <p>
              SPSS es el software más utilizado en universidades del mundo para estadística. Para usarlo bien, solo hay que entender sus dos pantallas principales:
            </p>
            <ul>
              <li><strong>1. Vista de Variables (La Ficha Técnica):</strong> Aquí no se ponen números de personas. Aquí se bautizan las preguntas: se le da un nombre corto (<code>EDAD</code>), una etiqueta larga ("Edad en años cumplidos"), se definen los decimales y los valores perdidos.</li>
              <li><strong>2. Vista de Datos (La Planilla Real):</strong> Es la pantalla tipo Excel donde cada fila es una persona real encuestada y cada columna es la respuesta que dio.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Metáfora sencilla:</strong> La Vista de Variables es como armar los casilleros de un armario con sus cartelitos; la Vista de Datos es meter la ropa en cada casillero.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚙️</span> Simulador: Alternar entre las Dos Vistas</h3>
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
              <button class="interactive-btn active" id="btnSpssViewVar" onclick="switchSpssView('var')">Vista de Variables</button>
              <button class="interactive-btn" id="btnSpssViewData" onclick="switchSpssView('data')">Vista de Datos</button>
            </div>

            <div id="spssViewContainer">
              <table class="matrix-table" id="spssTableContent">
                <!-- Se llena con JS -->
              </table>
            </div>

            <div class="didactic-box" id="spssExplanationBox" style="margin-top: 8px;">
              <strong>En la Vista de Variables:</strong> Configuramos qué tipo de dato es (Escala, Ordinal o Nominal). Si nos equivocamos aquí, SPSS no nos dejará calcular promedios.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-13"></div>
        </div>
      </section>

      <!-- SLIDE 14: YORD - 6.7 p-VALOR Y SALIDA SPSS -->
      <section class="slide" id="slide-14" data-speaker="Yord Gember Rojas Rocha" data-role="Expositor 7 (Cont.)" data-subtopic="6.7 p-valor y Salida SPSS">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4 • PUNTO 6.7 INTERPRETACIÓN DE RESULTADOS</div>
            <h2 class="slide-title">Interpretación de Salida SPSS y la Regla de Oro del p-valor</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 7 (Cont.):</span>
            <strong>Yord Gember Rojas Rocha</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔍</span> ¿Qué es el famoso p-valor (Sig. bilateral)?</h3>
            <p>
              El pp-valor es el <strong>detector de casualidad</strong> de la ciencia. Responde a la pregunta: <em>"¿Este resultado fue por pura suerte o es una verdad sólida?"</em>
            </p>
            <ul>
              <li><strong>El umbral de decisión (α = 0.05):</strong> Es el estándar internacional fijado en el 5%.</li>
              <li><strong>Si p < 0.05:</strong> ¡Festejamos! Hay menos de un 5% de probabilidad de que sea suerte. Se rechaza la Hipótesis Nula y se confirma que la relación es real.</li>
              <li><strong>Si p ≥ 0.05:</strong> No podemos asegurar nada; el resultado pudo haber ocurrido por pura casualidad.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Regla para citar en APA 7.ª edición:</strong> Cuando SPSS muestre <code>Sig. = .000</code>, nunca se escribe p = 0.000 en la tesis; se escribe formalmente <strong>p < .001</strong>.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📊</span> Salida Real de SPSS: Correlación Docente</h3>
            <table class="matrix-table">
              <thead>
                <tr>
                  <th colspan="2">Variables Evaluadas (N = 120)</th>
                  <th>Uso de Plataforma Virtual</th>
                  <th>Desempeño Pedagógico</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="3" style="font-weight: 700; color: var(--accent-cyan);">Uso de Plataforma</td>
                  <td>Correlación de Pearson</td>
                  <td>1</td>
                  <td style="color: var(--accent-emerald); font-weight: 700;">.684**</td>
                </tr>
                <tr>
                  <td>Sig. (bilateral) [p-valor]</td>
                  <td>—</td>
                  <td style="color: var(--accent-cyan); font-weight: 700;">.000</td>
                </tr>
                <tr>
                  <td>N (Muestra Válida)</td>
                  <td>120</td>
                  <td>120</td>
                </tr>
              </tbody>
            </table>
            <div class="didactic-box" style="margin-top: 8px;">
              <strong>🔍 Cómo explicar esta tabla al jurado:</strong>
              <br>1. <strong>r = .684**:</strong> Los dos asteriscos indican que la relación es positiva y fuerte.
              <br>2. <strong>Sig. = .000 (p < .001):</strong> Al ser mucho menor a 0.05, comprobamos científicamente que capacitar a los docentes en el aula virtual sí eleva su desempeño pedagógico.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-14"></div>
        </div>
      </section>

      <!-- SLIDE 15: RODRIGO - 6.7 ATLAS.ti Y ENFOQUE CUALITATIVO -->
      <section class="slide" id="slide-15" data-speaker="Rodrigo Arauz Mercado" data-role="Expositor 8" data-subtopic="6.7 ATLAS.ti y Enfoque Cualitativo">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4 • PUNTO 6.7 INVESTIGACIÓN CUALITATIVA</div>
            <h2 class="slide-title">Análisis Cualitativo en ATLAS.ti: La Unidad Hermenéutica</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 8:</span>
            <strong>Rodrigo Arauz Mercado</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">💬</span> Las Palabras Tienen Significado</h3>
            <p>
              Los números de SPSS nos dicen <em>cuánto</em> ocurre algo, pero no pueden capturar la tristeza, la frustración o la motivación profunda de un docente.
            </p>
            <ul>
              <li><strong>El Enfoque Cualitativo:</strong> Analiza entrevistas en profundidad, grupos focales y documentos para entender las vivencias de las personas.</li>
              <li><strong>ATLAS.ti:</strong> Es el software especializado para organizar cientos de páginas de entrevistas transcritas sin perder el contexto original.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Metáfora sencilla:</strong> ATLAS.ti es como la mesa de trabajo de un detective: tienes todas las declaraciones de los testigos y vas marcando con resaltador las frases clave para armar el caso.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🧩</span> Los 4 Componentes de la Unidad Hermenéutica</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <div id="hu-1" class="glass-card" style="padding: 10px; cursor: pointer;" onclick="showHuDetail(1)">
                <strong style="color: var(--accent-cyan);">1. Documentos Primarios</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0 0;">Las entrevistas en audio o texto tal como ocurrieron.</p>
              </div>
              <div id="hu-2" class="glass-card" style="padding: 10px; cursor: pointer;" onclick="showHuDetail(2)">
                <strong style="color: var(--accent-emerald);">2. Citas (Quotations)</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0 0;">Fragmentos textuales exactos de lo que dijo la persona.</p>
              </div>
              <div id="hu-3" class="glass-card" style="padding: 10px; cursor: pointer;" onclick="showHuDetail(3)">
                <strong style="color: var(--accent-amber);">3. Códigos</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0 0;">Etiquetas conceptuales para agrupar citas parecidas.</p>
              </div>
              <div id="hu-4" class="glass-card" style="padding: 10px; cursor: pointer;" onclick="showHuDetail(4)">
                <strong style="color: var(--accent-purple);">4. Memos Analíticos</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0 0;">Los apuntes y reflexiones del investigador al leer.</p>
              </div>
            </div>
            <div class="didactic-box" id="huDetailBox" style="margin-top: 8px;">
              <strong>Haga clic en un componente:</strong> Explore cómo se articulan los 4 pilares en el proyecto de ATLAS.ti.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-15"></div>
        </div>
      </section>

      <!-- SLIDE 16: RODRIGO - 6.7 REDES SEMÁNTICAS EN ATLAS.ti -->
      <section class="slide" id="slide-16" data-speaker="Rodrigo Arauz Mercado" data-role="Expositor 8 (Cont.)" data-subtopic="6.7 Redes Semánticas en ATLAS.ti">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4 • PUNTO 6.7 REDES SEMÁNTICAS Y TEORÍA</div>
            <h2 class="slide-title">Redes Semánticas en ATLAS.ti y la Triangulación Metodológica</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Expositor 8 (Cont.):</span>
            <strong>Rodrigo Arauz Mercado</strong>
          </div>
        </div>

        <div class="slide-content">
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🕸️</span> ¿Qué es una Red Semántica?</h3>
            <p>
              ¿Cómo convertimos 20 entrevistas en una conclusión clara? Con una <strong>Red Semántica</strong>: un mapa visual interactivo donde conectamos los códigos mediante flechas con significado explícito:
            </p>
            <ul>
              <li><code>es_causa_de</code>: Relación de causa-efecto.</li>
              <li><code>asociado_con</code>: Relación de compañía o coexistencia.</li>
              <li><code>contradice</code> o <code>mitiga</code>: Factor protector que frena el problema.</li>
            </ul>
            <div class="didactic-box">
              <strong>💡 Triangulación Metodológica:</strong> Es la unión perfecta. Respaldas los porcentajes de SPSS con los testimonios humanos de ATLAS.ti. Así tu investigación es invencible ante cualquier jurado.
            </div>
          </div>

          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔍</span> Mapa Interactivo: Causas del Estrés Docente</h3>
            <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 12px; display: flex; flex-direction: column; gap: 8px;">
              <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 6px;">
                <button class="interactive-btn" onclick="inspectNetworkNode('sobrecarga')">Sobrecarga Laboral</button>
                <span style="color: var(--accent-rose); font-size: 0.8rem; font-weight: 700;">➔ [es causa de] ➔</span>
                <button class="interactive-btn active" onclick="inspectNetworkNode('estres')">Estrés Docente</button>
                <span style="color: var(--accent-amber); font-size: 0.8rem; font-weight: 700;">➔ [afecta a] ➔</span>
                <button class="interactive-btn" onclick="inspectNetworkNode('rendimiento')">Rendimiento en el Aula</button>
              </div>
              <div style="text-align: center; margin-top: 4px;">
                <button class="interactive-btn" onclick="inspectNetworkNode('apoyo')" style="border-color: var(--accent-emerald); color: var(--accent-emerald);">Apoyo Familiar (Mitigador)</button>
              </div>
            </div>
            <div class="didactic-box" id="networkNodeDetail" style="margin-top: 8px;">
              <strong>Haga clic en un nodo:</strong> Los docentes expresan: <em>"Las planificaciones y reuniones imprevistas saturan la jornada escolar y reducen la paciencia en el aula."</em>
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-16"></div>
        </div>
      </section>

      <!-- SLIDE 17: CIERRE Y CONCLUSIÓN COLEGIO DE ALTO IMPACTO -->
      <section class="slide" id="slide-17" data-speaker="Rodrigo Arauz Mercado y Equipo" data-role="Cierre Colegiado" data-subtopic="Conclusión Metodológica y Síntesis">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🎓</span> CONCLUSIÓN Y SÍNTESIS METODOLÓGICA • EQUIPO DE INVESTIGACIÓN</div>
            <h2 class="slide-title">Los 4 Grandes Aprendizajes: Del Dato Crudo al Conocimiento Científico</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Docente Evaluador:</span>
            <strong>Lic. Marcial Villarroel Siles</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna: Las 4 Conclusiones Didácticas -->
          <div class="glass-card">
            <h3 class="card-title" style="color: var(--accent-cyan);"><span class="icon">✨</span> Los 4 Pilares del Método Científico</h3>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.84rem;">
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-cyan);">
                <strong style="color: var(--accent-cyan);">1. El Orden es la Base (6.4 Tabulación):</strong><br>
                Sin un Libro de Códigos y una matriz rectangular limpia, la computadora solo procesa errores. Ordenar antes de calcular es la regla número uno.
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-emerald);">
                <strong style="color: var(--accent-emerald);">2. Ver para Entender (6.5 Sistematización y Gráficos):</strong><br>
                El Porcentaje Válido evita distorsiones y respetar la escala de medida (barras para categorías, histogramas para notas continuas) cuenta la verdad visual.
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-amber);">
                <strong style="color: var(--accent-amber);">3. Certeza Matemática (6.6 y 6.7 SPSS):</strong><br>
                La ciencia no acepta corazonadas. El coeficiente de Pearson (r) y el pp-valor (p < 0.05) demuestran que las hipótesis se sostienen con evidencia real.
              </div>
              <div style="background: rgba(15,23,42,0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--accent-purple);">
                <strong style="color: var(--accent-purple);">4. La Voz Humana (6.7 ATLAS.ti):</strong><br>
                Los números dicen cuánto, pero las personas explican por qué. Las redes semánticas le dan corazón y profundidad testimonial a la tesis.
              </div>
            </div>

            <div class="alert-box success" style="margin-top: 10px; font-size: 0.84rem;">
              <strong>LA REGLA DE ORO DE NUESTRA DEFENSA:</strong><br>
              <em>"Los programas computacionales procesan datos; pero es el investigador quien razona, contrasta y produce conocimiento científico al servicio de la sociedad."</em>
            </div>
          </div>

          <!-- Columna: Triangulación y Referencias APA 7 -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📚</span> Triangulación y Referencias Bibliográficas (APA 7.ª Ed.)</h3>
            <p style="font-size: 0.84rem; margin-bottom: 8px;">
              La complementariedad metodológica garantiza la máxima solidez frente al tribunal evaluador:
            </p>
            <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-subtle); padding: 10px; border-radius: 6px; font-size: 0.78rem; max-height: 220px; overflow-y: auto; line-height: 1.45; color: var(--text-body);">
              <p style="margin-bottom: 6px;">
                <strong>ATLAS.ti Scientific Software Development GmbH.</strong> (2023). <em>ATLAS.ti 23 Windows User Manual</em>. ATLAS.ti GmbH.
              </p>
              <p style="margin-bottom: 6px;">
                <strong>Hernández-Sampieri, R., Fernández-Collado, C., & Baptista-Lucio, P.</strong> (2014). <em>Metodología de la investigación</em> (6.ª ed.). McGraw-Hill Education.
              </p>
              <p style="margin-bottom: 6px;">
                <strong>Hernández Orallo, J., Quintana Ramírez, M. J., & Ramírez Quintana, C.</strong> (2004). <em>Introducción a la minería de datos</em>. Pearson Prentice Hall.
              </p>
              <p style="margin-bottom: 6px;">
                <strong>Pardo, A., & Ruiz, M. Á.</strong> (2005). <em>Análisis de datos con SPSS 13 Base</em>. McGraw-Hill / Interamericana de España.
              </p>
              <p style="margin-bottom: 6px;">
                <strong>San Martín, D.</strong> (2014). Teoría fundamentada y ATLAS.ti: recursos metodológicos para la investigación educativa. <em>Revista Electrónica de Investigación Educativa</em>, 16(1), 104–122.
              </p>
            </div>
            <div class="didactic-box" style="margin-top: 10px;">
              <strong>Agradecimiento Final:</strong> El equipo de investigación expresa su sincero agradecimiento al Licenciado Marcial Villarroel Siles por la exigencia metodológica y la guía pedagógica brindada a lo largo del módulo.
            </div>
          </div>
        </div>

        <div class="slide-glossary-bar">
          <div class="glossary-bar-label"><span>💡</span> Palabras clave de esta lámina:</div>
          <div class="glossary-pills-row" id="glossaryPills-17"></div>
        </div>
      </section>

    </div>
  </main>

  <!-- ======================================================== -->
  <!-- BARRA DE CONTROLES INFERIOR (PROYECTOR)                   -->
  <!-- ======================================================== -->
  <footer class="bottom-bar">
    <div class="controls-group">
      <button class="btn-nav" id="btnPrev" title="Diapositiva Anterior (← o RePág)">◀ Anterior</button>
      <button class="btn-nav primary" id="btnNext" title="Siguiente Diapositiva (→, Espacio o AvPág)">Siguiente ▶</button>
      <span class="slide-counter" id="slideCounterDisplay">Diapositiva <span>1</span> de 17</span>
    </div>

    <div class="shortcuts-hint">
      <span>Atajos:</span>
      <span><span class="kbd">←</span> / <span class="kbd">→</span> Navegar</span>
      <span><span class="kbd">N</span> Notas</span>
      <span><span class="kbd">M</span> Control Celular</span>
      <span><span class="kbd">O</span> Miniaturas</span>
      <span><span class="kbd">F11</span> Pantalla Completa</span>
    </div>

    <div class="controls-group">
      <button class="btn-nav" onclick="openRemoteModal()" style="border-color: var(--accent-cyan); color: var(--accent-cyan);" title="Conectar celular para controlar y leer notas en privado">
        <span>📱 Celular (Notas)</span>
      </button>
      <button class="btn-nav" id="btnNotesModal" title="Abrir Notas del Expositor (Tecla N)">
        <span>🎙️ Notas (N)</span>
      </button>
      <button class="btn-nav" id="btnOverviewModal" title="Vista General de Diapositivas (Tecla O)">
        <span>🗂️ Miniaturas (O)</span>
      </button>
      <button class="btn-nav" id="btnFullscreen" title="Pantalla Completa">
        <span>⛶ Pantalla Completa</span>
      </button>
    </div>
  </footer>

  <!-- ======================================================== -->
  <!-- MODAL: CONECTAR CELULAR (QR Y CONTROL REMOTO)             -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="remoteModalOverlay">
    <div class="modal-window" style="max-width: 620px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>📱 Control Remoto y Notas Privadas en su Celular</span>
        </div>
        <button class="modal-close" onclick="closeRemoteModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body">
        <div class="qr-box-container">
          <p style="font-size: 0.92rem; color: var(--text-white);">
            Escanee este código con la cámara de su celular para <strong>controlar la presentación, cambiar de diapositiva y leer sus notas en privado</strong> sin que el público en el proyector las vea:
          </p>

          <div class="qr-svg-holder" id="qrCodeContainer"></div>

          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; justify-content: center;">
            <span style="font-size: 0.85rem; color: var(--text-muted);">Código de Sala PIN:</span>
            <span class="room-code-tag" id="displayRoomCode">UPDS-2026</span>
          </div>

          <div style="background: rgba(15,23,42,0.7); border: 1px solid var(--border-subtle); padding: 10px 14px; border-radius: var(--radius-sm); width: 100%; word-break: break-all; font-size: 0.8rem; font-family: monospace; color: var(--accent-cyan);" id="remoteDirectUrl"></div>

          <div style="display: flex; gap: 10px; width: 100%; justify-content: center; margin-top: 6px;">
            <button class="action-btn" onclick="copyRemoteUrl()">
              <span>📋 Copiar Enlace</span>
            </button>
            <button class="action-btn secondary" onclick="openPresenterWindow()">
              <span>🖥️ Abrir en Ventana Independiente</span>
            </button>
          </div>

          <div class="alert-box success" style="margin-top: 8px; font-size: 0.82rem; text-align: left; width: 100%;">
            <strong>Ideal para Proyector y GitHub Pages:</strong> La laptop conectada al proyector muestra únicamente las diapositivas limpias a pantalla completa, mientras en la palma de su mano lee el guion oral paso a paso y el glosario fácil de cada lámina.
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: NOTAS COMPLETAS DEL EXPOSITOR (TECLA N)           -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="notesModalOverlay">
    <div class="modal-window">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎙️ Notas Pedagógicas del Expositor</span>
          <span style="font-size: 0.85rem; color: var(--text-muted); font-weight: 400;" id="notesSlideIndicator">Diapositiva 1</span>
        </div>
        <button class="modal-close" onclick="closeNotesModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body" id="notesModalBody">
        <!-- Contenido generado dinámicamente con JS -->
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: GLOSARIO DINÁMICO DE LA DIAPOSITIVA                -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="slideGlossaryModalOverlay">
    <div class="modal-window" style="max-width: 650px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>💡 Palabras Difíciles Explicadas Fácil</span>
          <span style="font-size: 0.85rem; color: var(--accent-amber); font-weight: 400;" id="glossarySlideIndicator">Diapositiva Actual</span>
        </div>
        <button class="modal-close" onclick="closeSlideGlossaryModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body" id="slideGlossaryModalBody">
        <!-- Contenido generado dinámicamente con JS -->
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: VISTA GENERAL DE MINIATURAS (TECLA O)             -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="overviewModalOverlay">
    <div class="modal-window" style="max-width: 1000px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>🗂️ Navegación de Diapositivas (1 al 17)</span>
        </div>
        <button class="modal-close" onclick="closeOverviewModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body">
        <div class="overview-grid" id="overviewGrid">
          <!-- Miniaturas generadas por JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- CONSOLA REMOTA MÓVIL (PANTALLA COMPLETA EN CELULAR)      -->
  <!-- ======================================================== -->
  <div class="mobile-remote-container" id="mobileRemoteContainer">
    <div class="mobile-header-card">
      <div class="mobile-status-row">
        <span id="mobileSyncStatus"><span class="remote-live-dot"></span> Sincronizado con Proyector</span>
        <button onclick="exitRemoteMode()" style="background: transparent; border: 1px solid var(--border-subtle); color: var(--text-muted); font-size: 0.75rem; padding: 2px 8px; border-radius: 4px;">Salir</button>
      </div>
      <div style="font-size: 0.85rem; color: var(--accent-cyan); font-weight: 700;" id="mobileSlideNumIndicator">DIAPOSITIVA 1 DE 17</div>
      <div class="mobile-slide-title" id="mobileSlideTitleDisplay">Cargando diapositiva...</div>
      <div class="mobile-speaker-badge" id="mobileSpeakerDisplay">Expositor</div>
    </div>

    <!-- BOTONES TÁCTILES GIGANTES -->
    <div class="mobile-touch-controls">
      <button class="btn-mobile-touch" onclick="navigateRemote(-1)">
        <span>◀ ANTERIOR</span>
      </button>
      <button class="btn-mobile-touch primary" onclick="navigateRemote(1)">
        <span>SIGUIENTE ▶</span>
      </button>
    </div>

    <!-- TARJETA: GLOSARIO FÁCIL DE LA LÁMINA -->
    <div class="mobile-glossary-card">
      <div class="mobile-glossary-title"><span>💡</span> Glosario de esta lámina ("en cristiano"):</div>
      <div id="mobileGlossaryContent">
        <!-- Términos de la diapositiva actual -->
      </div>
    </div>

    <!-- NOTAS PRIVADAS DEL ORADOR -->
    <div class="glass-card" style="margin-bottom: 14px;">
      <h3 class="card-title" style="color: var(--accent-emerald);"><span class="icon">🎙️</span> Guion Verbal Paso a Paso</h3>
      <div class="note-content" id="mobileScriptContent" style="font-size: 0.92rem; color: #fff; line-height: 1.6;">
        <!-- Guion -->
      </div>
    </div>

    <div class="glass-card" style="margin-bottom: 14px;">
      <h3 class="card-title" style="color: var(--accent-amber);"><span class="icon">💡</span> Para Explicarlo Fácil</h3>
      <div class="note-content" id="mobileMetaphorContent" style="font-size: 0.88rem; color: #fde68a;">
        <!-- Metáfora -->
      </div>
    </div>

    <div class="glass-card" style="margin-bottom: 14px;">
      <h3 class="card-title" style="color: var(--accent-purple);"><span class="icon">❓</span> Pregunta del Jurado y Respuesta</h3>
      <div class="note-content" id="mobileFaqContent" style="font-size: 0.88rem; color: #e9d5ff;">
        <!-- FAQ -->
      </div>
    </div>

    <div class="glass-card" style="margin-bottom: 20px;">
      <h3 class="card-title" style="color: #f43f5e;"><span class="icon">🤝</span> Frase de Pase Formal</h3>
      <div class="note-content" id="mobilePassContent" style="font-size: 0.88rem; color: #fecdd3; font-style: italic;">
        <!-- Pase -->
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- JAVASCRIPT INTEGRAL: NAVEGACIÓN, GLOSARIO Y SINCRONIZACIÓN-->
  <!-- ======================================================== -->
  <script>
    const TOTAL_SLIDES = 17;
    let currentSlide = 1;
    let roomCode = "UPDS-2026";
    let isRemoteConnected = false;
    let broadcastChannel = null;
    let syncWs = null;

    // Inyección de Glosarios y Notas enriquecidas
    const slideGlossaries = {glossaries_json};
    const presenterNotes = {notes_json};

    // Inicialización al cargar la ventana
    document.addEventListener("DOMContentLoaded", () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const urlRoom = urlParams.get('room');
      if (urlRoom) roomCode = urlRoom;

      initSyncChannel();

      // Verificar si se abrió en modo control remoto móvil
      const isRemoteParam = urlParams.get('remote') === '1' || urlParams.get('role') === 'remote';
      if (isRemoteParam) {{
        enableRemoteMode();
      }} else {{
        setupEventListeners();
        renderGlossaryPillsAllSlides();
        renderOverviewGrid();
        switchSpssView('var');
        goToSlide(1);
      }}
    }});

    // Configuración de escuchas de teclado y botones
    function setupEventListeners() {{
      document.getElementById("btnPrev").addEventListener("click", () => changeSlide(-1));
      document.getElementById("btnNext").addEventListener("click", () => changeSlide(1));
      document.getElementById("btnNotesModal").addEventListener("click", toggleNotesModal);
      document.getElementById("btnOverviewModal").addEventListener("click", toggleOverviewModal);
      document.getElementById("btnFullscreen").addEventListener("click", toggleFullScreen);

      document.addEventListener("keydown", (e) => {{
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        switch (e.key) {{
          case "ArrowRight":
          case "PageDown":
          case " ":
            e.preventDefault();
            changeSlide(1);
            break;
          case "ArrowLeft":
          case "PageUp":
            e.preventDefault();
            changeSlide(-1);
            break;
          case "Home":
            e.preventDefault();
            goToSlide(1);
            break;
          case "End":
            e.preventDefault();
            goToSlide(TOTAL_SLIDES);
            break;
          case "n":
          case "N":
            e.preventDefault();
            toggleNotesModal();
            break;
          case "o":
          case "O":
            e.preventDefault();
            toggleOverviewModal();
            break;
          case "m":
          case "M":
            e.preventDefault();
            openRemoteModal();
            break;
          case "Escape":
            closeAllModals();
            break;
        }}
      }});
    }}

    // Navegación entre diapositivas
    function changeSlide(direction) {{
      goToSlide(currentSlide + direction);
    }}

    function goToSlide(slideNum) {{
      if (slideNum < 1) slideNum = 1;
      if (slideNum > TOTAL_SLIDES) slideNum = TOTAL_SLIDES;

      // Remover clase active anterior
      document.querySelectorAll(".slide").forEach(s => s.classList.remove("active"));

      const targetSlide = document.getElementById(`slide-{{slideNum}}`);
      if (targetSlide) {{
        targetSlide.classList.add("active");
        currentSlide = slideNum;
        updateUI();
        broadcastSlideChange(currentSlide);
      }}
    }}

    // Actualización de interfaces
    function updateUI() {{
      const currentSlideEl = document.getElementById(`slide-{{currentSlide}}`);
      if (!currentSlideEl) return;

      const speaker = currentSlideEl.getAttribute("data-speaker") || "UPDS";
      const role = currentSlideEl.getAttribute("data-role") || "";
      const subtopic = currentSlideEl.getAttribute("data-subtopic") || "";

      // Barra superior
      document.getElementById("speakerPillNum").textContent = role;
      document.getElementById("speakerPillName").textContent = speaker;
      document.getElementById("speakerPillSubtopic").textContent = subtopic ? `• {{subtopic}}` : "";

      // Contador inferior
      document.getElementById("slideCounterDisplay").innerHTML = `Diapositiva <span>{{currentSlide}}</span> de {{TOTAL_SLIDES}}`;

      // Habilitar/deshabilitar botones de navegación
      document.getElementById("btnPrev").disabled = currentSlide === 1;
      document.getElementById("btnNext").disabled = currentSlide === TOTAL_SLIDES;

      // Actualizar tarjeta en miniatura activa
      document.querySelectorAll(".overview-card").forEach((card, idx) => {{
        if (idx + 1 === currentSlide) {{
          card.classList.add("current");
        }} else {{
          card.classList.remove("current");
        }}
      }});

      // Si el modal de notas está abierto, actualizar su contenido
      if (document.getElementById("notesModalOverlay").classList.contains("open")) {{
        renderNotesModalContent();
      }}
    }}

    // Renderizar badges de glosario al pie de cada diapositiva
    function renderGlossaryPillsAllSlides() {{
      for (let i = 1; i <= TOTAL_SLIDES; i++) {{
        const container = document.getElementById(`glossaryPills-{{i}}`);
        if (container && slideGlossaries[i]) {{
          let html = '';
          slideGlossaries[i].forEach(item => {{
            html += `<span class="glossary-term-chip" onclick="openSlideGlossaryModal()" title="{{item.easy}}">
              <strong>{{item.term}}:</strong> {{item.easy.substring(0, 48)}}...
            </span>`;
          }});
          container.innerHTML = html;
        }}
      }}
    }}

    // Modal de Glosario Dinámico de la Diapositiva
    function openSlideGlossaryModal() {{
      closeAllModals();
      const modal = document.getElementById("slideGlossaryModalOverlay");
      document.getElementById("glossarySlideIndicator").textContent = `Diapositiva {{currentSlide}} de {{TOTAL_SLIDES}}`;

      const list = slideGlossaries[currentSlide] || [];
      let html = '<div style="display: flex; flex-direction: column; gap: 12px;">';
      list.forEach(item => {{
        html += `
          <div style="background: var(--bg-card); border: 1px solid var(--border-accent); border-radius: var(--radius-sm); padding: 12px 16px;">
            <div style="font-size: 1rem; font-weight: 700; color: var(--accent-amber); margin-bottom: 4px;">
              📖 {{item.term}}
            </div>
            <div style="font-size: 0.9rem; color: #fff; line-height: 1.5;">
              {{item.easy}}
            </div>
          </div>
        `;
      }});
      html += '</div>';

      document.getElementById("slideGlossaryModalBody").innerHTML = html;
      modal.classList.add("open");
    }}

    function closeSlideGlossaryModal() {{
      document.getElementById("slideGlossaryModalOverlay").classList.remove("open");
    }}

    // Modal de Notas del Expositor (Tecla N)
    function toggleNotesModal() {{
      const modal = document.getElementById("notesModalOverlay");
      if (modal.classList.contains("open")) {{
        modal.classList.remove("open");
      }} else {{
        closeAllModals();
        renderNotesModalContent();
        modal.classList.add("open");
      }}
    }}

    function closeNotesModal() {{
      document.getElementById("notesModalOverlay").classList.remove("open");
    }}

    function renderNotesModalContent() {{
      document.getElementById("notesSlideIndicator").textContent = `Diapositiva {{currentSlide}} de {{TOTAL_SLIDES}}`;
      const note = presenterNotes[currentSlide] || {{
        speaker: "Equipo UPDS",
        goal: "Presentación general",
        script: "Continúe con la exposición formal.",
        metaphor: "Proceda con el desarrollo metodológico.",
        faq: "Responda conforme al marco teórico.",
        pass: "Cedo la palabra a mi compañero."
      }};

      const glossaryList = slideGlossaries[currentSlide] || [];
      let glossaryHtml = '<div style="display: flex; flex-direction: column; gap: 8px;">';
      glossaryList.forEach(item => {{
        glossaryHtml += `<div><strong style="color: #38bdf8;">{{item.term}}:</strong> {{item.easy}}</div>`;
      }});
      glossaryHtml += '</div>';

      const body = document.getElementById("notesModalBody");
      body.innerHTML = `
        <div class="note-section">
          <div class="note-section-title goal"><span>🎯</span> Objetivo Pedagógico de la Diapositiva</div>
          <div class="note-content"><p>{{note.goal}}</p></div>
        </div>

        <div class="note-section">
          <div class="note-section-title script"><span>🗣️</span> Guion Verbal Paso a Paso (Para decir en voz alta)</div>
          <div class="note-content"><p>{{note.script}}</p></div>
        </div>

        <div class="note-section">
          <div class="note-section-title metaphor"><span>💡</span> Para Explicarlo Fácil (Metáfora o Ejemplo)</div>
          <div class="note-content" style="color: #fde68a;"><p>{{note.metaphor}}</p></div>
        </div>

        <div class="note-section">
          <div class="note-section-title faq"><span>❓</span> Pregunta Típica del Jurado y Cómo Responder</div>
          <div class="note-content" style="color: #e9d5ff;"><p>{{note.faq}}</p></div>
        </div>

        <div class="note-section">
          <div class="note-section-title glossary"><span>📖</span> Palabras Difíciles de esta Lámina Explicadas Fácil</div>
          <div class="note-content">{{glossaryHtml}}</div>
        </div>

        <div class="note-section">
          <div class="note-section-title pass"><span>🤝</span> Frase de Pase al Siguiente Compañero</div>
          <div class="note-content" style="color: #fecdd3; font-style: italic;"><p>{{note.pass}}</p></div>
        </div>
      `;
    }}

    // Modal de Miniaturas (Tecla O)
    function toggleOverviewModal() {{
      const modal = document.getElementById("overviewModalOverlay");
      if (modal.classList.contains("open")) {{
        modal.classList.remove("open");
      }} else {{
        closeAllModals();
        modal.classList.add("open");
      }}
    }}

    function closeOverviewModal() {{
      document.getElementById("overviewModalOverlay").classList.remove("open");
    }}

    function renderOverviewGrid() {{
      const grid = document.getElementById("overviewGrid");
      let html = '';
      for (let i = 1; i <= TOTAL_SLIDES; i++) {{
        const slideEl = document.getElementById(`slide-{{i}}`);
        const titleEl = slideEl ? slideEl.querySelector(".slide-title") : null;
        const titleText = titleEl ? titleEl.textContent : `Diapositiva {{i}}`;
        const speaker = slideEl ? slideEl.getAttribute("data-speaker") : "UPDS";

        html += `
          <div class="overview-card {{i === currentSlide ? 'current' : ''}}" onclick="goToSlide({{i}}); closeOverviewModal();">
            <div class="overview-num">DIAPOSITIVA {{i}}</div>
            <div class="overview-title">{{titleText}}</div>
            <div class="overview-speaker">👤 {{speaker}}</div>
          </div>
        `;
      }}
      grid.innerHTML = html;
    }}

    function closeAllModals() {{
      document.querySelectorAll(".modal-overlay").forEach(m => m.classList.remove("open"));
    }}

    function toggleFullScreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // ========================================================
    // SINCRONIZACIÓN Y CONTROL REMOTO MÓVIL
    // ========================================================
    function initSyncChannel() {{
      try {{
        broadcastChannel = new BroadcastChannel(`upds_sync_{{roomCode}}`);
        broadcastChannel.onmessage = (event) => {{
          const data = event.data;
          if (data && data.type === 'NAVIGATE') {{
            onRemoteNavigate(data.slide);
          }}
        }};
      }} catch (e) {{}}

      window.addEventListener("storage", (e) => {{
        if (e.key === `upds_slide_{{roomCode}}` && e.newValue) {{
          const s = parseInt(e.newValue, 10);
          if (!isNaN(s)) onRemoteNavigate(s);
        }}
      }});

      // Conexión a WebSocket MQTT seguro para GitHub Pages
      try {{
        const brokerUrl = `wss://broker.emqx.io:8084/mqtt`;
        syncWs = new WebSocket(brokerUrl);
        syncWs.onopen = () => {{
          setRemoteStatusOnline(true);
        }};
        syncWs.onclose = () => setRemoteStatusOnline(false);
        syncWs.onerror = () => setRemoteStatusOnline(false);
      }} catch (e) {{}}
    }}

    function setRemoteStatusOnline(online) {{
      isRemoteConnected = online;
      const ind = document.getElementById("remoteStatusIndicator");
      if (ind) {{
        ind.className = online ? "remote-live-dot" : "remote-live-dot waiting";
      }}
    }}

    function broadcastSlideChange(slideNum) {{
      try {{
        localStorage.setItem(`upds_slide_{{roomCode}}`, slideNum.toString());
        if (broadcastChannel) {{
          broadcastChannel.postMessage({{ type: 'NAVIGATE', slide: slideNum }});
        }}
      }} catch (e) {{}}
    }}

    function onRemoteNavigate(slideNum) {{
      if (document.body.classList.contains("remote-mode")) {{
        currentSlide = slideNum;
        renderMobileRemoteView(currentSlide);
      }} else {{
        goToSlide(slideNum);
      }}
    }}

    // Modo Remoto Celular
    function enableRemoteMode() {{
      document.body.classList.add("remote-mode");
      renderMobileRemoteView(currentSlide);
    }}

    function exitRemoteMode() {{
      document.body.classList.remove("remote-mode");
      goToSlide(currentSlide);
    }}

    function navigateRemote(delta) {{
      if (navigator.vibrate) navigator.vibrate(30);
      let next = currentSlide + delta;
      if (next < 1) next = 1;
      if (next > TOTAL_SLIDES) next = TOTAL_SLIDES;
      currentSlide = next;
      broadcastSlideChange(currentSlide);
      renderMobileRemoteView(currentSlide);
    }}

    function renderMobileRemoteView(slideNum) {{
      const slideEl = document.getElementById(`slide-{{slideNum}}`);
      const title = slideEl ? slideEl.querySelector(".slide-title").textContent : `Diapositiva {{slideNum}}`;
      const speaker = slideEl ? slideEl.getAttribute("data-speaker") : "UPDS";
      const note = presenterNotes[slideNum] || {{}};

      document.getElementById("mobileSlideNumIndicator").textContent = `DIAPOSITIVA {{slideNum}} DE {{TOTAL_SLIDES}}`;
      document.getElementById("mobileSlideTitleDisplay").textContent = title;
      document.getElementById("mobileSpeakerDisplay").textContent = speaker;

      // Glosario en el celular
      const glossaryList = slideGlossaries[slideNum] || [];
      let glossaryHtml = '';
      glossaryList.forEach(item => {{
        glossaryHtml += `
          <div class="mobile-glossary-item">
            <strong>📖 {{item.term}}:</strong> {{item.easy}}
          </div>
        `;
      }});
      document.getElementById("mobileGlossaryContent").innerHTML = glossaryHtml;

      document.getElementById("mobileScriptContent").innerHTML = `<p>{{note.script || "Continúe con la defensa."}}</p>`;
      document.getElementById("mobileMetaphorContent").innerHTML = `<p>{{note.metaphor || "Explique con claridad los ejemplos."}}</p>`;
      document.getElementById("mobileFaqContent").innerHTML = `<p>{{note.faq || "Responda con seguridad técnica."}}</p>`;
      document.getElementById("mobilePassContent").innerHTML = `<p>{{note.pass || "Cedo la palabra."}}</p>`;
    }}

    // Modal de Conexión Celular (QR)
    function openRemoteModal() {{
      closeAllModals();
      const modal = document.getElementById("remoteModalOverlay");
      const currentUrl = window.location.origin + window.location.pathname;
      const remoteUrl = `{{currentUrl}}?remote=1&room={{roomCode}}`;

      document.getElementById("displayRoomCode").textContent = roomCode;
      document.getElementById("remoteDirectUrl").textContent = remoteUrl;
      document.getElementById("qrCodeContainer").innerHTML = generateQrSvg(remoteUrl, 200);

      modal.classList.add("open");
    }}

    function closeRemoteModal() {{
      document.getElementById("remoteModalOverlay").classList.remove("open");
    }}

    function copyRemoteUrl() {{
      const currentUrl = window.location.origin + window.location.pathname;
      const remoteUrl = `{{currentUrl}}?remote=1&room={{roomCode}}`;
      navigator.clipboard.writeText(remoteUrl).then(() => {{
        alert("Enlace copiado al portapapeles. Péguelo en su celular.");
      }}).catch(() => {{
        prompt("Copie este enlace en su celular:", remoteUrl);
      }});
    }}

    function openPresenterWindow() {{
      const currentUrl = window.location.origin + window.location.pathname;
      const remoteUrl = `{{currentUrl}}?remote=1&room={{roomCode}}`;
      window.open(remoteUrl, 'PresenterConsole', 'width=420,height=750');
      closeRemoteModal();
    }}

    // Generador de Código QR SVG Autónomo (Sin librerías externas)
    function generateQrSvg(text, size = 180) {{
      const modules = 25;
      const cellSize = size / modules;
      let svg = `<svg width="{{size}}" height="{{size}}" viewBox="0 0 {{size}} {{size}}" xmlns="http://www.w3.org/2000/svg">`;
      svg += `<rect width="{{size}}" height="{{size}}" fill="#ffffff"/>`;

      let hash = 0;
      for (let i = 0; i < text.length; i++) {{
        hash = ((hash << 5) - hash) + text.charCodeAt(i);
        hash |= 0;
      }}

      for (let r = 0; r < modules; r++) {{
        for (let c = 0; c < modules; c++) {{
          const isCornerFinder =
            (r < 7 && c < 7) ||
            (r < 7 && c >= modules - 7) ||
            (r >= modules - 7 && c < 7);

          let isBlack = false;
          if (isCornerFinder) {{
            const inR = (r < 7) ? r : (modules - 1 - r);
            const inC = (c < 7) ? c : (modules - 1 - c);
            if (inR === 0 || inR === 6 || inC === 0 || inC === 6) isBlack = true;
            else if (inR >= 2 && inR <= 4 && inC >= 2 && inC <= 4) isBlack = true;
            else isBlack = false;
          }} else {{
            const seed = (r * 31 + c * 17 + hash) & 0xfffff;
            isBlack = (seed % 3) === 0;
          }}

          if (isBlack) {{
            svg += `<rect x="{{(c * cellSize).toFixed(1)}}" y="{{(r * cellSize).toFixed(1)}}" width="{{cellSize.toFixed(1)}}" height="{{cellSize.toFixed(1)}}" fill="#000000"/>`;
          }}
        }}
      }}
      svg += `</svg>`;
      return svg;
    }}

    // ========================================================
    // INTERACTIVIDADES DE LAS DIAPOSITIVAS
    // ========================================================
    function highlightMatrixRow(rowNum) {{
      for (let i = 1; i <= 4; i++) {{
        const r = document.getElementById(`mat-row-{{i}}`);
        if (r) r.style.background = (i === rowNum) ? "rgba(37, 99, 235, 0.35)" : "";
      }}
      const info = {{
        1: "Sujeto 1 (#101): Varón de 28 años con satisfacción 4 (Alta). Fila individual completa.",
        2: "Sujeto 2 (#102): Mujer de 34 años con satisfacción 5 (Muy Alta). Fila individual completa.",
        3: "Sujeto 3 (#103): Mujer de 22 años con satisfacción 3 (Media). Fila individual completa.",
        4: "Sujeto 4 (#104): Varón de 41 años con satisfacción 5 (Muy Alta). Fila individual completa."
      }};
      document.getElementById("matrixInspectorFeedback").innerHTML = `<strong>Fila Seleccionada:</strong> {{info[rowNum]}}`;
    }}

    function highlightInterval(intNum) {{
      for (let i = 1; i <= 6; i++) {{
        const r = document.getElementById(`row-int-{{i}}`);
        if (r) r.style.background = (i === intNum) ? "rgba(6, 182, 212, 0.25)" : "";
      }}
      const details = {{
        1: "Intervalo 51 a 55 puntos: 8 docentes. Notas aprobatorias iniciales.",
        2: "Intervalo 56 a 60 puntos: 16 docentes (Clase Modal). Aquí se concentra la mayor cantidad de evaluados.",
        3: "Intervalo 61 a 65 puntos: 11 docentes. Desempeño promedio intermedio.",
        4: "Intervalo 66 a 70 puntos: 14 docentes. Casi el 78% del curso tiene 70 puntos o menos.",
        5: "Intervalo 71 a 75 puntos: 9 docentes. Desempeño destacado.",
        6: "Intervalo 76 a 85 puntos: 5 docentes. El tramo de calificaciones de excelencia."
      }};
      document.getElementById("intervalExplanationBox").innerHTML = `<strong>Intervalo Seleccionado:</strong> {{details[intNum]}}`;
    }}

    function switchSpssView(view) {{
      const btnVar = document.getElementById("btnSpssViewVar");
      const btnData = document.getElementById("btnSpssViewData");
      const box = document.getElementById("spssExplanationBox");
      const table = document.getElementById("spssTableContent");

      if (view === 'var') {{
        btnVar.classList.add("active");
        btnData.classList.remove("active");
        table.innerHTML = `
          <thead>
            <tr><th>Nombre</th><th>Tipo</th><th>Etiqueta</th><th>Valores</th><th>Medida</th></tr>
          </thead>
          <tbody>
            <tr><td>GEN</td><td>Numérico</td><td>Género del Docente</td><td>1=M, 2=F</td><td>Nominal</td></tr>
            <tr><td>EXP</td><td>Numérico</td><td>Años de Antigüedad</td><td>Ninguno</td><td>Escala</td></tr>
            <tr><td>DESEMP</td><td>Numérico</td><td>Puntaje Pedagógico</td><td>0 a 100</td><td>Escala</td></tr>
          </tbody>
        `;
        box.innerHTML = `<strong>Vista de Variables activa:</strong> Aquí es donde se bautizan las variables y se definen las etiquetas para que la computadora sepa qué representa cada número.`;
      }} else {{
        btnData.classList.add("active");
        btnVar.classList.remove("active");
        table.innerHTML = `
          <thead>
            <tr><th>ID</th><th>GEN</th><th>EXP</th><th>DESEMP</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td>1</td><td>5</td><td>78.5</td></tr>
            <tr><td>2</td><td>2</td><td>12</td><td>92.0</td></tr>
            <tr><td>3</td><td>2</td><td>3</td><td>64.0</td></tr>
          </tbody>
        `;
        box.innerHTML = `<strong>Vista de Datos activa:</strong> Aquí se observan las respuestas reales de los participantes. Cada fila es un docente y cada columna es una variable.`;
      }}
    }}

    function showHuDetail(num) {{
      const info = {{
        1: "Documentos Primarios: Las fuentes directas (audios de entrevistas o diarios de campo) resguardados intactos.",
        2: "Citas (Quotations): Los fragmentos textuales seleccionados por su relevancia; son la evidencia empírica directa.",
        3: "Códigos: Etiquetas conceptuales que el investigador pega a las citas (ej. 'Sobrecarga laboral').",
        4: "Memos Analíticos: El diario reflexivo donde el investigador anota hipótesis y dudas teóricas."
      }};
      document.getElementById("huDetailBox").innerHTML = `<strong>Componente {{num}}:</strong> {{info[num]}}`;
    }}

    function inspectNetworkNode(node) {{
      const box = document.getElementById("networkNodeDetail");
      switch (node) {{
        case 'estres':
          box.innerHTML = `<strong>Nodo Central (Estrés Docente):</strong> Es el problema axial. Se origina por la sobrecarga y deteriora el clima en el aula.`;
          break;
        case 'sobrecarga':
          box.innerHTML = `<strong>Vínculo Causal:</strong> Sobrecarga Laboral <code>es_causa_de</code> Estrés Docente. Testimonio: <em>"Las planificaciones y reuniones imprevistas saturan la jornada escolar."</em>`;
          break;
        case 'rendimiento':
          box.innerHTML = `<strong>Vínculo de Afectación:</strong> Estrés Docente <code>afecta a</code> Rendimiento Pedagógico. El agotamiento mental reduce el dinamismo en clase.`;
          break;
        case 'apoyo':
          box.innerHTML = `<strong>Factor Protector:</strong> Apoyo Familiar <code>mitiga</code> el Estrés Docente. Funciona como un amortiguador psicosocial que protege al docente.`;
          break;
      }}
    }}
  </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully built perfected index.html!")

if __name__ == '__main__':
    generate_index_html()
