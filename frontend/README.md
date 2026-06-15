# Frontend (Vite + React 19)

Development:

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Run dev server:

```bash
npm run dev
```

Build:

```bash
npm run build
```

Environment:
- Copy `.env.example` to `.env` and set `VITE_API_URL` to your backend URL.

Running with Docker:

```bash
docker build -t book-frontend:latest .
docker run -p 3000:3000 book-frontend:latest
```

Integration with Django:
- Ensure your Django backend serves API at `VITE_API_URL`.
- For production you can build the frontend and serve `dist/` from Django static files or via a separate web server.
