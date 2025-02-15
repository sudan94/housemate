import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetGroupsTask = (id) => {
  return useQuery({
    queryKey: ["group_task",id],
    queryFn: async () => {
      const { data } = await request.get(`${API_ENDPOINTS.GROUP_TASK}${id}`);
      return data;
    },
  });
};