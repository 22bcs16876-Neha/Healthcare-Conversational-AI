 # 🏥 Healthcare Conversational AI

This project is a voice-based Healthcare Claims Assistant developed during my internship as a **Conversational AI Engineer at EXL**.

The goal of this project was to build an intelligent healthcare assistant that can understand users through natural voice conversations and help them perform common healthcare-related tasks without waiting for a customer support representative.
 
Using conversational AI, the assistant can authenticate users, answer healthcare-related queries, retrieve claim information, search providers, and escalate calls to a human agent whenever required.

---

## ✨ What the Assistant Can Do

- Authenticate health-plan members securely
- Check claim status and claim history
- Submit, update, or cancel claims
- Verify member eligibility
- Retrieve benefits and policy information
- Search healthcare providers
- Check preauthorization status
- Transfer the conversation to a live representative when needed

---

## 🛠 Technologies Used

- Google Conversational Agents (ADK)
- Gemini Live
- FastAPI
- Python
- Firestore
- Docker
- OpenAPI
- REST APIs
- Cloud Run

---

## 📁 Repository Structure

```text
Healthcare-Conversational-AI
│
├── Healthcare_Claims_Voice_Agent    # Conversational AI agent
├── healthcare-backend               # FastAPI backend services
├── healthcare-ui                    # User interface
└── PROJECT_OVERVIEW.md              # Project documentation
```

---

## 🏗️ How It Works

The application follows a simple flow:

```
User
   │
   ▼
Voice Conversation (Gemini Live)
   │
   ▼
Healthcare Claims Voice Agent
   │
   ▼
FastAPI Backend
   │
   ▼
Healthcare APIs & Firestore
```

The conversational agent understands the user's request, verifies their identity whenever necessary, communicates with backend APIs, and responds with accurate information in a natural conversational manner.

---

## 🔒 Security

Since the project handles healthcare-related information, several security measures were considered:

- Consent is obtained before accessing sensitive information.
- Users are authenticated before personal details are shared.
- Sensitive actions require confirmation.
- Conversations are protected using guardrails.
- Requests can be transferred to a human representative whenever appropriate.

---

## 📌 What I Learned

Working on this project helped me gain practical experience with:

- Designing conversational AI workflows
- Prompt engineering
- Multi-agent orchestration
- FastAPI development
- API integration
- Google Conversational Agents
- Gemini Live
- Building secure and scalable AI applications 

---

## 👩‍💻 About the Project

This project was developed as part of my **Conversational AI Engineer Internship at EXL**. It demonstrates how conversational AI can simplify healthcare support by enabling users to access important healthcare services through natural voice interactions while maintaining security, reliability, and a smooth user experience.
