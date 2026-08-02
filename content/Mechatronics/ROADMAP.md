# Roadmap

Checklist / book index. Update only when a milestone changes state.
Do not maintain this weekly.

**Legend:**
⬜ not started · 🔨 active · ✅ complete

## Phase 0 — Foundations & Vocabulary

|**Milestone**|**Status**|
|---|---|
|[0.1 — Problem-Solving + Toolchain](milestones/00_foundations.md#milestone-01-problem-solving-framework-toolchain)|⬜|
|[0.2 — Vectors + Trig](milestones/00_foundations.md#milestone-02-vectors-trig-frames-of-reference)|⬜|
|[0.3 — Calculus Intuition](milestones/00_foundations.md#milestone-03-calculus-intuition)|⬜|
|[0.4 — Statics + FBDs + FEM Intuition](milestones/00_foundations.md#milestone-04-statics-free-body-diagrams)|⬜|
|[0.5 — Circuits Basics](milestones/00_foundations.md#milestone-05-circuits-basics)|⬜|
|[0.6 — Power + Thermal](milestones/00_foundations.md#milestone-06-power-efficiency-thermal)|⬜|
|[0.7 — Materials + Failure + Selection](milestones/00_foundations.md#milestone-07-materials-failure-and-selection)|⬜|
|[0.8 — Manufacturing + DFMA](milestones/00_foundations.md#milestone-08-manufacturing-processes-dfma)|⬜|
|[0.9 — Mechanisms + Kinematic Elements](milestones/00_foundations.md#milestone-09-mechanisms-kinematic-elements)|⬜|

## Phase 1 — Signals, Actuators, Dynamics

|**Milestone**|**Status**|
|---|---|
|[1.1 — I2C Sensor + Telemetry](milestones/01_signals_actuators_dynamics.md#milestone-11-i2c-sensor-telemetry)|⬜|
|[1.2 — Noise + Filtering + Frequency Domain](milestones/01_signals_actuators_dynamics.md#milestone-12-noise-filtering-and-frequency-domain)|⬜|
|[1.3 — H-Bridge + BLDC Commutation](milestones/01_signals_actuators_dynamics.md#milestone-13-h-bridge-bldc-commutation-characterization)|⬜|
|[1.4 — Dynamics Model](milestones/01_signals_actuators_dynamics.md#milestone-14-pendulum-dynamics-model-hardware-validation)|⬜|
|[1.5 — Integration + Sensor Fusion + Calibration](milestones/01_signals_actuators_dynamics.md#milestone-15-phase-1-integration-sensor-fusion-calibration)|⬜|
|[1.6 — Stepper + Microstepping](milestones/01_signals_actuators_dynamics.md#milestone-16-stepper-motor-microstepping-driver)|⬜|

## Phase 2 — Embedded Architecture & Real-Time Control

|**Milestone**|**Status**|
|---|---|
|[2.1 — Bare-Metal STM32 + SPI + UART](milestones/02_embedded_realtime_control.md#milestone-21-bare-metal-stm32-foundation)|⬜|
|[2.2 — PID Theory + Tuning](milestones/02_embedded_realtime_control.md#milestone-22-pid-theory-tuning-in-simulation)|⬜|
|[2.3 — FOC Closed-Loop](milestones/02_embedded_realtime_control.md#milestone-23-foc-closed-loop-on-hardware)|⬜|
|[2.4 — FreeRTOS Multi-Task](milestones/02_embedded_realtime_control.md#milestone-24-freertos-multi-task-firmware)|⬜|
|[2.5 — Multi-DOF Dynamics + State-Space](milestones/02_embedded_realtime_control.md#milestone-25-multi-dof-dynamics-state-space-control)|⬜|
|[2.6 — Limit Switches + Homing + State Machines](milestones/02_embedded_realtime_control.md#milestone-26-limit-switches-homing-and-state-machine-design)|⬜|

## Phase 3 — Mechanical Design, PCB, Verification

|**Milestone**|**Status**|
|---|---|
|[3.1 — CAD + Machine Elements + FEA + Drawings](milestones/03_mech_pcb_verification.md#milestone-31-cad-machine-elements-fea-drawings)|⬜|
|[3.2 — First Custom PCB + Power Stage + EMC](milestones/03_mech_pcb_verification.md#milestone-32-first-custom-pcb-power-stage-emc)|⬜|

## Phase 4 — Capstone & Industrial Integration

|**Milestone**|**Status**|
|---|---|
|[4.1 — CAN + C++ Messaging](milestones/04_capstone_integration.md#milestone-41-can-c-messaging)|⬜|
|[4.2 — Motion + Dynamics-Aware Control](milestones/04_capstone_integration.md#milestone-42-motion-integration-dynamics-aware-control)|⬜|
|[4.3 — Safety + HIL](milestones/04_capstone_integration.md#milestone-43-safety-hil)|⬜|
|[4.4 — Workcell Polish](milestones/04_capstone_integration.md#milestone-44-workcell-polish)|⬜|

## Phase 5 — Portfolio & Delivery

|**Milestone**|**Status**|
|---|---|
|[5.1 — Portfolio + Documentation](milestones/05_portfolio_delivery.md#milestone-51-portfolio-documentation)|⬜|

## Calibration

|**Phase**|**Planned**|**Actual**|
|---|---|---|
|Phase 0|8–14 wk||
|Phase 1|10–18 wk||
|Phase 2|11–24 wk||
|Phase 3|10–19 wk||
|Phase 4|9–18 wk||
|Phase 5|3–6 wk||

_Update actuals only at phase completion._

## Resource Map

| **Phase** | **Primary**                                                                                             | **Secondary**                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **0**     | Ulaby Ch 1 · Nise Ch 2 · Rizzoni Ch 1–2 · Shigley Ch 1–3, 8, 13–17 · Norton, Design of Machinery Ch 1–5 | 3B1B · Efficient Engineer · Falstad · Velxio (local circuit sim) · Ashby, Materials Selection · 507 Mechanical Movements |
| **1**     | Ulaby Ch 4–5 · Nise Ch 2,7 · AoE Ch 9 · Hughes, Electric Motors and Drives Ch 1–4                       | White Ch 5 · scipy docs · Smith, DSP Guide · Velxio (ESP32 + I2C sim before hardware) · TMC2209 datasheet                |
| **2**     | STM32 Ref Manual · Nise Ch 8–10 · Craig, Intro to Robotics Ch 6–7                                       | White Ch 2–4 · ST/TI app notes · 3B1B linear algebra                                                                     |
| **3**     | Nise Ch 2 · AoE Ch 1,5,8 · Shigley Ch 3, 8, 11 · TI SLVA404 (buck layout)                               | Solid Edge CE · PrePoMax + CalculiX · KiCad 9 docs · Phil's Lab (YouTube) · IPC · SKF/NSK bearing catalogs               |
| **4**     | Lospinoso · White Ch 6 · Craig Ch 6–7                                                                   | ROS 2 docs · IEC 62061                                                                                                   |

## Speed Runs

_One per phase. Plus optional "from scratch" builds._

|**Phase**|**Speed Run**|**Your time**|
|---|---|---|
|**0**|LED blinky + motor spin on breadboard, video it|~1 wk|
|**0 opt**|**Speaker from scratch:** cup + magnet + coil → proper voice-coil speaker with 3D-printed frame. Hear F = BIL. Video it.|~1 weekend|
|**0 opt**|**Generator from scratch:** hand-crank a magnet past a coil, light an LED. Rectify it. Measure voltage vs. speed. Faraday's law in your hands.|~1 weekend|
|**0 opt**|**Mechanism speed run:** build a four-bar, a Geneva, and a ratchet from cardboard or 3D print in one afternoon. Film each one moving. Post with one-sentence explanations.|~1 afternoon|
|**1**|IMU → PlotJuggler, post screenshot + explanation|~3 days|
|**2**|Port SimpleFOC to your STM32 in a weekend|~1 wk|
|**3**|Order a PCB from a reference design, modify one thing. FEA one bracket: Solid Edge → STEP → PrePoMax, validate against hand calc.|~2 wk|
|**4**|Contribute a bug fix or doc improvement upstream|~1 wk of your time, review cycle is theirs|

> **Note:** "Your time" = hours you spend, not calendar days.
>
> Speed Runs produce something explainable to someone outside your head.
>
> That's the Hypothesis Loop aimed outward. Free byproduct, not extra task.
>
> The "from scratch" builds are optional but recommended. They make the equations physical. A speaker is a linear motor you can hear. A generator is a motor run backwards. Neither requires a roadmap entry — they're weekend speed runs that change how the theory feels.
>
> The mechanism speed run pairs with Milestone 0.9. Cardboard four-bars take 20 minutes. Seeing the Grashof condition change a crank-rocker into a double-rocker by flipping which link you hold is worth more than a page of derivation.