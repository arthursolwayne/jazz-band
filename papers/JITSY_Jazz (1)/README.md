# Just-in-Time-Symbolic Jazz: AAAI 2026 NeuSymBridge Workshop Paper

This directory contains the LaTeX source for the workshop paper submission to NeuSymBridge @ AAAI 2026.

## Files

- `paper.tex` - Main LaTeX source file
- `references.bib` - BibTeX bibliography file
- `aaai2026.sty` - AAAI 2026 style file (required)
- `aaai2026.bst` - AAAI bibliography style (required)

## Compilation Instructions

### Using pdflatex and bibtex

```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

The final PDF will be `paper.pdf`.

### Using latexmk (recommended)

```bash
latexmk -pdf paper.tex
```

To clean auxiliary files:

```bash
latexmk -c
```

## Current Status

### Complete Sections
- Introduction (merged from CLAUDE.md)
- Related Work (comprehensive survey)
- Problem Setup
- Methods (RLVR and GEPA with equations)
- Metrics and Checkers (outline)
- Discussion and Conclusion

### Sections Needing Work
- **Abstract** - Needs to be written
- **Metrics and Checkers** - Needs detailed metric formulas
- **Experimental Setup** - Needs specific model details and hyperparameters
- **Results** - Needs tables and figures
- **Analysis** - Needs experimental analysis

### Known Issues
- Some citations may need verification (e.g., `agrawal2025gepa` is a placeholder)
- Page count TBD - typical workshop limit is 6-8 pages
- Figures/tables need to be created and added
- Some TODO comments remain in the source

## AAAI 2026 Format Requirements

This paper uses the AAAI 2026 anonymous submission format:
- Two-column layout
- Times Roman font
- 10pt body text with 12pt leading
- Anonymous submission (no author names)
- US Letter paper size (8.5" x 11")

## Workshop Submission Details

- **Workshop**: W21 - Bridging Neurons and Symbols for NLP and Knowledge Graph Reasoning
- **Conference**: AAAI 2026
- **Location**: Singapore
- **Date**: January 26, 2026
- **Submission Deadline**: November 15, 2025

## Notes

- The paper is currently formatted for anonymous submission
- For camera-ready, update to `\usepackage{aaai2026}` (remove `[submission]`)
- Add author names and affiliations for camera-ready
- Add acknowledgments section for camera-ready (currently commented out)

## Contact

For questions about the paper content or submission, contact the workshop organizers at:
- qp241311@qmul.ac.uk
- td540@cam.ac.uk
