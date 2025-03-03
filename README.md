# MinRoob - Multiplayer Minesweeper Game

MinRoob is a **multiplayer minesweeper game** that allows two players to compete in finding hidden mines on an **8×7 grid**. The game features **turn-based gameplay**, **color-coded mines**, and a **scoring system**. The player who finds **50% or more of the mines first wins**.

## 🎮 Features
- **Multiplayer Mode** (2 Players)
- **Randomly Generated Mines**
- **Auto-Reveal for Empty Cells**
- **Color-coded Mines** for Players (Red & Blue)
- **Turn-based Gameplay**
- **Dynamic Score System**
- **Winning Threshold: 50% of the Mines**
- **Option to Restart or Exit after Each Game**

## 🛠 How to Run
1. Install Python (if not installed) [Download Python](https://www.python.org/downloads/)
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/MinRoob.git
   ```
3. Navigate to the project folder:
   ```bash
   cd MinRoob
   ```
4. Run the game:
   ```bash
   python minroob.py
   ```

## 📜 Rules
- Players take turns selecting a cell on the grid.
- If a **mine (M)** is found, the player earns **1 point**.
- If a number is revealed, it represents the number of **mines in adjacent cells**.
- If an **empty cell (0)** is revealed, the game **automatically uncovers connected empty cells**.
- The player who finds **8 mines (50% of 15) first wins**.
- If all **15 mines are found**, the player with the highest score wins.

## 🎨 Console Colors
- **Red (🔴)** → Player 1 (Finds red mines)
- **Blue (🔵)** → Player 2 (Finds blue mines)

## 🏆 Winning Conditions
- **First to reach 8 points** wins immediately.
- If **all 15 mines** are revealed, the **highest score wins**.
- In case of a tie, the game ends in a **draw**.

## 🚀 Future Updates
- Add **Single-Player Mode**
- Implement **Graphical User Interface (GUI)**
- More **difficulty levels** and board sizes

## 🤝 Contributing
Feel free to **fork**, **modify**, and **submit a pull request**! Any contributions to improve the game are welcome.

## 📜 License
This project is **open-source** and available under the **MIT License**.

---
# 🎮 مین‌روب - بازی مین‌یاب چندنفره

مین‌روب یک **بازی مین‌یاب چندنفره** است که به دو بازیکن اجازه می‌دهد تا در **یک صفحه ۸×۷** با یکدیگر رقابت کنند. هدف بازی **یافتن مین‌ها** است. **هر بازیکنی که ۵۰٪ از مین‌ها را زودتر پیدا کند، برنده خواهد شد.**

## ⚡ ویژگی‌ها
- **حالت دو نفره**
- **تولید تصادفی مین‌ها**
- **کشف خودکار خانه‌های خالی**
- **مین‌های رنگی برای بازیکنان (قرمز و آبی)**
- **بازی نوبتی**
- **سیستم امتیازدهی پویا**
- **حد نصاب برنده شدن: ۵۰٪ از مین‌ها**
- **گزینه شروع مجدد یا خروج پس از هر بازی**

## 🔧 نحوه اجرا
1. نصب **پایتون** (در صورت عدم نصب) [دانلود Python](https://www.python.org/downloads/)
2. کلون کردن مخزن:
   ```bash
   git clone https://github.com/yourusername/MinRoob.git
   ```
3. ورود به پوشه پروژه:
   ```bash
   cd MinRoob
   ```
4. اجرای بازی:
   ```bash
   python minroob.py
   ```

## 📜 قوانین بازی
- هر بازیکن **نوبتی یک خانه** را انتخاب می‌کند.
- اگر یک **مین (M)** پیدا کند، **۱ امتیاز** دریافت می‌کند.
- اگر یک **عدد** ظاهر شود، نشان‌دهنده تعداد مین‌های مجاور است.
- اگر **خانه‌ای خالی (0)** باشد، سیستم به‌صورت **خودکار خانه‌های متصل خالی را آشکار می‌کند**.
- **اولین بازیکنی که ۸ مین (۵۰٪ از ۱۵ مین) پیدا کند، برنده می‌شود.**
- اگر **همه ۱۵ مین** پیدا شوند، بازیکنی که **امتیاز بیشتری دارد، برنده است**.

## 🎨 رنگ‌های کنسول
- **🔴 قرمز** → بازیکن ۱ (مین‌های قرمز)
- **🔵 آبی** → بازیکن ۲ (مین‌های آبی)

## 🏆 شرایط برنده شدن
- **اولین بازیکنی که به ۸ امتیاز برسد، برنده است.**
- اگر **همه ۱۵ مین** کشف شوند، **بیشترین امتیاز برنده خواهد شد.**
- اگر امتیازات برابر باشند، بازی **مساوی** تمام می‌شود.

## 🚀 بروزرسانی‌های آینده
- **اضافه کردن حالت تک‌نفره**
- **ساخت رابط گرافیکی (GUI)**
- **سطوح سختی و اندازه‌های مختلف برای صفحه بازی**

## 🤝 مشارکت در توسعه
اگر علاقه‌مند به بهبود بازی هستید، می‌توانید **فورک کنید، تغییر دهید و Pull Request ارسال کنید**!

## 📜 مجوز
این پروژه **متن‌باز** است و تحت **مجوز MIT** منتشر شده است.
