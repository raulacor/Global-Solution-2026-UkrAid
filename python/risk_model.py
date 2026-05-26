#Imports:
import math

#K_ Variables:
# Threat attenuation constants
K_TROOPS = 0.1      # low — persistent, mobile threat
K_AIR_RAID = 0.3    # medium — wide area, temporary
K_MISSILE_MAX = 0.8 # high — blast fades fast with distance
LAMBDA_= 0.5        # how fast missile site becomes safe


#Functions:
def troop_risk(d, k = K_TROOPS):
    return math.exp(-k * d) / (d ** 2)


def air_raid_risk(d, k = K_AIR_RAID):
    return math.exp(-k* d) / (d ** 2)


def missile_strike(d, t, lambda_ = LAMBDA_, k_max = K_MISSILE_MAX):
    k =  k_max * (1 - math.exp(-lambda_ * t)) #This defines how much energy - potential destruction - an already striked zone could have.
    return math.exp(-k * d) / (d ** 2)


def total_risk(r_missile, r_air, r_troops):
    return max(r_missile, r_air, r_troops)