import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Exoplanets_project.settings')
django.setup()


from eplanet.models import Exoplanets
import pandas as pd



def create_data():
    df = pd.read_csv("oec.csv")
    for i in range(3584):
        name = df["PlanetIdentifier"][i]
        tofp = df["TypeFlag"][i]
        mass_jpt = df["PlanetaryMassJpt"][i]
        radius_jpt = df["RadiusJpt"][i]
        period_days = df["PeriodDays"][i]
        semi_major_axis = df["SemiMajorAxisAU"][i]
        eccentricity = df["Eccentricity"][i]
        surface_temp_K = df["SurfaceTempK"][i]
        discovery_method = df["DiscoveryMethod"][i]
        discovery_year = df["DiscoveryYear"][i]
        right_ascension = df["RightAscension"][i]
        declination = df["Declination"][i]
        distance_from_star = df["DistFromSunParsec"][i]
        mass_star_slr = df["HostStarMassSlrMass"][i]
        radious_star_slr = df["HostStarRadiusSlrRad"][i]
        metallicity_star = df["HostStarMetallicity"][i]
        tempK_star = df["HostStarTempK"][i]
        status = df["HostStarAgeGyr"][i]
        planet = Exoplanets(name=name, tofp=tofp, mass_jpt=mass_jpt, radius_jpt=radius_jpt, period_days=period_days,
                            semi_major_axis=semi_major_axis, eccentricity=eccentricity, surface_temp_K=surface_temp_K,
                            discovery_method=discovery_method,
                            discovery_year=discovery_year, right_ascension=right_ascension, declination=declination,
                            distance_from_star=distance_from_star, mass_star_slr=mass_star_slr,
                            radious_star_slr=radious_star_slr, metallicity_star=metallicity_star,
                            tempK_star=tempK_star, status=status)
        planet.save()
create_data()