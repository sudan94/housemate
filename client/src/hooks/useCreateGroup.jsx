import { useMutation } from "@tanstack/react-query";
import { API_ENDPOINTS } from "../utils/endpoints";
import request from "../utils/requests";



const createGroup = async (input) => {
  const { data } = await request.post(API_ENDPOINTS.GROUP_CREATE, {
    title: input.title,
    description: input.description,
  });
  return data;
};

export const useCreateGroup = () => {
  return useMutation({
    mutationFn: createGroup,
  });
};