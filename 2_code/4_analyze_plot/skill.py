import numpy as np
import xarray as xr


def skill(da_sim, da_obs, da_msk, hmin=0.15):
    sim = (da_sim > hmin).where(~da_msk, False)
    obs = (da_obs > 0).where(~da_msk, False)  # assume obs is binary mask of extent

    ds = xr.Dataset(
        dict(
            true_pos=np.logical_and(sim, obs),
            false_neg=np.logical_and(~sim, obs),
            false_pos=np.logical_and(sim, ~obs),
        )
    )

    ntot = np.logical_or(sim, obs).where(~da_msk, False).sum(("x", "y"))
    nobs = obs.where(~da_msk, False).sum(("x", "y"))
    nsim = sim.where(~da_msk, False).sum(("x", "y"))

    hit_rate = ds["true_pos"].sum(("x", "y")) / nobs
    false_rate = ds["false_pos"].sum(("x", "y")) / nsim
    csi = ds["true_pos"].sum(("x", "y")) / ntot
    bias = ds["false_pos"].sum(("x", "y")) / ds["false_neg"].sum(("x", "y"))
    da_skill = xr.merge(
        [
            csi.rename("C"),
            hit_rate.rename("H"),
            false_rate.rename("F"),
            bias.rename("E"),
        ]
    )

    # true negative and mask are both 0
    da_cm = (ds["true_pos"] * 3 + ds["false_pos"] * 2 + ds["false_neg"] * 1).astype(
        np.uint8
    )
    da_cm.raster.set_crs(da_sim.raster.crs)
    da_cm.raster.set_nodata(da_sim.raster.crs)

    return da_skill, da_cm
