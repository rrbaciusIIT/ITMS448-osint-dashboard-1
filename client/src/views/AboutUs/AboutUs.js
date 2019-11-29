import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// @material-ui/icons
import Close from "@material-ui/icons/Close";
import Check from "@material-ui/icons/Check";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Danger from "components/Typography/Danger.js";
import Success from "components/Typography/Success.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import Divider from "@material-ui/core/Divider";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import { deepOrange, deepPurple } from "@material-ui/core/colors";
import { team } from "./AboutUsModel";

const useListStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper
  },
  inline: {
    display: "inline"
  },
  bigAvatar: {
    width: "70px",
    height: "70px",
    marginRight: "10px"
  },
  orange: {
    color: "#fff",
    backgroundColor: deepOrange[500]
  },
  purple: {
    color: "#fff",
    backgroundColor: deepPurple[500]
  }
}));

const styles = {
  cardCategoryWhite: {
    "&,& a,& a:hover,& a:focus": {
      color: "rgba(255,255,255,.62)",
      margin: "0",
      fontSize: "14px",
      marginTop: "0",
      marginBottom: "0"
    },
    "& a,& a:hover,& a:focus": {
      color: "#FFFFFF"
    }
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none",
    "& small": {
      color: "#777",
      fontSize: "65%",
      fontWeight: "400",
      lineHeight: "1"
    }
  },
  tableUpgradeWrapper: {
    display: "block",
    width: "100%",
    overflowX: "auto",
    WebkitOverflowScrolling: "touch",
    MsOverflowStyle: "-ms-autohiding-scrollbar"
  },
  table: {
    width: "100%",
    maxWidth: "100%",
    marginBottom: "1rem",
    backgroundColor: "transparent",
    borderCollapse: "collapse",
    display: "table",
    borderSpacing: "2px",
    borderColor: "grey",
    "& thdead tr th": {
      fontSize: "1.063rem",
      padding: "12px 8px",
      verticalAlign: "middle",
      fontWeight: "300",
      borderTopWidth: "0",
      borderBottom: "1px solid rgba(0, 0, 0, 0.06)",
      textAlign: "inherit"
    },
    "& tbody tr td": {
      padding: "12px 8px",
      verticalAlign: "middle",
      borderTop: "1px solid rgba(0, 0, 0, 0.06)"
    },
    "& td, & th": {
      display: "table-cell"
    }
  },
  center: {
    textAlign: "center"
  }
};

const useStyles = makeStyles(styles);

export default function UpgradeToPro() {
  const classes = useStyles();
  const listClasses = useListStyles();
  return (
    <GridContainer justify="center">
      <GridItem xs={12} sm={12} md={8}>
        <Card>
          <CardHeader color="info">
            <h4 className={classes.cardTitleWhite}>About the Team</h4>
            <p className={classes.cardCategoryWhite}>More information availbile on Github</p>
          </CardHeader>
          <CardBody>
            <List className={listClasses.root}>
              {team.map(member => (
                <>
                  <ListItem alignItems="flex-start">
                    <ListItemText
                      primary={member.name}
                      secondary={
                        <>
                          <p>
                            <strong>Role: </strong>
                            {member.role}
                          </p>
                          {member.github ? (
                            <p>
                              <strong>Github: </strong>
                              <a href={member.github}>{member.github}</a>
                            </p>
                          ) : (
                            ""
                          )}
                        </>
                      }
                    />
                  </ListItem>
                  <Divider variant="fullWidth" component="li" />
                </>
              ))}
              <GridItem justify="center">
                <Button
                  style={{ display: "list-item" }}
                  color="info"
                  variant="contained"
                  href="https://github.com/Team-Bowser-ITMS-448/ITMS448-osint-dashboard"
                >
                  Go to Git Repo
                </Button>
              </GridItem>
            </List>
          </CardBody>
        </Card>
      </GridItem>
    </GridContainer>
  );
}
