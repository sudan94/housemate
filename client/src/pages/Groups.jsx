import React from "react";
import Layout from "../components/Layout";
import { Fab, Grid } from "@mui/material";
import GroupCard from "../components/GroupCard";
import AddGroupModal from "../components/AddGroupModal";
import { useGetGroups } from "../hooks/useGetGroups";

const Groups = () => {
  const {data, isLoading}  = useGetGroups();
  if(isLoading){
    return <div>Loading</div>
  }
  return (
    <Layout>
      <Grid container spacing={2}>
        {data.map((item) => (
          <Grid item xs={12} sm={6} md={4} key={item.id}>
            <GroupCard item={item} />
          </Grid>
        ))}

      </Grid>
      <AddGroupModal/>
    </Layout>
  );
};

export default Groups;
