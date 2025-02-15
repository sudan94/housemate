import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Chip from '@mui/material/Chip';
import { useGetGroupsTask } from '../hooks/useGetGroupTask';

function createData(name, calories, fat, carbs) {
  return { name, calories, fat, carbs };
}

const rows = [
  createData('sudan', 159, 6.0, "Completed"),
  createData('shehab', 237, 9.0, "Pending"),
  createData('Eclair', 262, 16.0, "Due"),
  createData('Cupcake', 305, 3.7, 67),
  createData('Gingerbread', 356, 16.0, 49),
];

function renderSwitch(param, is_completed) {
  if (is_completed == true){
    return ['success', 'Completed']
  }
  let today = new Date();
  let due_date = new Date(param);
  if(today <= due_date){
    return ['warning','Due']
  }else {
    return ['error','Pending']
  }
}

export default function TaskTable({item}) {
  const {data, isLoading}  = useGetGroupsTask(item);
  if(isLoading){
    return <div>Loading</div>
  }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell align="right">Email</TableCell>
            <TableCell align="right">Due Date</TableCell>
            <TableCell align="right">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row) => (
            <TableRow
              key={row.email}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.email}
              </TableCell>
              <TableCell align="right">{row.title}</TableCell>
              <TableCell align="right">{row.due_date}</TableCell>

              <TableCell align="right"><Chip label={renderSwitch(row.due_date, row.is_completed)[1]} color={renderSwitch(row.due_date, row.is_completed)[0]} /></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
