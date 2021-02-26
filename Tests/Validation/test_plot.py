import pytest
from SciDataTool import DataLinspace, DataTime
from SciDataTool import save_validation_path
from SciDataTool.Functions.Plot.plot_2D import plot_2D
from numpy import meshgrid, pi, linspace, zeros, sin, split, sum
from os.path import join


@pytest.mark.validation
# @pytest.mark.DEV
def test_plot():
    """Test plot"""
    Time = DataLinspace(name="time", unit="s", initial=0, final=10, number=1001)
    Angle = DataLinspace(name="angle", unit="rad", initial=0, final=2 * pi, number=2001)
    angle, time = meshgrid(Angle.get_values(), Time.get_values())
    field = time + angle
    Field = DataTime(name="Example field", symbol="Z", axes=[Time, Angle], values=field)

    Field.plot_2D_Data(
        "time",
        "angle=[0,pi/4,pi/2]",
        is_show_fig=False,
        save_path=join(save_validation_path, "plot_2D.png"),
    )
    Field.plot_3D_Data(
        "time",
        "angle{°}",
        is_2D_view=True,
        is_show_fig=False,
        save_path=join(save_validation_path, "plot_3D.png"),
    )


def test_normalization():
    Time = DataLinspace(name="time", unit="s", initial=0, final=10, number=1001)
    time = Time.get_values()
    speed = 5 * time + 2
    Time.normalizations = {"rpm": speed}
    Angle = DataLinspace(name="angle", unit="rad", initial=0, final=2 * pi, number=2001)
    angle, time = meshgrid(Angle.get_values(), Time.get_values())
    field = time + angle
    Field = DataTime(name="Example field", symbol="Z", axes=[Time, Angle], values=field)

    Field.plot_2D_Data(
        "time->rpm",
        is_show_fig=False,
        save_path=join(save_validation_path, "plot_norm.png"),
    )
    Field.plot_3D_Data(
        "time->rpm",
        "angle{°}",
        is_2D_view=True,
        is_show_fig=False,
        save_path=join(save_validation_path, "plot_norm_3D.png"),
    )


if __name__ == "__main__":
    test_plot()
    test_normalization()
