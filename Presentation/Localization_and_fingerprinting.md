# Before you proceed: 
- This document shall include what I think can be presented in my part, along possible images and script.
- It is susceptible to change, since I avoided some details for the sake of focusing on the subject in hand.

# What is localization:
- It is the determination of the position of the object under study using infrastucture to obtain the required information.
- Indoor localization can be done using Radio Frequency (RF) or Visible Light (VL) Systems.
- Why are we interested in VLS ?
  - The unlicensed spectrum of the visible light.
  - Can use the already existing LEDs in the infrasturcture.
  - Is preferable to RF systems due to:
    - Lower Power Consumption.
    - Inherent LOS of VLS (no inter-cell intereference).
    - No RF interference with alreadt existing RF signals.
- Along with robustness, cost-efficieny, and reliability, Visible Light Positioning (VLP) systems should satisfy illumination requirements without noticeable flicker or color change.

<p align="center">
<img src="https://github.com/MennaAnwar/OptimizationProject/assets/93788514/5b734ebe-3277-4ed0-8cca-040cd52af877" 
 title = "Localization Techs" width="150%" height="auto">
 </p>

# Localization Techniques in VLP System:
- Position related parameters: Time of Arrival (TOA), Time Difference of Arrival (TDOA), Angle of Arrival (AOA) and Received Signal Strength (RSS)
## Direct Localization:
- -The received signal from transmitters is directly used without examining parameters.
- For example: time of arrival $\tau_i = \frac{|l_i - l_t|_2}{c} + \Delta_i$, where &\Delta_i& depends on the synchronization between transmitters and recievers.
- Can be synchronous, asynchronous or quasi-synchronous.

## Two-Step Localization:
- Performs Position Estimation in two stages:
  1. Position-related parameters extraction.
  2. Position estimation using algorithms.
- These algorithms are grouped into: Proximity, Geometrical , Statistical, and Fingerprinting methods, which is the focus of this problem.

## Fingerprinting Method:
- Generally consists of two phases: Offline and Online. 
  - Offline: a database is constructed by gathering measurements over a grid of reference points in an indoor environment.Each entry of the database stores the location of the specified reference point and the parameter estimates (e.g., RSS, TOA, TDOA, AOA, or a combination of them) associated with the LED transmitters obtained at that location.
  - Online: The measured vector of parameters is compared with the database to decide on the location of the receiver according to a proximity measurement between the measured data and the offline database.

 # What can be included in the slides (This is a suggestion only):
Slide 1: title: What is Localization?
         "The determination of the position of the object under study using infrastucture to obtain the required information."
Slide 2: Middle: Why VL instead of RF ?
Slide 3: title: Localization Techniques:
          image: Localization Techs

  
