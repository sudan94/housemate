import { useMutation } from "@tanstack/react-query";
import { API_ENDPOINTS } from "../utils/endpoints";
import request from "../utils/requests";



const createUserGroup = async (input) => {
  const { data } = await request.post(API_ENDPOINTS.USER_GROUP, {
    group_id: input.group_id,
    email : input.email,

  });
  return data;
};

export const useCreateUserGroup = () => {
  return useMutation({
    mutationFn: createUserGroup,
  });
};