from napari_qrcode import qrcode_widget


def test_qrcode_widget(make_napari_viewer, capsys):
    viewer = make_napari_viewer()

    my_widget = qrcode_widget()

    assert my_widget is not None
