import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetGroupsUsers = (id) => {
  return useQuery({
    queryKey: ["groups_users",id],
    queryFn: async () => {
      const { data } = await request.get(`${API_ENDPOINTS.GROUP_USERS}${id}`);
      return data;
    },
  });
};