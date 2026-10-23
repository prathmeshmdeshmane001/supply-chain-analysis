# Brag Plan: Supply Chain Analytics & Predictive Delivery Risk Engine

## What is this app?
An end-to-end supply chain operational intelligence and machine learning pipeline that analyzes 172,765 global retail fulfillment orders, exposes a shocking 100% delay rate in First Class shipping with $2.06M in vulnerable profit, and deploys a pre-dispatch Random Forest risk classifier to protect delivery promises at checkout.

## The angle
Deadpan executive logistics teardown. Premium shipping tiers promise speed, but the hard data across 172K orders reveals First Class is late 100% of the time, while Standard Class beats it by 60 percentage points. The solution isn't hoping carriers get faster—it's using machine learning to predict delays at checkout and dynamically adjust promise windows.

## Hook (first 2-3 seconds)
A dark executive dashboard with an urgent crimson alert: "CUSTOMERS PAY EXTRA FOR FIRST CLASS SHIPPING. RESULT: 100.0% LATE DELIVERY RATE (26,513 / 26,513 ORDERS DELAYED)."

## Key moments (the middle)
- The $2.06M Profit Exposure: 54.71% overall SLA breach rate across 172,765 orders, exposing $2.06M in delayed order profits and 18.7% negative-margin shipments.
- The Shipping Mode Inversion: Bar chart showing First Class (100% late) and Second Class (79.8% late) vs Standard Class (39.8% late) and Same Day (0.0% late).
- The Pre-Dispatch Risk Engine: Live simulation of an incoming order scored by Random Forest + SMOTE (78% precision) triggering automated carrier tier routing and dynamic promise date extension (+1.5d).

## Outro / punchline
"Default to Standard Class. Buffer the promise date. Defend the margin." Followed by the project title and GitHub link: `github.com/prathmeshmdeshmane001/supply-chain-analysis`.

## User flow worth showing
The Order Checkout → Predictive Risk Scoring → Automated Mitigation flow:
1. Entry: Incoming checkout order (`Order #89201 · Central Africa · First Class`).
2. Key Action: Pre-dispatch ML engine evaluates 9 features using Random Forest + SMOTE, flagging `Late Risk: 84% [HIGH]`.
3. Result: Automated mitigation triggers: dynamic checkout promise buffered by +1.5 days and freight rerouted to Standard Class, defending margin.

## Tone
- Preset: `yc-parody`
- Creative direction: Deadpan executive logistics teardown
- Interpretation: Deliver astonishing, verified operational numbers completely straight with crisp terminal typography, dark slate backgrounds, Viridis neon accents, and zero corporate fluff.

## Format: landscape — 1920x1080
## Duration: 20.0s

## Visual identity (from the project)
- Background: `#0b0f19` (Deep slate / executive dark)
- Surface/Card: `#141c2e` (Elevated dark card with subtle glass border `#243354`)
- Primary Accent: `#21918c` (Viridis teal from project charts)
- Warning/Highlight: `#fde725` (Viridis yellow)
- Danger Alert: `#ff453a` / `#800000` (Crimson from project KPI plots)
- Text Primary: `#ffffff`
- Text Muted: `#94a3b8`
- Display font: `Plus Jakarta Sans`, `Inter`, -apple-system, sans-serif
- Body font: `JetBrains Mono`, `Inter`, monospace
- Strongest visual element: The high-contrast metric badge and the Shipping Mode horizontal bar breakdown from `outputs/figures/07_shipping_mode_delay_breakdown.png`.

## Share copy (draft)
We analyzed 172,765 supply chain orders and discovered First Class shipping has a 100% late delivery rate while Standard Class is 39.8%. Introducing the Predictive SLA Risk Engine.

## Audio direction
- Role: Rhythmic, forward-moving modern electronic business bed (`happy-beats-business-moves-vol-1-by-ende-dot-app.mp3`, 120.19 BPM) with crisp UI clicks and subtle impact accents.
- Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3`
- Music treatment: Starts at 0.0s, steady volume (0.75), subtle swell at 15.5s, clean fade-out at 19.5s.
- Music cue guidance: Preset cues read from `happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.md`. Strong cue at 16.02s and 17.02s aligned to Scene 4 reveal; beat grid (~0.50s intervals) snaps sequential metric cards in Scene 2 and mitigation badges in Scene 3.
- Audio-reactive treatment: Subtle; use music energy to breathe card glow and border intensity.
- SFX posture: Sparse, motion-matched interface clicks (`click_002.ogg`, `switch_001.ogg`) and low impact on the 100% metric reveal (`impactBell_heavy_000.ogg`).
- Audio-coupled moments:
  - 1.8s: First Class 100% alert badge slam (impact SFX)
  - 4.8s - 7.8s: Metric cards pop in sequentially on beat grid (subtle interface tick)
  - 12.2s: ML mitigation switches toggle on (switch click)
  - 16.0s: Outro hero lock (strong cue alignment)
- Restraint rule: No cartoon whooshes, no loud alarms, no abrasive risers. Professional and sharp.

## Storyboard

### Scene 1 — The Premium Shipping Paradox — 4.5s (0.0s - 4.5s)
Dark executive dashboard. Top pill badge enters: "LOGISTICS AUDIT · 172,765 FULFILLMENT ORDERS".
Hook statement types in: "Customers pay premium rates for First Class shipping."
At 1.8s, a massive red-accented metric panel slams in:
"FIRST CLASS DELAY RATE: 100.0%"
Subtext: "26,513 out of 26,513 orders arrived late."
Sequential/interaction: Pill badge enters at 0.2s -> text settles at 1.0s -> 100% card slams at 1.8s and holds through 4.5s.
Audio intent: Confident beat starts; low impact hit lands on the 100% stat reveal.
Audio-coupled idea: Heavy impact accent at 1.8s when 100.0% slams in.
Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3`
Transition mood: Hard cut → Scene 2

### Scene 2 — The $2.06M Margin Bleed — 5.0s (4.5s - 9.5s)
Grid of 3 executive metric cards appearing sequentially on beat ticks:
- Card 1 (4.8s): "54.71% LATE RATE" — 94,523 orders breached customer SLA
- Card 2 (5.8s): "$2,055,765 PROFIT AT RISK" — 27.4% of total enterprise profit exposed
- Card 3 (6.8s): "18.69% NEGATIVE MARGIN" — 32,295 orders fulfilled at a net loss
Bottom banner settles at 7.8s: "90th Percentile Lead Time Variance: +3.0 Days"
Sequential/interaction: Cards snap in one by one on consecutive beats (4.8s, 5.8s, 6.8s).
Audio intent: Rhythmic forward motion with subtle UI ticks reinforcing each metric arrival.
Audio-coupled idea: `click_002.ogg` on each card entry.
Transition mood: Clean wipe → Scene 3

### Scene 3 — The Predictive Dispatch Engine — 6.0s (9.5s - 15.5s)
Interactive simulation of the Order Management System (OMS) pre-dispatch classifier:
Left panel: "INCOMING ORDER #89201" (Central Africa · First Class Freight · $184.50).
At 10.5s, scanning beam illuminates: "PRE-DISPATCH ML SCAN · RANDOM FOREST + SMOTE".
At 11.5s, Risk Alert flashes: "LATE DELIVERY RISK: 84% [HIGH RISK] (Model Precision: 78%)".
At 12.5s, automated mitigation actions resolve:
- "[✔] Carrier Rerouted: Standard Class (-60.2% Delay Risk)"
- "[✔] Dynamic EDD: +1.5 Days Buffer Added at Checkout"
- "[✔] Margin Defended: $148.20 Profit Preserved"
Sequential/interaction: Order card -> scan line -> risk score -> 3 mitigation checkboxes check on.
Audio intent: High-tech precision, switch clicks on mitigation checks.
Audio-coupled idea: `switch_001.ogg` on mitigation triggers.
Transition mood: Crisp slide → Scene 4

### Scene 4 — The Fix & Outro — 4.5s (15.5s - 20.0s)
Executive conclusion card locks onto beat at 16.0s:
"Default to Standard Class. Buffer the checkout promise."
Headline: "Supply Chain Analytics & Predictive SLA Risk Engine"
Badges: "172K Orders Analyzed · 74% Accuracy · 78% Precision · Zero Source Data Overwritten"
Link: "github.com/prathmeshmdeshmane001/supply-chain-analysis"
Signature: "Built by Prathamesh Deshmane"
Sequential/interaction: Main takeaway centers -> title & badges resolve -> link & author lock in.
Audio intent: Music swell resolves into clean fade out; final subtle bell chime.
Audio-coupled idea: Chime / logo settle at 16.02s (aligned with `strongCues`).
Transition mood: Hold and fade out.

**Music mood for this video:** Confident, modern electronic tech bed with crisp rhythmic momentum.
**Audio summary:** Starts clean with a low impact on the 100% delay reveal, builds rhythm with beat-grid metric clicks, pulses with tech precision during the ML scan, and resolves on a strong musical hit for the final GitHub outro.
