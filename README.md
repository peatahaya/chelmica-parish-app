# Chełmica Parish CMS (Premium)

[PL] Nowoczesny, "decoupled" system CMS klasy Premium dla Parafii w Chełmicy Dużej.
[EN] Modern, decoupled Premium-class CMS for the Parish in Chełmica Duża.

---

## 🇵🇱 O projekcie (Polski)

Projekt stanowi dedykowane rozwiązanie typu single-tenant dla Parafii św. Jakuba Apostoła w Chełmicy Dużej. System został zaprojektowany w nowoczesnej architekturze **decoupled**, rozdzielającej logikę biznesową od warstwy prezentacji.

### Design & UI/UX
Głównym założeniem wizualnym jest **Luxury Dark Mode** – głęboka czerń, złote akcenty i wysoka czytelność, zapewniające poczucie powagi i nowoczesności. Interfejs jest zorientowany na wysokiej jakości UX, inspirowany dostarczonymi mockupami designu.

### Kluczowe Funkcjonalności
- **Intencje mszalne online**: Przeglądanie i rezerwacja wolnych terminów.
- **Ogłoszenia Parafialne**: Edytor Rich Text dla dynamicznych komunikatów.
- **Wirtualny Cmentarz**: Interaktywna mapa i wyszukiwarka miejsc pochówku.
- **Integracja Płatności**: Bezpieczne ofiary i opłaty za intencje (Stripe / Przelewy24).

---

## 🇬🇧 About the Project (English)

A dedicated single-tenant CMS solution for the St. James the Apostle Parish in Chełmica Duża. Built using a **decoupled** architecture to ensure scalability and high performance.

### Design & UI/UX
The project focuses on a **Luxury Dark Mode** aesthetic – featuring deep blacks, gold accents, and high readability to reflect both solemnity and modernity. The UI is UX-driven, inspired by professional visual design mockups.

### Key Features
- **Online Mass Intentions**: Browsing and booking available dates.
- **Parish Announcements**: Rich Text editor for dynamic communication.
- **Virtual Cemetery**: Interactive map and grave search engine.
- **Payment Integration**: Secure donations and intention fees (Stripe / Przelewy24).

---

## 🏗️ Struktura Projektu / Project Structure

- `backend/`: Django 5 API (Python 3.12+) + PostgreSQL.
- `frontend/`: Next.js 15 (React 19) + Tailwind CSS + Framer Motion.

---

## 🚀 Jak zacząć / Quick Start

### Backend
1. Wejdź do folderu backend: `cd backend`
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Skonfiguruj plik `.env` (na bazie przykładu).

### Frontend
1. Wejdź do folderu frontend: `cd frontend`
2. Zainstaluj paczki: `npm install` (po zainicjowaniu projektu Next.js).
