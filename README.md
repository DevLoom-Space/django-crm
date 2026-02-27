# DevLoom CRM (Django)

A clean, backend-focused Customer Relationship Management (CRM) system built with **Django**.  
Includes authentication, secured CRUD modules, analytics dashboard, and a Kanban-style pipeline board.

---

## ✨ Features

### ✅ Authentication & Security
- User signup, login, logout
- Redirects authenticated users away from `/login/` and `/signup/`
- `LoginRequiredMixin` protection on CRM pages
- Owner-based access control (prevents URL guessing)

### 🏢 CRM Modules
- Companies (CRUD)
- Contacts (CRUD)
- Deals (CRUD)
- Activities (CRUD)
- Notes (CRUD)

### 📊 Dashboard
- Company and contact counts
- Deal counts per user
- Deal stage stats (pipeline overview)
- Recent activities + notes

### 🧱 Pipeline Board (Kanban)
- Deals grouped by stage (Lead → Qualified → Proposal → Won/Lost)
- Drag & drop UI for moving cards (visual-only version)

### 🎨 UI
- Bootstrap 5 + Bootstrap Icons
- Consistent UI styling across forms and pages
- Responsive sidebar layout

---

## 🛠️ Tech Stack
- Python 3
- Django 6
- SQLite (development)
- Bootstrap 5

## Images

<img width="1919" height="961" alt="image" src="https://github.com/user-attachments/assets/074517bb-45c8-476f-96ed-15d17f88f648" />


<img width="1912" height="946" alt="image" src="https://github.com/user-attachments/assets/9de73199-1113-4fd8-a703-059579b70300" />


