# Housemate Client (React + Vite)

A frontend client for managing housemates' work schedules, built with React and Vite.

## Tech Stack
- **React** - Frontend library for UI development
- **Vite** - Fast build tool for React applications
- **React Router** - Navigation management
- **Axios** - HTTP client for API communication
- **Material UI** - Styling framework

## Installation

### Prerequisites
- Node.js 16+
- npm or yarn

### Clone the Repository
```sh
git clone https://github.com/yourusername/housemate-client-react.git
cd housemate-client-vite
```

### Install Dependencies
```sh
npm install  # or yarn install
```

### Environment Variables
Create a `.env` file in the root directory and configure the following variables:
```ini
VITE_API_BASE_URL=http://localhost:8000
```

### Start the Development Server
```sh
npm run dev  # or yarn dev
```

## Build for Production
```sh
npm run build  # or yarn build
```

## API Integration
Ensure the backend API (`housemate-fastapi-postgres`) is running before testing the frontend.

## License
This project is licensed under the MIT License.

