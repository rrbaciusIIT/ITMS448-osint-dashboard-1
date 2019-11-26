import React, { Component } from "react";
import ReactDOM from "react-dom";
import MaterialTable from "material-table";
import { forwardRef } from "react";

// import { Container } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

import { useStoreState, useStoreActions } from "easy-peasy";

// icons
import AddBox from "@material-ui/icons/AddBox";
import ArrowDownward from "@material-ui/icons/ArrowDownward";
import Check from "@material-ui/icons/Check";
import ChevronLeft from "@material-ui/icons/ChevronLeft";
import ChevronRight from "@material-ui/icons/ChevronRight";
import Clear from "@material-ui/icons/Clear";
import DeleteOutline from "@material-ui/icons/DeleteOutline";
import Edit from "@material-ui/icons/Edit";
import FilterList from "@material-ui/icons/FilterList";
import FirstPage from "@material-ui/icons/FirstPage";
import LastPage from "@material-ui/icons/LastPage";
import Remove from "@material-ui/icons/Remove";
import SaveAlt from "@material-ui/icons/SaveAlt";
import Search from "@material-ui/icons/Search";
import ViewColumn from "@material-ui/icons/ViewColumn";

import { tableHeaderNames } from "variables/general";

const tableIcons = {
  Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
  Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
  Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
  Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
  DetailPanel: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
  Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
  Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
  Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
  FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
  LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
  NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
  PreviousPage: forwardRef((props, ref) => <ChevronLeft {...props} ref={ref} />),
  ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
  Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
  SortArrow: forwardRef((props, ref) => <ArrowDownward {...props} ref={ref} />),
  ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
  ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />)
};

const styles = {
  detailPanel: {
    padding: "5px",
    maxWidth: "85vw"
  }
};

const MyMaterialTable = () => {
  const posts = useStoreState(state => state.posts);
  const useStyles = makeStyles(styles);
  const classes = useStyles();

  const { boards, data, headers, postAnaylzed, threads } = posts;
  headers.sort().reverse();

  const tableHeaders = headers.map(header => {
    let obj = {
      title: header,
      field: header
    };

    if (header === tableHeaderNames.Comment) {
      obj.hidden = true;
    }

    return obj;
  });

  return (
    <div style={{ maxWidth: "100%" }}>
      <MaterialTable
        title="Posts"
        icons={tableIcons}
        columns={tableHeaders}
        data={data}
        detailPanel={rowData => {
          return (
            <div className={classes.detailPanel}>
              <div>
                <strong>Comment:</strong>
                {rowData.full_comment}
              </div>
              <br />
              <div>
                <strong>Go to:</strong>
                <a href={rowData.post_url}> {rowData.post_url}</a>
              </div>
            </div>
          );
        }}
        options={{
          headerStyle: {
            minWidth: "max-content",
            borderBottom: "3px solid black",
            color: "#fb8c00"
          },
          rowStyle: {
            // backgroundColor: "#EEE",
            borderBottom: "1px solid black"
          },
          exportButton: true,
          grouping: true
        }}
      />
    </div>
  );
};

export default MyMaterialTable;
