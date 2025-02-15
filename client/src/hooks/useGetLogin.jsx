import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetLogin = (token) => {
  return useQuery({
    queryKey: ["login",token],
    queryFn: async () => {
      const { data } = await request.get(`${API_ENDPOINTS.LOGIN}${token}`);
      return data;
    },
  });
};