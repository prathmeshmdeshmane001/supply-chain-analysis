# Hyperframes Composition Brief: Supply Chain Analytics & Predictive SLA Risk Engine

## Objective
Create a short, polished, high-impact launch brag video for the Supply Chain Analytics & Predictive SLA Risk Engine project.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Poster frame: `brag-output/brag.jpg`
- Format: `landscape` — 1920x1080
- Duration: 20.0 seconds (600 frames at 30 fps)

## Source Material
- Project root: `/Users/prathameshdeshmane/Supply Chain Analysis`
- Primary files read: `README.md`, `run_analysis.py`, `SupplyChainManagementProject.ipynb`, `outputs/reports/business_kpis.json`, `outputs/figures/07_shipping_mode_delay_breakdown.png`
- Product name: Supply Chain Analytics & Predictive SLA Risk Engine
- Author: Prathamesh Deshmane (`prathmeshmdeshmane001`)
- Tagline / strongest claim: "First Class shipping had a 100.0% late delivery rate across 26,513 orders, while Same Day was 0% late and Standard Class was 39.8%."
- Key UI or visual moments to recreate:
  - The massive 100% SLA Breach Alert card.
  - The 3-metric KPI scorecard ($2.06M Profit at Risk, 54.71% Late Rate, 18.69% Negative Margin).
  - The Pre-Dispatch Machine Learning Scan interface with live mitigation triggers.
  - The executive project conclusion and GitHub repository lock.
- Copy that must appear verbatim:
  - "172,765 FULFILLMENT ORDERS ANALYZED"
  - "FIRST CLASS DELAY RATE: 100.0%"
  - "26,513 OF 26,513 ORDERS DELAYED"
  - "$2,055,765 PROFIT AT RISK"
  - "PRE-DISPATCH ML SCAN · RANDOM FOREST + SMOTE"
  - "github.com/prathmeshmdeshmane001/supply-chain-analysis"
  - "Built by Prathamesh Deshmane"

## Creative Direction
- Tone preset: `yc-parody` / `polished`
- Creative direction: Deadpan executive logistics teardown
- Interpretation: Deliver shocking, verified real-world supply chain numbers completely straight. Terminal-sharp typography, glowing borders, high contrast, zero corporate buzzwords.
- Hook (0-3s): "Customers pay extra for First Class shipping. The result: 100.0% late delivery rate."
- Outro / punchline (16-20s): "Default to Standard Class. Buffer the checkout promise. Defend the margin."
- Avoid:
  - Generic SaaS marketing clichés ("Streamline your workflow")
  - Abstract filler graphics and ungrounded shapes
  - Cluttered low-contrast text that hurts readability

## Visual Identity
- Background: `#0b0f19` (Deep slate background with subtle radial glow)
- Card Surfaces: `#141c2e` with subtle glass borders (`rgba(255, 255, 255, 0.08)`)
- Primary Accent: `#21918c` (Viridis teal from analytical charts)
- Secondary Accent: `#440154` (Viridis deep purple)
- Warning / Highlight: `#fde725` (Viridis yellow)
- Danger Alert: `#ff453a` (High-contrast alert crimson)
- Text Primary: `#ffffff`
- Text Secondary: `#94a3b8`
- Display font: `Plus Jakarta Sans`, `Inter`, -apple-system, sans-serif
- Monospace / Data font: `JetBrains Mono`, `SF Mono`, monospace

## Storyboard Summary
1. **Scene 1: The Premium Shipping Paradox (0.0s – 4.5s)**:
   - Audit badge appears at 0.2s.
   - Headline appears at 0.6s: "Customers pay extra for First Class shipping."
   - Crimson alert card slams in at 1.8s: "FIRST CLASS DELAY RATE: 100.0% (26,513 / 26,513 Orders Delayed)".
   - Holds settled until 4.5s.
2. **Scene 2: The $2.06M Margin Bleed (4.5s – 9.5s)**:
   - 3 executive metric cards snap in sequentially on beats:
     - Card 1 at 4.8s: `54.71% LATE RATE` (94,523 orders breached SLA)
     - Card 2 at 5.8s: `$2,055,765 PROFIT AT RISK` (27.4% of total profit exposed)
     - Card 3 at 6.8s: `18.69% NEGATIVE MARGIN` (32,295 orders losing money)
   - Bottom banner at 7.8s: `P90 Lead Time Buffer: +3.0 Days`.
3. **Scene 3: Pre-Dispatch ML Risk Engine (9.5s – 15.5s)**:
   - Order card appears at 9.8s (`Order #89201 · Central Africa · First Class`).
   - ML Scanner sweeps across at 10.6s: `RANDOM FOREST + SMOTE (78% PRECISION)`.
   - Risk badge pops at 11.6s: `LATE RISK: 84% [HIGH]`.
   - 3 mitigation checkboxes illuminate green at 12.6s:
     - `[✔] Rerouted: Standard Class (-60.2% Delay Rate)`
     - `[✔] Dynamic EDD: +1.5 Days Buffer at Checkout`
     - `[✔] Margin Defended: $148.20 Preserved`
4. **Scene 4: The Strategic Takeaway & Outro (15.5s – 20.0s)**:
   - Locks at 16.0s (aligned with 16.02s strong musical cue).
   - Display: "Default to Standard Class. Buffer the checkout."
   - Project Title: "Supply Chain Analytics & Predictive SLA Risk Engine"
   - Repository: "github.com/prathmeshmdeshmane001/supply-chain-analysis"
   - Signature: "Built by Prathamesh Deshmane"

## Audio
- Audio role: Modern, polished electronic business track with rhythmic drive.
- Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3` (120.19 BPM)
- Music treatment: Starts at 0.0s, volume 0.75, subtle swell at 15.5s, clean fade out at 19.5s to 20.0s.
- Music cue guidance: Preset cues loaded from `happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.json`. Scene 4 outro entrance locks to strong cue at 16.02s. Metric cards snap to beat grid (~0.50s spacing).
- SFX files selected:
  - `impact/impactBell_heavy_000.ogg` (at 1.8s for 100% card slam)
  - `interface/click_002.ogg` (at 4.8s, 5.8s, 6.8s for metric cards)
  - `interface/switch_001.ogg` (at 12.6s for mitigation triggers)
  - `casino/chipsCollide3.ogg` / chime (at 16.0s for outro lock)

## Hyperframes Requirements
- Use standard Hyperframes conventions (`data-track-index`, `data-start`, `data-duration`, `data-volume`).
- Build self-contained HTML/CSS/JS in `brag-output/composition/`.
- Ensure all text passes WCAG contrast and readability thresholds.
- Copy required audio files to `brag-output/composition/assets/`.
- Run `npx hyperframes check` and fix any lint or layout findings before rendering.
- Render final video to `brag-output/brag.mp4`.
