import { useMutation } from "@tanstack/react-query";
import { API_ENDPOINTS } from "../utils/endpoints";
import request from "../utils/requests";



const createTaskGroup = async (input) => {
  const { data } = await request.post(API_ENDPOINTS.USER_TASK, {
    title: input.title,
    description : input.description,
    frequency : input.frequency,
    date : input.date,
    starting_user : input.starting_user,
    group_id : input.group_id,

  });
  return data;
};

export const useCreateGroupTask = () => {
  return useMutation({
    mutationFn: createTaskGroup,
  });
};