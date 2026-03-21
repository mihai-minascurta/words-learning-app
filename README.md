<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=39FF14&center=true&vCenter=true&width=600&lines=%F0%9F%93%9A+Vocabulary+Flashcard+App;%E2%9A%A1+Interactive+Learning;%F0%9F%90%8D+Powered+by+Python+%26+Tkinter" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-2F2F2F?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Pandas-2F2F2F?style=for-the-badge&logo=pandas&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Tkinter-2F2F2F?style=for-the-badge&logo=python&logoColor=white" height="35">
</div>

<br>

<h3>
  <span style="color: #39FF14;">🚀 Project Overview</span><br>
  <img src="https://placehold.co/1000x2/39FF14/39FF14.png" width="100%" height="2" alt="Green Divider"/>
</h3>

A professional language-learning desktop application designed to facilitate active recall. The program displays a randomized word from a CSV database, provides a 3-second delay for the user to guess, and then flips the card to reveal the translation. 

**Technical Logic (Verified):**
* **⏳ Event-Driven Timer:** Uses `window.after()` to synchronize the UI "flip" animation with the data state, ensuring a seamless user experience.
* **💾 Data Persistence:** Implements a feedback loop where known words are removed from the dictionary and the remaining "to-learn" list is exported back to CSV.
* **📈 Dynamic Leveling:** Features a sequential file-loading system that transitions from Level 1 to Level 3 datasets using robust `try/except` blocks.
* **🖼️ Canvas Layering:** Leverages the Tkinter `Canvas` widget to dynamically update text properties (font, color, content) over graphical image assets.

<br>

<h3>
  <span style="color: #00E5FF;">📁 Project Structure</span><br>
  <img src="https://placehold.co/1000x2/00E5FF/00E5FF.png" width="100%" height="2" alt="Cyan Divider"/>
</h3>

```text
Words learning app/
├── main.py                     # Execution logic & UI Event Loop
├── words_to_learn.csv          # Local storage for mastered vocabulary
├── data/                       # Dataset directory (Lvl 1, 2, 3)
└── images/                     # UI Assets (Card fronts/backs & buttons)
```
<h3>
  <span style="color: #BC13FE;">🧠 Code Review & Complexity</span><br>
  <img src="https://placehold.co/1000x2/BC13FE/BC13FE.png" width="100%" height="2" alt="Purple Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-BEGINNER_/_INTERMEDIATE-2F2F2F?style=for-the-badge&logoColor=39FF14" height="35">
</div>

<br>

> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=39FF14&vCenter=true&width=400&lines=>_ANALYZING_SYSTEM_COMPLEXITY..." alt="Animated Loading" />
> 
> <table>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">Data Structuring (Pandas)</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/39FF14/39FF14.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #00E5FF;">UI Event Handling (Tkinter)</span></b></td>
>     <td width="200"><img src="https://placehold.co/140x10/00E5FF/00E5FF.png"/><img src="https://placehold.co/60x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #00E5FF;">70%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #BC13FE;">Hot-Swapping Datasets</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/BC13FE/BC13FE.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #BC13FE;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">Path Architecture</span></b></td>
>     <td width="200"><img src="https://placehold.co/100x10/39FF14/39FF14.png"/><img src="https://placehold.co/100x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">50%</span></b></td>
>   </tr>
> </table>

<br>

**🟢 High-Impact Wins:**
* **Logic Decoupling:** Effectively separating the "flip" timer from the "change card" mechanism.
* **File Resilience:** Proactive error handling ensures the app doesn't crash if a level dataset is missing.

**🔧 Technical Debt:**
* **Relative Paths:** Currently uses absolute paths; refactoring to `os.path` would make the code cross-platform compatible.
* **OOP Transition:** The code is functional but procedural. Moving to a class-based structure would enhance modularity.

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=16&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=500&lines=[SYSTEM_SCAN_COMPLETE]----------------------------" alt="Animated Scan Divider" />
</div>
