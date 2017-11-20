# Final Paper 
Tentative due date: December 05, 2017  
Final Day to submit: December 17, 2017

## Sections (tentative to change)
1. Introduction
2. Background
3. Motivation
4. Approach
5. Evaluation & Observations
6. Related Work
7. Conclusions & Future Work
8. Acknowledgements

## Helpful Tips for writing LaTeX (in Visual Studio Code)
- Use LaTeX-workshop extension available at: [https://github.com/James-Yu/LaTeX-Workshop]()
  - Can be found via the "Extensions" tab in VS Code by searching for "LaTeX Workshop"
  - Provides useful syntax highlighting and other LaTeX language features
- Use vscode-latex-preview extension available at: [https://github.com/ajshort/vscode-latex-preview]()
  - Can be found via the "Extensions" tab in VS Code by searching "LaTex Preview"
  - Similar to the markdown tool in Visual Studio Code, will allow for a preview of the document to be seen while working on it
  - Additionally, the extension provides syntax highlighting and other useful language-extension type functionalities
  - Requires the pdflatex command, so if you don't have it (and are running Fedora) it can be installed by using: 
      - ``sudo dnf install texlive-latex``
- A nice reference for using LatEx can be found at: [https://en.wikibooks.org/wiki/LaTeX]()
- .. and a quick tutorial can be found at: [http://www.rpi.edu/dept/arc/training/latex/class-slides-pc.pdf]()

## Acknowledgements
- This paper used the [USENIX LaTex template](https://www.usenix.org/sites/default/files/template.la_.txt) as a foundation
  - Out of the box, the USENIX template was not working on my machine because I was missing style files, they are as follows and can be found at:
  - ``usenix.sty`` can be downloaded from:[https://www.usenix.org/sites/default/files/usenix.sty_.txt]()
  - ``endnotes.sty`` can be downloaded from: [https://mirror.hmc.edu/ctan/macros/latex/contrib/endnotes/endnotes.sty]()
- Thanks to this [bug report](https://bugzilla.redhat.com/show_bug.cgi?id=578426) that helped me to get LaTeX running on my machine (Fedora 26)