# MeetMeet

MeetMeet is a community-centric event management platform designed to bridge the gap between local organizers and attendees. Built with a focus on ease of use and mobile-first design, MeetMeet allows users to discover upcoming events, manage their own gatherings, and interact with their community through a streamlined, secure interface.

As an active member of several local communities, I saw firsthand how time-consuming and fragmented organizing local events can be. MeetMeet was created to simplify that process — helping organizers create, manage and promote events more easily, and making it simpler for attendees to discover, RSVP and participate.

[View the Live Project on Render](https://meetmeet.onrender.com/)


## Responsive Design

The application is fully responsive, ensuring a consistent user experience across desktop, tablet, and mobile devices.

![MeetMeet Responsive Mockup](documentation/images/mock.webp)


## Agile Methodology

### Summary of Methodology

This project was developed using Agile principles, specifically utilizing the Kanban method to manage tasks and workflow. The development process focused on iterative delivery, ensuring that the Minimum Viable Product (MVP) was established first before moving on to advanced features. This approach allowed for continuous integration and rapid adaptation to technical challenges.

[Link to GitHub Project Board](https://github.com/users/sasha-fedorov/projects/4)

![Project Board](documentation/images/project_board.png)

### Specifics of Methodology

The work was organized using a hierarchical structure to maintain scope and clarity:

- **Themes:** The project was divided into high-level categories (User Identity, Content Lifecycle, Community Engagement, Discovery).
- **Epics:** These themes were broken down into Epics, such as "Organizer Control Center" and "Secure Authentication," which represented significant blocks of functionality.
- **User Stories:** Each feature implementation began as a User Story (e.g., "As a user, I want to join an event...").
  - **Acceptance Criteria:** Every User Story included specific criteria that defined the "Definition of Done," ensuring functional requirements were met before the task was closed.
  - **MoSCoW Prioritization:** Tasks were prioritized into "Must Have" (MVP) and "Won't Have" (Future Features) to strictly adhere to the project deadline.


## UX Planning

### Planning Description

The design process began with a "Content-First" approach, identifying the necessary data (Titles, Dates, Status) before determining the layout. The goal was to reduce cognitive load by presenting the most critical information—such as event status and "Call to Action" buttons—in prominent positions.

### Wireframes

Wireframes were created using Figma to visualize the layout for mobile and desktop views prior to writing code.

<details>
  <summary><b>Click to expand wireframes</b></summary>
  <table>
    <tr>
      <th>Desktop</th>
      <th>Tablet</th>
      <th>Mobile</th>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Meetup list (Home page)</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/meetup_list_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/meetup_list_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/meetup_list_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Meetup Form</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/meetup_form_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/meetup_form_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/meetup_form_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Meetup Details</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/meetup_detail_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/meetup_detail_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/meetup_detail_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Meetup management</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/meetup_manage_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/meetup_manage_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/meetup_manage_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Registration</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/account_register_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/account_register_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/account_register_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Login</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/account_login_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/account_login_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/account_login_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Logout</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/account_logout_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/account_logout_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/account_logout_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>About</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/about_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/about_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/about_mobile.png" /></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>Error code pages</b></td>
    </tr>
    <tr>
      <td width="58%"><img src="documentation/images/wireframes/error_desktop.png" /></td>
      <td width="25%" ><img src="documentation/images/wireframes/error_tablet.png" /></td>
      <td width="17%" ><img src="documentation/images/wireframes/error_mobile.png" /></td>
    </tr>
  </table>
</details>

### Design System

#### Color Palette

The palette uses a high-contrast primary pink for actions, with distinct status colors (Green/Success, Red/Danger, Yellow/Warning) to provide immediate feedback.

![Color Palette](documentation/images/color_palette.png)

#### Typography

- **Primary Font:** [DM Sans](https://fonts.google.com/specimen/DM+Sans)
- **Weights:**
  - **400 (Regular):** Used for body text and descriptions for readability.
  - **800 (ExtraBold):** Used for the Navbar Brand and major headings to establish hierarchy.

![Color Palette](documentation/images/typography.png)


## Features Implemented and Futures

### Existing Features

- **User Authentication:** Secure registration and login functionality handled via `django-allauth`.
  <details>
    <summary>Click to preview</summary>

    | ![Login](documentation/images/features/login.png) | ![Logout](documentation/images/features/logout.png) |
    | - | - |

    </details>
---

- **Event Management (CRUD):** Users can Create, Read, Update, and Delete their own meetups.
  <details>
  <summary>Click to preview</summary>

  | ![Create Meetup](documentation/images/features/meetup_create.png) | ![Update Delete Meetup](documentation/images/features/meetup_update_delete.png) |
  | - | - |

  </details>
---

- **Smart Permissions:** Only the organizer of an event can edit or delete it.
  <details>
  <summary>Click to preview</summary>

  | ![Update Delete Meetup](documentation/images/features/meetup_update_delete.png) | ![Meetup Update Restricted](documentation/images/features/meetup_update_restrict.png) |
  | - | - |

  </details>
---

- **Dynamic Participation:**
  - **Open Events:** Users can join instantly.
  - **Restricted Events:** Users must request approval; the status defaults to "Pending".
  <details>
  <summary>Click to preview</summary>

  | ![Join Meetup](documentation/images/features/meetup_join.png) | ![Request to Join Meetup](documentation/images/features/meetup_request_join.png) |
  | - | - |

  </details>
---

- **Organizer Dashboard:** A dedicated section on the event page for organizers to Approve, Reject, or Remove participants.

  <details>
  <summary>Click to preview</summary>

  ![Meetup Management Dashboard](documentation/images/features/meetup_approve.png)

  </details>
---

- **Prioritized Feed:** The homepage automatically sorts events created by the logged-in user to the top of the list.

  <details>
  <summary>Click to preview</summary>

  ![Meetups Sorting](documentation/images/features/meetup_sort.png)

  </details>
---

- **Defensive Design:** Backend validation prevents users from scheduling events in the past or joining events that have already finished.

  <details>
  <summary>Click to preview</summary>

  ![Meetup Validation Error](documentation/images/features/meetup_validation_error.png)

  </details>
---

- **Participant Limits:** Automatically closing an event when `max_participants` is reached.

  <details>
  <summary>Click to preview</summary>

  ![meetup Full](documentation/images/features/meetup_full.png)

  </details>
---

### Future Features (Roadmap)

- **User Profile:** Ability to upload a profile image and set a display name.
- **Notifications:** Email alerts for organizers when a new join request is received.
- **Advanced Security:** Password reset via email and email address confirmation.
- **Search & Filter:** Filtering events by date range or location.


## Data Model and Schema

### Data Model Strategy

The project utilized a "Model-First" approach. The relational database structure was defined in Python classes (`models.py`) before any views or templates were created. This ensured that data integrity rules (such as unique constraints between Users and Meetups) were enforced at the database level.

### Django Migrations

Django's migration system was utilized to propagate changes from the Python models to the PostgreSQL database schema. This allowed for version-controlled database evolution throughout the development lifecycle.

### Database Schema

ERDs provide a visual blueprint of your database structure throughout the entire development lifecycle.

![Database Diagram](documentation/images/schema_diagram.png)

**Key Logic:** A User owns the meetups they create and manages the participation requests for them, while participating in others' meetups through the participation table.


## Validation and Testing

For detailed information about testing, bugfixing, validation, please refer to **[TESTING.md](TESTING.md)**.


## Libraries, Languages, and Tools

### Languages & Frameworks

- **Python:** Selected for its readability and robust ecosystem.
- **Django:** Chosen for its "batteries-included" approach, providing built-in authentication, ORM, and security against common attacks (CSRF, SQL Injection).
- **HTML5 / CSS3:** Used for semantic markup and styling.

### Libraries & Utilities

- **PostgreSQL:** Chosen as the production database for its reliability and relational integrity compared to SQLite.
- **Gunicorn:** A production-grade WSGI HTTP Server for UNIX, used to serve the Django application on Render.
- **WhiteNoise:** Used to serve static files efficiently directly from the Django application in production.
- **Dotenv:** Used to manage environment variables (secrets) securely during local development.
- **Django-Bootstrap5:** Used for rapid, responsive UI development, forms and notifications.

### Tools & Programs

- **[VS Code](https://code.visualstudio.com/)** – Main code editor for development.
- **[Google Chrome](https://www.google.com/chrome/)** – Browser for testing and verifying web functionality.
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools)** – Used for debugging and checking responsiveness.
- **[flake8 VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)** – Enforced PEP8 compliance.
- **[Figma](https://www.figma.com/)** – used to create site favicon, wireframes and documentation images
- **[Fork](https://fork.dev/)** – Git client for version control.

### Services

- **[Render](https://render.com/)** – Cloud platform for deployment and database hosting.
- **[GitHub](https://github.com/)** – Code repository and project board hosting.
- **[ChatGPT](https://chat.openai.com/)** – Used as a search tool and syntax reference.
- **[Gemini](https://gemini.google.com/)** – Used for documentation structure, logic troubleshooting, and content generation.
- **[Coolors](https://coolors.co/)** – Color palette generation.
- **[dbdiagram.io](https://dbdiagram.io/)** – Database schema visualization.


## Deployment & Local Development

### Deployment (Render)

This project is deployed on Render (https://render.com). A Render account is required — accounts can be created for free and provide a straightforward path to deploy the app and provision a managed PostgreSQL database.

Follow these step-by-step instructions to deploy the project to Render:

1. Create a Render account
  - Visit https://render.com and sign up (free plans available). Verify your email.

2. Prepare your GitHub repository
  - Push your project to a GitHub repository (public or private). Ensure the repository contains the `requirements.txt` and `build.sh` files.

3. Create a managed PostgreSQL instance on Render
  - In the Render dashboard choose **New → PostgreSQL**.
  - Select a plan (free trial or paid plan as needed) and create the database.
  - After creation, copy the provided database URL — you will use it as `DATABASE_URL`.

4. Create a new Web Service on Render
  - In the Render dashboard choose **New → Web Service**.
  - Connect your GitHub repository and select the branch to deploy (e.g., `main`).
  - For the **Environment**, choose `Python` and set the **Build Command** and **Start Command** if needed (the project includes `build.sh` to automate build tasks).

5. Set environment variables in the Render service settings
  - Add these environment variables in the Render Web Service settings:
    - `DATABASE_URL`: connection string from the PostgreSQL service.
    - `SECRET_KEY`: a securely generated Django secret key.
    - `PYTHON_VERSION`: `3.14.0` (or the desired supported version).
    - `WEB_CONCURRENCY`: `4` (optional; tune for your instance size).

6. Add the build script and static file collection
  - Ensure `build.sh` exists at the repository root and is executable. Typical responsibilities:
    - Install dependencies (`pip install -r requirements.txt`).
    - Run migrations (`python manage.py migrate`).
    - Collect static files (`python manage.py collectstatic --noinput`).
  - Example `build.sh` usage is already included in this repo.

7. Deploy and verify
  - Trigger a manual deploy from the Render dashboard or push a new commit to the branch.
  - Monitor the build logs for errors and confirm the service becomes healthy.
  - Visit the assigned Render URL to verify the site.

8. Post-deploy checks
  - Confirm environment variables are applied and migrations ran successfully.
  - Check static assets, login/registration, and a sample meetup creation flow.

Notes:
- Render provides free-tier accounts for small projects and evaluation — upgrade if you need more resources or production SLA.
- Keep secrets secure; do not commit `SECRET_KEY` or production credentials to the repository.

### Local Development

To run this project locally, follow these steps:

1.  **Cloning:**
    - Navigate to the location where you want to create the project directory.
      - Example: `cd Documents/GitHub_Projects`
    - Type the following command and press **Enter**:

    ```bash
    git clone https://github.com/sasha-fedorov/meetmeet.git
    ```

2.  **Environment Setup:**
    - Ensure Python 3.14 is installed.
    - Create a virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use: venv\Scripts\activate
      ```
    - Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```
3.  **Configuration:**
    - Create a `.env` file in the root directory.
    - Add your `SECRET_KEY` and `DATABASE_URL` (or use local SQLite).
4.  **Database:**
    - Run migrations:
      ```bash
      python manage.py migrate
      ```
    - Create a superuser:
      ```bash
      python manage.py createsuperuser
      ```
5.  **Running:**
    - Start the server:
      ```bash
      python manage.py runserver
      ```

### Forking

To fork the **MeetMeet** repository to your own GitHub account:

1. Log in (or sign up) to GitHub.
2. Go to the repository: **[sasha-fedorov/meetmeet](https://github.com/sasha-fedorov/meetmeet)**.
3. Click the **Fork** button in the top right corner to create a copy under your own account.

### Seeding

To populate realistic test data (useful locally or after a free Render database reset), a helper script is included.

- **File:** `seed_test_data.py`
- **Purpose:** Creates test users and a collection of realistic meetups for manual testing and development.
- **How to run:**

```bash
# From the project root run the Django shell and execute the script:
python manage.py shell
exec(open('seed_test_data.py', encoding='utf-8').read())
```

- **Notes:**
  - The script is safe for development and deletes previously created `testuser_` users before creating new ones.
  - This makes re-populating a Render free-tier PostgreSQL instance straightforward after automatic resets.
  - Adjust `APP_NAME` or event pools in the script if you customize the app structure.


## Credits

### Media

- **Meetups List Background Image:** [Freepik - Happy friends home party](https://www.freepik.com/free-vector/happy-friends-home-party-isolated-flat-vector-illustration-cartoon-group-students-dancing-talking-having-fun-together-apartment_10172831.htm)

### Code & Reference

- **Python Gitignore:** [GitHub Python .gitignore template](https://github.com/github/gitignore/blob/main/Python.gitignore)
- **Django Documentation:** Referenced for Class-Based Views and Authentication patterns.
