<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FE428E&center=true&vCenter=true&width=600&lines=%F0%9F%93%9A+Vocabulary+Flashcard+App;%E2%9A%A1+Interactive+Learning;%F0%9F%90%8D+Powered+by+Python+%26+Tkinter" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Pandas-FE428E?style=for-the-badge&logo=pandas&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Tkinter-A9FEF7?style=for-the-badge&logo=python&logoColor=black" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A professional language-learning desktop application designed to facilitate active recall. The program displays a randomized word from a CSV database, provides a 3-second delay for the user to guess, and then flips the card to reveal the translation. 

**Technical Logic (Verified):**
* **⏳ Event-Driven Timer:** Uses `window.after()` to synchronize the UI "flip" animation with the data state, ensuring a seamless user experience.
* **💾 Data Persistence:** Implements a feedback loop where known words are removed from the dictionary and the remaining "to-learn" list is exported back to CSV.
* **📈 Dynamic Leveling:** Features a sequential file-loading system that transitions from Level 1 to Level 3 datasets using robust `try/except` blocks.
* **🖼️ Canvas Layering:** Leverages the Tkinter `Canvas` widget to dynamically update text properties (font, color, content) over graphical image assets.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
Words learning app/
├── main.py                     # Execution logic & UI Event Loop
├── words_to_learn.csv          # Local storage for mastered vocabulary
├── data/                       # Dataset directory (Lvl 1, 2, 3)
└── images/                     # UI Assets (Card fronts/backs & buttons)
```

<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-BEGINNER_/_INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛ **80%** | **Data Structuring (Pandas Dicts)**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **UI Event Handling (Tkinter)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **Hot-Swapping Datasets**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **Path Architecture**

<br>

**🟢 High-Impact Wins:**
* **Logic Decoupling:** Effectively separating the "flip" timer from the "change card" mechanism.
* **File Resilience:** Proactive error handling ensures the app doesn't crash if a level dataset is missing.

**🔧 Technical Debt:**
* **Relative Paths:** Currently uses absolute paths; refactoring to `os.path` would make the code cross-platform compatible.
* **OOP Transition:** The code is functional but procedural. Moving to a class-based structure would enhance modularity.

<br>


<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
