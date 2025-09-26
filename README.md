# my-better-t-app

This project was created with [Better-T-Stack](https://github.com/AmanVarshney01/create-better-t-stack), a modern TypeScript stack that combines Next.js, Next, TRPC, and more.

## Features

- **TypeScript** - For type safety and improved developer experience
- **Next.js** - Full-stack React framework
- **TailwindCSS** - Utility-first CSS for rapid UI development
- **shadcn/ui** - Reusable UI components
- **Next.js** - Full-stack React framework
- **tRPC** - End-to-end type-safe APIs
- **Bun** - Runtime environment
- **Prisma** - TypeScript-first ORM
- **SQLite/Turso** - Database engine
- **Authentication** - Better-Auth
- **Turborepo** - Optimized monorepo build system

## Getting Started

First, install the dependencies:

```bash
npm install
```
## Database Setup

This project uses SQLite with Prisma.

1. Start the local SQLite database:
```bash
cd apps/server && npm run db:local
```


2. Update your `.env` file in the `apps/server` directory with the appropriate connection details if needed.

3. Generate the Prisma client and push the schema:
```bash
npm run db:push
```


Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3001](http://localhost:3001) in your browser to see the web application.
The API is running at [http://localhost:3000](http://localhost:3000).







## Project Structure

```
my-better-t-app/
├── apps/
│   ├── web/         # Frontend application (Next.js)
│   └── server/      # Backend API (Next, TRPC)
```

## Available Scripts

- `npm run dev`: Start all applications in development mode
- `npm run build`: Build all applications
- `npm run dev:web`: Start only the web application
- `npm run dev:server`: Start only the server
- `npm run check-types`: Check TypeScript types across all apps
- `npm run db:push`: Push schema changes to database
- `npm run db:studio`: Open database studio UI
