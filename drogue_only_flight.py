import datetime
from rocketpy import Environment, SolidMotor, Rocket, Flight

env = Environment(latitude=-21.90795, longitude=-48.96156, elevation=495)


tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 14)
)  # Hour given in UTC time

env.set_atmospheric_model(
    type="custom_atmosphere",
    pressure=None,  # utiliza ISA para pressão
    temperature=None,  # utiliza ISA para temperatura
    wind_u=[(0, 10)],  # 10 m/s na componente leste (U) a partir do solo
    wind_v=[(0, 0)],  # 0 m/s na componente norte (V) a partir do solo
)

Kratosv3 = SolidMotor(
    thrust_source="data/thrust_curve.csv",  # o arquivo .csv deve ter as colunas na ordem: tempo(s), empuxo(N)
    dry_mass=8.507,
    dry_inertia=(0.8723763, 0.8723763, 0.02510097),
    nozzle_radius=37 / 1000,
    grain_number=5,
    grain_density=1749,
    grain_outer_radius=92.20 / 1000,
    grain_initial_inner_radius=52.2 / 1000,
    grain_initial_height=170 / 1000,
    grain_separation=4 / 1000,
    grains_center_of_mass_position=598.3051 / 1000,
    center_of_dry_mass_position=635.69 / 1000,
    nozzle_position=0,
    burn_time=3.239,
    throat_radius=12.75 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

LTS = Rocket(
    radius=127 / 2000,
    mass=26490 / 1000,
    inertia=(-12.54, 360.79, 1000),
    power_off_drag="data/drag_curve.csv",
    power_on_drag="data/drag_curve.csv",
    center_of_mass_without_motor=1830 / 1000,
    coordinate_system_orientation="tail_to_nose",
)
LTS.add_motor(Kratosv3, position=2)

nose_cone = LTS.add_nose(
    length=300 / 1000,
    kind="elliptical",
    position=2200 / 1000,
)

fin_set = LTS.add_trapezoidal_fins(
    n=4,
    root_chord=300 / 1000,
    tip_chord=150 / 1000,
    span=170 / 1000,
    position=2200 / 1000,
)

tail = LTS.add_tail(
    top_radius=102 / 2000,
    bottom_radius=60 / 2000,
    length=0.080,
    position=1.92,
)
rail_buttons = LTS.set_rail_buttons(
    upper_button_position=985 / 1000,
    lower_button_position=10 / 1000,
    angular_position=90,
)

drogue = LTS.add_parachute(
    name="Drogue",
    cd_s=1.27125,
    trigger="apogee",
    sampling_rate=100,
)

test_flight = Flight(
    rocket=LTS,
    environment=env,
    rail_length=6,
    inclination=80,
    heading=90,
)

test_flight.all_info()
