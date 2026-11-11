
# Software Development Life Cycle (SDLC)

## 1. What is SDLC?

SDLC stands for **Software Development Life Cycle**.

It is a systematic, step-by-step process used to develop software applications, from planning and requirement collection to development, testing, deployment and maintenance.

### Example

Imagine developing an online shopping application.

The application needs:
- User registration and login
- Product search
- Shopping cart
- Online payment
- Order tracking

SDLC provides a structured process to develop this application.

---

## 2. Phases of SDLC

There are seven commonly described phases:

1. Planning
2. Requirement Analysis
3. System Design
4. Development (Coding)
5. Testing
6. Deployment
7. Maintenance

### SDLC Flow

```text
       Planning
          |
          v
  Requirement Analysis
          |
          v
     System Design
          |
          v
     Development
          |
          v
       Testing
          |
          v
      Deployment
          |
          v
      Maintenance
```

---

## 3. Phase 1 – Planning

Planning is the first phase of SDLC.

In this phase, the project team decides what software to develop and how to develop it.

### Main activities

- Identify the project goal.
- Understand the problem.
- Estimate project cost.
- Estimate development time.
- Identify required resources.
- Identify possible risks.
- Decide project scope.

### Example

For an online shopping application:

- Project goal: Build an online shopping platform.
- Budget: Estimate development and hosting costs.
- Time: Plan the development schedule.
- Resources: Developers, designers and testers.

### Output

A project plan containing the goals, scope, timeline, resources and estimated cost.

---

## 4. Phase 2 – Requirement Analysis

In this phase, developers collect and analyse the requirements of the software.

Requirements describe what users expect from the application.

### Main activities

- Communicate with customers.
- Collect user requirements.
- Identify functional requirements.
- Identify non-functional requirements.
- Analyse technical feasibility.
- Document requirements.

### Functional Requirements

Functional requirements describe what the system should do.

Examples:

- User registration.
- User login.
- Product search.
- Add products to cart.
- Make payments.
- Track orders.

### Non-Functional Requirements

Non-functional requirements describe how well the system should work.

Examples:

- Performance.
- Security.
- Reliability.
- Scalability.
- Availability.
- Usability.

### Output

SRS – Software Requirements Specification.

SRS is a document containing the software requirements.

---

## 5. Phase 3 – System Design

In this phase, developers convert the collected requirements into a technical design.

It explains how the software will be built.

### Main activities

- Design system architecture.
- Design database structure.
- Design user interfaces.
- Define APIs.
- Select technologies.
- Plan system components.
- Define security design.

### Example

For an online shopping application:

**Frontend:**
- React.js

**Backend:**
- Python FastAPI

**Database:**
- PostgreSQL

**Architecture:**
- Frontend communicates with backend APIs.
- Backend processes requests.
- PostgreSQL stores application data.

### Database Design Example

Users table:

| user_id | name | email |
|---|---|---|
| 1 | Rahul | rahul@gmail.com |
| 2 | Priya | priya@gmail.com |

Products table:

| product_id | product_name | price |
|---|---|---|
| 101 | Laptop | 50000 |
| 102 | Mouse | 500 |

### Output

- System architecture.
- Database design.
- API design.
- UI design.
- Technical design documents.

---

## 6. Phase 4 – Development (Coding)

In this phase, developers write the actual source code based on the design.

### Main activities

- Write program code.
- Develop frontend.
- Develop backend.
- Create database tables.
- Implement APIs.
- Integrate application components.
- Follow coding standards.

### Example

Developers create:

- Login API.
- Registration API.
- Product API.
- Cart API.
- Payment integration.

### Python FastAPI Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Online Shopping Application"}
```

### Output

Working software modules and source code.

---

## 7. Phase 5 – Testing

Testing is performed to identify errors and verify that the software works according to the requirements.

A software error is commonly called a bug.

### Main activities

- Find bugs.
- Verify application functionality.
- Check security.
- Check performance.
- Test application components.
- Verify requirements.

### Types of Testing

#### 1. Unit Testing

Tests individual functions or components.

Example: Test a function that calculates the total price.

#### 2. Integration Testing

Tests whether different modules work correctly together.

Example: Check whether the cart module communicates correctly with the payment module.

#### 3. System Testing

Tests the complete application.

Example: Test the entire shopping application.

#### 4. Acceptance Testing

Checks whether the software satisfies customer or user requirements.

Example: Customer verifies that the shopping application works as expected.

### Other Important Testing Types

- Functional Testing: Checks application functionality.
- Performance Testing: Checks speed and responsiveness.
- Security Testing: Checks security vulnerabilities.
- Regression Testing: Checks whether new changes have broken existing features.

### Output

Test reports, identified bugs and verified software.

---

## 8. Phase 6 – Deployment

Deployment is the process of releasing software into a production environment so that users can access it.

### Main activities

- Prepare production environment.
- Configure servers.
- Deploy application code.
- Configure database.
- Set environment variables.
- Verify the deployed application.
- Monitor the initial release.

### Example

Deploy an online shopping application using:

- Backend: Cloud server.
- Frontend: Vercel.
- Database: PostgreSQL.

After deployment, users can access the application.

### Output

Software available to users in the production environment.

---

## 9. Phase 7 – Maintenance

Maintenance happens after the software is released.

The development team continues to monitor, improve and support the application.

### Main activities

- Fix bugs.
- Improve performance.
- Update security.
- Add new features.
- Update dependencies.
- Improve user experience.
- Monitor application health.

### Example

After releasing the shopping application:

- Fix payment failures.
- Improve product search.
- Add new payment methods.
- Improve application speed.

### Types of Maintenance

1. Corrective Maintenance – Fixing identified bugs.
2. Adaptive Maintenance – Updating software to work with changed environments.
3. Perfective Maintenance – Improving performance and adding features.
4. Preventive Maintenance – Making changes to reduce future problems.

### Output

Updated, improved and supported software.

---

## 10. Advantages of SDLC

1. Provides a structured development process.
2. Helps manage project time and cost.
3. Improves software quality.
4. Helps identify problems early.
5. Improves communication between team members.
6. Makes project progress easier to track.
7. Supports software maintenance.

---

## 11. Disadvantages of SDLC

1. Some SDLC approaches require significant documentation.
2. Changes in requirements can affect the development plan.
3. Following a rigid process can take additional time.
4. Poor requirement collection can cause project problems.
5. Testing and documentation may increase project cost.

---

## 12. Important SDLC Interview Questions

### Q1. What is SDLC?

SDLC stands for Software Development Life Cycle. It is a systematic process used to plan, design, develop, test, deploy and maintain software.

### Q2. What are the phases of SDLC?

The seven commonly described phases are:

1. Planning
2. Requirement Analysis
3. System Design
4. Development
5. Testing
6. Deployment
7. Maintenance

### Q3. What is SRS?

SRS stands for Software Requirements Specification. It is a document that describes the functional and non-functional requirements of software.

### Q4. What is the difference between functional and non-functional requirements?

Functional requirements describe what a system should do.

Non-functional requirements describe how well the system should perform.

### Q5. What happens during the design phase?

The system architecture, database, APIs, user interface and technical structure are planned.

### Q6. What happens during the development phase?

Developers write source code and implement the software features.

### Q7. What is software testing?

Software testing is the process of checking software to identify bugs and verify that it meets its requirements.

### Q8. What is deployment?

Deployment is the process of releasing software into a production environment for users.

### Q9. What is maintenance?

Maintenance involves fixing bugs, improving performance, updating security and adding new features after software release.

### Q10. What is the difference between a bug and an error?

An error is a mistake in software development or execution. A bug is a defect in the software that can cause incorrect behaviour.

### Q11. What is unit testing?

Unit testing checks individual functions or components independently.

### Q12. What is integration testing?

Integration testing checks whether multiple software modules work correctly together.

### Q13. What is system testing?

System testing checks the complete integrated application.

### Q14. What is acceptance testing?

Acceptance testing verifies whether the software meets user or customer requirements.

### Q15. Why is SDLC important?

SDLC provides a structured approach to software development, helps manage resources and improves software quality.

---

## 13. Quick Revision

| Phase | Main Purpose |
|---|---|
| Planning | Decide project goals, cost and timeline |
| Requirement Analysis | Understand user requirements |
| System Design | Plan architecture, database and APIs |
| Development | Write the source code |
| Testing | Find bugs and verify functionality |
| Deployment | Release software to users |
| Maintenance | Fix, improve and update software |

### Remember This Order

**Planning → Requirement Analysis → Design → Development → Testing → Deployment → Maintenance**

---

## 14. SDLC Practice Checklist

- [ ] Understand the meaning of SDLC.
- [ ] Remember all seven phases.
- [ ] Understand Planning.
- [ ] Understand Requirement Analysis.
- [ ] Understand Functional Requirements.
- [ ] Understand Non-Functional Requirements.
- [ ] Understand SRS.
- [ ] Understand System Design.
- [ ] Understand Development.
- [ ] Understand Testing and its types.
- [ ] Understand Deployment.
- [ ] Understand Maintenance and its types.
- [ ] Practise interview questions.
- [ ] Explain the complete SDLC process using an online shopping application example.

**Final Interview Tip:**

If an interviewer asks you to explain SDLC, define it first, explain all seven phases in order, and use one real-world software example to demonstrate your understanding.
