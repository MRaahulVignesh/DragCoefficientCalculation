# DragCoefficientCalculationDrag Coefficient

## Definition 
In fluid dynamics, the drag coefficient (commonly denoted as: Cd, Cx or Cw) is a dimensionless quantity that is used to quantify the drag or resistance of an object in a fluid environment, such as air or water. It is used in the drag equation in which a lower drag coefficient indicates the object will have less aerodynamic or hydrodynamic drag. The drag coefficient is always associated with a particular surface area.

The drag coefficient of any object comprises the effects of the two basic contributors to fluid dynamic drag: skin friction and form drag. The drag coefficient of a lifting airfoil or hydrofoil also includes the effects of lift-induced drag. The drag coefficient of a complete structure such as an aircraft also includes the effects of interference drag.


## Drag Equation
In fluid dynamics, the drag equation is a formula used to calculate the force of drag experienced by an object due to movement through a fully enclosing fluid. The formula is accurate only under certain conditions: the objects must have a blunt form factor and the system must have a large enough Reynolds number to produce turbulence behind the object. 

The equation is  Fd = 12  u2 Cd A  --------------------> 1

Where,
Fd is the drag force, which is by definition the force component in the direction of the flow velocity, 
Ρ is the mass density of the fluid,

u is the flow velocity relative to the object, 
A is the reference area, and
Cd is the drag coefficient.

## Calculation Method

### 1 : Using Gradient Descent Method


#### Formula Used:
   Fd = -Cd*A*0.5*rho*V^2
   Frr = -Crr*M*g 
   F = Fd + Frr 
   F = M*a (total force)
 
Using the equations 1,2,3,4, the acceleration due to air and wind resistance as a function of velocity is calculated


 
Where, 
   
   Fd is the force on the vehicle due to air resistance (drag) in Newtons
   Frr is the force on the vehicle due to rolling resistance in Newtons
   F is the total force on the vehicle in Newtons
   V is the vehicle's velocity in m/s
   a is the vehicle's acceleration in m/s^2
   A is vehicle frontal area in m^2
   M is vehicle mass including occupants in kg
   rho is the density of air which is 1.22 kg/m^3 at sea level
   g is the gravitational acceleration constant which is 9.81 m/s^2
   Crr is the vehicle's coefficient of rolling resistance
   Cd is the vehicle's drag coefficient we want to determine
 
We arrive at this formula assuming the following conditions:

1. Since, during the calculation of V, the vehicle will be coasting in neutral. Therefore, the propulsive force is taken as zero (Ft = 0).

2. The angle of inclination of the road is 0ofrom the horizontal. (assumed)
 
Therefore, the actuatal motion equation becomes into,

 Ft - (Fd+Frr) = Ma
 
#### Procedure:
1. Drive to a flat road with little traffic or wind.
2. Have the passenger ready with a stopwatch and paper to record data.
3. Have the driver accelerate up to above 70 km/h or so, and shift into neutral.
4. Record data as follows. The driver should indicate when the speed drops to exactly 70 km/h. At this time (t=0) the passenger should start the clock. The passenger should indicate every 10 seconds after that and the driver should call out the current speed to the nearest whole km. The passenger should record this value next to each time.
5. Repeat the test in the opposite direction.
6. Repeat the test in both directions twice more (possibly, 6 trials in all, 3 in each direction). All these values will be averaged for a more accurate analysis.
7. Enter these values in a spreadsheet and feed it to the code given below. The algorithm averages data from all 6 trials to create a single data set representing velocity (V actual) as a function of time. It then generates it's own model for velocity (V model) based on entered constants and initial guesses for Cd and Crr. Gradient descent function is used to adjust Cd and Crr in order to minimize the error between the model and actual data. Once the error is minimized and the model data matches the actual data as best it can, then Cd is correct.
8. The estimated result will closely represent the original value of Cd and Cr.

** _For directly interacting with the code, follow the below link_
https://colab.research.google.com/drive/1m7HbeyILhITISCZrKSfL-EKgYk_Nu7Hz?usp=sharing#scrollTo=Xxs7giRrHStv_ **

### References
https://www.researchgate.net/publication/321482419_Determination_of_drag_coefficient_for_TOYOTA_car_model_Using_Strain_Gauge_Method
https://www.instructables.com/id/Measure-the-drag-coefficient-of-your-car/
https://www.engineeringtoolbox.com/drag-coefficient-d_627.html  
https://www.britannica.com/science/fluid-mechanics/Drag#ref611768 
https://www.grc.nasa.gov/WWW/K-12/airplane/dragco.html 


