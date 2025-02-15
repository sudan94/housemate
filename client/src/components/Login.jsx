import { GoogleLogin, googleLogout, useGoogleLogin } from "@react-oauth/google";
import Cookies from 'js-cookie';
import React from "react";
import { useNavigate } from "react-router-dom";
import { useGetUsers } from "../hooks/useGetUsers";

const Login = () => {
  const navigate = useNavigate();

  const googleLogin = useGoogleLogin({
    onSuccess: (tokenResponse) => {
      console.log(tokenResponse);
      const authorizationCode = tokenResponse.access_token;
      fetch("http://127.0.0.1:8000/user/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code: authorizationCode }),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the response from your backend server
          // console.log("Login successful, backend response:", data);
          const token = data;
          Cookies.set('token', token, { expires: 7, secure: true });
          navigate("/")

        })
        .catch((error) => {
          // Handle errors in communicating with your backend server
          console.error("Error exchanging authorization code:", error);
        });

      // console.log("Google login successful", tokenResponse);
      // You can now use the tokenResponse to authenticate the user in your app
    },

    // flow: "auth-code", // Use 'auth-code' for the authorization code flow
  });

  const { data, isLoading } = useGetUsers();
  if(data){
    navigate("/")
  }



  return <button onClick={googleLogin}>Sign in with Google 🚀</button>;
};
export default Login;
