# 🧾 Changelog  
All notable changes to **NUDaVizEngine** will be documented in this file.  

The format follows [Semantic Versioning](https://semver.org/).  
Each version will include notes on **new features**, **changes**, **fixes**, and **future directions**.

---

## [0.0.1] - 2025-10-20  
### 🧩 Initial Development Phase

**Summary:**  
This is the first internal development version of **NUDaVizEngine**, marking the beginning of the project’s journey.  
This release establishes the foundation for a modular and maintainable architecture for scientific data visualization.

### Added  
- 🧠 **Core Architecture**
  - Implemented the `Dataset` abstraction for generic data handling.  
  - Added support for dataset extensions specific to instruments (e.g., `UVVisDatasetHP8453`).  
  - Added a `UVVisSpectra` class with an `addDataset()` method to manage multiple datasets.  
- 🧰 **Data Handling**
  - Initial I/O management through utility functions.  
  - Early design of file loading, parsing, and metadata handling.  
- 🧪 **Structure & Packaging**
  - Created package directory structure (`dataset`, `scientific_data`, `utils`, etc.)  
  - Added placeholder modules for future features (`physical_quantities`, `visualizers`).  
- 📦 **Project Setup**
  - Added `README.md`, `LICENSE`, `.gitignore`, and `pyproject.toml`.  
  - Defined project intent and roadmap.  
- 🧭 **Documentation**
  - Added initial documentation of architecture and project vision in README.

### Coming Next  
- 📊 Plotting capabilities and visualization layer (`visualizers` module).  
- ⚙️ Unit and quantity conversion engine (`physical_quantities` module).  
- 🧩 Dataset registry system for auto-detection of data sources.  
- 🧪 Expanded experimental and computational technique support (e.g., TGA, DFT).

---

## [Unreleased]  
### Planned
- Full integration with **NuSciTools** web interface.  
- Additional instrument-specific dataset handlers.  
- Automated testing and continuous integration setup.  
- Initial release on **PyPI** (v0.1.0 milestone).

---

🧠 *NUDaVizEngine — Part of the NanoUncovered ecosystem, where scientific research meets tech reviews.*
