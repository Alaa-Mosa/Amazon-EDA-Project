# 🏛️ OpenGL (FreeGLUT) Setup Guide for Windows
### 👨‍💻 Developed & Documented by: Eng Amr Reda

هذا الدليل مخصص لمساعدتك في إعداد بيئة تطوير متكاملة للرسومات (Graphics Programming) باستخدام لغة **C++** ومكتبة **OpenGL** عبر **FreeGLUT** على نظام ويندوز، باستخدام **VS Code** و **MSYS2**.

---

## 🛠️ الخطوة 1: تحميل البرامج الأساسية (The Installation)

1. **Visual Studio Code (VS Code):**
   - قم بتحميله من الموقع الرسمي: [Download VS Code](https://code.visualstudio.com/download)
   - قم بتثبيته مع التأكد من اختيار "Add to PATH".

2. **MSYS2:**
   - هو مدير الحزم الذي سيوفر لنا المترجم (Compiler) والمكتبات.
   - قم بتحميله من: [Download MSYS2](https://www.msys2.org/)
   - ابدأ التثبيت، وبشكل افتراضي سيتم تثبيته في المسار `C:\msys64`.

---

## 🌍 الخطوة 2: إعداد متغيرات البيئة (Environment Variables)

يجب تعريف الويندوز على مكان وجود الأدوات البرمجية لكي تعمل الأوامر في أي مكان:

1. افتح قائمة ابدأ (Start) وابحث عن: **"Edit the system environment variables"**.
2. اضغط على الزر **Environment Variables** أسفل النافذة.
3. تحت قسم **System Variables**، اضغط على **New** وأضف:
   - **Variable Name:** `MSYS2`
   - **Variable Value:** `C:\msys64`
4. ابحث عن متغير اسمه **Path** في نفس القسم، واضغط عليه **Edit** ثم **New** وأضف هذا المسار:
   - `C:\msys64\mingw64\bin`
5. اضغط **OK** في كل النوافذ لحفظ التغييرات.



---

## ⌨️ الخطوة 3: تثبيت المكتبات عبر MSYS2 (Terminal Commands)

افتح تطبيق **MSYS2 MINGW64** من قائمة ابدأ (تأكد أنه MINGW64) وقم بنسخ ولصق الأوامر التالية بالترتيب:

```bash
# 1. تحديث قاعدة بيانات الحزم والنظام
pacman -Syu

# 2. تثبيت مترجم لغة C++ (GCC)
pacman -S mingw-w64-ucrt-x86_64-gcc

# 3. التأكد من نجاح تثبيت المترجم (سيظهر لك إصدار الـ GCC)
gcc --version

# 4. تثبيت مكتبة GLEW (OpenGL Extension Wrangler)
pacman -S mingw-w64-x86_64-glew

# 5. تثبيت مكتبة GLFW (Graphics Framework)
pacman -S mingw-w64-x86_64-glfw

# 6. تثبيت مكتبة FreeGLUT (The Utility Toolkit)
pacman -S mingw-w64-x86_64-freeglut

# 7. تثبيت حزمة أدوات التطوير الكاملة (لضمان وجود كل الـ Headers)
pacman -S mingw-w64-x86_64-toolchain

---

## 🔧 الخطوة 4: تهيئة VS Code (Extensions & Paths)

بعد تثبيت المكتبات، نحتاج لضبط المحرر ليتعرف على المسارات الجديدة:

1. **إضافات VS Code:**
   قم بفتح VS Code وتثبيت الإضافات التالية من قسم (Extensions):
   - **C/C++**: من شركة Microsoft (أساسية لعمل الـ IntelliSense والـ Debugging).
   - **Code Runner**: لتشغيل الكود بضغطة زر واحدة.

2. **ضبط Include Path:**
   - اذهب إلى **Settings** (عن طريق الاختصار `Ctrl + ,`).
   - ابحث في شريط البحث عن `includepath`.
   - تحت قسم **C_Cpp > Default: Include Path**، اضغط على **Add Item**.
   - أضف المسار التالي:
     `${env:MSYS2}/mingw64/include/`
   - هذا يضمن اختفاء الخطوط الحمراء تحت `#include <GL/glut.h>`.