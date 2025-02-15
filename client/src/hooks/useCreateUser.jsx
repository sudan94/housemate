import { useMutation } from "@tanstack/react-query";
import { API_ENDPOINTS } from "../utils/endpoints";
import request from "../utils/requests";

const createUser = async (input) => {
  const { data } = await request.post(API_ENDPOINTS.USER, {
    name: input.name,
    email: input.email,
    is_active: true,
  });
  return data;
};

export const useCreateUser = () => {
  return useMutation({
    mutationFn: createUser,
  });
};