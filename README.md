# Visual Mathematics

**Visual Mathematics** is an interactive collection of notebooks designed to build _intuition_ for mathematical, signal-processing, and machine-learning concepts through **visualisation, interactivity, and direct manipulation of equations**.

Rather than presenting mathematics as static symbols on a page, this repository focuses on _seeing_ how mathematical objects behave: how parameters change shapes, how structure emerges, and how abstract formulas map onto concrete visuals.

The emphasis is on **understanding before formalism**, without sacrificing technical correctness.

## Project Philosophy

Many mathematical, signal-processing, and machine-learning ideas are not difficult because they are inherently complex, but because they are **experienced only through static symbols and final equations**. Too often, learners are asked to accept results without ever seeing how structure emerges, how parameters influence behaviour, or why a particular formulation makes sense in the first place.

This creates a gap between _knowing_ an equation and _understanding_ it.

In practice, most intuition is built through experimentation: changing a parameter, observing what breaks, noticing patterns, and gradually forming a mental model. However, traditional resources rarely support this process. Concepts are presented as fixed truths rather than dynamic systems, and learners are left to build intuition implicitly or not at all.

This project exists to address that gap.

**Visual Mathematics** treats mathematical objects as things you can _interact with_, not just write down. Sliders, widgets, and live plots are used to expose how equations behave under change, how geometry encodes algebra, and how abstract definitions translate into visible structure. The aim is not to simplify mathematics, but to make its internal logic more transparent.

This project is built around three principles:

- **Interactivity** – sliders, widgets, and controls allow parameters to be changed in real time
- **Visual grounding** – equations are always tied to plots, geometry, or distributions
- **Incremental intuition** – concepts are explored progressively, not presented as finished results

The goal is not to replace textbooks or lectures, but to complement them by making abstract ideas

The goal is not to replace textbooks or lectures, but to **complement them by making abstract ideas _feel obvious_...feel inevitable rather than arbitrary**. When a formula finally appears, it should feel like a natural conclusion of what has already been observed.

## Repository Structure

The repository is organised by conceptual domain, reflecting how these topics naturally build on one another.

```text
visual-mathematics/
├── README.md
├── requirements.txt
└── notebooks/
    ├── fundamental_mathematics/
    │   ├── README.md
    │   ├── 01_unit_circle.ipynb
    │   ├── 02_trigonometric_identities.ipynb
    │   └── 03_gaussian_distribution.ipynb
    │
    ├── signal_processing/
    │   ├── README.md
    │   └── (DSP-focused visual notebooks)
    │
    └── machine_learning/
        ├── README.md
        └── (ML intuition and visualisation notebooks)
```

Each subfolder contains its own `README.md` describing the scope and assumed background for that domain.

## What This Project Covers

### Fundamental Mathematics

- Trigonometry (unit circle, sine/cosine geometry)
- Trigonometric identities through geometric interpretation
- Gaussian distributions and parameter effects
- Sampling behaviour and structure (e.g. Sobol vs random)

### Signal Processing (growing)

- Frequency-domain intuition
- Windowing and transforms
- Time–frequency representations
- Visual explanations of DSP operations

### Machine Learning (future expansion)

- Loss landscapes
- Optimisation behaviour
- Bias–variance intuition
- Probability distributions and geometry in ML contexts

## What This Project Does _Not_ Aim to Do

To keep expectations clear:

- This is **not** a formal course or curriculum
- It does **not** claim pedagogical completeness
- It does **not** focus on performance, benchmarking, or production code
- It is **not** intended as a replacement for mathematical rigor

The notebooks prioritise **clarity and intuition** over abstraction or efficiency.

## How to Use This Repository

1.  Clone the repository
2.  Install dependencies from `requirements.txt`
3.  Launch Jupyter Lab or Jupyter Notebook
4.  Open any notebook and interact with the widgets

Many notebooks rely on `ipywidgets`, so running them locally (rather than via static previews) is strongly recommended.

## Intended Audience

This project is suitable for:

- Students building intuition alongside formal study
- Engineers and scientists revisiting fundamentals
- Curious learners who prefer visual explanations
- Anyone who has thought _“I understand the equation, but I don’t quite feel it yet”_

The only assumed background is basic mathematical literacy and curiosity.

## Status and Ongoing Development

This repository is **actively evolving**.

New notebooks will be added over time, existing ones refined, and concepts expanded as new ideas become visually interesting enough to explore.

There is no fixed endpoint by design.

## Acknowledgements

Some notebooks and explanations were developed with the assistance of ChatGPT (OpenAI), used strictly as a drafting and ideation aid. All final structure, intent, and technical decisions reflect my own understanding and goals.
