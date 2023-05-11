import lmfit

def TC(x, ystress=1.0, eta_bg=0.1, gammadot_crit=0.1):
    """Three component model
    Args:
        ystress: yield stress [Pa]
        eta_bg : Background viscosity [Pa s]
        gammadot_crit : Critical shear rate [1/s]
    Returns:
        stress : Shear Stress, [Pa]
    """
    return ystress + ystress * (x / gammadot_crit) ** 0.5 + eta_bg * x

TC_model = lmfit.Model(TC, prefix="TC_")

# set parameters for model class
TC_model.set_param_hint("ystress", min=0)
TC_model.set_param_hint("eta_bg", min=0, value=0, vary=False)
TC_model.set_param_hint("gammadot_crit", min=0)

def carreau(x, eta_0=1.0, gammadot_crit=1.0, n=0.5, prefix="carreau"):
    """carreau Model

    Note:

    .. math::
       \sigma=\dot\gamma \cdot \eta_0 \cdot (1+(\dot\gamma/\dot\gamma_c)^2)^{(n-1)/2}

    Args:
        eta_0: low shear viscosity [Pa s]

        gammadot_crit: critical shear rate [1/s]

        n : shear thinning exponent

    Returns:
        stress : Shear Stress, [Pa]
    """
    return x * eta_0 * (1 + (x / gammadot_crit) ** 2) ** ((n - 1) / 2)


carreau_model = lmfit.Model(carreau, prefix="carreau_")

carreau_model.set_param_hint("eta_0", min=0)
carreau_model.set_param_hint("gammadot_crit", min=0, vary=True)
carreau_model.set_param_hint("n", min=0, max=1, value=0, vary=False)

TCC_model=TC_model+carreau_model
