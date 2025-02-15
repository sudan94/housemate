import { ReactNode } from "react";
import {Route, useNavigate} from 'react-router-dom';
import { useGetUsers } from "./hooks/useGetUsers";
import Cookies from 'js-cookie';

const ProtectedRoute = ({ children }) => {
  const navigate = useNavigate();
  const { data, isLoading } = useGetUsers();
  if (!data) {
    navigate("/auth");
    return <h1>Redirecting...</h1>;
  }
  Cookies.set('image', data.picture, { expires: 7, secure: true });
  Cookies.set('name', data.name, { expires: 7, secure: true });

  return <>{children}</>;
};

export default ProtectedRoute;