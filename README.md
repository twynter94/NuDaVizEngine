# 🧠 NUDaVizEngine  
**NanoUncovered Data Visualization Engine**  
_A modular Python library for scientific data visualization and analysis._

⚠️ **Pre-Alpha / Early Development**  
This library is **not yet ready for public use**
---

## 🌍 Overview  

**NUDaVizEngine** is part of the **NanoUncovered** initiative — a project born out of my PhD research in **nanosensors**, created to inspire upcoming researchers and help make nanosensor research more accessible to a wider audience.  

During my work, I realized how much time researchers spend collecting, analyzing, and visualizing data.  
This engine was created to make that process **easier, faster, and more reproducible** — allowing scientists to focus on the science, not the formatting.

**Mission:**  
To empower students and researchers with open, high-quality visualization tools that make scientific communication effortless — from raw data to publication-ready graphs.

---

## ✨ Key Features (in progress)

- 📊 Unified data handling through the `Dataset` abstraction  
- ⚙️ Modular architecture for **scientific techniques** (e.g., UV-Vis, TGA, DFT outputs)  
- 🧱 Extensible registry for adding new data sources or instruments  
- 📐 Physical quantities and unit conversion engine  
- 🧰 Clean, maintainable, object-oriented design for research workflows  
- 🔄 Future integration with **NuSciTools** (web interface for non-coders)

---

## 🧩 Project Structure  
```
NUDaVizEngine/
└── src/
    ├── nudavizengine/
    │ ├── init.py
    │ ├── dataset/ # Core data abstractions (Dataset, UVVisDatasetGaussian16, etc.)
    │ ├── physical_quantities/ # Physical quantities and unit conversion
    │ ├── scientific_data/ # Domain-specific modules (UVVisSpectra, TGA, etc.)
    │ ├── utils/ # I/O handling, helpers, and shared functionality
    │ └── visualizers/ # Core visualization engine (matplotlib, seaborn, etc.)
    └── tests/
│
├── docs/
├── tests/
├── examples/
├── pyproject.toml
├── LICENSE
└── README.md
```
---

## 🚀 Getting Started  

### Installation (coming soon)  
Once released on PyPI:
```bash
pip install nudavizengine
```
For now, you can clone the repository:
```bash
git clone https://github.com/twynter94/NUDaVizEngine.git
cd NUDaVizEngine
```
## 🧪 Example (early implementation)
```python
from nudavizengine import Dataset, UVVisSpectra, UVVisDatasetHP8453

# Create a UV-Vis object and add a dataset from the Agilent HP8453 spectrophotometer
filepath = "/path/to/data.csv"
uvSpectra = UVVisSpectra()
uvData = UVVisDatasetHP8453(filePath=filepath)
uvSpectra.addDataset(uvData)

# Examine the datasets
print(uvSpectra.describeDatasets())

# Analyze or visualize
uvSpectra.visualize(preview=True)
```
⚠️ Note: Plotting and visualization functions are still under development.

## 🧭 Project Vision
NUDaVizEngine is part of the NanoUncovered brand — where scientific research meets tech reviews.

Through the NanoUncovered ecosystem:

🧠 NUDaVizEngine → the data visualization and analysis library

💻 NuSciTools → the web interface for non-technical users

🎥 NanoUncovered YouTube Channel → outreach to communicate nanosensor research and inspire young scientists

This project exists to lighten the load for researchers, so anyone — from a PhD student to a professor — can produce high-quality scientific graphics effortlessly.

## 📚 Citation
If you use NUDaVizEngine in research or videos, please cite:

Wynter, T. (2025). NUDaVizEngine: A modular Python library for scientific data visualization and analysis.
Part of the NanoUncovered ecosystem.
https://github.com/twynter94/NUDaVizEngine

## 🤝 Contributing
Contributions are welcome!
Whether it’s code, documentation, or feedback — feel free to open an issue or submit a pull request.

## 📜 License
Released under the BSD 3-Clause License — see LICENSE for details.
You’re free to use, modify, and distribute this software with proper attribution.

## 🔬 About the Author
Theodore Wynter — Scientist & Software Developer

PhD student and founder of **NanoUncovered**, a brand where Scientific Research Meets Tech Reviews.

Passionate about nanosensor research, scientific communication, and creating tools that empower the next generation of scientists.

## 🌐 Connect with NanoUncovered

- YouTube: [NanoUncovered Channel](https://www.youtube.com/@NanoUncovered)  
- LinkedIn: [Theodore Wynter](https://www.linkedin.com/in/theodorewynter/)

🧭 NUDaVizEngine is still in early development follow for updates on NUDaVizEngine, NUSciTools, scientific visualization tutorials, and nanosensor research insights!
