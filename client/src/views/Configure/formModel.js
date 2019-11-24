import * as yup from "yup";

const initialValues = {
  company: "",
  username: "",
  email: "",
  firstName: "",
  lastName: "",
  city: "",
  country: "",
  postalCode: "",
  aboutMe: ""
};

const validationSchema = yup.object().shape({
  company: yup.string().max(50),
  username: yup
    .string()
    .max(50)
    .required(),
  email: yup
    .string()
    .max(255)
    .email()
    .required(),
  firstName: yup
    .string()
    .max(50)
    .required(),
  lastName: yup
    .string()
    .max(50)
    .required(),
  city: yup
    .string()
    .max(50)
    .required(),
  country: yup
    .string()
    .max(50)
    .required(),
  postalCode: yup
    .string()
    .max(7)
    .required(),
  aboutMe: yup
    .string()
    .max(255)
    .required()
});

const inputsModels = {
  general: [
    {
      id: "company-disabled",
      name: "company",
      label: "Company (disabled)",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 5 },
      formControlProps: {
        fullWidth: true
      },
      inputProps: {
        disabled: true
      }
    },
    {
      id: "username",
      name: "username",
      label: "Username",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 3 },
      formControlProps: {
        fullWidth: true
      }
    },
    {
      id: "email-address",
      name: "email",
      label: "Email address",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      }
    }
  ],
  personal: [
    {
      id: "first-name",
      name: "firstName",
      label: "First Name",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 6 },
      formControlProps: {
        fullWidth: true
      }
    },
    {
      id: "last-name",
      name: "lastName",
      label: "Last Name",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 6 },
      formControlProps: {
        fullWidth: true
      }
    }
  ],
  address: [
    {
      id: "city",
      name: "city",
      label: "City",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      }
    },
    {
      id: "country",
      name: "country",
      label: "Country",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      }
    },
    {
      id: "postal-code",
      name: "postalCode",
      label: "Postal Code",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      }
    }
  ],
  aboutMe: [
    {
      id: "about-me",
      name: "aboutMe",
      label: "About Me",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 12 },
      formControlProps: {
        fullWidth: true
      },
      inputProps: {
        multiline: true,
        rows: 5
      },
      isTextArea: true
    }
  ]
};

export { inputsModels, initialValues, validationSchema };
