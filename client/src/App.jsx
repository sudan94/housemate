import "./App.css";
import Groups from "./pages/Groups";
import GroupDetail from "./pages/GroupDetail";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import ProtectedRoute from "./ProtectedRoutes";
import Auth from "./pages/Auth";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          {" "}
          <Route path="/group/:id" element={<ProtectedRoute><GroupDetail /></ProtectedRoute>}></Route>
          <Route path="/" element={<ProtectedRoute><Groups /></ProtectedRoute>}></Route>
          {/* <Route path="/logout" element={<Logout />}></Route> */}
          <Route path="/auth" element={<Auth />}></Route>

        </Routes>
      </BrowserRouter>
      {/* <Logout /> */}
    </>
  );
}

export default App;
