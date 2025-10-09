from rocketpy import Environment, SolidMotor, Rocket, Flight

env = Environment(latitude=-21.90795, longitude=-48.96156, elevation=495)

import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 14)
)  # Hour given in UTC time

env.set_atmospheric_model(
    type="custom_atmosphere",
    pressure=None,       # utiliza ISA para pressão
    temperature=None,    # utiliza ISA para temperatura
    wind_u=[(0, -10)],    # 10 m/s na componente leste (U) a partir do solo
    wind_v=[(0, 0)]      # 0 m/s na componente norte (V) a partir do solo
)

Kratosv3 = SolidMotor(
    thrust_source="data/meteor-RASP_Kratos v3.2.eng",
    dry_mass=1.758,
    dry_inertia=(0.0567, 0.0567, 0.0016),
    nozzle_radius=24.5 / 1000,
    grain_number=4,
    grain_density=1890,
    grain_outer_radius=29.7/ 1000,
    grain_initial_inner_radius=12.7 / 1000,
    grain_initial_height=100 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.2978,
    center_of_dry_mass_position=0.268,
    nozzle_position=0,
    burn_time=3.911,
    throat_radius=8.25 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

LTS = Rocket(
    radius=105 / 2000,
    mass=5.365,
    inertia=(1.22, 1.22, 0.01),
    power_off_drag="data/drag_curve.csv",
    power_on_drag="data/drag_curve.csv",
    center_of_mass_without_motor=0.991,
    coordinate_system_orientation="nose_to_tail",
    
)
LTS.add_motor(Kratosv3, position=2)

nose_cone = LTS.add_nose(
    length=0.21, kind="elliptical", position=0
)

fin_set = LTS.add_trapezoidal_fins(
    n=4,
    root_chord=0.147,
    tip_chord=0.050,
    span=0.110,
    position=1.76,
)

tail = LTS.add_tail(
    top_radius=102/2000, bottom_radius=60/2000, length=0.080, position=1.92
)

rail_buttons = LTS.set_rail_buttons(
    upper_button_position=0.975,
    lower_button_position=1.89,
    angular_position=45,
)
test_flight = Flight(
    rocket=LTS, environment=env, rail_length=4, inclination=80, heading=90
    )

test_flight.all_info()