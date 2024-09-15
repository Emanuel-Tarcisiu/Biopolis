import openeo
import os
import shutil
import rasterio
from rasterio.plot import show
from rasterio.plot import reshape_as_image
import numpy as np
from matplotlib import pyplot as plt


def get_new_vegHealth_png():
    con = openeo.connect("openeo.dataspace.copernicus.eu")
    con.authenticate_oidc_client_credentials(
        client_id="sh-47f8b039-dbe2-4811-81bd-38e3d1accb4e",
        client_secret="cQ5Z8gsWi9jh2DvjmYeoHMaa2zhn2GM8",
    )

    datacube = con.load_collection(
        "SENTINEL2_L1C",
        spatial_extent={"west": 25.97413, "south": 44.43, "east": 25.99284, "north": 44.45},
        temporal_extent = ["2022-02-01", "2023-02-11"],
        bands=["B04", "B08"],
        max_cloud_cover=25,
    )

    datacube = datacube.process(
        process_id="ndvi", 
        arguments={
            "data": datacube, 
            "nir": "B08", 
            "red": "B04"}
    )

    tmp_path="tmp/ndvi.tiff"
    out_path="output/ndvi.png"

    if (os.path.exists("tmp")):
        shutil.rmtree("tmp", ignore_errors=True)

    os.mkdir("tmp")

    result = datacube.max_time().download(outputfile=tmp_path)

    with rasterio.open(tmp_path) as src:
        # Read the data from the file
        data = src.read()

        # If the data has more than one band, reshape it for visualization
        # Assuming the data has 3 bands (RGB)
        if data.shape[0] == 3:
            # Reshape data to (height, width, bands)
            image = reshape_as_image(data)

        # If the data has only one band, you might need to normalize it
        elif data.shape[0] == 1:
            image = data[0]
            # Normalize data to the range 0-255
            image = (image - image.min()) / (image.max() - image.min()) * 255
            image = image.astype(np.uint8)

        else:
            raise ValueError("Unsupported number of bands in GeoTIFF")

        # Save the image as a PNG
        plt.imsave(out_path, image)