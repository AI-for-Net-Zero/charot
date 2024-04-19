import uuid
from datetime import datetime


def generate_exp_name(cfg) -> str:
    """Generates an ID (str) for the described experiment using UUID and current date."""
    exp_name = "_".join(
        (
            cfg.env.exp_name,
            cfg.network.architecture,
            f"S{cfg.env.num_sensors}",
            f"A{cfg.env.num_actuators}",
            f"nu{cfg.env.nu:.2f}",
            str(uuid.uuid4())[:8],
            datetime.now().strftime("%y_%m_%d-%H_%M_%S"),
        )
    )
    return exp_name