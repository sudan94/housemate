import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetToken = (code) => {
  return useQuery({
    queryKey: ["groups_users",code],
    queryFn: async () => {
      const { data } = await request.get(`${API_ENDPOINTS.TOKEN}${code}`);
      return data;
    },
  });
};