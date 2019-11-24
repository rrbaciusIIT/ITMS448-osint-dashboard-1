import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import TextField from "@material-ui/core/TextField";

// formik
import { Formik, Form, useField } from "formik";

// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardAvatar from "components/Card/CardAvatar.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";

import avatar from "assets/img/faces/marc.jpg";

import { inputsModels, initialValues, validationSchema } from "./formModel";
import useHttp from "hooks/useHttp.hook";
import inputStyles from "assets/jss/material-dashboard-react/components/customInputStyle.js";
import classNames from "classnames";

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
  }
};

const MyCustomInput = ({ label, name, type, inputProps, ...rest }) => {
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

  return (
    <TextField
      {...field}
      {...rest}
      {...inputProps}
      label={label}
      helperText={errorText}
      error={error}
    ></TextField>
  );
};

const useStyles = makeStyles(styles);

export default function UserProfile() {
  const classes = useStyles();
  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={(values, { setSubmitting }) => {
        setSubmitting(true);
        // make async call
        console.log(values);
        async function fetchData(url, options) {
          console.log({ url, ...options });

          try {
            // setIsLoading(true);

            const response = await fetch(url, { ...options });
            const data = await response.json();

            if (!response.ok) {
              throw new Error("Could not fetch person!");
            }

            // setFetchData(data);
            // setIsLoading(false);
          } catch (error) {
            console.log(error);
          }
        }

        fetchData("https://reqres.in/api/users/2", {
          method: "PUT",
          body: {
            name: "morpheus",
            job: "zion resident"
          }
        });
        // const [isLoading, fetchData] = useHttp();

        setSubmitting(false);
      }}
    >
      {({ values, errors, isSubmitting }) => (
        // Formik auto pass in onSubmit handler | onSubmit={handleSubmit}
        <Form>
          <GridContainer>
            <GridItem xs={12} sm={12} md={8}>
              <Card>
                <CardHeader color="primary">
                  <h4 className={classes.cardTitleWhite}>Edit Profile</h4>
                  <p className={classes.cardCategoryWhite}>Complete your profile</p>
                </CardHeader>
                <CardBody>
                  {/* General */}
                  <GridContainer>
                    {inputsModels.general.map(field => {
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

                  {/* Personal */}
                  <GridContainer>
                    {inputsModels.personal.map(field => {
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

                  {/* Address */}
                  <GridContainer>
                    {inputsModels.address.map(field => {
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

                  {/* About me */}
                  <GridContainer>
                    {inputsModels.aboutMe.map(field => {
                      const { columnSpan, isTextArea, formControlProps, ...rest } = field;
                      return isTextArea ? (
                        <GridItem {...columnSpan} key={field.name}>
                          <FormControl {...formControlProps}>
                            {/* <InputLabel style={{ color: "#AAAAAA" }}>
                              {field.id.toUpperCase().replace("-", " ")}
                            </InputLabel> */}
                            <MyCustomInput {...rest} />
                          </FormControl>
                        </GridItem>
                      ) : (
                        <GridItem {...columnSpan}>
                          <MyCustomInput {...rest} />
                        </GridItem>
                      );
                    })}
                  </GridContainer>
                </CardBody>
                <CardFooter>
                  <Button color="primary" type="submit">
                    Update Profile
                  </Button>
                </CardFooter>
              </Card>
            </GridItem>
            <GridItem xs={12} sm={12} md={4}>
              <Card profile>
                <CardAvatar profile>
                  <a href="#pablo" onClick={e => e.preventDefault()}>
                    <img src={avatar} alt="..." />
                  </a>
                </CardAvatar>
                <CardBody profile>
                  <h6 className={classes.cardCategory}>CEO / CO-FOUNDER</h6>
                  <h4 className={classes.cardTitle}>Alec Thompson</h4>
                  <p className={classes.description}>
                    Don{"'"}t be scared of the truth because we need to restart the human foundation
                    in truth And I love you like Kanye loves Kanye I love Rick Owens’ bed design but
                    the back is...
                  </p>
                  <Button color="primary" round>
                    Follow
                  </Button>
                </CardBody>
              </Card>
            </GridItem>
          </GridContainer>
          <div>
            <pre>{JSON.stringify(values, null, 2)}</pre>
            <pre>{JSON.stringify(errors, null, 2)}</pre>
          </div>
        </Form>
      )}
    </Formik>
  );
}
