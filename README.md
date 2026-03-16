<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FE428E&center=true&vCenter=true&width=600&lines=%F0%9F%93%9A+Vocabulary+Flashcard+App;%E2%9A%A1+Interactive+Learning;%F0%9F%90%8D+Powered+by+Python+%26+Tkinter" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Pandas-FE428E?style=for-the-badge&logo=pandas&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Tkinter-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A dynamic, interactive Desktop GUI application built to accelerate language learning through the active recall method. The app uses a smart flashcard system that automatically saves your progress and scales the difficulty as you master new words.

**Key Features:**
* **⏳ Auto-Flip Mechanism:** Cards automatically flip from Romanian to English after a 3-second delay using Tkinter's `.after()` loop.
* **💾 State Management:** Known words are removed from the queue, and progress is dynamically saved to a `words_to_learn.csv` file. You never study the same mastered word twice!
* **📈 Auto-Leveling System:** Seamlessly transitions the user to Level 2 and Level 3 datasets once the current vocabulary pool is exhausted.
* **🎨 Custom UI:** Built with Tkinter Canvas for a sleek, borderless, and image-driven user experience.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
Words learning app/
├── main.py                     # Main application script & UI logic
├── words_to_learn.csv          # Dynamically generated state file
├── data/                       # Vocabulary datasets
│   ├── romanian_words.csv      # Level 1 words
│   ├── romanian_words_lvl2.csv # Level 2 words
│   └── romanian_words_lvl3.csv # Level 3 words
└── images/                     # UI Assets
    ├── card_front.png          
    ├── card_back.png           
    ├── right.png               
    └── wrong.png
```

<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛ **80%** | **Data Integration (Pandas)**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **Canvas UI (Tkinter)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛ **90%** | **State Logic & Auto-Leveling**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **Path Architecture** *(Refactor needed)*

<br>

**🟢 High-Impact Wins:**
* **Data Mastery:** Smart use of Pandas for rapid CSV processing.
* **UX Flow:** Tkinter `.after()` mechanism implements auto-flip flawlessly.

**🔧 Key Recommendations:**
* **Paths:** Shift from absolute to relative file paths.
* **Architecture:** Transition global state to an OO `class` structure.

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
