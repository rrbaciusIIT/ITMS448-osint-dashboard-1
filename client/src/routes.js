/*!

=========================================================
* Material Dashboard React - v1.8.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import Person from "@material-ui/icons/Person";
import LibraryBooks from "@material-ui/icons/LibraryBooks";
import BubbleChart from "@material-ui/icons/BubbleChart";
import LocationOn from "@material-ui/icons/LocationOn";
import Notifications from "@material-ui/icons/Notifications";
import Unarchive from "@material-ui/icons/Unarchive";
import Language from "@material-ui/icons/Language";
import Build from "@material-ui/icons/Build";
import AccessibilityNew from "@material-ui/icons/AccessibilityNew";
// core components/views for Admin layout
import DashboardPage from "views/Dashboard/Dashboard.js";
import MockDashboardPage from "views/DashboardMock/Dashboard.js";
import DashboardRedditPage from "views/DashboardReddit/Dashboard.js";
import UserProfile from "views/UserProfile/UserProfile.js";
import Configure from "views/Configure/Configure.js";
import ConfigureReddit from "views/ConfigureReddit/ConfigureReddit.js";
import TableList from "views/TableList/TableList.js";
import Typography from "views/Typography/Typography.js";
import Icons from "views/Icons/Icons.js";
import Maps from "views/Maps/Maps.js";
import NotificationsPage from "views/Notifications/Notifications.js";
import UpgradeToPro from "views/UpgradeToPro/UpgradeToPro.js";
import AboutUs from "views/AboutUs/AboutUs.js";
// core components/views for RTL layout
import RTLPage from "views/RTLPage/RTLPage.js";

const dashboardRoutes = [
  {
    path: "/dashboard",
    name: "4Chan Dashboard",
    rtlName: "لوحة القيادة",
    icon: Dashboard,
    component: MockDashboardPage,
    layout: "/admin"
  },
  {
    path: "/configure",
    name: "Configure 4Chan",
    rtlName: "ملف تعريفي للمستخدم",
    icon: Build,
    component: Configure,
    layout: "/admin"
  },
  {
    path: "/configure-reddit",
    name: "(Beta) Configure Reddit",
    rtlName: "ملف تعريفي للمستخدم",
    icon: Build,
    component: ConfigureReddit,
    layout: "/admin"
  },
  {
    path: "/dashboard-reddit",
    name: "(Beta) Reddit Dashboard",
    rtlName: "ملف تعريفي للمستخدم",
    icon: Dashboard,
    component: DashboardRedditPage,
    layout: "/admin"
  },
  // {
  //   path: "/notifications",
  //   name: "Notifications",
  //   rtlName: "إخطارات",
  //   icon: Notifications,
  //   component: NotificationsPage,
  //   layout: "/admin"
  // },
  {
    path: "/about",
    name: "About Us",
    rtlName: "التطور للاحترافية",
    icon: AccessibilityNew,
    component: AboutUs,
    layout: "/admin"
  }
  // {
  //   path: "/upgrade-to-pro",
  //   name: "Upgrade To PRO",
  //   rtlName: "التطور للاحترافية",
  //   icon: Unarchive,
  //   component: UpgradeToPro,
  //   layout: "/admin"
  // }
];

export default dashboardRoutes;
