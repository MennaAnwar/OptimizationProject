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

![image](https://github.com/MennaAnwar/OptimizationProject/assets/93788514/5b734ebe-3277-4ed0-8cca-040cd52af877)

# Localization Techniques in VLP System:
- Position related parameters: Time of Arrival (TOA), Time Difference of Arrival (TDOA), Angle of Arrival (AOA) and Received Signal Strength (RSS)
## Direct Localization:
- -The received signal from transmitters is directly used without examining parameters.
- For example: time of arrival $\tau_i = \frac{|l_i - l_t|_2}{c} + \Delta_i$, where &\Delta_i& depends on the synchronization between transmitters and recievers.
- Can be synchronous, asynchronous or quasi-synchronous.

## Two-Step Localization:

  
