# Optimisation-Final-Project

This repository contains the final project for F216 - Computational Methods and Optimisation. The project implements and compares several image interpolation algorithms (nearest neighbour, bilinear, bicubic, Lanczos) and provides tooling to apply, visualise, and evaluate them.

---

## Highlights

* Implementations of four interpolation methods used for image upscaling:

  * `nearest_neighbour.py`
  * `bilinear.py`
  * `_bicubic.py`
  * `_lanczos.py`
* CLI entrypoint: `__main__.py` for running experiments or batch processing images.
* Utilities for image handling and evaluation: `utils.py`, `apply_interpolation.py`.
* A short interactive questionnaire/runner: `questionaire.py`.
* A demo video demonstrating the system: `Demo Video.mp4`.

---

## Motivation & Goal

The primary goal is educational: to implement common interpolation techniques and compare their qualitative and quantitative behaviour. This is useful for understanding numerical methods, sampling theory, and practical trade-offs between complexity and visual quality.

---

## Repository structure

```
Optimisation-Final-Project/
├── Demo Video.mp4         # short demonstration of the project
├── LICENSE                # MIT license
├── README.md              # this file
├── __main__.py            # command-line entrypoint
├── apply_interpolation.py # orchestrates applying a chosen interpolator to images
├── nearest_neighbour.py   # nearest neighbour implementation
├── bilinear.py            # bilinear interpolation implementation
├── _bicubic.py            # bicubic interpolation implementation
├── _lanczos.py            # lanczos implementation
├── questionaire.py        # interactive runner / config helper
└── utils.py               # image I/O, helpers, evaluation metrics
```

---

## Requirements

* Python 3.8+
* Recommended packages (install via pip):

  * `numpy`
  * `Pillow` (PIL)
  * `matplotlib` (optional, for plotting/saving comparisons)

> There is no `requirements.txt` included in the repo. To create one quickly:
>
> ```bash
> pip freeze | grep -E "numpy|Pillow|matplotlib" > requirements.txt
> ```

---

## Quick start

1. Clone the repository:

```bash
git clone https://github.com/Briyoji/Optimisation-Final-Project.git
cd Optimisation-Final-Project
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate    # use `venv\Scripts\activate` on Windows
pip install numpy Pillow matplotlib
```

3. Run the main script (example):

```bash
python __main__.py --input data/image.jpg --method bicubic --scale 2 --output out/image_bicubic.jpg
```

If `__main__.py` does not provide these exact CLI flags, open it and adapt the command to the script's CLI options. The `apply_interpolation.py` module can be used directly from Python to run batch jobs or integrate into other pipelines.

---

## Example usage (Python API)

```python
from apply_interpolation import apply_to_image
from utils import load_image, save_image

img = load_image('data/image.jpg')
result = apply_to_image(img, method='lanczos', scale=3)
save_image(result, 'out/image_lanczos.jpg')
```

---

## Evaluation suggestions

* Compare methods visually and using objective metrics such as PSNR and SSIM (implementations can be added to `utils.py`).
* Measure runtime for each method on representative images to show complexity trade-offs.
* Produce a small table and side-by-side image grid for the report.

---

## Demo

Open `Demo Video.mp4` to see the code in action and a sample comparison.

---

## Contribution and next steps

If you want to improve the repository further, consider:

1. Adding `requirements.txt` and `setup.py` or `pyproject.toml`.
2. Implementing unit tests for correctness and regression checks.
3. Adding an automated benchmark script and an output report (CSV/plot).
4. Adding SSIM/PSNR implementations to `utils.py` and producing a results notebook.
5. Writing a short report (PDF/Markdown) summarising methods and results.

Contributions are welcome — feel free to open issues or PRs.

---

## License

This project is distributed under the MIT License. See `LICENSE` for details.

---

## Contact

If you want me to convert this README into a commit-ready `README.md` or open a PR with the updated file, tell me and I will generate the file contents and provide the exact git commands to apply it locally.
