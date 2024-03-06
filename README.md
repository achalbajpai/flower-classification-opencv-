# Flower Classification with OpenVINO

This project uses OpenVINO (Open Visual Inference and Neural network Optimization) to deploy a flower classification model. The model is trained to recognize various types of flowers, including daisy, dandelion, roses, sunflowers, and tulips.

## Prerequisites

- OpenVINO toolkit installed
- Python 3.x
- OpenCV
- NumPy

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flower-classification-openvino.git
    ```

2. Download the pre-trained model (`flower.xml`) and place it in the project directory.

3. Install the required dependencies:

    ```bash
    pip install openvino opencv-python numpy
    ```

4. Run the classification script:

    ```bash
    python3 flower_classification.py
    ```

## Usage

1. Adjust the input image path (`op`) in the script to test different flower images.

2. The script will resize the input image, load the pre-trained model, and output the predicted flower class.

## Model Information

The flower classification model is based on the OpenVINO framework. You can find more information about OpenVINO at [OpenVINO Toolkit](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html).

## Class Labels

- 0: Daisy
- 1: Dandelion
- 2: Roses
- 3: Sunflowers
- 4: Tulips

## Acknowledgments

- Special thanks to the contributors and maintainers of the OpenVINO toolkit.

## License

This project is licensed under the [MIT License](LICENSE).

