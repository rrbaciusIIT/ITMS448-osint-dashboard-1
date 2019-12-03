import React from "react";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";
import Icon from "@material-ui/core/Icon";
import Typography from "@material-ui/core/Typography";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import MaterialTable from "components/MaterialTable/MaterialTable.js";
import Tasks from "components/Tasks/Tasks.js";
import CustomTabs from "components/CustomTabs/CustomTabs.js";
import Danger from "components/Typography/Danger.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import MyChart from "components/Chart/Chart.js";

import { useStoreState, useStoreActions } from "easy-peasy";

import { bugs, website, server } from "variables/general.js";

import { dailySalesChart, emailsSubscriptionChart, completedTasksChart } from "variables/charts.js";

import styles from "assets/jss/material-dashboard-react/views/dashboardStyle.js";

const materialTabelStyles = {
  detailPanel: {
    padding: "5px",
    maxWidth: "85vw"
  }
};
const useStyles = makeStyles(styles);
const useMaterialTableStyles = makeStyles(materialTabelStyles);

export default function Dashboard() {
  const classes = useStyles();
  const materialTableClasses = useMaterialTableStyles();

  const posts = useStoreState(state => state.reddit);

  return (
    <div>
      <GridContainer>
        {/* Quick Stats section */}
        <GridItem xs={12}>
          <Typography
            // className={classes.marginTopBot}
            component="p"
          >
            {" "}
            Quick Stats
          </Typography>
        </GridItem>
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="warning" stats icon>
              <CardIcon color="warning">
                <Icon>content_copy</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Number of Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.data.length ? (
                  <>
                    {posts.data.length} <small>posts</small>
                  </>
                ) : (
                  <div>- - -</div>
                )}
              </h3>
            </CardHeader>
            <CardFooter stats>
              {posts.postAnaylzed ? (
                <div className={classes.stats}>
                  <Update />
                  Just Updated
                </div>
              ) : (
                ""
              )}
            </CardFooter>
          </Card>
        </GridItem>

        <GridItem xs={12} sm={12} md={12}>
          <Card>
            <CardHeader color="warning">
              <h4 className={classes.cardTitleWhite}>Reddit Stats</h4>
              {/* <p className={classes.cardCategoryWhite}>New employees on 15th September, 2016</p> */}
            </CardHeader>
            <CardBody>
              <MaterialTable
                headers={posts.headers}
                data={posts.data}
                dataType={posts.dataType}
                hidden={["selftext", "title"]}
                detailPanel={rowData => {
                  return (
                    <div className={materialTableClasses.detailPanel}>
                      <div>
                        <strong>Title:</strong>
                        {rowData.title}
                        <br />
                        <strong>Comment:</strong>
                        {rowData.selftext}
                      </div>
                      <br />
                      <div>
                        <strong>Go to:</strong>
                        <a href={rowData.url}> {rowData.url}</a>
                      </div>
                    </div>
                  );
                }}
              ></MaterialTable>
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    </div>
  );
}
