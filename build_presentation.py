# -*- coding: utf-8 -*-
"""
Generator script for UPDS Research Methodology Interactive Defense Presentation
Creates a single self-contained index.html with all styles, scripts, SVGs, and speaker notes.
"""

import os

def generate():
    html_content = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Defensa Metodológica: Puntos 6.4 al 6.7 | UPDS</title>
  <meta name="description" content="Presentación interactiva doctoral para defensa de informe metodológico de investigación científica en la Universidad Privada Domingo Savio.">
  <style>
    :root {
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
      --transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
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
    }

    /* TOP BAR PERSISTENTE */
    .top-bar {
      height: 60px;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
      flex-shrink: 0;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .institution-badge {
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
    }

    .speaker-pill {
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
    }

    .speaker-pill .speaker-num {
      background: var(--primary);
      color: var(--text-white);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 800;
    }

    .speaker-pill .subtopic {
      color: var(--text-muted);
      font-weight: 400;
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    /* TIMER WIDGET */
    .timer-widget {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid var(--border-subtle);
      padding: 4px 12px;
      border-radius: 20px;
    }

    .timer-display {
      font-family: monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-amber);
      min-width: 48px;
      text-align: center;
    }

    .timer-display.danger {
      color: var(--accent-rose);
      animation: pulse-danger 1s infinite;
    }

    @keyframes pulse-danger {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.7; transform: scale(1.05); }
    }

    .timer-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.8rem;
      padding: 2px 6px;
      border-radius: 4px;
      transition: var(--transition);
      display: flex;
      align-items: center;
    }

    .timer-btn:hover {
      color: var(--text-white);
      background: rgba(255, 255, 255, 0.1);
    }

    .slide-jump-select {
      background: var(--bg-surface);
      color: var(--text-white);
      border: 1px solid var(--border-subtle);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      cursor: pointer;
      outline: none;
    }

    .slide-jump-select:focus {
      border-color: var(--primary);
    }

    /* PROGRESS BAR */
    .progress-bar-container {
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.05);
      position: relative;
      z-index: 99;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent-cyan));
      width: 0%;
      transition: width 0.3s ease;
      box-shadow: 0 0 10px var(--primary-glow);
    }

    /* MAIN STAGE VIEWPORT (16:9 CONTAINER) */
    .presentation-viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .slide-deck {
      width: 100%;
      max-width: 1400px;
      height: 100%;
      max-height: 820px;
      position: relative;
      perspective: 1000px;
    }

    /* SLIDE STYLING */
    .slide {
      position: absolute;
      inset: 0;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.97) translateY(12px);
      transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.4s;
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 32px 40px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-md), 0 0 40px rgba(0, 0, 0, 0.6);
      overflow-y: auto;
      overflow-x: hidden;
    }

    .slide.active {
      opacity: 1;
      visibility: visible;
      transform: scale(1) translateY(0);
      z-index: 10;
    }

    /* SLIDE HEADER */
    .slide-header {
      margin-bottom: 22px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 14px;
      flex-shrink: 0;
    }

    .slide-pretitle {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }

    .slide-title {
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.5px;
      line-height: 1.2;
    }

    .slide-meta-badge {
      font-size: 0.8rem;
      padding: 4px 12px;
      border-radius: 14px;
      background: rgba(37, 99, 235, 0.12);
      border: 1px solid var(--border-accent);
      color: var(--text-white);
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* SLIDE BODY LAYOUTS */
    .slide-content {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
      align-items: stretch;
      min-height: 0;
    }

    .slide-content.single-col {
      grid-template-columns: 1fr;
    }

    .slide-content.three-col {
      grid-template-columns: 1fr 1fr 1fr;
    }

    /* CARDS & PANELS */
    .glass-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 22px;
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(10px);
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }

    .glass-card:hover {
      border-color: rgba(255, 255, 255, 0.15);
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card-title .icon {
      color: var(--accent-cyan);
    }

    /* TYPOGRAPHY IN SLIDES */
    p, li {
      font-size: 0.94rem;
      color: var(--text-body);
      margin-bottom: 8px;
    }

    strong {
      color: var(--text-white);
      font-weight: 600;
    }

    ul, ol {
      padding-left: 20px;
      margin-bottom: 12px;
    }

    li {
      margin-bottom: 6px;
    }

    .highlight-pill {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 600;
      background: rgba(37, 99, 235, 0.2);
      color: var(--accent-cyan);
      border: 1px solid rgba(6, 182, 212, 0.3);
    }

    .stat-badge {
      display: inline-flex;
      align-items: baseline;
      gap: 4px;
      font-weight: 700;
      color: var(--accent-emerald);
    }

    .alert-box {
      background: rgba(245, 158, 11, 0.1);
      border-left: 4px solid var(--accent-amber);
      padding: 10px 14px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-top: 12px;
      font-size: 0.85rem;
      color: #fde68a;
    }

    .alert-box.danger {
      background: rgba(244, 63, 94, 0.1);
      border-left-color: var(--accent-rose);
      color: #fecdd3;
    }

    .alert-box.success {
      background: rgba(16, 185, 129, 0.1);
      border-left-color: var(--accent-emerald);
      color: #a7f3d0;
    }

    .alert-box.info {
      background: rgba(6, 182, 212, 0.1);
      border-left-color: var(--accent-cyan);
      color: #bae6fd;
    }

    /* BOTTOM CONTROL BAR */
    .bottom-bar {
      height: 56px;
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      z-index: 100;
      flex-shrink: 0;
    }

    .controls-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-nav {
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
    }

    .btn-nav:hover {
      background: var(--bg-surface-elevated);
      border-color: var(--border-accent);
      transform: translateY(-1px);
    }

    .btn-nav:active {
      transform: translateY(1px);
    }

    .btn-nav.primary {
      background: var(--primary);
      border-color: var(--primary-light);
      box-shadow: 0 2px 8px var(--primary-glow);
    }

    .btn-nav.primary:hover {
      background: #1d4ed8;
    }

    .slide-counter {
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }

    .slide-counter span {
      color: var(--text-white);
    }

    .shortcuts-hint {
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .kbd {
      background: var(--bg-surface);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 0.7rem;
      color: var(--text-white);
      font-family: monospace;
    }

    /* MODAL OVERLAYS */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 30px;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
    }

    .modal-overlay.open {
      opacity: 1;
      visibility: visible;
    }

    .modal-window {
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 900px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      transform: scale(0.95);
      transition: var(--transition);
      overflow: hidden;
    }

    .modal-overlay.open .modal-window {
      transform: scale(1);
    }

    .modal-header {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.6);
    }

    .modal-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-white);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .modal-close {
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
    }

    .modal-close:hover {
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-white);
    }

    .modal-body {
      padding: 24px;
      overflow-y: auto;
      flex: 1;
    }

    /* PRESENTER NOTES MODAL CONTENT */
    .note-section {
      margin-bottom: 20px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
    }

    .note-section-title {
      font-size: 0.85rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .note-section-title.goal { color: var(--accent-cyan); }
    .note-section-title.script { color: var(--accent-emerald); }
    .note-section-title.pass { color: var(--accent-amber); }

    .note-content {
      font-size: 0.95rem;
      line-height: 1.6;
      color: var(--text-white);
    }

    .note-content p {
      margin-bottom: 10px;
    }

    .pass-quote {
      font-style: italic;
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--accent-amber);
      padding: 8px 12px;
      border-radius: 4px;
      color: #fde68a;
    }

    /* OVERVIEW THUMBNAILS GRID */
    .overview-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 16px;
      padding: 4px;
    }

    .overview-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 14px;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .overview-card:hover {
      border-color: var(--primary);
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
    }

    .overview-card.current {
      border-color: var(--accent-cyan);
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
    }

    .overview-card .num-badge {
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 0.72rem;
      background: var(--bg-surface);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--text-muted);
    }

    .overview-card .slide-speaker {
      font-size: 0.75rem;
      color: var(--accent-cyan);
      font-weight: 700;
      margin-bottom: 4px;
    }

    .overview-card .slide-heading {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-white);
      line-height: 1.3;
      margin-bottom: 6px;
    }

    .overview-card .sub-tag {
      font-size: 0.72rem;
      color: var(--text-muted);
    }

    /* GLOSSARY STYLING */
    .glossary-search {
      width: 100%;
      background: var(--bg-dark);
      border: 1px solid var(--border-subtle);
      padding: 10px 16px;
      border-radius: var(--radius-md);
      color: var(--text-white);
      font-size: 0.9rem;
      margin-bottom: 18px;
      outline: none;
    }

    .glossary-search:focus {
      border-color: var(--primary);
    }

    .glossary-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    .glossary-item {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 14px;
    }

    .glossary-term {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .glossary-def {
      font-size: 0.84rem;
      color: var(--text-body);
      line-height: 1.45;
    }

    /* CUSTOM COMPONENT WIDGETS */
    /* Tables styling */
    .academic-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      margin: 10px 0;
      border-radius: var(--radius-sm);
      overflow: hidden;
    }

    .academic-table th {
      background: rgba(37, 99, 235, 0.25);
      color: var(--text-white);
      font-weight: 700;
      text-align: left;
      padding: 8px 12px;
      border-bottom: 2px solid var(--primary);
    }

    .academic-table td {
      padding: 7px 12px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-body);
    }

    .academic-table tr:hover td {
      background: rgba(255, 255, 255, 0.03);
    }

    .academic-table tr.highlighted td {
      background: rgba(6, 182, 212, 0.15);
      color: var(--text-white);
      font-weight: 700;
    }

    .academic-table tr.modal-highlight td {
      background: rgba(16, 185, 129, 0.2);
      color: #a7f3d0;
      font-weight: 700;
      border-left: 3px solid var(--accent-emerald);
    }

    /* Flow diagram steps */
    .flow-steps {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin: 18px 0;
      position: relative;
    }

    .flow-step-node {
      flex: 1;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 10px;
      text-align: center;
      cursor: pointer;
      transition: var(--transition);
      position: relative;
    }

    .flow-step-node:hover, .flow-step-node.active {
      border-color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.12);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(6, 182, 212, 0.2);
    }

    .flow-step-node .step-num {
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--accent-cyan);
      display: block;
      margin-bottom: 4px;
    }

    .flow-step-node .step-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-white);
    }

    .flow-step-arrow {
      color: var(--text-muted);
      font-size: 1.1rem;
    }

    /* Buttons inside widgets */
    .action-btn {
      background: linear-gradient(135deg, var(--primary) 0%, #1d4ed8 100%);
      color: var(--text-white);
      border: none;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }

    .action-btn:hover {
      filter: brightness(1.15);
      transform: translateY(-1px);
    }

    .action-btn.secondary {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-white);
    }

    .action-btn.secondary:hover {
      background: var(--bg-surface-elevated);
      border-color: var(--border-accent);
    }

    /* Slide 1 Team Grid */
    .team-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-top: 14px;
    }

    .team-card {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: var(--transition);
      cursor: pointer;
    }

    .team-card:hover {
      border-color: var(--primary);
      background: rgba(37, 99, 235, 0.12);
      transform: translateY(-2px);
    }

    .team-badge {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }

    .team-name {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 2px;
    }

    .team-subtheme {
      font-size: 0.74rem;
      color: var(--text-muted);
    }

    /* Slide 2 Raw data pill cloud */
    .raw-data-cloud {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      max-height: 160px;
      overflow-y: auto;
      padding: 10px;
      background: rgba(15, 23, 42, 0.6);
      border-radius: var(--radius-sm);
      border: 1px dashed var(--border-subtle);
    }

    .raw-item {
      font-size: 0.74rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 2px 7px;
      border-radius: 4px;
      color: var(--text-muted);
      transition: var(--transition);
    }

    .raw-item.pub { border-color: rgba(37, 99, 235, 0.4); color: #93c5fd; }
    .raw-item.auto { border-color: rgba(6, 182, 212, 0.4); color: #a5f3fc; }
    .raw-item.bici { border-color: rgba(16, 185, 129, 0.4); color: #a7f3d0; }

    /* Interactive Scatter Slider */
    .scatter-slider-container {
      margin-top: 14px;
      padding: 12px;
      background: rgba(15, 23, 42, 0.7);
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
    }

    .scatter-slider {
      width: 100%;
      height: 6px;
      accent-color: var(--primary);
      cursor: pointer;
    }

    /* Decision tree node */
    .tree-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      text-align: center;
      margin: 4px 0;
    }

    /* SVG network styles */
    .network-node {
      cursor: pointer;
      transition: var(--transition);
    }

    .network-node:hover circle {
      stroke: #38bdf8;
      stroke-width: 3px;
    }

    .network-node text {
      font-size: 11px;
      fill: #ffffff;
      font-weight: 600;
      pointer-events: none;
      text-anchor: middle;
    }

    /* SPSS Tabs */
    .spss-tabs {
      display: flex;
      gap: 2px;
      background: #0f172a;
      padding: 6px 6px 0 6px;
      border-bottom: 2px solid #2563eb;
    }

    .spss-tab-btn {
      padding: 6px 16px;
      background: #1e293b;
      border: 1px solid var(--border-subtle);
      border-bottom: none;
      color: var(--text-muted);
      border-radius: 6px 6px 0 0;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }

    .spss-tab-btn.active {
      background: #2563eb;
      color: white;
    }

    .spss-window {
      background: #1e293b;
      border: 1px solid var(--border-subtle);
      border-top: none;
      border-radius: 0 0 var(--radius-md) var(--radius-md);
      overflow: hidden;
      min-height: 250px;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(0, 0, 0, 0.2);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .slide-content {
        grid-template-columns: 1fr;
      }
      .slide-content.three-col {
        grid-template-columns: 1fr;
      }
      .team-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .top-bar {
        padding: 0 12px;
      }
      .shortcuts-hint {
        display: none;
      }
    }
  </style>
</head>
<body>

  <!-- TOP BAR PERSISTENTE -->
  <header class="top-bar">
    <div class="brand-group">
      <div class="institution-badge">
        <span>🏛️ UPDS</span>
        <span style="opacity: 0.6;">|</span>
        <span>Metodología de la Inv.</span>
      </div>
      <div class="speaker-pill" id="currentSpeakerPill">
        <span class="speaker-num" id="speakerNumber">APERTURA</span>
        <span id="speakerName">Docente: Marcial Villarroel Siles</span>
        <span class="subtopic" id="speakerSubtopic">Puntos 6.4 al 6.7</span>
      </div>
    </div>

    <div class="top-actions">
      <!-- CRONÓMETRO DE INTERVENCIÓN (3 MINUTOS) -->
      <div class="timer-widget">
        <span style="font-size: 0.75rem; color: var(--text-muted);">⏱️ 3 min:</span>
        <div class="timer-display" id="timerDisplay">03:00</div>
        <button class="timer-btn" id="timerStartBtn" title="Iniciar">▶</button>
        <button class="timer-btn" id="timerPauseBtn" title="Pausar">⏸</button>
        <button class="timer-btn" id="timerResetBtn" title="Reiniciar">↺</button>
      </div>

      <!-- SELECTOR DIRECTO DE DIAPOSITIVA -->
      <select class="slide-jump-select" id="slideSelect" aria-label="Saltar a diapositiva">
        <!-- Generado por JS -->
      </select>
    </div>
  </header>

  <!-- BARRA DE PROGRESO EN TIEMPO REAL -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="progressBar"></div>
  </div>

  <!-- VIEWPORT DE PRESENTACIÓN -->
  <main class="presentation-viewport">
    <div class="slide-deck" id="slideDeck">

      <!-- ========================================== -->
      <!-- LÁMINA 1: PORTADA INSTITUCIONAL Y APERTURA -->
      <!-- ========================================== -->
      <section class="slide active" id="slide-1" data-speaker="EQUIPO DE INVESTIGACIÓN" data-role="Apertura Formal" data-subtopic="Defensa Metodológica (6.4 - 6.7)">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>📚</span> UNIVERSIDAD PRIVADA DOMINGO SAVIO • FACULTAD ACADÉMICA</div>
            <h1 class="slide-title">Recolección, Tabulación, Sistematización e Interpretación de Datos en Trabajo de Campo</h1>
          </div>
          <div class="slide-meta-badge">
            <span>Docente Guía:</span>
            <strong>Lic. Marcial Villarroel Siles</strong>
          </div>
        </div>

        <div class="glass-card" style="padding: 16px 20px; margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 0.85rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase;">
              Flujo Metodológico Integrado de los Puntos 6.4 al 6.7 (Haga clic en cada fase)
            </div>
            <span style="font-size: 0.75rem; color: var(--text-muted);">Ciclo epistemológico completo</span>
          </div>

          <div class="flow-steps">
            <div class="flow-step-node active" onclick="highlightFlow(1, 'Fase 6.4: Recolección y vaciado en matriz rectangular N x K con codificación y control de datos perdidos.')">
              <span class="step-num">FASE 1</span>
              <span class="step-label">1. Campo & Matriz</span>
            </div>
            <div class="flow-step-arrow">→</div>
            <div class="flow-step-node" onclick="highlightFlow(2, 'Fase 6.5: Sistematización en tablas canónicas de 5 columnas y selección gráfica estricta según la escala.')">
              <span class="step-num">FASE 2</span>
              <span class="step-label">2. Frecuencias</span>
            </div>
            <div class="flow-step-arrow">→</div>
            <div class="flow-step-node" onclick="highlightFlow(3, 'Fase 6.6: Modelado estadístico inferencial, correlaciones r, regresiones y minería de patrones KDD.')">
              <span class="step-num">FASE 3</span>
              <span class="step-label">3. Patrones & KDD</span>
            </div>
            <div class="flow-step-arrow">→</div>
            <div class="flow-step-node" onclick="highlightFlow(4, 'Fase 6.7: Procesamiento cuantitativo del p-valor en SPSS y análisis cualitativo inductivo en ATLAS.ti.')">
              <span class="step-num">FASE 4</span>
              <span class="step-label">4. SPSS / ATLAS.ti</span>
            </div>
            <div class="flow-step-arrow">→</div>
            <div class="flow-step-node" onclick="highlightFlow(5, 'Síntesis: Conclusiones contrastadas donde el investigador valida el conocimiento frente a la teoría.')">
              <span class="step-num">FASE 5</span>
              <span class="step-label">5. Conclusiones</span>
            </div>
          </div>
          <div id="flowExplanation" class="alert-box info" style="margin-top: 6px; font-size: 0.82rem;">
            <strong>Fase 6.4 (Tabulación):</strong> Puente entre el instrumento empírico y la matriz rectangular de datos sin casillas vacías.
          </div>
        </div>

        <div style="font-size: 0.82rem; font-weight: 700; color: var(--text-white); margin-bottom: 6px; display: flex; justify-content: space-between;">
          <span>EQUIPO DE 8 EXPOSITORES ASIGNADOS (Haga clic en un expositor para ir directo a su tema):</span>
          <span style="color: var(--text-muted);">Defensa estricta de 3 minutos por exponente</span>
        </div>

        <div class="team-grid">
          <div class="team-card" onclick="goToSlide(2)">
            <span class="team-badge">EXPOSITOR 1 (Lám. 2)</span>
            <span class="team-name">Deivy Melgar Perez</span>
            <span class="team-subtheme">6.4 Tabulación: Fundamentos y Rol</span>
          </div>
          <div class="team-card" onclick="goToSlide(3)">
            <span class="team-badge">EXPOSITOR 2 (Lám. 3-4)</span>
            <span class="team-name">María Teresa Paco Flores</span>
            <span class="team-subtheme">6.4 Matriz N×K y Missing Data</span>
          </div>
          <div class="team-card" onclick="goToSlide(5)">
            <span class="team-badge">EXPOSITOR 3 (Lám. 5-6)</span>
            <span class="team-name">José Maria Peredo Barba</span>
            <span class="team-subtheme">6.5 Frecuencias e Intervalos</span>
          </div>
          <div class="team-card" onclick="goToSlide(7)">
            <span class="team-badge">EXPOSITOR 4 (Lám. 7-8)</span>
            <span class="team-name">Mishel Alcázar Valdez</span>
            <span class="team-subtheme">6.5 Gráficos y Detección Boxplot</span>
          </div>
          <div class="team-card" onclick="goToSlide(9)">
            <span class="team-badge">EXPOSITOR 5 (Lám. 9-10)</span>
            <span class="team-name">Carlos Alberto Choque Serrano</span>
            <span class="team-subtheme">6.6 Cuantitativo y Regresión</span>
          </div>
          <div class="team-card" onclick="goToSlide(11)">
            <span class="team-badge">EXPOSITOR 6 (Lám. 11-12)</span>
            <span class="team-name">Dapne Scarlet Salvatierra Nina</span>
            <span class="team-subtheme">6.6 Minería KDD y Causalidad</span>
          </div>
          <div class="team-card" onclick="goToSlide(13)">
            <span class="team-badge">EXPOSITOR 7 (Lám. 13-14)</span>
            <span class="team-name">Yord Gember Rojas Rocha</span>
            <span class="team-subtheme">6.7 SPSS y Lectura de p-valor</span>
          </div>
          <div class="team-card" onclick="goToSlide(15)">
            <span class="team-badge">EXPOSITOR 8 (Lám. 15-17)</span>
            <span class="team-name">Rodrigo Arauz Mercado</span>
            <span class="team-subtheme">6.7 ATLAS.ti y Síntesis Final</span>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 2: EXPOSITOR 1 - DEIVY MELGAR PEREZ -->
      <!-- ========================================== -->
      <section class="slide" id="slide-2" data-speaker="Deivy Melgar Perez" data-role="Expositor 1" data-subtopic="6.4 Tabulación: Fundamentos y Rol">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1: 6.4 TABULACIÓN DE DATOS • EXPOSITOR 1</div>
            <h2 class="slide-title">Concepto, Finalidad y Rol Metodológico de la Tabulación</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Deivy Melgar Perez</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📐</span> Definición y Marco Epistemológico</h3>
            <p>La tabulación es el procedimiento metódico mediante el cual las respuestas o puntuaciones recogidas en campo se <strong>cuentan, clasifican y estructuran ordenadamente</strong> (Hernández-Sampieri et al., 2014).</p>
            <p>Constituye el <strong>puente indispensable</strong> entre la recolección física y el análisis estadístico formal (Pardo & Ruiz, 2005). Sin tabulación previa, los datos no pueden computarse con validez.</p>

            <h3 class="card-title" style="margin-top: 14px;"><span class="icon">🎯</span> Los Tres Objetivos Fundamentales</h3>
            <ul>
              <li><strong>1. Resumir y condensar:</strong> Transforma volúmenes caóticos en estructuras legibles e interpretables.</li>
              <li><strong>2. Limpieza y control de errores:</strong> Detecta omisiones, dígitos espurios o dobles marcaciones a tiempo.</li>
              <li><strong>3. Cálculos matemáticos exactos:</strong> Discrimina respuestas válidas de valores en blanco para evitar porcentajes sesgados.</li>
            </ul>

            <div class="alert-box success">
              <strong>Flujo de trabajo unívoco:</strong> Recolección en campo ➔ Codificación numérica ➔ Tabulación en matriz general.
            </div>
          </div>

          <!-- Columna Interactiva: Comparador Dato Bruto vs Organizado -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚡</span> Demostración: Dato Bruto vs. Dato Tabulado (N = 50)</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted);">
              A la izquierda se observa el caos de 50 respuestas de texto recogidas en campo sobre <em>"Medio de transporte principal"</em>.
            </p>

            <div style="display: flex; gap: 10px; margin-bottom: 12px;">
              <button class="action-btn" id="btnTabulateDemo" onclick="runTabulationDemo()">
                <span>⚙️ Tabular y Agrupar Datos</span>
              </button>
              <button class="action-btn secondary" onclick="resetTabulationDemo()">
                <span>↺ Reiniciar</span>
              </button>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; align-items: start;">
              <!-- Caja Bruta -->
              <div>
                <div style="font-size: 0.78rem; font-weight: 700; color: var(--accent-rose); margin-bottom: 4px;">
                  1. DATO BRUTO (Disperso y Caótico)
                </div>
                <div class="raw-data-cloud" id="rawCloud">
                  <!-- Llenado dinámico -->
                </div>
              </div>

              <!-- Caja Tabulada -->
              <div>
                <div style="font-size: 0.78rem; font-weight: 700; color: var(--accent-emerald); margin-bottom: 4px;">
                  2. DATO TABULADO (Estructurado)
                </div>
                <table class="academic-table" id="tabulatedTable">
                  <thead>
                    <tr>
                      <th>Categoría</th>
                      <th>f</th>
                      <th>% Válido</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td colspan="3" style="text-align: center; color: var(--text-muted); font-style: italic;">Haga clic en "Tabular Datos"...</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div id="tabulationOutcome" class="alert-box info" style="display: none; margin-top: 10px; font-size: 0.82rem;">
              <strong>Conclusión metodológica:</strong> El dato tabulado permite declarar de inmediato que el <strong>56%</strong> de los sujetos depende del Transporte Público, dato imposible de certificar a simple vista en el caos bruto.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 3: EXPOSITOR 2 - MARÍA TERESA PACO -->
      <!-- ========================================== -->
      <section class="slide" id="slide-3" data-speaker="María Teresa Paco Flores" data-role="Expositor 2" data-subtopic="6.4 Codificación y Matriz N×K">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1: 6.4 TABULACIÓN DE DATOS • EXPOSITOR 2</div>
            <h2 class="slide-title">Codificación Técnica y Anatomía de la Matriz de Datos ($N \times K$)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>María Teresa Paco Flores</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🏷️</span> Codificación Operativa</h3>
            <p>La codificación convierte respuestas verbales o escritas en <strong>valores numéricos unívocos</strong> para su cómputo algorítmico (Pardo & Ruiz, 2005):</p>
            <ul>
              <li><strong>Preguntas cerradas dicotómicas:</strong> 1 = Masculino, 2 = Femenino.</li>
              <li><strong>Escalas ordinales (Likert 1-5):</strong> 1 = Totalmente en desacuerdo ... 5 = Totalmente de acuerdo.</li>
              <li><strong>Preguntas abiertas:</strong> Lectura sistemática, detección de patrones semánticos y asignación de códigos inductivos a ideas recurrentes (Sampieri et al., 2014).</li>
            </ul>

            <h3 class="card-title" style="margin-top: 12px;"><span class="icon">📐</span> Los 3 Componentes de la Matriz ($N \times K$)</h3>
            <ul>
              <li><strong>Filas (Casos $N$):</strong> Cada fila horizontal representa exactamente a un participante o unidad muestral.</li>
              <li><strong>Columnas (Variables $K$):</strong> Cada columna es un ítem o propiedad medida (edad, género, puntaje).</li>
              <li><strong>Celdas ($X_{ij}$):</strong> Intersección unívoca entre el sujeto $i$ y la variable $j$. Contiene un único valor escalar.</li>
            </ul>
          </div>

          <!-- Columna Interactiva: Inspector de Matriz -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">🖥️</span> Render de la Matriz Rectangular</h3>
              <span class="highlight-pill">Participante i=4 Seleccionado</span>
            </div>
            <p style="font-size: 0.83rem; color: var(--text-muted); margin-bottom: 8px;">
              Pase el cursor o haga clic sobre cualquier celda para inspeccionar su valor codificado y metadatos:
            </p>

            <div style="overflow-x: auto; background: rgba(15, 23, 42, 0.6); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
              <table class="academic-table" style="margin: 0;" id="matrixTable">
                <thead>
                  <tr>
                    <th>Caso ($i$)</th>
                    <th>Género ($X_1$)</th>
                    <th>Edad ($X_2$)</th>
                    <th>Nivel ($X_3$)</th>
                    <th>Satisfacción ($X_4$)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr onclick="inspectCell(1, 'Mujer', '22 años', 'Pregrado', '4 (Satisfecho)')">
                    <td><strong>Sujeto 01</strong></td><td>2</td><td>22</td><td>1</td><td>4</td>
                  </tr>
                  <tr onclick="inspectCell(2, 'Varón', '29 años', 'Posgrado', '5 (Muy Satisfecho)')">
                    <td><strong>Sujeto 02</strong></td><td>1</td><td>29</td><td>2</td><td>5</td>
                  </tr>
                  <tr onclick="inspectCell(3, 'Mujer', '24 años', 'Pregrado', '2 (En desacuerdo)')">
                    <td><strong>Sujeto 03</strong></td><td>2</td><td>24</td><td>1</td><td>2</td>
                  </tr>
                  <tr class="modal-highlight" id="row-subject-4" onclick="inspectCell(4, 'Varón', '35 años', 'Posgrado', '5 (Muy Satisfecho)')">
                    <td><strong>Sujeto 04 ★</strong></td><td>1</td><td>35</td><td>2</td><td>5</td>
                  </tr>
                  <tr onclick="inspectCell(5, 'Mujer', '21 años', 'Pregrado', '3 (Neutral)')">
                    <td><strong>Sujeto 05</strong></td><td>2</td><td>21</td><td>1</td><td>3</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Inspector panel -->
            <div id="cellInspectorBox" class="alert-box info" style="margin-top: 12px;">
              <strong>Celda Activa:</strong> Sujeto $i=4$, Variable $X_2$ (Edad) = <strong>35 años</strong>. Sujeto varón, cursando posgrado, calificación Likert 5.
            </div>

            <div class="alert-box danger" style="margin-top: 8px; font-size: 0.78rem;">
              <strong>Principio de rectangularidad:</strong> Ninguna celda puede quedar vacía o desalineada, bajo pena de invalidar las rutinas matriciales del software.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 4: EXPOSITOR 2 - MARÍA TERESA PACO -->
      <!-- ========================================== -->
      <section class="slide" id="slide-4" data-speaker="María Teresa Paco Flores" data-role="Expositor 2 (Cont.)" data-subtopic="6.4 Missing Data y Contingencia 2×2">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 1: 6.4 TABULACIÓN DE DATOS • EXPOSITOR 2</div>
            <h2 class="slide-title">Tratamiento del Missing Data y Tabulación Cruzada ($2 \times 2$)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>María Teresa Paco Flores</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Valores Perdidos -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚠️</span> El Peligro del System-Missing en SPSS</h3>
            <p>Dejar casillas en blanco induce al programa a generar puntos (.) de pérdida del sistema (<em>system-missing</em>), provocando la <strong>eliminación listwise</strong> de todo el caso en análisis multivariados (Sampieri et al., 2014).</p>

            <h4 style="font-size: 0.9rem; color: var(--accent-cyan); margin: 10px 0 6px;">Códigos Numéricos de Usuario Estandarizados:</h4>
            <ul>
              <li><strong style="color: var(--accent-amber);">Código 8 / 88:</strong> <em>"No aplica"</em> (filtro previo justificado; ej. hijos en solteros sin descendencia).</li>
              <li><strong style="color: var(--accent-rose);">Código 9 / 99:</strong> <em>"No contestó"</em> o <em>"No sabe"</em> (omisión deliberada o duda del sujeto).</li>
              <li><strong style="color: var(--accent-purple);">Código 4 / 44:</strong> <em>"Respuesta inválida"</em> (marca múltiple en opción única o texto ilegible).</li>
            </ul>
            <p style="font-size: 0.83rem; color: var(--text-muted);">
              Al declarar estos números como <em>User-Missing</em>, SPSS los aísla en el denominador y garantiza la validez muestral.
            </p>
          </div>

          <!-- Columna Tabulación Cruzada 2x2 Interactiva -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">📊</span> Contingencia $2 \times 2$ (N = 150)</h3>
              <div style="display: flex; gap: 6px;">
                <button class="action-btn secondary" id="btnToggleCounts" style="font-size: 0.76rem; padding: 4px 10px;" onclick="setContingencyMode('counts')">Recuentos (f)</button>
                <button class="action-btn" id="btnTogglePercents" style="font-size: 0.76rem; padding: 4px 10px;" onclick="setContingencyMode('percents')">% de Fila</button>
              </div>
            </div>

            <p style="font-size: 0.83rem; color: var(--text-muted); margin-bottom: 8px;">
              Variable Fila: <strong>Género Docente</strong> | Variable Columna: <strong>Uso de Entorno Virtual</strong>
            </p>

            <table class="academic-table" id="contingencyTable">
              <thead>
                <tr>
                  <th>Género Docente</th>
                  <th>Usa Entorno: SÍ</th>
                  <th>Usa Entorno: NO</th>
                  <th>Total Marginal</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Masculino</strong></td>
                  <td id="cell-m-yes">40 <span style="font-size: 0.75rem; color: var(--text-muted);">(57.1%)</span></td>
                  <td id="cell-m-no">30 <span style="font-size: 0.75rem; color: var(--text-muted);">(42.9%)</span></td>
                  <td id="cell-m-tot"><strong>70</strong> (100.0%)</td>
                </tr>
                <tr>
                  <td><strong>Femenino</strong></td>
                  <td id="cell-f-yes">60 <span style="font-size: 0.75rem; color: var(--text-muted);">(75.0%)</span></td>
                  <td id="cell-f-no">20 <span style="font-size: 0.75rem; color: var(--text-muted);">(25.0%)</span></td>
                  <td id="cell-f-tot"><strong>80</strong> (100.0%)</td>
                </tr>
                <tr style="background: rgba(15, 23, 42, 0.8); font-weight: 700;">
                  <td><strong>Total Columna</strong></td>
                  <td id="cell-tot-yes">100 (66.7%)</td>
                  <td id="cell-tot-no">50 (33.3%)</td>
                  <td>150 (100.0%)</td>
                </tr>
              </tbody>
            </table>

            <div id="contingencyInsight" class="alert-box success" style="font-size: 0.82rem; margin-top: 8px;">
              <strong>Lectura metodológica:</strong> Al comparar porcentajes de fila, se observa que el <strong>75.0%</strong> de las docentes mujeres utiliza entornos virtuales, frente al <strong>57.1%</strong> de los docentes varones. Esta tabla es el insumo previo para la prueba $\chi^2$ de independencia.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 5: EXPOSITOR 3 - JOSÉ MARIA PEREDO -->
      <!-- ========================================== -->
      <section class="slide" id="slide-5" data-speaker="José Maria Peredo Barba" data-role="Expositor 3" data-subtopic="6.5 Sistematización y Frecuencias">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2: 6.5 SISTEMATIZACIÓN Y GRÁFICOS • EXPOSITOR 3</div>
            <h2 class="slide-title">Sistematización y los 5 Componentes Canónicos de la Distribución</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>José Maria Peredo Barba</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📋</span> El Proceso de Sistematizar</h3>
            <p>Sistematizar es <strong>clasificar, condensar y unificar metódicamente</strong> los registros empíricos para hacer visible su patrón subyacente sin introducir distorsiones (Sampieri et al., 2014; Pardo & Ruiz, 2005).</p>

            <h4 style="font-size: 0.9rem; color: var(--accent-cyan); margin: 10px 0 6px;">Las 5 Columnas Canónicas Obligatorias:</h4>
            <ol>
              <li><strong>1. Categoría o Intervalo:</strong> Rango o modalidad que adopta la variable.</li>
              <li><strong>2. Frecuencia Absoluta ($f$):</strong> Conteo directo de casos observados.</li>
              <li><strong>3. Porcentaje Total (%):</strong> Calculado sobre el $100\%$ de la muestra física bruta recolectada: $\frac{f}{N_{total}} \times 100$.</li>
              <li><strong>4. Porcentaje Válido (%):</strong> Recalculado <em>exclusivamente</em> sobre los casos válidos, omitiendo los valores perdidos.</li>
              <li><strong>5. Porcentaje Acumulado (%):</strong> Sumatoria progresiva de los porcentajes válidos hasta alcanzar el $100\%$.</li>
            </ol>
          </div>

          <!-- Columna Interactiva: Tabla de Frecuencias con Missing -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">⚖️</span> ¿Por Qué el % Válido es Vital? (Muestra N = 10)</h3>
              <button class="action-btn" id="btnToggleDistortion" style="font-size: 0.78rem; padding: 4px 10px;" onclick="toggleFreqHighlight()">
                Comparar Distorsión
              </button>
            </div>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px;">
              Variable: <em>Satisfacción con la Infraestructura Tecnológica</em>. 2 participantes no respondieron válidamente.
            </p>

            <table class="academic-table" id="freqCanonTable">
              <thead>
                <tr>
                  <th>Categoría</th>
                  <th>$f$</th>
                  <th id="th-pct-tot">% Total</th>
                  <th id="th-pct-val" style="color: var(--accent-cyan);">% Válido</th>
                  <th>% Acum.</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Insatisfecho (1)</td><td>2</td><td>20.0%</td><td>25.0%</td><td>25.0%</td>
                </tr>
                <tr class="modal-highlight">
                  <td>Satisfecho (2)</td><td>5</td><td>50.0%</td><td>62.5%</td><td>87.5%</td>
                </tr>
                <tr>
                  <td>Muy Satisfecho (3)</td><td>1</td><td>10.0%</td><td>12.5%</td><td>100.0%</td>
                </tr>
                <tr style="border-top: 1px dashed var(--accent-cyan); font-weight: 700;">
                  <td>Subtotal Válido</td><td>8</td><td>80.0%</td><td>100.0%</td><td>—</td>
                </tr>
                <tr style="color: var(--accent-rose); opacity: 0.85;">
                  <td>No contestó (Cód. 8)</td><td>1</td><td>10.0%</td><td>Excluido</td><td>—</td>
                </tr>
                <tr style="color: var(--accent-rose); opacity: 0.85;">
                  <td>Error marcación (Cód. 9)</td><td>1</td><td>10.0%</td><td>Excluido</td><td>—</td>
                </tr>
                <tr style="background: rgba(15, 23, 42, 0.85); font-weight: 800;">
                  <td>Total Muestra</td><td>10</td><td>100.0%</td><td>—</td><td>—</td>
                </tr>
              </tbody>
            </table>

            <div id="freqExplanationBox" class="alert-box success" style="font-size: 0.82rem; margin-top: 6px;">
              <strong>Demostración de impacto:</strong> Si el investigador reporta erróneamente el % Total, dirá que solo el <strong>50%</strong> está satisfecho. Sin embargo, el % Válido demuestra que el <strong>62.5%</strong> de quienes respondieron válidamente está satisfecho, y el <strong>87.5%</strong> se ubica entre Satisfecho y Muy Satisfecho.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 6: EXPOSITOR 3 - JOSÉ MARIA PEREDO -->
      <!-- ========================================== -->
      <section class="slide" id="slide-6" data-speaker="José Maria Peredo Barba" data-role="Expositor 3 (Cont.)" data-subtopic="6.5 Intervalos y Marca de Clase">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2: 6.5 SISTEMATIZACIÓN Y GRÁFICOS • EXPOSITOR 3</div>
            <h2 class="slide-title">Agrupación en Intervalos de Clase y Marca de Clase</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>José Maria Peredo Barba</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Fórmulas y Reglas -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📏</span> Criterios para Variables Continuas</h3>
            <p>Cuando se evalúan escalas con decenas de valores continuos (ej. notas 0-100), listar cada número generaría una tabla inmanejable. Se agrupa en <strong>intervalos de clase</strong> uniformes (Pardo & Ruiz, 2005):</p>
            <ul>
              <li><strong>Rango Total ($R$):</strong> $R = X_{\max} - X_{\min}$.</li>
              <li><strong>Número de clases ($k$):</strong> Usualmente entre 5 y 15 (Regla de Sturges: $k = 1 + 3.322 \log_{10} N$).</li>
              <li><strong>Amplitud constante ($c$):</strong> $c = \frac{R}{k}$. Todos los intervalos deben tener exactamente el mismo ancho métrico.</li>
              <li><strong>Marca de Clase ($X_i$):</strong> Punto medio paramétrico del intervalo:
                $$X_i = \frac{\text{Límite Inferior} + \text{Límite Superior}}{2}$$
                Actúa como el representante algebraico del grupo para calcular medias ponderadas y construir polígonos.
              </li>
            </ul>
          </div>

          <!-- Columna Tabla N=63 Desempeño Docente -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">📈</span> Prueba de Desempeño ($N = 63$ Docentes)</h3>
              <div style="display: flex; gap: 6px;">
                <button class="action-btn secondary" style="font-size: 0.74rem; padding: 4px 8px;" onclick="highlightInterval('modal')">Ver Clase Modal</button>
                <button class="action-btn" style="font-size: 0.74rem; padding: 4px 8px;" onclick="highlightInterval('cum')">Acumulado $\le 70$</button>
              </div>
            </div>

            <div style="max-height: 250px; overflow-y: auto; border: 1px solid var(--border-subtle); border-radius: var(--radius-sm);">
              <table class="academic-table" id="intervalDocTable" style="margin: 0;">
                <thead>
                  <tr>
                    <th>Intervalo (Puntos)</th>
                    <th>Marca ($X_i$)</th>
                    <th>$f$</th>
                    <th>% Total</th>
                    <th>% Válido</th>
                    <th>% Acum.</th>
                  </tr>
                </thead>
                <tbody>
                  <tr id="row-int-1"><td>$\le 55$ pts</td><td>52.5</td><td>3</td><td>4.8%</td><td>5.0%</td><td>5.0%</td></tr>
                  <tr id="row-int-2" class="modal-highlight"><td>56 a 60 pts ★</td><td>58.0</td><td>16</td><td>25.4%</td><td>26.7%</td><td>31.7%</td></tr>
                  <tr id="row-int-3"><td>61 a 65 pts</td><td>63.0</td><td>9</td><td>14.3%</td><td>15.0%</td><td>46.7%</td></tr>
                  <tr id="row-int-4"><td>66 a 70 pts</td><td>68.0</td><td>3</td><td>4.8%</td><td>5.0%</td><td>51.7%</td></tr>
                  <tr id="row-int-5"><td>71 a 75 pts</td><td>73.0</td><td>7</td><td>11.1%</td><td>11.7%</td><td>63.3%</td></tr>
                  <tr id="row-int-6"><td>76 a 80 pts</td><td>78.0</td><td>9</td><td>14.3%</td><td>15.0%</td><td>78.3%</td></tr>
                  <tr id="row-int-7"><td>81 a 85 pts</td><td>83.0</td><td>4</td><td>6.3%</td><td>6.7%</td><td>85.0%</td></tr>
                  <tr id="row-int-8"><td>86 a 90 pts</td><td>88.0</td><td>9</td><td>14.3%</td><td>15.0%</td><td>100.0%</td></tr>
                  <tr style="border-top: 1px dashed var(--accent-cyan); font-weight: 700;"><td>Subtotal Válido</td><td>—</td><td>60</td><td>95.2%</td><td>100.0%</td><td>—</td></tr>
                  <tr style="color: var(--accent-rose);"><td>Sin examen (Perdido)</td><td>—</td><td>3</td><td>4.8%</td><td>Excluido</td><td>—</td></tr>
                </tbody>
              </table>
            </div>

            <div id="intervalCommentBox" class="alert-box info" style="margin-top: 8px; font-size: 0.8rem;">
              <strong>Hallazgo clave:</strong> La clase modal corresponde al tramo <strong>56-60 puntos</strong> ($f=16$, $26.7\%$). Además, el porcentaje acumulado evidencia que exactamente el <strong>51.7%</strong> de los docentes evaluados obtuvo una nota igual o menor a 70 puntos.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 7: EXPOSITOR 4 - MISHEL ALCÁZAR -->
      <!-- ========================================== -->
      <section class="slide" id="slide-7" data-speaker="Mishel Alcázar Valdez" data-role="Expositor 4" data-subtopic="6.5 Visualización y Gráficos">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2: 6.5 SISTEMATIZACIÓN Y GRÁFICOS • EXPOSITOR 4</div>
            <h2 class="slide-title">Criterios de Selección Gráfica según la Escala de Medición</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Mishel Alcázar Valdez</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Reglas Metodológicas -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🎯</span> La Escala Condiciona el Gráfico</h3>
            <p>Un gráfico no es un ornamento estético; es una síntesis matemática unívoca. La regla de oro dicta que <strong>el tipo de variable define estrictamente el formato gráfico</strong> (Sampieri et al., 2014; Pardo & Ruiz, 2005):</p>

            <h4 style="font-size: 0.88rem; color: var(--accent-cyan); margin: 8px 0 4px;">A. Variables Cualitativas / Categóricas (Nominal / Ordinal):</h4>
            <ul>
              <li><strong>Barras:</strong> Rectángulos separados obligatoriamente por un espacio interbarras para indicar que cada categoría es discreta e independiente.</li>
              <li><strong>Sectores (Pastel):</strong> Máximo 3 a 5 clases mutuamente excluyentes cuya suma sea exactamente el $100\%$. Prohibido en variables continuas.</li>
            </ul>

            <h4 style="font-size: 0.88rem; color: var(--accent-emerald); margin: 8px 0 4px;">B. Variables Cuantitativas Continuas (Intervalo / Razón):</h4>
            <ul>
              <li><strong>Histograma:</strong> Rectángulos estrictamente unidos sin espacio interbarras, reflejando continuidad métrica ininterrumpida.</li>
              <li><strong>Polígono de frecuencias:</strong> Línea continua que une las marcas de clase superiores.</li>
            </ul>
          </div>

          <!-- Columna Interactiva: Error Metodológico vs Acierto -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">⚡</span> Comparador: Error Metodológico vs. Acierto</h3>
              <div style="display: flex; gap: 6px;">
                <button class="action-btn secondary" id="btnShowError" style="font-size: 0.76rem; padding: 4px 10px;" onclick="setChartComparison('error')">❌ Ver Error</button>
                <button class="action-btn" id="btnShowCorrect" style="font-size: 0.76rem; padding: 4px 10px;" onclick="setChartComparison('correct')">✅ Ver Acierto</button>
              </div>
            </div>

            <div id="chartContainer" style="height: 230px; display: flex; align-items: center; justify-content: center; background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); padding: 10px;">
              <!-- Render SVG dinámico de Error o Acierto -->
            </div>

            <div id="chartExplanation" class="alert-box danger" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Error Metodológico Crítico:</strong> Emplear un gráfico de pastel para calificaciones continuas (8 porciones fragmentadas). Confunde al jurado, oculta la continuidad y añade efectos 3D que falsean la percepción angular de las áreas.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 8: EXPOSITOR 4 - MISHEL ALCÁZAR -->
      <!-- ========================================== -->
      <section class="slide" id="slide-8" data-speaker="Mishel Alcázar Valdez" data-role="Expositor 4 (Cont.)" data-subtopic="6.5 Boxplot y Detección de Outliers">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 2: 6.5 SISTEMATIZACIÓN Y GRÁFICOS • EXPOSITOR 4</div>
            <h2 class="slide-title">Diagrama de Caja y Bigotes (Boxplot) y Detección de Outliers</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Mishel Alcázar Valdez</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Resumen de 5 Números -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📦</span> El Resumen de los 5 Números</h3>
            <p>El diagrama de caja (<em>Boxplot</em>) sintetiza la distribución de variables cuantitativas mediante estadísticas resistentes a valores extremos (Pardo & Ruiz, 2005):</p>
            <ul>
              <li><strong>Caja Central (50% central de la muestra):</strong> Su base es el Cuartil 1 ($Q_1$, percentil 25) y su techo es el Cuartil 3 ($Q_3$, percentil 75). Su altura es el Rango Intercuartílico ($\text{IQR} = Q_3 - Q_1$).</li>
              <li><strong>Línea Mediana ($Q_2$):</strong> Línea interna que divide a la muestra en dos mitades del 50%. Si está desplazada hacia la base, evidencia asimetría positiva.</li>
              <li><strong>Bigotes:</strong> Líneas que se extienden hasta el máximo y mínimo no atípicos.</li>
            </ul>

            <h4 style="font-size: 0.88rem; color: var(--accent-rose); margin: 10px 0 4px;">Reglas Matemáticas de Detección de Outliers:</h4>
            <ul>
              <li><strong>Atípico Moderado ($\circ$):</strong> Puntos entre $1.5 \times \text{IQR}$ y $3.0 \times \text{IQR}$ más allá de los cuartiles.</li>
              <li><strong>Atípico Extremo ($*$):</strong> Puntos a más de $3.0 \times \text{IQR}$ de la caja. Provocan graves desviaciones en medias aritméticas y deben auditarse individualmente.</li>
            </ul>
          </div>

          <!-- Columna Boxplot SVG Interactivo -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔍</span> Boxplot Interactivo (Pase el cursor por los elementos)</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px;">
              Pase el cursor por la mediana, los cuartiles o el outlier extremo para desplegar su justificación:
            </p>

            <div style="background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); padding: 10px; display: flex; justify-content: center;">
              <svg width="420" height="210" viewBox="0 0 420 210" style="overflow: visible;" id="boxplotSvg">
                <!-- Eje vertical -->
                <line x1="50" y1="20" x2="50" y2="180" stroke="#475569" stroke-width="2" />
                <text x="40" y="25" fill="#94a3b8" font-size="10" text-anchor="end">100</text>
                <text x="40" y="65" fill="#94a3b8" font-size="10" text-anchor="end">80</text>
                <text x="40" y="105" fill="#94a3b8" font-size="10" text-anchor="end">60</text>
                <text x="40" y="145" fill="#94a3b8" font-size="10" text-anchor="end">40</text>
                <text x="40" y="180" fill="#94a3b8" font-size="10" text-anchor="end">20</text>

                <!-- Bigote Superior -->
                <line x1="170" y1="50" x2="250" y2="50" stroke="#94a3b8" stroke-width="2" onmouseenter="showBoxplotCard('Bigote Superior (Límite no atípico = 88 pts)')" />
                <line x1="210" y1="50" x2="210" y2="80" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4" />

                <!-- Caja Intercuartílica -->
                <rect x="140" y="80" width="140" height="70" fill="rgba(37, 99, 235, 0.3)" stroke="#3b82f6" stroke-width="2" rx="4" onmouseenter="showBoxplotCard('Rango Intercuartílico (IQR = Q3 - Q1 = 78 - 58 = 20 pts). Contiene al 50% central de los docentes.')" />

                <!-- Línea Mediana (Q2) -->
                <line x1="140" y1="120" x2="280" y2="120" stroke="#06b6d4" stroke-width="3" onmouseenter="showBoxplotCard('Mediana (Q2 = 65 pts): El 50% de los docentes evaluados obtuvo 65 puntos o menos.')" />

                <!-- Bigote Inferior -->
                <line x1="210" y1="150" x2="210" y2="175" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4" />
                <line x1="170" y1="175" x2="250" y2="175" stroke="#94a3b8" stroke-width="2" onmouseenter="showBoxplotCard('Bigote Inferior (Límite no atípico = 52 pts)')" />

                <!-- Outlier Extremo (*) -->
                <g transform="translate(210, 25)" style="cursor: pointer;" onmouseenter="showBoxplotCard('OUTLIER EXTREMO (*): Sujeto #42 (99 pts). Distancia > 3 × IQR. Se aísla para no inflar la media.')">
                  <circle cx="0" cy="0" r="7" fill="#f43f5e" />
                  <text x="0" y="4" fill="#ffffff" font-size="10" font-weight="900" text-anchor="middle">*</text>
                  <text x="14" y="4" fill="#f43f5e" font-size="10" font-weight="700">Sujeto #42 (99 pts)</text>
                </g>

                <!-- Etiquetas de referencia -->
                <text x="290" y="84" fill="#cbd5e1" font-size="10">Q3 (78)</text>
                <text x="290" y="124" fill="#06b6d4" font-size="10" font-weight="700">Mediana (65)</text>
                <text x="290" y="154" fill="#cbd5e1" font-size="10">Q1 (58)</text>
              </svg>
            </div>

            <div id="boxplotDetailCard" class="alert-box info" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Pase el cursor:</strong> Seleccione una parte del boxplot arriba para inspeccionar su interpretación matemática formal.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 9: EXPOSITOR 5 - CARLOS CHOQUE -->
      <!-- ========================================== -->
      <section class="slide" id="slide-9" data-speaker="Carlos Alberto Choque Serrano" data-role="Expositor 5" data-subtopic="6.6 Análisis Cuantitativo y Fases">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3: 6.6 ANÁLISIS DE DATOS Y PATRONES • EXPOSITOR 5</div>
            <h2 class="slide-title">Propósito del Análisis Cuantitativo y las 4 Fases Secuenciales</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Carlos Alberto Choque Serrano</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🎯</span> De los Números a las Conclusiones Científicas</h3>
            <p>El análisis no consiste en calcular cifras mecánicamente, sino en <strong>responder a los objetivos de investigación y contrastar las hipótesis</strong> minimizando la incertidumbre y el error muestral (Sampieri et al., 2014; Pardo & Ruiz, 2005).</p>

            <div class="alert-box success" style="margin-top: 12px;">
              <strong>Principio de rigor:</strong> Ningún investigador debe pasar a probar hipótesis avanzadas sin haber superado previamente la fase de depuración y consistencia métrica.
            </div>

            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 14px;">
              Haga clic en cualquiera de las 4 etapas a la derecha para examinar sus operaciones técnicas obligatorias y criterios de validación.
            </p>
          </div>

          <!-- Columna 4 Fases Interactivas -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🪜</span> Secuencia de Ejecución Metodológica</h3>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div class="team-card" id="phaseCard-1" style="background: rgba(37, 99, 235, 0.15); border-color: var(--primary);" onclick="showPhaseDetail(1)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--text-white); font-size: 0.88rem;">Fase 1: Exploración y Depuración</strong>
                  <span class="highlight-pill">Control previo</span>
                </div>
                <p style="font-size: 0.8rem; margin: 4px 0 0; color: var(--text-body);">Auditoría de celdas en blanco, corrección de digitación y tipificación de valores perdidos.</p>
              </div>

              <div class="team-card" id="phaseCard-2" onclick="showPhaseDetail(2)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--text-white); font-size: 0.88rem;">Fase 2: Descriptivos Univariados</strong>
                  <span class="highlight-pill" style="background: rgba(6, 182, 212, 0.2); color: var(--accent-cyan);">Tendencia central</span>
                </div>
                <p style="font-size: 0.8rem; margin: 4px 0 0; color: var(--text-body);">Cálculo de medias, medianas, desviación estándar ($s$) y forma de la distribución (asimetría).</p>
              </div>

              <div class="team-card" id="phaseCard-3" onclick="showPhaseDetail(3)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--text-white); font-size: 0.88rem;">Fase 3: Confiabilidad Métrica ($\alpha$)</strong>
                  <span class="highlight-pill" style="background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald);">Alfa $\ge 0.70$</span>
                </div>
                <p style="font-size: 0.8rem; margin: 4px 0 0; color: var(--text-body);">Evaluación de consistencia interna del instrumento mediante el Coeficiente Alfa de Cronbach.</p>
              </div>

              <div class="team-card" id="phaseCard-4" onclick="showPhaseDetail(4)">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--text-white); font-size: 0.88rem;">Fase 4: Inferencia y Prueba de Hipótesis</strong>
                  <span class="highlight-pill" style="background: rgba(245, 158, 11, 0.2); color: var(--accent-amber);">p-valor vs $\alpha$</span>
                </div>
                <p style="font-size: 0.8rem; margin: 4px 0 0; color: var(--text-body);">Contrastación de hipótesis nula ($H_0$), correlaciones bivariadas y modelos lineales de predicción.</p>
              </div>
            </div>

            <div id="phaseDetailBox" class="alert-box info" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Detalle Técnico Fase 1:</strong> Se ejecutan frecuencias de todas las variables en software para detectar puntuaciones fuera de rango (ej. marcar código 7 en una escala de 1 a 5) y se recodifican en los perdidos de usuario.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 10: EXPOSITOR 5 - CARLOS CHOQUE -->
      <!-- ========================================== -->
      <section class="slide" id="slide-10" data-speaker="Carlos Alberto Choque Serrano" data-role="Expositor 5 (Cont.)" data-subtopic="6.6 Correlación y Regresión Lineal">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3: 6.6 ANÁLISIS DE DATOS Y PATRONES • EXPOSITOR 5</div>
            <h2 class="slide-title">Modelos Estadísticos Clásicos: Correlación ($r$) y Regresión Lineal</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Carlos Alberto Choque Serrano</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📐</span> Fundamento Matemático</h3>
            <p><strong>Correlación de Pearson ($r$):</strong> Cuantifica la fuerza y dirección lineal entre dos variables continuas normalizadas ($-1.00 \le r \le +1.00$). Si los datos son ordinales o no normales, se emplea Spearman ($\rho$).</p>
            <p><strong>Coeficiente de Determinación ($r^2$):</strong> Representa la proporción de varianza común o explicada entre variables.</p>
            <p><strong>Ecuación de Regresión Simple:</strong>
              $$Y = \beta_0 + \beta_1 X + \epsilon$$
              Donde $\beta_0$ es el intercepto, $\beta_1$ la pendiente del cambio marginal en $Y$ por cada unidad de $X$, y $\epsilon$ el error residual estocástico (Pardo & Ruiz, 2005).
            </p>
            <div class="alert-box success" style="font-size: 0.82rem;">
              <strong>Predicción informada:</strong> Permite proyectar el desempeño académico del estudiante a partir del tiempo dedicado a la plataforma.
            </div>
          </div>

          <!-- Columna Dispersión y Slider Dinámico -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📉</span> Gráfico de Dispersión y Ajuste de Regresión</h3>

            <div style="background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); padding: 8px; display: flex; justify-content: center;">
              <svg width="400" height="190" viewBox="0 0 400 190" id="scatterPlotSvg">
                <!-- Ejes -->
                <line x1="45" y1="20" x2="45" y2="160" stroke="#475569" stroke-width="2" />
                <line x1="45" y1="160" x2="380" y2="160" stroke="#475569" stroke-width="2" />
                <text x="210" y="180" fill="#94a3b8" font-size="10" text-anchor="middle">Horas de uso de plataforma (X)</text>
                <text x="20" y="90" fill="#94a3b8" font-size="10" text-anchor="middle" transform="rotate(-90 20 90)">Nota (Y)</text>

                <!-- Puntos simulados -->
                <circle cx="70" cy="140" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="95" cy="130" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="130" cy="120" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="160" cy="115" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="190" cy="95" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="225" cy="85" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="260" cy="70" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="295" cy="60" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="330" cy="45" r="4" fill="#38bdf8" opacity="0.7"/>
                <circle cx="360" cy="35" r="4" fill="#38bdf8" opacity="0.7"/>

                <!-- Recta de regresión dinámica -->
                <line id="regressionLine" x1="45" y1="150" x2="380" y2="35" stroke="#10b981" stroke-width="3" />

                <!-- Punto de prueba interactivo -->
                <circle id="interactivePoint" cx="210" cy="92" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
              </svg>
            </div>

            <!-- Slider interactivo -->
            <div class="scatter-slider-container">
              <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 4px;">
                <span>Horas asignadas: <strong id="sliderHoursVal" style="color: var(--accent-amber);">20 hrs/sem</strong></span>
                <span>Calificación Estimada: <strong id="sliderGradeVal" style="color: var(--accent-emerald);">71.5 pts</strong></span>
              </div>
              <input type="range" min="5" max="35" value="20" class="scatter-slider" id="hoursSlider" oninput="updateRegressionDemo(this.value)">
              <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: var(--text-muted); margin-top: 2px;">
                <span>5 hrs (Mín)</span>
                <span style="color: var(--accent-cyan); font-weight: 700;">$r = .78$ • $r^2 = 60.8\%$</span>
                <span>35 hrs (Máx)</span>
              </div>
            </div>

            <div class="alert-box info" style="margin-top: 8px; font-size: 0.8rem;">
              <strong>Ecuación empírica calculada:</strong> $\hat{Y} = 42.5 + 1.45 \cdot X$. Por cada hora adicional en la plataforma, la nota esperada se incrementa en 1.45 puntos.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 11: EXPOSITOR 6 - DAPNE SALVATIERRA -->
      <!-- ========================================== -->
      <section class="slide" id="slide-11" data-speaker="Dapne Scarlet Salvatierra Nina" data-role="Expositor 6" data-subtopic="6.6 Minería KDD y Patrones">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3: 6.6 ANÁLISIS DE DATOS Y PATRONES • EXPOSITOR 6</div>
            <h2 class="slide-title">Minería de Datos y el Proceso KDD (*Knowledge Discovery in Databases*)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Dapne Scarlet Salvatierra Nina</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">💎</span> ¿Qué es un Patrón en Ciencia de Datos?</h3>
            <p>Un patrón es una estructura no trivial descubierta en grandes volúmenes de datos que debe cumplir obligatoriamente <strong>cuatro condiciones canónicas</strong> (Hernández Orallo et al., 2004):</p>
            <ul>
              <li><strong>1. Válido:</strong> Debe mantenerse con certidumbre ante nuevos conjuntos de datos futuros.</li>
              <li><strong>2. Novedoso:</strong> Debe revelar conexiones no conocidas con antelación.</li>
              <li><strong>3. Potencialmente útil:</strong> Debe servir para guiar acciones o tomar decisiones concretas.</li>
              <li><strong>4. Comprensible:</strong> Los investigadores y evaluadores deben poder interpretar su lógica.</li>
            </ul>

            <div class="alert-box info" style="margin-top: 14px;">
              <strong>De la hipótesis a la minería:</strong> Mientras la estadística clásica contrasta supuestos predefinidos, la minería KDD descubre estructuras emergentes no anticipadas.
            </div>
          </div>

          <!-- Columna Túnel de Refinamiento KDD -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔄</span> Túnel de Refinamiento Metodológico KDD</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 10px;">
              Haga clic en cualquiera de las 5 fases del proceso para ver qué operaciones se ejecutan:
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div class="team-card" id="kdd-1" style="background: rgba(37, 99, 235, 0.15); border-color: var(--primary);" onclick="showKddDetail(1)">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--text-white); font-size: 0.86rem;">1. Selección e Integración</strong>
                  <span class="highlight-pill">Bases dispersas</span>
                </div>
              </div>

              <div class="team-card" id="kdd-2" onclick="showKddDetail(2)">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--text-white); font-size: 0.86rem;">2. Limpieza y Transformación</strong>
                  <span class="highlight-pill">Normalización</span>
                </div>
              </div>

              <div class="team-card" id="kdd-3" onclick="showKddDetail(3)">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--text-white); font-size: 0.86rem;">3. Minería de Datos (Data Mining)</strong>
                  <span class="highlight-pill" style="background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald);">Algoritmos</span>
                </div>
              </div>

              <div class="team-card" id="kdd-4" onclick="showKddDetail(4)">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--text-white); font-size: 0.86rem;">4. Evaluación e Interpretación</strong>
                  <span class="highlight-pill">Validación</span>
                </div>
              </div>

              <div class="team-card" id="kdd-5" onclick="showKddDetail(5)">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--text-white); font-size: 0.86rem;">5. Uso y Difusión del Conocimiento</strong>
                  <span class="highlight-pill" style="background: rgba(245, 158, 11, 0.2); color: var(--accent-amber);">Acción real</span>
                </div>
              </div>
            </div>

            <div id="kddDetailBox" class="alert-box success" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Fase 1 (Selección e Integración):</strong> Se unifican los datos provenientes del registro académico, asistencia y cuestionarios de campo en un único almacén homogéneo.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 12: EXPOSITOR 6 - DAPNE SALVATIERRA -->
      <!-- ========================================== -->
      <section class="slide" id="slide-12" data-speaker="Dapne Scarlet Salvatierra Nina" data-role="Expositor 6 (Cont.)" data-subtopic="6.6 Modelos y Advertencia Causal">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 3: 6.6 ANÁLISIS DE DATOS Y PATRONES • EXPOSITOR 6</div>
            <h2 class="slide-title">Modelos de Patrones (Clusters, Árboles) y Advertencia de Causalidad</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Dapne Scarlet Salvatierra Nina</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Simulador de Clusters / Árboles -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">👥</span> Modelos No Supervisados vs. Supervisados</h3>
              <div style="display: flex; gap: 6px;">
                <button class="action-btn" id="btnShowClusters" style="font-size: 0.74rem; padding: 4px 8px;" onclick="toggleModelView('cluster')">K-Medias (3 Grupos)</button>
                <button class="action-btn secondary" id="btnShowTree" style="font-size: 0.74rem; padding: 4px 8px;" onclick="toggleModelView('tree')">Árbol IF-THEN</button>
              </div>
            </div>

            <div id="modelVisualContainer" style="min-height: 200px; background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); padding: 12px; display: flex; flex-direction: column; justify-content: center;">
              <!-- Llenado dinámico -->
            </div>

            <div id="modelVisualComment" class="alert-box info" style="margin-top: 8px; font-size: 0.8rem;">
              <strong>K-Medias:</strong> Agrupamiento no supervisado mediante distancia euclídea que optimiza la homogeneidad intra-cluster y la heterogeneidad inter-cluster.
            </div>
          </div>

          <!-- Columna Advertencia Epistemológica de Causalidad -->
          <div class="glass-card">
            <h3 class="card-title" style="color: var(--accent-rose);"><span class="icon">⚠️</span> Advertencia Crítica: ¡Correlación no es Causalidad!</h3>
            <p>Encontrar que dos variables covarían o que un algoritmo extrae un patrón <strong>jamás prueba que una sea la causa de la otra</strong> (Sampieri et al., 2014; Hernández Orallo et al., 2004).</p>

            <div class="alert-box danger" style="margin: 6px 0 10px; font-size: 0.82rem;">
              <strong>Ejemplo de Relación Espuria:</strong> En verano aumenta la venta de helados y los ahogamientos en playas. Comer helado no causa ahogamiento; existe una tercera variable oculta: el calor ambiental.
            </div>

            <h4 style="font-size: 0.86rem; color: var(--text-white); margin-bottom: 4px;">Las 4 Condiciones Obligatorias para Demostrar Causalidad:</h4>
            <ol style="font-size: 0.82rem;">
              <li><strong>1. Covariación estadística:</strong> Demostrar relación significativa ($p \le 0.05$).</li>
              <li><strong>2. Precedencia temporal:</strong> La causa $X$ debe ocurrir estrictamente antes que el efecto $Y$.</li>
              <li><strong>3. Control de variables rivales:</strong> Descartar factores extraños mediante diseño experimental o control estadístico.</li>
              <li><strong>4. Mecanismo teórico explicativo:</strong> Justificación teórica sólida de por qué ocurre el fenómeno.</li>
            </ol>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 13: EXPOSITOR 7 - YORD ROJAS -->
      <!-- ========================================== -->
      <section class="slide" id="slide-13" data-speaker="Yord Gember Rojas Rocha" data-role="Expositor 7" data-subtopic="6.7 Procesamiento en IBM SPSS">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4: 6.7 INTERPRETACIÓN COMPUTARIZADA • EXPOSITOR 7</div>
            <h2 class="slide-title">Entorno Operativo de IBM SPSS: Vista de Variables vs. Vista de Datos</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Yord Gember Rojas Rocha</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Teórica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">💻</span> Arquitectura del Sistema IBM SPSS</h3>
            <p>IBM SPSS estructura la investigación mediante dos pantallas complementarias unidas a una misma base analítica (Pardo & Ruiz, 2005):</p>
            <ul>
              <li><strong>Vista de Variables (Diccionario de Códigos):</strong> Cada fila es una variable. Se parametrizan: Nombre técnico, Tipo, Etiqueta descriptiva, Valores cualitativos, Perdidos de usuario (8, 9) y Escala de medida (Nominal, Ordinal, Escala).</li>
              <li><strong>Vista de Datos (Matriz Rectangular):</strong> Cada fila es un participante ($N$) y cada columna es una variable configurada.</li>
            </ul>

            <h4 style="font-size: 0.88rem; color: var(--accent-cyan); margin: 12px 0 6px;">Rutas Canónicas del Menú Analizar:</h4>
            <ul style="font-size: 0.83rem;">
              <li><code>Analizar > Estadísticos descriptivos > Frecuencias...</code> (Tablas y porcentajes válidos).</li>
              <li><code>Analizar > Estadísticos descriptivos > Descriptivos...</code> (Medias y dispersión $s$).</li>
              <li><code>Analizar > Estadísticos descriptivos > Tablas cruzadas...</code> (Contingencia y $\chi^2$).</li>
            </ul>
          </div>

          <!-- Columna Simulador SPSS Interactivo -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🖥️</span> Simulador de Interfaz IBM SPSS Statistics</h3>

            <div class="spss-tabs">
              <button class="spss-tab-btn active" id="tabVarBtn" onclick="switchSpssTab('var')">Vista de Variables (Diccionario)</button>
              <button class="spss-tab-btn" id="tabDataBtn" onclick="switchSpssTab('data')">Vista de Datos (Matriz N)</button>
            </div>

            <div class="spss-window" id="spssWindowContent">
              <!-- Render dinámico de tabla de variables o datos -->
            </div>

            <div id="spssExplanation" class="alert-box info" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Vista de Variables:</strong> Obsérvese cómo en la columna <em>Perdidos</em> se fijaron los códigos <code>8, 9</code> para evitar que SPSS distorsione los porcentajes válidos o descarte al participante por error.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 14: EXPOSITOR 7 - YORD ROJAS -->
      <!-- ========================================== -->
      <section class="slide" id="slide-14" data-speaker="Yord Gember Rojas Rocha" data-role="Expositor 7 (Cont.)" data-subtopic="6.7 p-valor y Salida SPSS">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4: 6.7 INTERPRETACIÓN COMPUTARIZADA • EXPOSITOR 7</div>
            <h2 class="slide-title">Interpretación del $p$-valor frente al Umbral $\alpha = 0.05$ y Salida SPSS</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Yord Gember Rojas Rocha</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Criterio Decisional -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">⚖️</span> Regla de Decisión Probabilística</h3>
            <p><strong>Umbral Alfa ($\alpha = 0.05$):</strong> Riesgo máximo admisible de cometer Error Tipo I (declarar un hallazgo cuando fue producto del azar). Equivale a un <strong>95% de nivel de confianza</strong>.</p>
            <p><strong>$p$-valor (Sig. bilateral):</strong> Probabilidad exacta de que los datos observados ocurrieran bajo la verdad de la Hipótesis Nula ($H_0$).</p>

            <div class="alert-box success" style="margin: 8px 0;">
              <strong>Criterio de Rechazo:</strong><br>
              • Si $p \le 0.05$ ➔ <strong>Significativo</strong>. Se rechaza $H_0$; el efecto es real en la población.<br>
              • Si $p > 0.05$ ➔ <strong>No Significativo</strong>. Se retiene $H_0$; no hay evidencia suficiente.
            </div>

            <div class="alert-box danger" style="font-size: 0.8rem;">
              <strong>Regla de oro:</strong> SPSS entrega números a milésimas de segundo, pero <strong>no piensa</strong> ni entiende el contexto social. El sentido recae en el investigador.
            </div>
          </div>

          <!-- Columna Salida Comentada SPSS -->
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <h3 class="card-title" style="margin: 0;"><span class="icon">📑</span> Salida Real SPSS Comentada ($N = 120$)</h3>
              <span class="highlight-pill">Haga clic en las celdas</span>
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 6px;">
              Correlación entre <em>Estrés Docente</em> y <em>Agotamiento Emocional</em>.
            </p>

            <table class="academic-table" id="spssOutputTable">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Estadístico</th>
                  <th>Estrés</th>
                  <th>Agotamiento</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="3"><strong>Estrés Docente</strong></td>
                  <td>Correlación Pearson ($r$)</td>
                  <td>1.000</td>
                  <td id="cell-r" class="modal-highlight" style="cursor: pointer;" onclick="explainSpssStat('r')">.684**</td>
                </tr>
                <tr>
                  <td>Sig. (bilateral)</td>
                  <td>—</td>
                  <td id="cell-sig" class="highlighted" style="cursor: pointer;" onclick="explainSpssStat('sig')">.000</td>
                </tr>
                <tr>
                  <td>$N$ (casos válidos)</td>
                  <td>120</td>
                  <td id="cell-n" style="cursor: pointer;" onclick="explainSpssStat('n')">120</td>
                </tr>
                <tr>
                  <td rowspan="3"><strong>Agotamiento Emocional</strong></td>
                  <td>Correlación Pearson ($r$)</td>
                  <td style="cursor: pointer;" onclick="explainSpssStat('r')">.684**</td>
                  <td>1.000</td>
                </tr>
                <tr>
                  <td>Sig. (bilateral)</td>
                  <td style="cursor: pointer;" onclick="explainSpssStat('sig')">.000</td>
                  <td>—</td>
                </tr>
                <tr>
                  <td>$N$ (casos válidos)</td>
                  <td style="cursor: pointer;" onclick="explainSpssStat('n')">120</td>
                  <td>120</td>
                </tr>
              </tbody>
            </table>

            <div id="spssStatCommentBox" class="alert-box info" style="margin-top: 8px; font-size: 0.82rem;">
              <strong>Clic en .684**:</strong> Magnitud de correlación positiva moderada-alta. Al elevar al cuadrado ($r^2 = 0.468$), se comprueba que el estrés comparte el <strong>46.8% de la varianza</strong> del agotamiento emocional de los docentes.
            </div>

            <div style="margin-top: 8px; display: flex; justify-content: flex-end;">
              <button class="action-btn secondary" style="font-size: 0.74rem; padding: 4px 10px;" onclick="showApaStyleModal()">
                Ver Redacción Formal APA 7.ª Edición
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 15: EXPOSITOR 8 - RODRIGO ARAUZ -->
      <!-- ========================================== -->
      <section class="slide" id="slide-15" data-speaker="Rodrigo Arauz Mercado" data-role="Expositor 8" data-subtopic="6.7 ATLAS.ti y Enfoque Cualitativo">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4: 6.7 INTERPRETACIÓN COMPUTARIZADA • EXPOSITOR 8</div>
            <h2 class="slide-title">Fundamento Epistemológico y Arquitectura de ATLAS.ti</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Rodrigo Arauz Mercado</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Epistemológica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📖</span> Paradigma Cuantitativo vs. Cualitativo</h3>
            <p>Mientras SPSS opera bajo lógica <strong>hipotético-deductiva</strong> (fórmulas y números), ATLAS.ti asiste la lógica <strong>inductiva-constructiva</strong> fundamentada en la Teoría Fundamentada (<em>Grounded Theory</em>) (San Martín, 2014; ATLAS.ti GmbH, 2023).</p>
            <p>Su meta no es calcular promedios, sino <strong>estructurar significados profundos</strong>, comprender la experiencia vivida y construir teoría conceptual a partir del discurso.</p>

            <div class="alert-box info" style="margin-top: 14px;">
              <strong>Método de Comparaciones Constantes:</strong> Proceso iterativo donde el investigador contrasta sistemáticamente citas, incidentes y códigos textuales hasta lograr consistencia teórica.
            </div>
          </div>

          <!-- Columna Arquitectura Unidad Hermenéutica -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🏛️</span> Los 4 Pilares de la Unidad Hermenéutica</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">
              Haga clic en cualquiera de los 4 componentes para ver su rol en el proyecto cualitativo:
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <div class="team-card" id="hu-1" style="background: rgba(37, 99, 235, 0.15); border-color: var(--primary);" onclick="showHuDetail(1)">
                <strong style="color: var(--accent-cyan); font-size: 0.85rem;">1. Documentos Primarios</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0;">Transcripciones de entrevistas, notas de campo y audios originales.</p>
              </div>

              <div class="team-card" id="hu-2" onclick="showHuDetail(2)">
                <strong style="color: var(--accent-emerald); font-size: 0.85rem;">2. Citas (Quotations)</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0;">Fragmentos textuales directos resaltados con significado analítico.</p>
              </div>

              <div class="team-card" id="hu-3" onclick="showHuDetail(3)">
                <strong style="color: var(--accent-amber); font-size: 0.85rem;">3. Códigos (Codes)</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0;">Etiquetas conceptuales aplicadas a las citas (ej. 'Estrés laboral').</p>
              </div>

              <div class="team-card" id="hu-4" onclick="showHuDetail(4)">
                <strong style="color: var(--accent-purple); font-size: 0.85rem;">4. Memos Analíticos</strong>
                <p style="font-size: 0.78rem; margin: 4px 0 0;">Bitácora de reflexiones teóricas y decisiones del investigador.</p>
              </div>
            </div>

            <div id="huDetailBox" class="alert-box success" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Documentos Primarios:</strong> Constituyen el corpus empírico bruto. En ATLAS.ti se preservan intactos mientras se vinculan a la codificación sin alterar la fuente original.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 16: EXPOSITOR 8 - RODRIGO ARAUZ -->
      <!-- ========================================== -->
      <section class="slide" id="slide-16" data-speaker="Rodrigo Arauz Mercado" data-role="Expositor 8 (Cont.)" data-subtopic="6.7 Redes Semánticas en ATLAS.ti">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> BLOQUE 4: 6.7 INTERPRETACIÓN COMPUTARIZADA • EXPOSITOR 8</div>
            <h2 class="slide-title">Patrones Textuales: Coocurrencia y Redes Semánticas (*Networks*)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Responsable:</span>
            <strong>Rodrigo Arauz Mercado</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Coocurrencia y Niveles -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔀</span> Coocurrencia y Niveles de Codificación</h3>
            <p><strong>Tablas de Coocurrencia:</strong> Miden la frecuencia con la que dos códigos solapan o aparecen yuxtapuestos en el mismo testimonio (visualizados con Diagramas de Sankey).</p>

            <h4 style="font-size: 0.88rem; color: var(--accent-cyan); margin: 10px 0 4px;">Los Tres Niveles de la Teoría Fundamentada:</h4>
            <ol style="font-size: 0.83rem;">
              <li><strong>1. Codificación Abierta:</strong> Descomposición inductiva del texto y asignación de códigos iniciales.</li>
              <li><strong>2. Codificación Axial:</strong> Agrupación en categorías y establecimiento de vínculos relacionales.</li>
              <li><strong>3. Codificación Selectiva:</strong> Identificación de la <em>Categoría Central</em> que integra todos los hallazgos.</li>
            </ol>

            <div class="alert-box info" style="margin-top: 10px; font-size: 0.82rem;">
              <strong>Saturación Teórica:</strong> Umbral metodológico en el que incorporar nuevas entrevistas ya no aporta propiedades ni conceptos nuevos al modelo.
            </div>
          </div>

          <!-- Columna Red Semántica Interactiva SVG -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🕸️</span> Red Semántica con Vínculos con Nombre (*Named Links*)</h3>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 6px;">
              Haga clic sobre los nodos para inspeccionar el tipo de vínculo relacional y su testimonio de campo:
            </p>

            <div style="background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); padding: 8px; display: flex; justify-content: center;">
              <svg width="420" height="210" viewBox="0 0 420 210" id="semanticNetSvg">
                <defs>
                  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#06b6d4" />
                  </marker>
                  <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b" />
                  </marker>
                  <marker id="arrow-rose" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e" />
                  </marker>
                </defs>

                <!-- Vínculo Causa (Izquierda a Centro) -->
                <line x1="110" y1="105" x2="190" y2="105" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow-amber)" />
                <text x="150" y="98" fill="#fde68a" font-size="9" text-anchor="middle">es_causa_de</text>

                <!-- Vínculo Asociación (Centro a Derecha Arriba) -->
                <line x1="230" y1="85" x2="310" y2="55" stroke="#06b6d4" stroke-width="2" marker-end="url(#arrow)" />
                <text x="280" y="65" fill="#a5f3fc" font-size="9" text-anchor="middle">asociado_con</text>

                <!-- Vínculo Contradicción (Centro a Derecha Abajo) -->
                <line x1="230" y1="125" x2="310" y2="155" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-rose)" />
                <text x="280" y="150" fill="#fecdd3" font-size="9" text-anchor="middle">contradice</text>

                <!-- Nodo Central: Estrés Universitario -->
                <g class="network-node" transform="translate(210, 105)" onclick="inspectNetworkNode('estres')">
                  <circle cx="0" cy="0" r="32" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
                  <text y="-4">ESTRÉS</text>
                  <text y="10">DOCENTE</text>
                </g>

                <!-- Nodo Causa: Sobrecarga de Tareas -->
                <g class="network-node" transform="translate(70, 105)" onclick="inspectNetworkNode('sobrecarga')">
                  <circle cx="0" cy="0" r="28" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                  <text y="-3">Sobrecarga</text>
                  <text y="9">Laboral</text>
                </g>

                <!-- Nodo Asociación: Rendimiento Pedagógico -->
                <g class="network-node" transform="translate(345, 45)" onclick="inspectNetworkNode('rendimiento')">
                  <circle cx="0" cy="0" r="28" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
                  <text y="-3">Rendimiento</text>
                  <text y="9">Docente</text>
                </g>

                <!-- Nodo Conflicto: Apoyo Familiar -->
                <g class="network-node" transform="translate(345, 165)" onclick="inspectNetworkNode('apoyo')">
                  <circle cx="0" cy="0" r="28" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
                  <text y="-3">Apoyo</text>
                  <text y="9">Familiar</text>
                </g>
              </svg>
            </div>

            <div id="networkNodeDetail" class="alert-box info" style="margin-top: 8px; font-size: 0.8rem;">
              <strong>Vínculo Activo:</strong> Sobrecarga Laboral <code>es_causa_de</code> Estrés Docente. Testimonio Docente #12: <em>"Las horas administrativas duplican la carga presencial y no dejan tiempo para preparar clase."</em>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 17: CIERRE Y SÍNTESIS GENERAL -->
      <!-- ========================================== -->
      <section class="slide" id="slide-17" data-speaker="Rodrigo Arauz Mercado y Equipo" data-role="Cierre Colegiado" data-subtopic="Síntesis Metodológica y Glosario">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🔹</span> SÍNTESIS METODOLÓGICA • EQUIPO DE INVESTIGACIÓN</div>
            <h2 class="slide-title">El Ciclo Integral de Investigación Científica (Puntos 6.4 al 6.7)</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Conclusión General:</span>
            <strong>Defensa 8 Expositores</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Resumen de las 4 Fases en 30s -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">🔄</span> Síntesis del Ciclo en 30 Segundos</h3>
            <ul style="font-size: 0.88rem; line-height: 1.55;">
              <li><strong>6.4 Tabulación Rigurosa:</strong> Limpieza y codificación en matriz rectangular completa sin system-missing, declarando códigos 8 y 9.</li>
              <li><strong>6.5 Sistematización & Visualización:</strong> Tablas canónicas de 5 columnas (destacando el % Válido) y gráficos que respetan la escala (barras vs. histogramas y boxplots para outliers).</li>
              <li><strong>6.6 Modelado Cuantitativo & KDD:</strong> Análisis secuencial en 4 fases, correlaciones $r$, regresiones lineales y minería KDD sujeta a las 4 condiciones de causalidad.</li>
              <li><strong>6.7 Sinergia Computarizada:</strong> Deducción probabilística con el $p$-valor en SPSS e inducción conceptual con redes semánticas en ATLAS.ti.</li>
            </ul>

            <div class="alert-box success" style="margin-top: 14px; font-size: 0.85rem;">
              <strong>LA REGLA DE ORO METODOLÓGICA:</strong><br>
              <em>"Las herramientas computacionales computan y ordenan; el investigador razona, contrasta y produce conocimiento científico."</em>
            </div>
          </div>

          <!-- Columna Accesos Rápidos y Glosario Modal -->
          <div class="glass-card" style="justify-content: center; align-items: center; text-align: center; padding: 30px;">
            <div style="font-size: 2.8rem; margin-bottom: 10px;">📖</div>
            <h3 style="font-size: 1.25rem; color: var(--text-white); margin-bottom: 8px;">Guía Conceptual y Glosario Técnico</h3>
            <p style="font-size: 0.88rem; color: var(--text-muted); max-width: 380px; margin-bottom: 20px;">
              Acceda a las definiciones formales y operativas de los <strong>18 conceptos clave</strong> del informe para consulta directa del tribunal.
            </p>
            <button class="action-btn" style="padding: 12px 24px; font-size: 0.95rem;" onclick="openGlossaryModal()">
              <span>🔍 Abrir Glosario Rápido (18 Términos Clave)</span>
            </button>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- LÁMINA 18: RONDA DE PREGUNTAS Y REFERENCIAS -->
      <!-- ========================================== -->
      <section class="slide" id="slide-18" data-speaker="TRIBUNAL EVALUADOR" data-role="Ronda de Preguntas" data-subtopic="Evaluación Académica">
        <div class="slide-header">
          <div>
            <div class="slide-pretitle"><span>🎓</span> CONCLUSIÓN FORMAL • UNIVERSIDAD PRIVADA DOMINGO SAVIO</div>
            <h2 class="slide-title">Ronda de Preguntas del Jurado y Referencias Bibliográficas</h2>
          </div>
          <div class="slide-meta-badge">
            <span>Docente Evaluador:</span>
            <strong>Lic. Marcial Villarroel Siles</strong>
          </div>
        </div>

        <div class="slide-content">
          <!-- Columna Panel de Preguntas -->
          <div class="glass-card">
            <h3 class="card-title" style="color: var(--accent-cyan);"><span class="icon">💬</span> Espacio para Preguntas y Defensa Oral</h3>
            <p>El equipo de investigación queda a disposición del docente evaluador para absolver dudas conceptuales, operativas y procedimentales sobre los temas defendidos:</p>
            <ul>
              <li>Tratamiento de <em>Missing Data</em> y sesgo en porcentajes totales.</li>
              <li>Selección gráfica de histogramas frente a gráficos de barras.</li>
              <li>Diferencia entre significancia estadística ($p \le 0.05$) e inferencia causal.</li>
              <li>Complementariedad metodológica entre SPSS y ATLAS.ti.</li>
            </ul>

            <div class="alert-box success" style="margin-top: 16px;">
              <strong>Equipo preparado:</strong> Los 8 expositores responderán conforme a los estándares de citación de las normas APA (7.ª edición).
            </div>
          </div>

          <!-- Columna Referencias en APA 7ma Edición -->
          <div class="glass-card">
            <h3 class="card-title"><span class="icon">📚</span> Referencias Bibliográficas (Normas APA 7.ª Ed.)</h3>
            <div style="font-size: 0.8rem; line-height: 1.5; color: var(--text-body); max-height: 260px; overflow-y: auto; padding-right: 6px;">
              <p style="margin-bottom: 8px;">
                <strong>ATLAS.ti Scientific Software Development GmbH.</strong> (2023). <em>ATLAS.ti 23 Windows User Manual</em>. ATLAS.ti GmbH.
              </p>
              <p style="margin-bottom: 8px;">
                <strong>Hernández-Sampieri, R., Fernández-Collado, C., & Baptista-Lucio, P.</strong> (2014). <em>Metodología de la investigación</em> (6.ª ed.). McGraw-Hill Education.
              </p>
              <p style="margin-bottom: 8px;">
                <strong>Hernández Orallo, J., Quintana Ramírez, M. J., & Ramírez Quintana, C.</strong> (2004). <em>Introducción a la minería de datos</em>. Pearson Prentice Hall.
              </p>
              <p style="margin-bottom: 8px;">
                <strong>Pardo, A., & Ruiz, M. Á.</strong> (2005). <em>Análisis de datos con SPSS 13 Base</em>. McGraw-Hill / Interamericana de España.
              </p>
              <p style="margin-bottom: 8px;">
                <strong>San Martín, D.</strong> (2014). Teoría fundamentada y ATLAS.ti: recursos metodológicos para la investigación educativa. <em>Revista Electrónica de Investigación Educativa</em>, 16(1), 104–122.
              </p>
            </div>
          </div>
        </div>
      </section>

    </div>
  </main>

  <!-- BARRA DE CONTROLES INFERIOR -->
  <footer class="bottom-bar">
    <div class="controls-group">
      <button class="btn-nav" id="btnPrev" title="Diapositiva Anterior (← o RePág)">◀ Anterior</button>
      <button class="btn-nav primary" id="btnNext" title="Siguiente Diapositiva (→, Espacio o AvPág)">Siguiente ▶</button>
      <span class="slide-counter" id="slideCounterDisplay">Diapositiva <span>1</span> de 18</span>
    </div>

    <div class="shortcuts-hint">
      <span>Atajos de teclado:</span>
      <span><span class="kbd">←</span> / <span class="kbd">→</span> Navegar</span>
      <span><span class="kbd">N</span> Notas</span>
      <span><span class="kbd">O</span> Miniaturas</span>
      <span><span class="kbd">F</span> Pantalla Completa</span>
    </div>

    <div class="controls-group">
      <button class="btn-nav" id="btnNotesModal" title="Abrir Notas del Expositor (Tecla N)">🎙️ Notas (N)</button>
      <button class="btn-nav" id="btnOverviewModal" title="Vista General de Diapositivas (Tecla O)">🗂️ Vista General (O)</button>
      <button class="btn-nav" id="btnFullscreen" title="Pantalla Completa (Tecla F)">⛶ Pantalla Completa</button>
    </div>
  </footer>

  <!-- ======================================================== -->
  <!-- MODAL: NOTAS DEL EXPOSITOR (PRESENTER NOTES - TECLA N) -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="notesModalOverlay">
    <div class="modal-window">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎙️ Notas del Expositor</span>
          <span style="font-size: 0.85rem; color: var(--text-muted); font-weight: 400;" id="notesSlideIndicator">Diapositiva 1</span>
        </div>
        <button class="modal-close" onclick="closeNotesModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body" id="notesModalBody">
        <!-- Llenado dinámico por diapositiva -->
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: VISTA GENERAL DE DIAPOSITIVAS (OVERVIEW - TECLA O) -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="overviewModalOverlay">
    <div class="modal-window" style="max-width: 1100px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>🗂️ Vista General de Diapositivas (Seleccione una lámina)</span>
        </div>
        <button class="modal-close" onclick="closeOverviewModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body">
        <div class="overview-grid" id="overviewThumbnailsGrid">
          <!-- Generado por JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: GLOSARIO RÁPIDO (18 CONCEPTOS CLAVE)              -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="glossaryModalOverlay">
    <div class="modal-window" style="max-width: 1050px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>📖 Glosario Conceptual y Metodológico (18 Términos Clave)</span>
        </div>
        <button class="modal-close" onclick="closeGlossaryModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body">
        <input type="text" class="glossary-search" id="glossarySearchInput" placeholder="🔍 Buscar término o concepto clave (ej. p-valor, Boxplot, Outlier, KDD, SPSS)..." oninput="filterGlossary(this.value)">
        <div class="glossary-grid" id="glossaryContainer">
          <!-- Generado dinámicamente -->
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: REDACCIÓN FORMAL APA 7MA EDICIÓN                   -->
  <!-- ======================================================== -->
  <div class="modal-overlay" id="apaModalOverlay">
    <div class="modal-window" style="max-width: 700px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>📝 Modelo de Redacción Formal en Normas APA (7.ª Edición)</span>
        </div>
        <button class="modal-close" onclick="closeApaModal()" title="Cerrar">&times;</button>
      </div>
      <div class="modal-body">
        <p style="font-size: 0.9rem; margin-bottom: 12px;">Para reportar la correlación de la Tabla 4 ante el jurado evaluador, la redacción canónica estandarizada es:</p>
        <div style="background: rgba(15, 23, 42, 0.85); border-left: 4px solid var(--accent-emerald); padding: 14px 18px; border-radius: 4px; font-size: 0.95rem; line-height: 1.6; color: var(--text-white); margin-bottom: 14px;">
          "Se llevó a cabo una correlación de Pearson para evaluar la relación entre el estrés percibido por los docentes y su nivel de agotamiento emocional. Los resultados indican una asociación lineal positiva y estadísticamente significativa de magnitud moderada-alta, <em>r</em>(118) = .68, <em>p</em> &lt; .001. El coeficiente de determinación evidenció que el nivel de estrés explica el 46.8% de la varianza en el agotamiento emocional (<em>r</em>² = .468)."
        </div>
        <p style="font-size: 0.82rem; color: var(--text-muted);">
          <strong>Nota de formato APA 7:</strong> Obsérvese que no se antepone cero al coeficiente <em>r</em> ni al valor <em>p</em> (.68 en vez de 0.68), ya que ambos estadísticos tienen un límite máximo teórico de 1. Los grados de libertad corresponden a $N - 2 = 120 - 2 = 118$.
        </p>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- LOGICA JAVASCRIPT ES6+ INTEGRADA Y OPTIMIZADA           -->
  <!-- ======================================================== -->
  <script>
    /* BASE DE DATOS DE NOTAS DEL EXPOSITOR (3 MINUTOS POR EXPOSITOR + GUION EXACTO) */
    const presenterNotes = {
      1: {
        speaker: "EQUIPO DE INVESTIGACIÓN",
        goal: "Presentar la defensa formal, estructura del equipo de 8 expositores y el flujo integral de los puntos 6.4 al 6.7.",
        script: "Estimado docente Lic. Marcial Villarroel Siles y miembros del jurado evaluador: Sean bienvenidos a la defensa formal del informe metodológico sobre 'Recolección, Tabulación, Sistematización e Interpretación de Datos en Trabajo de Campo'. A lo largo de esta intervención, demostraremos cómo los datos empíricos brutos se transforman paso a paso en conocimiento científico riguroso a través de cuatro etapas concatenadas: la tabulación técnica, la sistematización gráfica, el modelado inferencial y la analítica computarizada en IBM SPSS y ATLAS.ti.",
        pass: "Iniciamos de inmediato con el Bloque 1. Cedo la palabra a nuestro compañero Deivy Melgar Perez, quien expondrá los fundamentos metodológicos de la tabulación."
      },
      2: {
        speaker: "Deivy Melgar Perez (Expositor 1)",
        goal: "Explicar el concepto, finalidad y rol de la tabulación como puente entre la recolección física y el análisis formal.",
        script: "Buenos días docente y compañeros. Mi intervención aborda el punto 6.4: Tabulación de datos. Como señalan Hernández-Sampieri et al. (2014) y Pardo y Ruiz (2005), los datos obtenidos de cuestionarios o pruebas no hablan por sí mismos; en su estado bruto son caóticos y propensos a errores. La tabulación cumple tres funciones vitales: primero, resume volúmenes masivos de respuestas en tablas ordenadas; segundo, permite detectar inconsistencias a tiempo; y tercero, garantiza cálculos matemáticos exactos aislando los datos vacíos. En pantalla observamos nuestro comparador: 50 respuestas caóticas sobre transporte público, auto y bicicleta, que al ser tabuladas se convierten de inmediato en proporciones cuantitativas claras donde el 56% depende del transporte público.",
        pass: "Habiendo sentado los fundamentos analíticos de la tabulación, doy el paso a mi compañera María Teresa Paco Flores, quien explicará el proceso técnico de codificación y la estructura formal de la matriz de datos."
      },
      3: {
        speaker: "María Teresa Paco Flores (Expositor 2)",
        goal: "Demostrar cómo se codifican preguntas cualitativas y cuantitativas y exponer la anatomía formal de la matriz N x K.",
        script: "Gracias Deivy. Continuando con el punto 6.4, la codificación es el procedimiento técnico que asigna valores numéricos inequívocos a las respuestas de los participantes para que el software estadístico pueda computarlas. En preguntas dicotómicas asignamos 1 a masculino y 2 a femenino; en escalas Likert usamos números del 1 al 5. Esta información se consolida en una 'matriz de datos' rectangular, definida por tres componentes: las filas, que representan a cada uno de los N participantes; las columnas, que representan a las K variables medidas; y las celdas, que son la intersección unívoca donde reside un único valor escalar. Como apreciamos en el inspector interactivo de la lámina, el sujeto 4 es un varón de 35 años con calificación máxima de satisfacción.",
        pass: "Continuando en mi misma intervención, paso a detallar el tratamiento metodológico de los valores perdidos y las tablas de contingencia."
      },
      4: {
        speaker: "María Teresa Paco Flores (Expositor 2 - Cont.)",
        goal: "Alertar sobre el peligro del missing data en SPSS y explicar las tablas de contingencia 2x2.",
        script: "Un aspecto metodológico crítico es jamás dejar casillas vacías en la matriz. En SPSS, una celda vacía se convierte en 'system-missing' y el software suele descartar a todo el participante de análisis multivariados posteriores. Para evitarlo, usamos códigos de usuario: 8 u 88 para 'No aplica', 9 u 99 para 'No contestó' y 4 para respuestas inválidas. Asimismo, cuando cruzamos dos variables cualitativas, como género y el uso de entornos virtuales en 150 docentes, recurrimos a las tablas de contingencia bidimensionales 2x2. Al analizar los porcentajes de fila observamos que el 75% de las docentes mujeres utiliza entornos virtuales frente al 57.1% de los varones, insumo base para la prueba Chi-cuadrada.",
        pass: "Para continuar con el Bloque 2 correspondiente a la sistematización y distribución de frecuencias, cedo la palabra a mi compañero José Maria Peredo Barba."
      },
      5: {
        speaker: "José Maria Peredo Barba (Expositor 3)",
        goal: "Explicar los 5 componentes obligatorios de la distribución canónica de frecuencias y evidenciar la importancia del % válido.",
        script: "Muchas gracias María Teresa. En el punto 6.5 abordamos la sistematización. Sistematizar significa unificar y resumir la información en tablas de frecuencias con cinco componentes indispensables: la categoría, la frecuencia absoluta, el porcentaje total, el porcentaje válido y el porcentaje acumulado. Es vital enfatizar ante este jurado la diferencia entre el porcentaje total y el válido. En el ejemplo interactivo en pantalla de 10 encuestados, 2 omitieron responder. Si calculamos sobre el total general de 10, la satisfacción aparente es solo del 50%. Pero el porcentaje válido, calculado estrictamente sobre los 8 sujetos reales, demuestra que la satisfacción real alcanza el 62.5% y el 87.5% acumulado. Usar el porcentaje total distorsiona la realidad muestral.",
        pass: "A continuación, en mi segunda lámina, explicaré cómo se agrupan variables continuas en intervalos de clase y el cálculo de la marca de clase."
      },
      6: {
        speaker: "José Maria Peredo Barba (Expositor 3 - Cont.)",
        goal: "Detallar el cálculo de rango, número de intervalos, amplitud y marca de clase mediante el caso de 63 docentes.",
        script: "Cuando medimos variables cuantitativas continuas con decenas de notas distintas, como un examen de 0 a 100 puntos, hacer una fila por cada nota crearía una tabla caótica. Por ello calculamos el Rango total (nota máxima menos mínima), definimos k intervalos de clase uniformes y fijamos una amplitud c constante. Cada intervalo cuenta con su 'Marca de Clase' o punto medio Xi, que representa a todo el tramo en fórmulas matemáticas y gráficos. En la tabla real en pantalla de 63 docentes evaluados, observamos que la clase modal corresponde al intervalo de 56 a 60 puntos con 16 docentes, y el porcentaje acumulado evidencia que exactamente el 51.7% obtuvo 70 puntos o menos.",
        pass: "Habiendo organizado las frecuencias, doy paso a mi compañera Mishel Alcázar Valdez, quien explicará los criterios rigurosos de selección gráfica y detección de anomalías."
      },
      7: {
        speaker: "Mishel Alcázar Valdez (Expositor 4)",
        goal: "Fundamentar por qué la escala de medición impone el tipo de gráfico estadístico y exhibir errores metodológicos habituales.",
        script: "Gracias José María. En investigación científica un gráfico no es decorativo; su diseño está determinado estrictamente por la escala de medición de la variable. Para variables categóricas nominales u ordinales debemos emplear gráficos de barras con separación interbarras visible, o gráficos de sectores circulares con un máximo de 3 a 5 clases. En cambio, para variables continuas es mandatorio usar Histogramas con barras unidas sin espacios, reflejando continuidad métrica. En pantalla presentamos la comparativa entre el error metodológico común —fragmentar notas continuas en un gráfico de pastel 3D confuso— y el acierto formal: un histograma limpio con marcas de clase que transmite con precisión la distribución de las calificaciones.",
        pass: "En mi siguiente lámina, abordaré el diagrama de caja y bigotes para la detección de valores atípicos u outliers."
      },
      8: {
        speaker: "Mishel Alcázar Valdez (Expositor 4 - Cont.)",
        goal: "Explicar la estructura del Boxplot y las fórmulas matemáticas para identificar outliers moderados y extremos.",
        script: "El diagrama de caja y bigotes o Boxplot es la herramienta visual más potente para resumir variables cuantitativas mediante los 5 números: el valor mínimo, el Cuartil 1, la Mediana, el Cuartil 3 y el valor máximo. La caja encierra al 50% central de los participantes y su altura es el Rango Intercuartílico (IQR). Si la mediana está pegada a la base, existe asimetría positiva. Lo más valioso del Boxplot es su capacidad algorítmica para detectar 'Outliers' o valores atípicos: aquellos que superan 1.5 veces el IQR son atípicos moderados, y los que superan 3 veces el IQR son extremos, como el sujeto 42 en pantalla con 99 puntos. Detectarlos a tiempo previene distorsiones en la media muestral.",
        pass: "Con los datos limpios y graficados, cedo la palabra a mi compañero Carlos Alberto Choque Serrano para iniciar el análisis cuantitativo inferencial y de regresión."
      },
      9: {
        speaker: "Carlos Alberto Choque Serrano (Expositor 5)",
        goal: "Exponer el propósito del análisis cuantitativo y las cuatro fases secuenciales obligatorias antes de contrastar hipótesis.",
        script: "Buenos días docente evaluador. Mi intervención en el punto 6.6 se enfoca en el análisis cuantitativo. El propósito de esta fase es transformar datos en conocimiento validado, contrastando los objetivos de investigación y controlando el margen de error. Este proceso exige avanzar por cuatro fases ineludibles: 1) Exploración preliminar de datos; 2) Estadísticos descriptivos univariados; 3) Confiabilidad métrica del instrumento mediante el Alfa de Cronbach, donde exigimos valores iguales o superiores a 0.70 u 0.80 para garantizar precisión; y 4) Inferencia y comprobación de hipótesis. Omitir la validación del instrumento e ir directamente a probar hipótesis es una falla metodológica grave.",
        pass: "Paso de inmediato a mi segunda lámina para analizar los modelos clásicos de correlación de Pearson y regresión lineal."
      },
      10: {
        speaker: "Carlos Alberto Choque Serrano (Expositor 5 - Cont.)",
        goal: "Explicar el coeficiente r de Pearson, el r^2 de determinación y el modelado de regresión lineal predictivo.",
        script: "Cuando analizamos la asociación entre dos variables cuantitativas continuas, utilizamos el coeficiente de correlación de Pearson r, que oscila entre -1 y +1. Al elevarlo al cuadrado obtenemos el coeficiente de determinación r², que indica la proporción de varianza compartida. Para predecir resultados formulamos la ecuación de regresión lineal Y = beta 0 + beta 1 por X más error. En nuestro simulador interactivo relacionamos las horas de uso de plataforma con la nota final: con una correlación r de .78 y un r² de 60.8%, la recta demuestra que por cada hora adicional de estudio en plataforma, el estudiante incrementa su rendimiento esperado en 1.45 puntos.",
        pass: "Para ingresar al campo de la minería de datos y el descubrimiento de patrones ocultos en grandes bases de datos, cedo la palabra a mi compañera Dapne Scarlet Salvatierra Nina."
      },
      11: {
        speaker: "Dapne Scarlet Salvatierra Nina (Expositor 6)",
        goal: "Definir qué es un patrón formal bajo el enfoque de Hernández Orallo et al. y explicar las 5 fases del KDD.",
        script: "Gracias Carlos. En el punto 6.6 abordamos la minería de datos. En investigación contemporánea, los algoritmos permiten descubrir patrones ocultos en grandes volúmenes de información. Según Hernández Orallo et al. (2004), un patrón es una estructura no trivial que debe cumplir cuatro condiciones obligatorias: ser Válido en datos futuros, Novedoso, Potencialmente útil para tomar decisiones y Comprensible para los humanos. Este descubrimiento se logra mediante el proceso KDD en cinco etapas: integración de fuentes, limpieza y preparación de datos, aplicación de algoritmos de minería, evaluación de resultados y uso del conocimiento en la toma de decisiones institucionales.",
        pass: "En mi siguiente lámina profundizaré en los algoritmos de clustering y árboles de decisión, junto con la advertencia crítica sobre correlación y causalidad."
      },
      12: {
        speaker: "Dapne Scarlet Salvatierra Nina (Expositor 6 - Cont.)",
        goal: "Diferenciar modelos de clustering y árboles IF-THEN, y advertir por qué correlación no implica causalidad.",
        script: "En minería aplicamos modelos no supervisados como K-medias, que agrupa automáticamente a los participantes optimizando la similitud interna y la diferencia entre grupos, revelando perfiles como alumnos con bajo compromiso, navegadores nocturnos y de alto rendimiento. En modelos supervisados, los árboles de decisión generan reglas comprensibles del tipo SI... ENTONCES. Sin embargo, como investigadora formulo una advertencia metodológica indispensable: correlación o patrón no significa causalidad. Dos variables pueden covariar por una relación espuria explicada por una tercera variable. Probar causalidad exige cuatro condiciones estrictas: covariación estadística, precedencia temporal, control de factores alternativos y un mecanismo teórico explicativo.",
        pass: "A continuación, cedo la palabra a mi compañero Yord Gember Rojas Rocha para abordar el procesamiento estadístico computarizado en IBM SPSS."
      },
      13: {
        speaker: "Yord Gember Rojas Rocha (Expositor 7)",
        goal: "Describir el entorno operativo de IBM SPSS, diferenciando la Vista de Variables de la Vista de Datos.",
        script: "Buenos días docente y compañeros. En el punto 6.7 ingresamos a la interpretación con herramientas informáticas, iniciando con IBM SPSS Statistics. SPSS opera mediante dos interfaces interconectadas: la 'Vista de Variables', que funciona como el libro de códigos donde configuramos el nombre, tipo, etiquetas descriptivas, valores cualitativos y los valores perdidos 8 y 9; y la 'Vista de Datos', que es la matriz rectangular donde residen los datos empíricos de los participantes. A través del menú superior 'Analizar' accedemos a frecuencias descriptivas, tablas cruzadas y pruebas inferenciales con total precisión computacional.",
        pass: "En mi segunda lámina, explicaré la regla de decisión probabilística del p-valor frente al umbral alfa 0.05 y la lectura de una salida real."
      },
      14: {
        speaker: "Yord Gember Rojas Rocha (Expositor 7 - Cont.)",
        goal: "Explicar el criterio de decisión del p-valor <= 0.05 y modelar la lectura e informe en normas APA 7 de una correlación en SPSS.",
        script: "Al contrastar hipótesis en SPSS, el software entrega la significancia o p-valor. Este valor se compara contra el umbral alfa prefijado en 0.05, que representa un 95% de confianza. La regla de decisión es contundente: si p es menor o igual a 0.05, el resultado es estadísticamente significativo y rechazamos la hipótesis nula H0. En la salida real de correlación entre estrés y agotamiento en 120 docentes, observamos un r de .684 con una Sig. de .000. Siguiendo las normas APA 7, redactamos: existe una correlación positiva moderada-alta, r(118) = .68, p < .001, con un r² de 46.8%. Recordamos siempre que SPSS calcula con exactitud, pero el investigador es quien otorga el sentido teórico a los resultados.",
        pass: "Para culminar con el análisis cualitativo inductivo y la detección de redes de significado, doy paso a nuestro compañero Rodrigo Arauz Mercado con ATLAS.ti."
      },
      15: {
        speaker: "Rodrigo Arauz Mercado (Expositor 8)",
        goal: "Fundamentar el enfoque cualitativo inductivo y la arquitectura de la Unidad Hermenéutica en ATLAS.ti.",
        script: "Muchas gracias Yord. Como último expositor, abordo el análisis cualitativo asistido por computadora mediante ATLAS.ti. A diferencia de SPSS, que es cuantitativo y deductivo, ATLAS.ti se fundamenta en la Teoría Fundamentada de Glaser y Strauss y el método de comparaciones constantes. Su meta no son los números, sino estructurar significados y vivencias en el discurso. Todo el proyecto se congrega en la Unidad Hermenéutica, conformada por cuatro pilares: Documentos primarios (entrevistas y audios), Citas o fragmentos textuales seleccionados, Códigos conceptuales asignados a las citas, y Memos analíticos donde el investigador registra sus reflexiones epistemológicas.",
        pass: "En mi siguiente diapositiva explicaré las tablas de coocurrencia y la construcción de redes semánticas con vínculos relacionales."
      },
      16: {
        speaker: "Rodrigo Arauz Mercado (Expositor 8 - Cont.)",
        goal: "Demostrar la detección de patrones cualitativos mediante tablas de coocurrencia y redes semánticas con Named Links.",
        script: "En ATLAS.ti descubrimos patrones textuales mediante tablas de coocurrencia, que contabilizan cuántas veces dos códigos coinciden en las mismas citas, representadas en diagramas de Sankey. El análisis avanza desde la codificación abierta, pasando por la axial, hasta la selectiva, culminando cuando se alcanza la 'Saturación Teórica'. La cúspide analítica son las Redes Semánticas que apreciamos en pantalla, donde los códigos se interconectan mediante 'Vínculos con Nombre': la sobrecarga laboral 'es_causa_de' estrés docente, el estrés 'está_asociado_con' el rendimiento pedagógico, y el apoyo familiar 'contradice' o mitiga el impacto negativo del estrés.",
        pass: "Paso de inmediato a la lámina de síntesis general y cierre formal de nuestra defensa colegiada."
      },
      17: {
        speaker: "Rodrigo Arauz Mercado y Equipo",
        goal: "Sintetizar el ciclo metodológico completo en 30 segundos, reafirmar la regla de oro y presentar el glosario técnico.",
        script: "Para concluir formalmente nuestra defensa, sintetizamos el ciclo en cuatro certezas: 6.4 limpia y ordena en la matriz rectangular sin missing data; 6.5 sistematiza en tablas canónicas de 5 columnas y gráficos acordes a la escala; 6.6 modela inferencias y patrones KDD bajo rigor causal; y 6.7 procesa con precisión en SPSS y ATLAS.ti. Reafirmamos nuestra regla de oro epistemológica: 'Las herramientas computacionales computan y ordenan; el investigador razona, contrasta y produce conocimiento científico'. Invitamos al tribunal a revisar el glosario interactivo de 18 términos clave incorporado en esta presentación.",
        pass: "Quedamos a entera disposición del docente evaluador Lic. Marcial Villarroel Siles para la ronda de preguntas."
      },
      18: {
        speaker: "TRIBUNAL EVALUADOR",
        goal: "Apertura formal de la ronda de preguntas y verificación de las referencias bibliográficas en normas APA 7.ª edición.",
        script: "Agradecemos la atención prestada por el docente guía y los presentes. Abrimos formalmente el espacio de defensa oral para atender cada una de las interrogantes y observaciones metodológicas del Lic. Marcial Villarroel Siles. En pantalla se encuentran las referencias bibliográficas completas conforme a los estándares de citación de las normas APA 7.ª edición. Muchas gracias.",
        pass: "Fin de la presentación interactiva."
      }
    };

    /* GLOSARIO DE 18 CONCEPTOS CLAVE DEL INFORME */
    const glossaryData = [
      { term: "Matriz de datos rectangular", def: "Estructura tabular donde cada fila representa a un participante (N) y cada columna a una variable (K). Se denomina rectangular porque todos los casos tienen exactamente el mismo número de registros, sin huecos." },
      { term: "Valores perdidos (Missing Data)", def: "Respuestas no obtenidas por omisión, duda o inaplicabilidad. Deben tipificarse con códigos de usuario (8 u 9) para evitar su conversión en puntos del sistema (system-missing)." },
      { term: "Porcentaje válido vs. Porcentaje total", def: "El porcentaje total se calcula sobre la muestra bruta recolectada. El porcentaje válido se recalcula descontando las omisiones, reflejando con fidelidad la opinión de quienes sí respondieron." },
      { term: "Intervalos de clase y Marcas de clase", def: "Agrupamiento de puntuaciones continuas en tramos uniformes de amplitud c. La marca de clase (Xi) es el punto medio matemático de cada intervalo utilizado como su representante paramétrico." },
      { term: "Rango Intercuartílico (IQR)", def: "Distancia métrica entre el Cuartil 1 (percentil 25) y el Cuartil 3 (percentil 75). Define la altura de la caja central en un Boxplot y mide la dispersión del 50% central de la muestra." },
      { term: "Valor atípico (Outlier)", def: "Puntuación extraordinariamente separada del comportamiento común. Se clasifica en moderado (> 1.5 × IQR) y extremo (> 3.0 × IQR), debiendo auditarse para evitar distorsiones en la media." },
      { term: "Coeficiente Alfa de Cronbach", def: "Métrica de consistencia interna y confiabilidad de escalas psicométricas o cuestionarios. Se exigen valores superiores a 0.70 u 0.80 para certificar que los ítems miden el mismo constructo." },
      { term: "Coeficiente de correlación de Pearson (r)", def: "Estadístico paramétrico entre -1.00 y +1.00 que mide la fuerza y sentido lineal entre dos variables continuas. Un valor positivo indica relación directa; cero indica ausencia de asociación lineal." },
      { term: "Coeficiente de determinación (r²)", def: "Resultado de elevar al cuadrado la correlación de Pearson (r²). Expresa el porcentaje de varianza compartida o explicada entre dos variables continuas." },
      { term: "Umbral alfa (α = 0.05) y p-valor", def: "El umbral alfa es el límite máximo admisible de cometer Error Tipo I (5%). Si el p-valor calculado por SPSS es ≤ 0.05, se rechaza formalmente la Hipótesis Nula H0 con respaldo estadístico." },
      { term: "Proceso KDD y Minería de Datos", def: "Knowledge Discovery in Databases: metodología computacional de cinco fases orientada a descubrir patrones válidos, novedosos, potencialmente útiles y comprensibles en grandes bases de datos." },
      { term: "Clustering (K-medias)", def: "Algoritmo no supervisado que agrupa automáticamente a los participantes según similitud vectorial (distancia euclídea), maximizando la homogeneidad interna y heterogeneidad externa." },
      { term: "Árboles de decisión y reglas IF-THEN", def: "Modelos supervisados de clasificación y predicción que segmentan los datos mediante ramificaciones jerárquicas comprensibles en reglas lógicas condicionales." },
      { term: "Reglas de asociación (Soporte y Confianza)", def: "Técnica de minería orientada a identificar coexistencia de eventos. El Soporte mide la frecuencia general del par y la Confianza la probabilidad condicional de que ocurra el segundo evento." },
      { term: "Relación espuria", def: "Asociación matemática aparente entre dos variables que no tienen conexión causal real, sino que covarían debido a la influencia oculta de una tercera variable no controlada." },
      { term: "Unidad Hermenéutica (en ATLAS.ti)", def: "Estructura de proyecto digital en ATLAS.ti que reúne los cuatro componentes del corpus cualitativo: documentos primarios, citas (quotations), códigos (codes) y memos analíticos." },
      { term: "Tablas de coocurrencia y Redes semánticas", def: "Las tablas de coocurrencia cuantifican la concurrencia temática de códigos en las citas. Las redes semánticas son grafos conceptuales con vínculos relacionales con nombre (Named Links)." },
      { term: "Saturación teórica", def: "Momento metodológico en la investigación cualitativa donde la recolección de nuevas entrevistas ya no aporta propiedades o relaciones novedosas a las categorías emergentes." }
    ];

    /* ESTADO GLOBAL DE LA APLICACIÓN */
    let currentSlide = 1;
    const totalSlides = 18;
    let timerSeconds = 180; // 3 minutos
    let timerInterval = null;
    let isTimerRunning = false;

    /* INICIALIZACIÓN AL CARGAR EL DOM */
    document.addEventListener("DOMContentLoaded", () => {
      buildSlideSelector();
      buildOverviewGrid();
      buildGlossaryGrid();
      initRawDataCloud();
      setChartComparison('error');
      switchSpssTab('var');
      toggleModelView('cluster');
      updateSlideView(1);

      // Eventos de teclado
      document.addEventListener("keydown", handleKeydown);

      // Botones de navegación principal
      document.getElementById("btnPrev").addEventListener("click", () => changeSlide(-1));
      document.getElementById("btnNext").addEventListener("click", () => changeSlide(1));
      document.getElementById("slideSelect").addEventListener("change", (e) => goToSlide(parseInt(e.target.value)));

      // Botones modales
      document.getElementById("btnNotesModal").addEventListener("click", toggleNotesModal);
      document.getElementById("btnOverviewModal").addEventListener("click", toggleOverviewModal);
      document.getElementById("btnFullscreen").addEventListener("click", toggleFullScreen);

      // Cronómetro
      document.getElementById("timerStartBtn").addEventListener("click", startTimer);
      document.getElementById("timerPauseBtn").addEventListener("click", pauseTimer);
      document.getElementById("timerResetBtn").addEventListener("click", resetTimer);
    });

    /* NAVEGACIÓN DE DIAPOSITIVAS */
    function goToSlide(n) {
      if (n < 1 || n > totalSlides) return;
      currentSlide = n;
      updateSlideView(currentSlide);
    }

    function changeSlide(delta) {
      const target = currentSlide + delta;
      if (target >= 1 && target <= totalSlides) {
        goToSlide(target);
      }
    }

    function updateSlideView(index) {
      // Activar la lámina correcta
      document.querySelectorAll(".slide").forEach((s, i) => {
        if (i + 1 === index) {
          s.classList.add("active");
        } else {
          s.classList.remove("active");
        }
      });

      // Actualizar selector y contador
      document.getElementById("slideSelect").value = index;
      document.getElementById("slideCounterDisplay").innerHTML = `Diapositiva <span>${index}</span> de ${totalSlides}`;

      // Barra de progreso
      const progressPercent = ((index - 1) / (totalSlides - 1)) * 100;
      document.getElementById("progressBar").style.width = `${progressPercent}%`;

      // Header speaker pill
      const activeSlideEl = document.getElementById(`slide-${index}`);
      if (activeSlideEl) {
        const speaker = activeSlideEl.getAttribute("data-speaker") || "UPDS";
        const role = activeSlideEl.getAttribute("data-role") || "Defensa";
        const subtopic = activeSlideEl.getAttribute("data-subtopic") || "";

        document.getElementById("speakerNumber").textContent = role.toUpperCase();
        document.getElementById("speakerName").textContent = speaker;
        document.getElementById("speakerSubtopic").textContent = subtopic ? `| ${subtopic}` : "";
      }

      // Actualizar contenido del modal de notas
      renderPresenterNotes(index);

      // Resaltar miniatura actual en overview
      document.querySelectorAll(".overview-card").forEach((card, idx) => {
        if (idx + 1 === index) {
          card.classList.add("current");
        } else {
          card.classList.remove("current");
        }
      });
    }

    function handleKeydown(e) {
      // Evitar interceptar si se está escribiendo en el buscador del glosario
      if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") {
        if (e.key === "Escape") {
          closeAllModals();
        }
        return;
      }

      switch (e.key) {
        case "ArrowRight":
        case " ":
        case "PageDown":
          e.preventDefault();
          changeSlide(1);
          break;
        case "ArrowLeft":
        case "PageUp":
          e.preventDefault();
          changeSlide(-1);
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
        case "f":
        case "F":
          e.preventDefault();
          toggleFullScreen();
          break;
        case "Escape":
          closeAllModals();
          break;
      }
    }

    /* CONSTRUCCIÓN DEL SELECTOR DROPDOWN */
    function buildSlideSelector() {
      const select = document.getElementById("slideSelect");
      select.innerHTML = "";
      for (let i = 1; i <= totalSlides; i++) {
        const opt = document.createElement("option");
        opt.value = i;
        const note = presenterNotes[i];
        opt.textContent = `${i}. ${note ? note.speaker : 'Diapositiva ' + i}`;
        select.appendChild(opt);
      }
    }

    /* CRONÓMETRO DE INTERVENCIÓN (3 MINUTOS) */
    function startTimer() {
      if (isTimerRunning) return;
      isTimerRunning = true;
      timerInterval = setInterval(() => {
        if (timerSeconds > 0) {
          timerSeconds--;
          updateTimerDisplay();
        } else {
          pauseTimer();
        }
      }, 1000);
    }

    function pauseTimer() {
      isTimerRunning = false;
      clearInterval(timerInterval);
    }

    function resetTimer() {
      pauseTimer();
      timerSeconds = 180;
      updateTimerDisplay();
    }

    function updateTimerDisplay() {
      const min = Math.floor(timerSeconds / 60);
      const sec = timerSeconds % 60;
      const display = document.getElementById("timerDisplay");
      display.textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;

      if (timerSeconds <= 30) {
        display.classList.add("danger");
      } else {
        display.classList.remove("danger");
      }
    }

    /* PANTALLA COMPLETA */
    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.warn(`Error al intentar pantalla completa: ${err.message}`);
        });
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    /* GESTIÓN DE MODALES */
    function closeAllModals() {
      document.querySelectorAll(".modal-overlay").forEach(m => m.classList.remove("open"));
    }

    function toggleNotesModal() {
      const modal = document.getElementById("notesModalOverlay");
      if (modal.classList.contains("open")) {
        modal.classList.remove("open");
      } else {
        closeAllModals();
        renderPresenterNotes(currentSlide);
        modal.classList.add("open");
      }
    }

    function closeNotesModal() {
      document.getElementById("notesModalOverlay").classList.remove("open");
    }

    function toggleOverviewModal() {
      const modal = document.getElementById("overviewModalOverlay");
      if (modal.classList.contains("open")) {
        modal.classList.remove("open");
      } else {
        closeAllModals();
        modal.classList.add("open");
      }
    }

    function closeOverviewModal() {
      document.getElementById("overviewModalOverlay").classList.remove("open");
    }

    function openGlossaryModal() {
      closeAllModals();
      document.getElementById("glossaryModalOverlay").classList.add("open");
    }

    function closeGlossaryModal() {
      document.getElementById("glossaryModalOverlay").classList.remove("open");
    }

    function showApaStyleModal() {
      closeAllModals();
      document.getElementById("apaModalOverlay").classList.add("open");
    }

    function closeApaModal() {
      document.getElementById("apaModalOverlay").classList.remove("open");
    }

    /* RENDER DE NOTAS DEL EXPOSITOR */
    function renderPresenterNotes(slideNum) {
      const note = presenterNotes[slideNum];
      document.getElementById("notesSlideIndicator").textContent = `Diapositiva ${slideNum} de ${totalSlides} • ${note ? note.speaker : ''}`;

      const body = document.getElementById("notesModalBody");
      if (!note) {
        body.innerHTML = "<p>No hay notas asignadas para esta lámina.</p>";
        return;
      }

      body.innerHTML = `
        <div class="note-section">
          <div class="note-section-title goal">🎯 Objetivo de la intervención (Examen de Grado)</div>
          <div class="note-content">
            <p><strong>${note.goal}</strong></p>
          </div>
        </div>

        <div class="note-section">
          <div class="note-section-title script">🎙️ Guion Clave / Puntos a decir en voz alta (3 Minutos de Rigor)</div>
          <div class="note-content">
            <p>${note.script}</p>
          </div>
        </div>

        <div class="note-section">
          <div class="note-section-title pass">🔄 Frase de Pase al Siguiente Compañero</div>
          <div class="pass-quote">
            "${note.pass}"
          </div>
        </div>
      `;
    }

    /* CONSTRUCCIÓN DE LA VISTA GENERAL (OVERVIEW GRID) */
    function buildOverviewGrid() {
      const grid = document.getElementById("overviewThumbnailsGrid");
      grid.innerHTML = "";

      for (let i = 1; i <= totalSlides; i++) {
        const slideEl = document.getElementById(`slide-${i}`);
        const speaker = slideEl ? slideEl.getAttribute("data-speaker") : "Expositor";
        const role = slideEl ? slideEl.getAttribute("data-role") : "";
        const title = slideEl ? slideEl.querySelector(".slide-title").textContent : `Diapositiva ${i}`;

        const card = document.createElement("div");
        card.className = `overview-card ${i === currentSlide ? 'current' : ''}`;
        card.onclick = () => {
          goToSlide(i);
          closeOverviewModal();
        };

        card.innerHTML = `
          <span class="num-badge">#${i}</span>
          <span class="slide-speaker">${role} • ${speaker}</span>
          <span class="slide-heading">${title}</span>
          <span class="subtag">Haga clic para saltar</span>
        `;

        grid.appendChild(card);
      }
    }

    /* CONSTRUCCIÓN DEL GLOSARIO */
    function buildGlossaryGrid(filter = "") {
      const container = document.getElementById("glossaryContainer");
      container.innerHTML = "";

      const q = filter.trim().toLowerCase();
      const filtered = glossaryData.filter(item => 
        item.term.toLowerCase().includes(q) || item.def.toLowerCase().includes(q)
      );

      if (filtered.length === 0) {
        container.innerHTML = `<p style="grid-column: 1 / -1; text-align: center; color: var(--text-muted); padding: 20px;">No se encontraron términos coincidentes con "${filter}".</p>`;
        return;
      }

      filtered.forEach(item => {
        const div = document.createElement("div");
        div.className = "glossary-item";
        div.innerHTML = `
          <div class="glossary-term"><span>🔹</span> ${item.term}</div>
          <div class="glossary-def">${item.def}</div>
        `;
        container.appendChild(div);
      });
    }

    function filterGlossary(val) {
      buildGlossaryGrid(val);
    }

    /* ======================================================== */
    /* INTERACTIVIDAD ESPECÍFICA DE LAS DIAPOSITIVAS           */
    /* ======================================================== */

    /* LÁMINA 1: FLUJO METODOLÓGICO */
    function highlightFlow(stage, text) {
      document.querySelectorAll(".flow-step-node").forEach((node, idx) => {
        if (idx + 1 === stage) {
          node.classList.add("active");
        } else {
          node.classList.remove("active");
        }
      });
      const box = document.getElementById("flowExplanation");
      box.innerHTML = `<strong>Fase ${stage}:</strong> ${text}`;
    }

    /* LÁMINA 2: COMPARADOR DATO BRUTO VS TABULADO */
    const rawTransportData = [
      "Público","Público","Auto","Bici","Público","Auto","Público","Público","Bici","Público",
      "Auto","Público","Público","Bici","Auto","Público","Auto","Público","Bici","Público",
      "Público","Auto","Público","Bici","Público","Auto","Público","Público","Auto","Bici",
      "Público","Auto","Público","Público","Bici","Auto","Público","Público","Auto","Público",
      "Público","Auto","Bici","Público","Público","Auto","Público","Auto","Público","Público"
    ];

    function initRawDataCloud() {
      const container = document.getElementById("rawCloud");
      if (!container) return;
      container.innerHTML = "";
      rawTransportData.forEach(item => {
        const span = document.createElement("span");
        span.className = `raw-item ${item === 'Público' ? 'pub' : item === 'Auto' ? 'auto' : 'bici'}`;
        span.textContent = item;
        container.appendChild(span);
      });
    }

    function runTabulationDemo() {
      const tableBody = document.querySelector("#tabulatedTable tbody");
      tableBody.innerHTML = `
        <tr class="modal-highlight">
          <td><strong>Transporte Público</strong></td>
          <td><strong>28</strong></td>
          <td><strong>56.0%</strong></td>
        </tr>
        <tr>
          <td>Auto Particular</td>
          <td>14</td>
          <td>28.0%</td>
        </tr>
        <tr>
          <td>Bicicleta</td>
          <td>8</td>
          <td>16.0%</td>
        </tr>
        <tr style="border-top: 2px solid var(--primary); font-weight: 800; background: rgba(15,23,42,0.8);">
          <td>Total Muestra</td>
          <td>50</td>
          <td>100.0%</td>
        </tr>
      `;
      document.getElementById("tabulationOutcome").style.display = "block";
    }

    function resetTabulationDemo() {
      const tableBody = document.querySelector("#tabulatedTable tbody");
      tableBody.innerHTML = `<tr><td colspan="3" style="text-align: center; color: var(--text-muted); font-style: italic;">Haga clic en "Tabular Datos"...</td></tr>`;
      document.getElementById("tabulationOutcome").style.display = "none";
    }

    /* LÁMINA 3: INSPECTOR DE MATRIZ */
    function inspectCell(subjectNum, genero, edad, nivel, satisfaccion) {
      document.querySelectorAll("#matrixTable tbody tr").forEach((tr, i) => {
        if (i + 1 === subjectNum) {
          tr.className = "modal-highlight";
        } else {
          tr.className = "";
        }
      });
      const box = document.getElementById("cellInspectorBox");
      box.innerHTML = `
        <strong>Inspección Sujeto ${subjectNum.toString().padStart(2, '0')}:</strong> 
        Género: <strong>${genero}</strong> | Edad: <strong>${edad}</strong> | Nivel Académico: <strong>${nivel}</strong> | Satisfacción: <strong>${satisfaccion}</strong>.
      `;
    }

    /* LÁMINA 4: TABLA DE CONTINGENCIA 2x2 */
    function setContingencyMode(mode) {
      const btnCounts = document.getElementById("btnToggleCounts");
      const btnPercents = document.getElementById("btnTogglePercents");
      const insight = document.getElementById("contingencyInsight");

      if (mode === 'counts') {
        btnCounts.className = "action-btn";
        btnPercents.className = "action-btn secondary";

        document.getElementById("cell-m-yes").innerHTML = `40 <span style="font-size: 0.75rem; color: var(--text-muted);">(57.1%)</span>`;
        document.getElementById("cell-m-no").innerHTML = `30 <span style="font-size: 0.75rem; color: var(--text-muted);">(42.9%)</span>`;
        document.getElementById("cell-f-yes").innerHTML = `60 <span style="font-size: 0.75rem; color: var(--text-muted);">(75.0%)</span>`;
        document.getElementById("cell-f-no").innerHTML = `20 <span style="font-size: 0.75rem; color: var(--text-muted);">(25.0%)</span>`;

        insight.innerHTML = `<strong>Vista Recuentos Absolutos:</strong> De los 150 docentes encuestados, 100 afirman utilizar entornos virtuales (40 varones y 60 mujeres).`;
      } else {
        btnCounts.className = "action-btn secondary";
        btnPercents.className = "action-btn";

        document.getElementById("cell-m-yes").innerHTML = `<strong style="color: var(--accent-cyan); font-size: 1.05rem;">57.1%</strong> <span style="font-size: 0.72rem;">(f=40)</span>`;
        document.getElementById("cell-m-no").innerHTML = `<strong>42.9%</strong> <span style="font-size: 0.72rem;">(f=30)</span>`;
        document.getElementById("cell-f-yes").innerHTML = `<strong style="color: var(--accent-emerald); font-size: 1.05rem;">75.0%</strong> <span style="font-size: 0.72rem;">(f=60)</span>`;
        document.getElementById("cell-f-no").innerHTML = `<strong>25.0%</strong> <span style="font-size: 0.72rem;">(f=20)</span>`;

        insight.innerHTML = `<strong>Porcentajes de Fila:</strong> El <strong>75.0%</strong> de las docentes mujeres utiliza entornos virtuales frente al <strong>57.1%</strong> de los docentes varones. Esta asimetría motiva la prueba de hipótesis Chi-cuadrada.`;
      }
    }

    /* LÁMINA 5: DISTRO DE FRECUENCIAS % VÁLIDO */
    let freqHighlightDistorted = false;
    function toggleFreqHighlight() {
      freqHighlightDistorted = !freqHighlightDistorted;
      const thTot = document.getElementById("th-pct-tot");
      const thVal = document.getElementById("th-pct-val");
      const box = document.getElementById("freqExplanationBox");

      if (freqHighlightDistorted) {
        thTot.style.color = "var(--accent-rose)";
        thTot.style.fontWeight = "800";
        thVal.style.color = "var(--text-white)";
        box.className = "alert-box danger";
        box.innerHTML = `<strong>Atención Jurado (Error por % Total):</strong> Si el investigador toma el 50.0% de la columna total, distorsiona la realidad pues computa a dos personas que jamás respondieron la pregunta.`;
      } else {
        thTot.style.color = "var(--text-white)";
        thVal.style.color = "var(--accent-cyan)";
        thVal.style.fontWeight = "800";
        box.className = "alert-box success";
        box.innerHTML = `<strong>Corrección Metodológica (% Válido):</strong> El software aísla las 2 omisiones y recalcula la satisfacción real sobre los 8 casos válidos: <strong>62.5% Satisfecho</strong> y <strong>87.5% Acumulado</strong>.`;
      }
    }

    /* LÁMINA 6: INTERVALOS DE CLASE N=63 */
    function highlightInterval(type) {
      const rows = [1,2,3,4,5,6,7,8];
      rows.forEach(r => document.getElementById(`row-int-${r}`).className = "");
      const box = document.getElementById("intervalCommentBox");

      if (type === 'modal') {
        document.getElementById("row-int-2").className = "modal-highlight";
        box.innerHTML = `<strong>Clase Modal (56 a 60 puntos):</strong> Concentra la mayor densidad de frecuencias con $f=16$ docentes y una marca de clase de 58.0 puntos.`;
      } else {
        [1,2,3,4].forEach(r => document.getElementById(`row-int-${r}`).className = "highlighted");
        box.innerHTML = `<strong>Corte Acumulado $\le 70$ puntos:</strong> Sumando los 4 primeros intervalos ($f = 3+16+9+3 = 31$), se constata que exactamente el <strong>51.7%</strong> de la planta docente evaluada obtuvo 70 puntos o menos.`;
      }
    }

    /* LÁMINA 7: COMPARADOR GRÁFICO ERROR VS ACIERTO */
    function setChartComparison(type) {
      const container = document.getElementById("chartContainer");
      const expl = document.getElementById("chartExplanation");
      const btnErr = document.getElementById("btnShowError");
      const btnCor = document.getElementById("btnShowCorrect");

      if (type === 'error') {
        btnErr.className = "action-btn";
        btnCor.className = "action-btn secondary";

        expl.className = "alert-box danger";
        expl.innerHTML = `<strong>Error Metodológico Severo:</strong> Utilizar un gráfico de sectores (pastel 3D) para calificaciones continuas divididas en 8 intervalos. Distorsiona la continuidad métrica, engaña el ojo humano y transgrede el estándar APA.`;

        container.innerHTML = `
          <svg width="340" height="210" viewBox="0 0 340 210">
            <g transform="translate(170, 105) scale(1, 0.75)">
              <path d="M 0 0 L 80 0 A 80 80 0 0 1 56 56 Z" fill="#ef4444" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L 56 56 A 80 80 0 0 1 -20 77 Z" fill="#f97316" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L -20 77 A 80 80 0 0 1 -75 27 Z" fill="#eab308" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L -75 27 A 80 80 0 0 1 -75 -27 Z" fill="#84cc16" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L -75 -27 A 80 80 0 0 1 -20 -77 Z" fill="#06b6d4" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L -20 -77 A 80 80 0 0 1 56 -56 Z" fill="#8b5cf6" stroke="#0f172a" stroke-width="2"/>
              <path d="M 0 0 L 56 -56 A 80 80 0 0 1 80 0 Z" fill="#ec4899" stroke="#0f172a" stroke-width="2"/>
            </g>
            <text x="170" y="200" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">❌ Ruleta 3D ilegible (8 fragmentos continuos)</text>
          </svg>
        `;
      } else {
        btnErr.className = "action-btn secondary";
        btnCor.className = "action-btn";

        expl.className = "alert-box success";
        expl.innerHTML = `<strong>Acierto Metodológico Formal:</strong> Histograma con barras estrictamente unidas (sin espacio interbarras) y marcas de clase. Comunica con fidelidad la forma de la campana y la continuidad métrica.`;

        container.innerHTML = `
          <svg width="360" height="210" viewBox="0 0 360 210">
            <!-- Ejes -->
            <line x1="40" y1="20" x2="40" y2="160" stroke="#64748b" stroke-width="2"/>
            <line x1="40" y1="160" x2="340" y2="160" stroke="#64748b" stroke-width="2"/>
            
            <!-- Barras unidas del histograma (ancho 34px cada una, unidas) -->
            <!-- 55-: f=3 -->
            <rect x="42" y="132" width="34" height="28" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 56-60: f=16 -->
            <rect x="76" y="20" width="34" height="140" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 61-65: f=9 -->
            <rect x="110" y="80" width="34" height="80" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 66-70: f=3 -->
            <rect x="144" y="132" width="34" height="28" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 71-75: f=7 -->
            <rect x="178" y="98" width="34" height="62" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 76-80: f=9 -->
            <rect x="212" y="80" width="34" height="80" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 81-85: f=4 -->
            <rect x="246" y="124" width="34" height="36" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
            <!-- 86-90: f=9 -->
            <rect x="280" y="80" width="34" height="80" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>

            <!-- Polígono de frecuencias trazado en puntos medios -->
            <polyline points="59,132 93,20 127,80 161,132 195,98 229,80 263,124 297,80" fill="none" stroke="#06b6d4" stroke-width="2.5"/>

            <text x="190" y="180" fill="#94a3b8" font-size="10" text-anchor="middle">Calificaciones (Marcas de clase continuas)</text>
            <text x="190" y="200" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">✅ Histograma con barras continuas unidas</text>
          </svg>
        `;
      }
    }

    /* LÁMINA 8: BOXPLOT HOVER CARD */
    function showBoxplotCard(text) {
      document.getElementById("boxplotDetailCard").innerHTML = `<strong>Elemento Boxplot:</strong> ${text}`;
    }

    /* LÁMINA 9: 4 FASES DEL ANÁLISIS CUANTITATIVO */
    const phaseDetails = {
      1: "Se ejecutan frecuencias de todas las variables en software para detectar puntuaciones fuera de rango (ej. marcar código 7 en una escala de 1 a 5) y se recodifican en los perdidos de usuario.",
      2: "Cálculo formal de medidas de tendencia central (media, mediana) y de dispersión (desviación típica s). Se examina el coeficiente de asimetría para verificar normalidad paramétrica.",
      3: "Evaluación de consistencia interna mediante el Alfa de Cronbach. En escalas psicométricas o de actitud, se exige un coeficiente mayor o igual a 0.70 u 0.80 para validar el instrumento.",
      4: "Contraste riguroso de hipótesis bivariadas o multivariadas mediante correlaciones, regresiones o pruebas t/ANOVA, comparando el p-valor frente al umbral prefijado α = 0.05."
    };

    function showPhaseDetail(num) {
      for (let i = 1; i <= 4; i++) {
        const el = document.getElementById(`phaseCard-${i}`);
        if (i === num) {
          el.style.borderColor = "var(--accent-cyan)";
          el.style.background = "rgba(6, 182, 212, 0.15)";
        } else {
          el.style.borderColor = "var(--border-subtle)";
          el.style.background = "rgba(30, 41, 59, 0.6)";
        }
      }
      document.getElementById("phaseDetailBox").innerHTML = `<strong>Detalle Técnico Fase ${num}:</strong> ${phaseDetails[num]}`;
    }

    /* LÁMINA 10: REGRESIÓN LINEAL CON SLIDER */
    function updateRegressionDemo(hours) {
      const h = parseFloat(hours);
      // Ecuación: Y = 42.5 + 1.45 * X
      const grade = (42.5 + 1.45 * h).toFixed(1);

      document.getElementById("sliderHoursVal").textContent = `${h} hrs/sem`;
      document.getElementById("sliderGradeVal").textContent = `${grade} pts`;

      // Actualizar posición del punto interactivo en SVG (X de 45 a 380, Y de 160 a 20)
      const svgX = 45 + ((h - 5) / 30) * 335;
      const svgY = 160 - ((grade - 40) / 60) * 140;

      const pt = document.getElementById("interactivePoint");
      if (pt) {
        pt.setAttribute("cx", svgX);
        pt.setAttribute("cy", svgY);
      }
    }

    /* LÁMINA 11: FASES KDD */
    const kddDetails = {
      1: "Se unifican bases de datos aisladas (asistencia, calificaciones y encuestas) en una única estructura homogénea libre de duplicidades.",
      2: "Limpieza de valores espurios, imputación controlada de datos faltantes y normalización de escalas vectoriales para los algoritmos.",
      3: "Ejecución de algoritmos inteligentes de clustering (K-medias), inducción de árboles (C4.5/CART) o reglas de asociación (Apriori).",
      4: "El investigador humano audita los patrones descubiertos para verificar si son válidos, no triviales y coherentes con la ciencia previa.",
      5: "El conocimiento extraído se integra a políticas educativas, planes de remediación docente o mejoras en plataformas institucionales."
    };

    function showKddDetail(num) {
      for (let i = 1; i <= 5; i++) {
        const el = document.getElementById(`kdd-${i}`);
        if (i === num) {
          el.style.borderColor = "var(--accent-emerald)";
          el.style.background = "rgba(16, 185, 129, 0.15)";
        } else {
          el.style.borderColor = "var(--border-subtle)";
          el.style.background = "rgba(30, 41, 59, 0.6)";
        }
      }
      document.getElementById("kddDetailBox").innerHTML = `<strong>Fase ${num} del KDD:</strong> ${kddDetails[num]}`;
    }

    /* LÁMINA 12: MODELOS DE PATRONES */
    function toggleModelView(mode) {
      const container = document.getElementById("modelVisualContainer");
      const comment = document.getElementById("modelVisualComment");
      const btnCluster = document.getElementById("btnShowClusters");
      const btnTree = document.getElementById("btnShowTree");

      if (mode === 'cluster') {
        btnCluster.className = "action-btn";
        btnTree.className = "action-btn secondary";

        comment.innerHTML = `<strong>K-Medias (No supervisado):</strong> Segmenta automáticamente a los estudiantes en perfiles sin etiquetas previas mediante optimización de centroides euclídeos.`;

        container.innerHTML = `
          <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px;">
            <div style="background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 6px; padding: 10px; text-align: center;">
              <span style="font-size: 0.72rem; color: #fca5a5; font-weight: 700;">CLUSTER 1 (n=38)</span>
              <div style="font-size: 0.85rem; font-weight: 800; color: #fff; margin: 4px 0;">Bajo Compromiso</div>
              <p style="font-size: 0.72rem; color: #cbd5e1; margin: 0;">Uso &lt; 4 hrs • Promedio 54 pts</p>
            </div>
            <div style="background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 6px; padding: 10px; text-align: center;">
              <span style="font-size: 0.72rem; color: #fde68a; font-weight: 700;">CLUSTER 2 (n=54)</span>
              <div style="font-size: 0.85rem; font-weight: 800; color: #fff; margin: 4px 0;">Navegadores Nocturnos</div>
              <p style="font-size: 0.72rem; color: #cbd5e1; margin: 0;">Conexión 22:00-02:00 • Prom. 71 pts</p>
            </div>
            <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 6px; padding: 10px; text-align: center;">
              <span style="font-size: 0.72rem; color: #a7f3d0; font-weight: 700;">CLUSTER 3 (n=28)</span>
              <div style="font-size: 0.85rem; font-weight: 800; color: #fff; margin: 4px 0;">Alto Rendimiento</div>
              <p style="font-size: 0.72rem; color: #cbd5e1; margin: 0;">Constancia diaria • Promedio 88 pts</p>
            </div>
          </div>
        `;
      } else {
        btnCluster.className = "action-btn secondary";
        btnTree.className = "action-btn";

        comment.innerHTML = `<strong>Árbol de Decisión (Supervisado):</strong> Genera reglas comprensibles que explican qué condiciones determinan el rendimiento docente.`;

        container.innerHTML = `
          <div style="display: flex; flex-direction: column; align-items: center; gap: 6px;">
            <div class="tree-box" style="border-color: var(--primary);">
              ¿Experiencia Docente &gt; 5 años?
            </div>
            <div style="display: flex; gap: 40px; width: 100%; justify-content: center;">
              <div style="display: flex; flex-direction: column; align-items: center;">
                <span style="font-size: 0.7rem; color: var(--accent-rose); font-weight: 700;">NO</span>
                <div class="tree-box" style="background: rgba(244, 63, 94, 0.15); border-color: var(--accent-rose);">
                  Rendimiento: <strong>Medio-Bajo</strong> (78%)
                </div>
              </div>
              <div style="display: flex; flex-direction: column; align-items: center;">
                <span style="font-size: 0.7rem; color: var(--accent-emerald); font-weight: 700;">SÍ</span>
                <div class="tree-box" style="border-color: var(--accent-cyan);">
                  ¿Posee Posgrado Pedagógico?
                </div>
                <div style="display: flex; gap: 14px; margin-top: 4px;">
                  <span style="font-size: 0.7rem; color: var(--accent-emerald); font-weight: 700;">SÍ ➔ <strong>Excelente (92%)</strong></span>
                </div>
              </div>
            </div>
          </div>
        `;
      }
    }

    /* LÁMINA 13: IBM SPSS TABS */
    function switchSpssTab(tab) {
      const btnVar = document.getElementById("tabVarBtn");
      const btnData = document.getElementById("tabDataBtn");
      const content = document.getElementById("spssWindowContent");
      const expl = document.getElementById("spssExplanation");

      if (tab === 'var') {
        btnVar.className = "spss-tab-btn active";
        btnData.className = "spss-tab-btn";

        expl.innerHTML = `<strong>Vista de Variables (Libro de Códigos):</strong> Permite declarar el tipo de variable, los valores cualitativos y los <em>Perdidos de usuario (8, 9)</em> para que SPSS no sesgue los promedios.`;

        content.innerHTML = `
          <div style="overflow-x: auto;">
            <table class="academic-table" style="margin: 0; font-size: 0.78rem;">
              <thead>
                <tr style="background: #1e3a8a;">
                  <th>Nombre</th>
                  <th>Tipo</th>
                  <th>Etiqueta</th>
                  <th>Valores</th>
                  <th>Perdidos</th>
                  <th>Medida</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>id_docente</td><td>Numérico</td><td>Identificador del sujeto</td><td>Ninguno</td><td>Ninguno</td><td>Nominal</td></tr>
                <tr><td>genero</td><td>Numérico</td><td>Género del docente</td><td>{1, Masc}...</td><td>Ninguno</td><td>Nominal</td></tr>
                <tr><td>estres</td><td>Numérico</td><td>Escala de Estrés Laboral</td><td>Ninguno</td><td>8, 9</td><td>Escala</td></tr>
                <tr><td>agotamiento</td><td>Numérico</td><td>Agotamiento Emocional</td><td>Ninguno</td><td>8, 9</td><td>Escala</td></tr>
                <tr><td>entorno_virt</td><td>Numérico</td><td>Usa Entornos Virtuales</td><td>{1, Sí}...</td><td>9</td><td>Nominal</td></tr>
              </tbody>
            </table>
          </div>
        `;
      } else {
        btnVar.className = "spss-tab-btn";
        btnData.className = "spss-tab-btn active";

        expl.innerHTML = `<strong>Vista de Datos (Matriz de Casos):</strong> Cada fila es un participante real del estudio con sus respuestas codificadas en números para el cálculo de correlaciones y frecuencias.`;

        content.innerHTML = `
          <div style="overflow-x: auto;">
            <table class="academic-table" style="margin: 0; font-size: 0.78rem;">
              <thead>
                <tr style="background: #1e3a8a;">
                  <th>id_docente</th>
                  <th>genero</th>
                  <th>estres</th>
                  <th>agotamiento</th>
                  <th>entorno_virt</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>001</td><td>2</td><td>48</td><td>62</td><td>1</td></tr>
                <tr><td>002</td><td>1</td><td>35</td><td>40</td><td>1</td></tr>
                <tr><td>003</td><td>2</td><td>52</td><td>70</td><td>2</td></tr>
                <tr><td>004</td><td>1</td><td>29</td><td>31</td><td>1</td></tr>
                <tr><td>005</td><td>2</td><td>45</td><td>58</td><td>1</td></tr>
              </tbody>
            </table>
          </div>
        `;
      }
    }

    /* LÁMINA 14: SALIDA COMENTADA SPSS */
    function explainSpssStat(stat) {
      const box = document.getElementById("spssStatCommentBox");
      if (stat === 'r') {
        box.innerHTML = `<strong>Coeficiente de Pearson ($r = .684^{**}$):</strong> Asociación lineal positiva y moderada-alta. Dos asteriscos indican significancia estricta al nivel $\alpha = 0.01$. Varianza explicada $r^2 = 46.8\%$.`;
      } else if (stat === 'sig') {
        box.innerHTML = `<strong>Sig. bilateral ($p = .000$):</strong> Se reporta en APA 7 como $p < .001$. Al ser ampliamente menor a $0.05$, se rechaza la Hipótesis Nula $H_0$; la relación no es producto del azar.`;
      } else {
        box.innerHTML = `<strong>Tamaño muestral válido ($N = 120$):</strong> Corresponde a los 120 docentes que completaron ambos instrumentos sin valores omitidos.`;
      }
    }

    /* LÁMINA 15: ARQUITECTURA ATLAS.TI (UNIDAD HERMENÉUTICA) */
    const huDetails = {
      1: "Los Documentos Primarios son las fuentes brutas: entrevistas a profundidad, archivos de audio o diarios de campo, resguardados sin alteración en el proyecto.",
      2: "Las Citas (Quotations) son fragmentos de texto seleccionados por su relevancia testimonial; constituyen la evidencia empírica directa del discurso.",
      3: "Los Códigos son etiquetas conceptuales que el investigador adscribe a las citas para capturar ideas recurrentes (ej. 'Falta de apoyo institucional').",
      4: "Los Memos Analíticos son espacios reflexivos donde el investigador anota hipótesis teóricas, dudas metodológicas y conexiones conceptuales durante la lectura."
    };

    function showHuDetail(num) {
      for (let i = 1; i <= 4; i++) {
        const el = document.getElementById(`hu-${i}`);
        if (i === num) {
          el.style.borderColor = "var(--accent-cyan)";
          el.style.background = "rgba(6, 182, 212, 0.15)";
        } else {
          el.style.borderColor = "var(--border-subtle)";
          el.style.background = "rgba(30, 41, 59, 0.6)";
        }
      }
      document.getElementById("huDetailBox").innerHTML = `<strong>Componente ${num}:</strong> ${huDetails[num]}`;
    }

    /* LÁMINA 16: REDES SEMÁNTICAS ATLAS.TI */
    function inspectNetworkNode(node) {
      const box = document.getElementById("networkNodeDetail");
      switch (node) {
        case 'estres':
          box.innerHTML = `<strong>Nodo Central: Estrés Docente.</strong> Categoría axial conectada causalmente con la sobrecarga de tareas y con impacto directo en el rendimiento académico.`;
          break;
        case 'sobrecarga':
          box.innerHTML = `<strong>Vínculo Causal:</strong> Sobrecarga Laboral <code>es_causa_de</code> Estrés Docente. Testimonio #12: <em>"Las planificaciones y reuniones imprevistas saturan la jornada escolar."</em>`;
          break;
        case 'rendimiento':
          box.innerHTML = `<strong>Vínculo de Asociación:</strong> Estrés Docente <code>está_asociado_con</code> Rendimiento Pedagógico. El agotamiento reduce la paciencia y dinamismo en el aula.`;
          break;
        case 'apoyo':
          box.innerHTML = `<strong>Vínculo de Conflicto/Mitigación:</strong> Apoyo Familiar <code>contradice</code> el Estrés Docente. Actúa como factor protector psicosocial amortiguador.`;
          break;
      }
    }
  </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully generated index.html with UTF-8 encoding!")

if __name__ == "__main__":
    generate()
