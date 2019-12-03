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

import { tableHeaderNames } from "variables/general.js";

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

  const posts = useStoreState(state => state.posts);

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
                {posts.postAnaylzed ? (
                  <>
                    {posts.postAnaylzed} <small>posts</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="success" stats icon>
              <CardIcon color="success">
                <Icon>call_split</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Threads Anaylzed</p>
              <h3 className={classes.cardTitle}>
                {posts.threads.count ? (
                  <>
                    {posts.threads.count} <small>threads</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="info" stats icon>
              <CardIcon color="info">
                <Icon>developer_board</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Boards scorched</p>
              <h3 className={classes.cardTitle}>
                {posts.boards.count ? (
                  <>
                    {posts.boards.count} <small>boards</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="success" stats icon>
              <CardIcon color="success">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Post that passed Triggers</p>
              <h3 className={classes.cardTitle}>
                {posts.noContentFlagCount ? (
                  <>
                    {posts.noContentFlagCount} <small>posts</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Terroism Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.terroismFlagCount ? (
                  <>
                    {posts.terroismFlagCount} <small>flagged</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>NSA PRISM Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.nsaPrismFlagCount ? (
                  <>
                    {posts.nsaPrismFlagCount} <small>flagged</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>NSA ECHELON Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.nsaEchelonFlagCount ? (
                  <>
                    {posts.nsaEchelonFlagCount} <small>flagged</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Hate Speech Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.hateSpeechFlagCount ? (
                  <>
                    {posts.hateSpeechFlagCount} <small>flagged</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Conspiracy Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.conspiracyFlagCount ? (
                  <>
                    {posts.conspiracyFlagCount} <small>flagged</small>
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
        <GridItem xs={12} sm={6} md={3}>
          <Card>
            <CardHeader color="danger" stats icon>
              <CardIcon color="danger">
                <Icon>info_outline</Icon>
              </CardIcon>
              <p className={classes.cardCategory}>Racism Flagged Posts</p>
              <h3 className={classes.cardTitle}>
                {posts.racismFlagCount ? (
                  <>
                    {posts.racismFlagCount} <small>flagged</small>
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
      </GridContainer>

      {/* Charts section */}
      <GridContainer>
        <GridItem xs={12}>
          <Typography className={classes.marginTopBot} component="p">
            {" "}
            Charts
          </Typography>
        </GridItem>
        <GridItem xs={12} sm={12} md={6}>
          <Card chart>
            <CardHeader>
              <MyChart
                type="Pie"
                labels={[
                  `Terroism(${posts.terroismFlagCount})`,
                  `NSA PRISM(${posts.nsaPrismFlagCount})`,
                  `NSA ECHELON(${posts.nsaEchelonFlagCount})`,
                  `Hate Speech(${posts.hateSpeechFlagCount})`,
                  `Conspiracy(${posts.conspiracyFlagCount})`,
                  `Racism(${posts.racismFlagCount})`,
                  `Passed(${posts.noContentFlagCount})`
                ]}
                series={[
                  posts.terroismFlagCount,
                  posts.nsaPrismFlagCount,
                  posts.nsaEchelonFlagCount,
                  posts.hateSpeechFlagCount,
                  posts.conspiracyFlagCount,
                  posts.racismFlagCount,
                  posts.noContentFlagCount
                ]}
              ></MyChart>
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Pie Chart</h4>
              <p className={classes.cardCategory}>Data from 4chan</p>
            </CardBody>
            <CardFooter chart>
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
        <GridItem xs={12} sm={12} md={6}>
          <Card chart>
            <CardHeader>
              <MyChart
                type="Column"
                labels={[
                  `Terroism(${posts.terroismFlagCount})`,
                  `NSA PRISM(${posts.nsaPrismFlagCount})`,
                  `NSA ECHELON(${posts.nsaEchelonFlagCount})`,
                  `Hate Speech(${posts.hateSpeechFlagCount})`,
                  `Conspiracy(${posts.conspiracyFlagCount})`,
                  `Racism(${posts.racismFlagCount})`,
                  `Passed(${posts.noContentFlagCount})`
                ]}
                series={[
                  posts.terroismFlagCount,
                  posts.nsaPrismFlagCount,
                  posts.nsaEchelonFlagCount,
                  posts.hateSpeechFlagCount,
                  posts.conspiracyFlagCount,
                  posts.racismFlagCount,
                  posts.noContentFlagCount
                ]}
              ></MyChart>
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Column Chart</h4>
              <p className={classes.cardCategory}>Data from 4chan</p>
            </CardBody>
            <CardFooter chart>
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
      </GridContainer>

      {/* Table Section */}
      <GridContainer>
        <GridItem xs={12}>
          <Typography className={classes.marginTopBot} component="p">
            {" "}
            Data Table
          </Typography>
        </GridItem>
        <GridItem xs={12} sm={12} md={12}>
          <Card>
            <CardHeader color="warning">
              <h4 className={classes.cardTitleWhite}>Posts Stats</h4>
              {/* <p className={classes.cardCategoryWhite}>New employees on 15th September, 2016</p> */}
            </CardHeader>
            <CardBody>
              <MaterialTable
                headers={posts.headers}
                data={posts.data}
                dataType={posts.dataType}
                hidden={[tableHeaderNames.Comment]}
                detailPanel={rowData => {
                  return (
                    <div className={materialTableClasses.detailPanel}>
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
              ></MaterialTable>
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    </div>
  );
}
