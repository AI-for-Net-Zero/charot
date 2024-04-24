import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from solver.KS_solver import KS
import torch


def contourplot_KS(uu, dt=0.5, num_plot_points=1000, plot_frame=False, frameskip=1, filename=''):
    # Make contour plot of solution
    fig, ax = plt.subplots()
    tt = np.arange(uu.shape[0]) * dt
    N = uu.shape[1]
    x = np.arange(0, 2 * np.pi, 2 * np.pi / N)
    ct = ax.contourf(x, tt[:num_plot_points][:num_plot_points][::frameskip], uu[:num_plot_points][::frameskip],
                     61,
                     cmap=cm.RdBu,
                     vmin=-2.5,
                     vmax=2.5)
    if plot_frame:
        ax.set_xlabel('x')
        ax.set_ylabel('t')
        # ax.colorbar()
        ax.set_title('Solution of the KS equation')
    else:
        ax.axis('off')
    fig.colorbar(ct)
    # plt.savefig(f'ks_plot_{filename}.png', bbox_inches = 'tight', dpi=3000)
    plt.show()


if __name__ == '__main__':

    N = 256  # number of collocation points
    dt = 0.05 # timestep size
    nu = 0.08156697852139966
    actuator_locs = torch.tensor(np.linspace(0.0, 2*np.pi, num=3, endpoint=False))
    actuator_locs = torch.tensor(np.linspace(1.0, 2*np.pi-1, num=3, endpoint=True))
    ks = KS(nu=nu, N=N, dt=dt, actuator_locs=actuator_locs, actuator_scale=0.2)

    # Random initial data
    u = 1e-2 * np.random.normal(size=N)  # noisy intial data
    u = u - u.mean()
    u = torch.tensor(u)

    action = torch.zeros(ks.num_actuators)
    action1 = torch.ones(ks.num_actuators)
    action2 = torch.tensor(np.random.uniform(size=ks.num_actuators), dtype=torch.float32)

    # Plot the profile of the actuators
    show_frame = False
    xx = np.linspace(0.0, 2*np.pi, num=N)
    fig, ax = plt.subplots()
    ax.plot(xx, ks.B @ action2)
    #plt.plot(xx, torch.sum(ks.B, dim=1))
    if show_frame:
        ax.title('Actuator profile in domain')
    else:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        # ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
    # plt.show()

    # Burn-in
    burnin = 0
    for _ in range(burnin):
        u = ks.advance(u, action)
    # Advance solver
    uu = []
    for _ in range(1000):
        u = ks.advance(u, action)
        uu.append(u.detach().numpy())
    uu = np.array(uu)

    contourplot_KS(uu, dt=dt, plot_frame=True, frameskip=2, filename=f'{nu:.3f}')


    reward = np.mean(np.linalg.norm(uu, axis=-1))
    print(reward)