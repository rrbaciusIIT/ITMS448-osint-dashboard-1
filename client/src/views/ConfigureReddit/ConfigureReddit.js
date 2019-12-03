import React, { useState } from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import TextField from "@material-ui/core/TextField";
import Checkbox from "@material-ui/core/Checkbox";
import Select from "@material-ui/core/Select";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Typography from "@material-ui/core/Typography";
import Fade from "@material-ui/core/Fade";

// formik
import { Formik, Form, useField, Field } from "formik";

// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardAvatar from "components/Card/CardAvatar.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Snackbar from "components/Notification/Notification.js";

// import avatar from "public/img/faces/bowser-img192.png";

import { inputsModels, initialValues, validationSchema } from "./formModel";
import useHttp from "hooks/useHttp.hook";
import inputStyles from "assets/jss/material-dashboard-react/components/customInputStyle.js";
import classNames from "classnames";
import { Paper, MenuItem } from "@material-ui/core";

import { useStoreActions } from "easy-peasy";
import { useHistory } from "react-router-dom";
import { conditionalExpression } from "@babel/types";

const styles = {
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  },
  customInput: {
    marginTop: "20px",
    marginBottom: "15px"
  },
  marginTopBot: {
    marginTop: "35px",
    marginBottom: "10px"
  }
};

const MyCustomInput = ({ label, name, type, inputProps, component, id, value, menuItems }) => {
  const useStyles = makeStyles(styles);
  const classes = useStyles();

  const [field, meta] = useField({ label, name, type });
  const errorText = meta.error && meta.touched ? meta.error : "";
  const error = !!errorText;

  const labelClasses = classNames({
    [" " + classes.labelRootError]: error,
    [" " + classes.labelRootSuccess]: !error
  });
  const underlineClasses = classNames({
    [classes.underlineError]: error,
    [classes.underlineSuccess]: !error,
    [classes.underline]: true
  });
  const marginTop = classNames({
    [classes.marginTop]: label === undefined
  });

  inputProps = {
    ...inputProps,
    className: classes.customInput
  };

  switch (component) {
    case "TextField":
      return (
        <Field
          {...field}
          {...inputProps}
          id={id}
          label={label}
          helperText={errorText}
          error={error}
          as={TextField}
        ></Field>
      );
    case "Checkbox":
      return (
        <FormControlLabel
          control={<Field name={name} value={value} as={Checkbox}></Field>}
          label={label}
        />
      );
    case "Select":
      return (
        <Field name={name} className={classes.marginTopBot} as={Select}>
          {menuItems.map(item => (
            <MenuItem value={item.value}>{item.text}</MenuItem>
          ))}
        </Field>
      );
  }
};

const useStyles = makeStyles(styles);

export default function UserProfile() {
  const history = useHistory();
  const classes = useStyles();
  const fetchData = useStoreActions(actions => actions.reddit.fetchData);

  const setNotification = useStoreActions(actions => actions.notifications.setNotification);
  const [mySubmitCount, setMySubmitCount] = useState(0);

  const getRequestString = ({
    host,
    port,
    actionString,
    boards,
    flaggers,
    startPage,
    stopPage
  }) => {
    let requestString = "";

    if (host) {
      requestString = requestString + host;
    }
    if (port) {
      requestString = requestString + `:${port}`;
    }
    if (actionString) {
      requestString = requestString + actionString;
    }
    if (boards) {
      requestString = requestString + `?boards=${boards.join(",")}`;
    }
    if (flaggers) {
      requestString = requestString + `&flaggers=${flaggers.join(",")}`;
    }
    if (startPage) {
      requestString = requestString + `&start_page=${startPage}`;
    }
    if (stopPage) {
      requestString = requestString + `&stop_page=${stopPage}`;
    }

    return requestString;
  };

  return (
    <>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={async (values, { setSubmitting }) => {
          setSubmitting(true);
          // make async call
          // console.log(values);
          try {
            await fetchData({
              url: getRequestString(values),
              method: "GET",
              responseType: values.actionString.includes("csv")
                ? "csv"
                : values.actionString.includes("json")
                ? "json"
                : "text"
            });
            await setNotification({
              type: "success",
              message: "Request completed successfully"
            });
            await setMySubmitCount(prevState => prevState++);
          } catch (error) {
            console.log(error, error.stack);
            setNotification({ type: "danger", message: "Error with request, please try again" });
            console.debug("Error posting try again");
          }

          setSubmitting(false);
        }}
      >
        {({ values, errors, isSubmitting, isValid, isValidating, submitCount, dirty }) => (
          // Formik auto pass in onSubmit handler | onSubmit={handleSubmit}
          <Form>
            <GridContainer>
              <GridItem xs={12} sm={12} md={12}>
                <Card>
                  <CardHeader color="primary">
                    <h4 className={classes.cardTitleWhite}>Configure Reddit Data Query</h4>
                    <p className={classes.cardCategoryWhite}>Adjust settings</p>
                  </CardHeader>
                  <CardBody>
                    {/* Host Section */}
                    <GridItem xs={12}>
                      <Typography className={classes.marginTopBot} component="p">
                        Host Configuration
                      </Typography>
                    </GridItem>

                    <GridContainer>
                      {inputsModels.hostSection.map(field => {
                        const { columnSpan, formControlProps, ...rest } = field;
                        return (
                          <GridItem {...columnSpan} key={field.name}>
                            <FormControl {...formControlProps}>
                              <MyCustomInput {...rest} />
                            </FormControl>
                          </GridItem>
                        );
                      })}
                    </GridContainer>

                    {/* Request String */}
                    <GridContainer>
                      <GridItem xs={12}>
                        <Paper
                          className={classes.marginTopBot}
                          style={{ padding: "10px", border: "1px dashed #9c27b0" }}
                        >
                          Request String: {getRequestString(values)}
                        </Paper>
                      </GridItem>
                    </GridContainer>
                  </CardBody>
                  {!isSubmitting && isValid && submitCount !== mySubmitCount ? (
                    <Fade in={isValid && submitCount !== mySubmitCount}>
                      <CardFooter style={{ justifyContent: "center" }}>
                        <Button
                          color="success"
                          type="button"
                          onClick={() => {
                            history.push("/admin/dashboard-reddit");
                            setMySubmitCount(prevState => prevState--);
                          }}
                        >
                          Go to dashboard
                        </Button>
                      </CardFooter>
                    </Fade>
                  ) : isSubmitting ? (
                    <CardFooter style={{ justifyContent: "center" }}>
                      <Button disabled>Processing...</Button>
                    </CardFooter>
                  ) : !isValid ? (
                    <Fade in={!isValid}>
                      <CardFooter style={{ justifyContent: "center" }}>
                        <Button color="danger" disabled>
                          Errors...
                        </Button>
                      </CardFooter>
                    </Fade>
                  ) : (
                    <CardFooter style={{ justifyContent: "center" }}>
                      <Button color="primary" type="submit">
                        Send Request
                      </Button>
                    </CardFooter>
                  )}
                </Card>
              </GridItem>
              {/* <GridItem xs={12} sm={12} md={4}>
                <Card profile>
                  <CardAvatar profile>
                    <a href="#bowser" onClick={e => e.preventDefault()}>
                      <img src={"/bowser-img192.png"} alt="Bowser" />
                    </a>
                  </CardAvatar>
                  <CardBody profile>
                    <h6 className={classes.cardCategory}>CEO / CO-FOUNDER</h6>
                    <h4 className={classes.cardTitle}>Alec Thompson</h4>
                    <p className={classes.description}>
                      Don{"'"}t be scared of the truth because we need to restart the human
                      foundation in truth And I love you like Kanye loves Kanye I love Rick Owens’
                      bed design but the back is...
                    </p>
                    <Button color="primary" round>
                      Follow
                    </Button>
                  </CardBody>
                </Card>
              </GridItem> */}
            </GridContainer>
            {/* <div>
              <pre>{JSON.stringify(values, null, 2)}</pre>
              <pre>{JSON.stringify(errors, null, 2)}</pre>
            </div> */}
          </Form>
        )}
      </Formik>
    </>
  );
}
