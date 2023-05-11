model_description='''# Three component + Carreau model fit

Workflow:
1. Upload data
2. Load data
3. Select step
3. Analyze data
4. Download results

Rheological model: $$\sigma=\sigma_y + \sigma_y (\dot\gamma / \dot\gamma_c)^{1/2} + \dot\gamma \eta_0 \cdot (1+(\dot\gamma/\dot\gamma_{c_carreau})^2)^{(1)/2} $$
* $\sigma$: stress [Pa] (dependent variable) measured stress
* $\sigma_y$: yield stress [Pa] (model parameter) indicates the minimum stress required to initiate material flow
* $\dot\gamma$: shear rate [1/s](independent variable) imposed shear rate
* $\dot\gamma_{c_{TC}}$: critical shear rate TC model component [1/s](model parameter) Can be interpreted as the minimum shear rate to ensure uniform flow in the sample volume
* $\eta_0$ : Low shear limit of carreau background viscosity (model parameter) Can be interpreted as the limit at low shear of the clear phase viscosity
* $\dot\gamma_{c_{Carreau}}$: critical shear rate from Carreau model [1/s] (model parameter) Onset of shear thinning for clear phase 

for more information about the model see [link](https://pubs.aip.org/sor/jor/article/64/2/413/241704/Variations-of-the-Herschel-Bulkley-exponent)
'''