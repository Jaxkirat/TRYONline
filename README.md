# TRYONline

TRYONline is an interactive virtual fitting room application that allows users to upload photos and garments to visualize how clothes will look on them. It leverages advanced image processing and deep learning models to create realistic previews, enhancing the online shopping experience.

## Demo

Watch the demo video to see how TRYONline works in action:


https://github.com/user-attachments/assets/f13b6173-4037-4bcd-afb0-73b38e54ceef




## Features



## Technologies Used

- **Streamlit** for the web application interface.
- **OpenCV** for image processing and manipulation.
- **TensorFlow** for deep learning model integration.
- **Pillow** for image handling and transformation.
- **Dressing in Order Framework** for garment modeling and virtual try-on, as referenced from [this paper](https://github.com/cuiaiyu/dressing-in-order).

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/TRYONline.git
   cd TRYONline
   
2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Project Structure
- main.py: The main application script.
- requirements.txt: List of dependencies.
- .env: Environment variables file (not included in the repository, create it manually).
- /static: Contains images, CSS, and other static files.

## Disclaimer
Please note that software dependencies listed in requirements.txt can become outdated over time. It is advisable to periodically review and update the dependencies to ensure compatibility and security.

## Future Improvements
- Enhance the garment overlay algorithm for better accuracy.
- Expand support for more garment types and body shapes.
- Improve the user interface for a more immersive experience.
- Add support for augmented reality (AR) try-ons.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements 
- OpenCV
- TensorFlow
- Pillow
- Dressing in Order Framework
  
----
Created by [Jaskirat Singh](https://Github.com/Jaxkirat)
