import { API_ENDPOINTS } from "../utils/endpoints";
import { useQuery } from "@tanstack/react-query";
import request from "../utils/requests";

export const useGetGroupDetail = (id) => {
  return useQuery({
    queryKey: ["group_detail",id],
    queryFn: async () => {
      const { data } = await request.get(`${API_ENDPOINTS.GROUP_DETAIL}${id}`);
      return data;
    },
  });
};