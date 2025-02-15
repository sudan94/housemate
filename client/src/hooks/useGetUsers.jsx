import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetUsers = () => {
  return useQuery({
    queryKey: ["active_users"],
    retry: false,
    queryFn: async () => {
      const { data } = await request.get(API_ENDPOINTS.ACTIVE_USER);
      return data;
    },
  });
};