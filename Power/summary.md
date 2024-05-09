# Resource Optimization in Visible Light Communication for Internet of Things

## Optimization Problem:

**Objective:** Minimize the total consumed energy emitted by each LED.

### Constraints:

- **LEDs’ Power Budget:** Each LED has a maximum power limit.
- **Users’ Perceived Quality-of-Service:** Maintain effective data transmission quality.
- **LED-User Associations:** Properly associate each LED with at most one user.
- **Illumination Uniformity Constraints:** Ensure uniform lighting throughout the area.

### Solution Approach:

- **Stage 1: LED-User Association for Fixed LED Powers:**\
   Design an efficient algorithm to associate users with LEDs, assuming the power of each LED is fixed.

- **Stage 2: Power Optimization using LED-User Association:**\
  Using the established LED-user association, optimize the power levels of the LEDs. This involves finding an approximate solution using the Taylor series to balance energy consumption and constraints.

## System Model:

- **The bulb is a hemispherical structure with multiple LEDs to cover different parts of the room, serving as both a light source and a wireless access point:**

  > This structure aligns with the optimization problem's focus on ensuring illumination uniformity and effective LED-user associations to provide both lighting and data transmission.

- **The system consists of 𝑀 LEDs and 𝑈 users, with each LED emitting power
  𝑃<sub>𝑚</sub>
  Watts. Users are equipped with photo-detectors (PDs) to receive data from LEDs.**

  > This setup directly relates to the LEDs’ power budget constraint and the users’ perceived quality-of-service (QoS) constraint, as each LED’s power needs to be optimized for efficient data transmission and adequate lighting.

- **LEDs provide dual functionality: illumination and wireless data download to mobile users. Each LED acts as a transmitter, facilitating simultaneous downloads to multiple users:**
  > This dual functionality is central to the optimization problem, which aims to minimize total energy consumption while maintaining both lighting and communication efficiency.

### Assumptions:

- Inside the room, each mobile user can have one PD
  receiver and one RF transmitter, and this user is able to
  extricate the desired signal from the optical transmitters.
- Locations of the mobile users are known.
- There are N fixed sensors uniformly distributed inside
  the room. These are not equipped with decoders and are
  only used for measuring the illumination uniformity in
  the room. The light intensity received at these sensors
  determine how uniform the lighting is inside the room. It
  is possible to place these sensors at a place of interest,
  however, we assume that they are uniformly distributed, in a lattice placement pattern, to the room floor.

- A binary variable ϵ
  <sub>mu</sub> that indicates the
  association between LED m and user u which is given as
  follows:
  <div style="text-align: center;">
  <img src="image-3.png" alt="">
  <img src="image-4.png">
  </div>

  we assume that user u can be associated to many
  LEDs at the same time. In contrary, an LED is not allowed to
  associate with more than one user simultaneously

## Problem Formulation:

We formulate an optimization problem aiming to minimize
the total energy consumption of LEDs while satisfying a certain
rate threshold for users and taking into consideration the
association and illumination uniformity constraints. So, the
optimization problem can be written as:

<div style="text-align: center;">
    <img src="image-2.png" alt="Optimization Problem">
</div>

**where:**

- _(2) and (8)_ represent the LEDs’ power budget and association constraints.
- (9) represents the illumination uniformity
  constraint.\
  I<sub>min</sub> is defined as the minimum acceptable illumination uniformity threshold which we set to be 0.7.
- (10) represents the minimum rate QoS, where R is
  the minimum rate expected for each IoT device.

## Problem Solution:

The formulated optimization problem given in (7)-(10)
is a non-convex and mixed-integer non-linear programming
problem. So, we propose a low complexity two stages solution.\
**P0:** In the first stage, we propose a ’Nearest User
Assignment’ approach to determine the value of ϵ
<sub>mu</sub> .\
**P1:** given the LED-user associations, we optimize the LEDs’ power
allocations in the second stage.

Optimizing ϵ <sub>mu</sub> and P<sub>m</sub>
really complex specially for IoT scenarios where we have large number of users U and large number of LEDs M.

In a practical scenario, IoT devices or users will be moving in the room and every time users’ locations change the optimization will need to be re-performed.\
Therefore, a Two-Stage Solution (TSS) as a practical and efficient solution with less complexity is used.

### 1) LED-User Association:

---

> ### Nearest User Assignment Approach
>
> #### Purpose:
>
> To efficiently assign each LED to the nearest user, ensuring optimal alignment for data transmission.
>
> #### Steps:
>
> 1. **Identify Light Cone of Each LED:**
>    - Determine the light cone region for each LED.
> 2. **Determine User Coordinates:**
>    - Obtain the positions of all users in the room.
> 3. **Calculate Proximity:**
>    - For each LED \( m \), compute the distance to each user’s position.
> 4. **Assign Nearest User:**
>    - Find the user \( u \) closest to the LED’s light cone center.
>    - Set \( ϵ<sub>mu</sub> = 1 \) for the nearest user and \( ϵ<sub>mu'</sub> = 0 \) for all other users.
> 5. **Ensure Exclusive Assignment:**
>    - Ensure each LED is assigned to only one user at a time.
> 6. **Use Association Matrix:**
>    - Use the resulting LED-User association matrix \( ϵ<sub>mu</sub> \) for further optimization.

<div style="text-align: center;">
    <img src="image-5.png" alt="Optimization Problem">
</div>

### 2) Power Optimization:

---

For given LED-user association, the optimization problem **P0** that optimizes LEDs’ power can be written as:

<div style="text-align: center;">
    <img src="image-6.png" alt="Optimization Problem">
</div>

the objective function is a convex function
and all constraints are convex functions except (10). This constraint is neither concave nor convex with respect to the LED
transmit power P<sub>m</sub> . Hence, the goal is to convert constraint (10)
into a convex one in order to solve the problem efficiently.
Therefore, constraint (10) can be re-written as:

<div style="text-align: center;">
    <img src="image-7.png" alt="Optimization Problem">
    <img src="image-8.png" alt="Optimization Problem">
</div>
