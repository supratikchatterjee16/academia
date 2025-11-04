# Agile Methods for Business Analysis

The following methods are discussed here:

- Walk the wall: For stakeholder alignment
- INVEST model: Define concise user stories
- Last Responsible Moment: Decision making principle for project and product development
- Minimum Viable Product: How to define "done" for initial product offering
- Template statement for experiments

## Walk the wall

**Walk the Wall** is a **collaborative review technique** commonly used in **Agile and iterative project environments** to review **requirements, user stories, progress, or solution designs**.
It involves **physically or virtually** walking along a visual display (a “wall”) where work items are posted, and reviewing them **as a group** to ensure shared understanding and alignment.

---

### **How It Works**

1. Requirements, user stories, workflows, prototypes, or plans are displayed on a **wall**, whiteboard, or digital board (e.g., Jira, Miro, Trello).
2. The team **physically or virtually gathers** around this wall.
3. Participants **discuss each item** in sequence — usually **left to right** or **top to bottom**.
4. Questions, clarifications, dependencies, and risks are identified.
5. Updates are made immediately, or follow-up actions are noted.

---

### **Purpose of Walk the Wall**

* Build **shared understanding** of the work.
* Confirm **requirements are interpreted correctly**.
* Visualize **progress, gaps, and dependencies**.
* Encourage **collaboration instead of isolated interpretation**.

---

### **When It’s Used**

* **Before development:** Reviewing user stories for completeness.
* **During development:** Checking progress against the roadmap.
* **During testing:** Reviewing coverage and outcomes.
* **During release planning:** Ensuring feature alignment.

---

### **Who Participates**

| Role                                | Contribution                                 |
| ----------------------------------- | -------------------------------------------- |
| **Business Analyst**                | Clarifies requirements & rules               |
| **Product Owner / Product Manager** | Confirms business priorities & value         |
| **Developers**                      | Confirm feasibility & technical dependencies |
| **Testers**                         | Identify validation and test coverage needs  |
| **UX/Design**                       | Ensure experience alignment                  |
| **Stakeholders**                    | Provide acceptance or feedback               |

---

### **Example Scenario of Walk the Wall**

**Context:** Development of a new customer self-service portal.

#### On the wall, the team displays:

* User stories
* Wireframes
* Acceptance criteria
* Workflow diagrams

#### Walk-through:

The group walks left-to-right across the posted process:

| Step                | Discussion Focus                            |
| ------------------- | ------------------------------------------- |
| Login Screen        | Authentication method and data requirements |
| Dashboard           | Which widgets are must-have for MVP         |
| FAQ Search          | What search filters should be included      |
| Support Ticket Form | Which fields must be mandatory              |

**Result:**
Everyone leaves understanding **what is being built**, **why**, and **in what order**.

---


## INVEST model

The **INVEST model** is a guideline used to evaluate the **quality of user stories** in Agile projects. It ensures that each user story is well-formed, actionable, and testable before development begins.

**INVEST** is an acronym:

| Letter | Meaning         | What It Means                                                                                                       |
| ------ | --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **I**  | **Independent** | The story should stand on its own and not be tightly dependent on another story.                                    |
| **N**  | **Negotiable**  | The details can be discussed and refined between stakeholders and the development team — it’s not a fixed contract. |
| **V**  | **Valuable**    | The story should deliver clear business value to the user or organization.                                          |
| **E**  | **Estimable**   | The team should be able to estimate the size or effort to complete the story.                                       |
| **S**  | **Small**       | The story should be small enough to complete within one iteration (typically 1–2 weeks).                            |
| **T**  | **Testable**    | The story must have clear acceptance criteria to validate that it’s done correctly.                                 |

---

### **Example of an INVEST-Compliant User Story**

> **As a** returning customer,
> **I want** to save multiple delivery addresses,
> **So that** I can quickly choose where I want my order delivered.

**Acceptance Criteria:**

* I can add a new address.
* I can edit or delete an existing address.
* I can choose a saved address during checkout.

**Why it meets INVEST:**

* Independent → Doesn’t require other checkout features to work.
* Negotiable → Details can be clarified with Product Manager/BA.
* Valuable → Improves user convenience and repeat purchase flow.
* Estimable → Developers can assess complexity.
* Small → Can likely be done within one sprint.
* Testable → Acceptance criteria define how we validate completion.

---

### **When the INVEST Model Is Used**

* During **backlog refinement / grooming**
* When writing **new user stories**
* Before planning a sprint to ensure **stories are ready to be worked on**

---

## Last Responsible Moment

**The “Last Responsible Moment”** (LRM) is a **decision-making principle** used in project and product development, especially in **Agile and Lean** environments.

---

### What It Means

The **Last Responsible Moment** is the **latest point in time** at which a decision **can be made without negatively affecting cost, schedule, or outcome**.

In simple terms:

> **Don’t make a decision too early when information is unclear — but don’t wait so long that it becomes a problem.**

It encourages **delaying decisions responsibly** so teams have **maximum learning**, **more accurate information**, and **reduced rework**.

---

### Why It’s Used

Because **early decisions can be wrong**.

If you commit to technical choices, designs, processes, or requirements before enough is known, you risk:

* Rework
* Cost overruns
* Delivering the wrong thing
* Locking into poor solutions

By waiting until the **Last Responsible Moment**, decisions are:

* **Better informed**
* **More accurate**
* **More aligned with real user needs**

---

### Example

#### Scenario:

A product team is building a new mobile app. They need to choose:

* **Which payment processor** to integrate (Stripe, PayPal, Apple Pay, etc.)

If they decide **too early**, they may:

* Choose a processor that users don’t prefer
* Miss new pricing options
* Lock themselves into a more expensive contract

If they wait too **late**, the system’s architecture may restrict them or delay launch.

#### **Last Responsible Moment Approach:**

The BA and technical team design the app **so the payment module is pluggable**.
They **gather user data during beta testing**, then **select the payment processor right before integration**.

This timing:
✔ Uses real customer insight
✔ Avoids rework
✔ Keeps flexibility without delaying delivery

---

### Visual Summary

```
|-------------------|----------------------|-------------------|
   Too Early         Last Responsible        Too Late
  (Risk of Wrong)      (Ideal Choice)        (Risk of Delay)
```

---

### Stakeholder Involvement

| Role                                | Contribution to LRM                                                       |
| ----------------------------------- | ------------------------------------------------------------------------- |
| **Product Manager / Product Owner** | Sets priorities, ensures decisions align with product vision.             |
| **Business Analyst**                | Gathers requirements and data to support informed decisions.              |
| **Development Team**                | Identifies technical constraints and suggests the safest point to decide. |
| **Stakeholders**                    | Provide feedback to inform decision timing.                               |

**The Business Analyst plays a key role** by supplying the **information** needed to decide at the right time.

> The **Last Responsible Moment** is the practice of **delaying decisions until the point when delaying any further risks cost, schedule, or quality.**

## Minimum Viable Product

A **Minimum Viable Product (MVP)** is the **smallest, simplest version of a product** that can be released to real users **to validate assumptions**, **test value**, and **gather feedback** with **minimal effort and cost**.

The MVP **is not a prototype**—it is a working product that delivers **just enough value** for early users to use it and for the team to **learn what to improve next**.

---

### What is an MVP?

#### **Formal Definition:**

> A Minimum Viable Product is the **minimum set of features** required to deliver **value to early users** and generate **validated learning** about the product’s direction.

#### **Purpose of an MVP**

* Validate market demand
* Avoid building unnecessary features
* Reduce development cost and time
* Learn quickly from real users

---

### Real Example

A company wants to build a **full fitness tracking app**.

**Full product vision:**

* Custom workouts
* Nutrition plans
* Progress charts
* Community features
* Wearable device sync

**MVP:**

* A simple mobile app that lets users choose one workout plan and track exercises manually.

This lets the team **test whether people want structured workout guidance** before building everything else.

---

### Methods to Define an MVP

There are several structured approaches to deciding *what should be included* in the first release:

---

#### **1. MoSCoW Prioritization**

Divide features into:

* **Must Have** *(Required for product to function and deliver core value)*
* **Should Have**
* **Could Have**
* **Won’t Have (now)**

**MVP = Must Have items only**

---

#### **2. User Story Mapping**

Steps:

1. Map the **user journey** (e.g., Find product → View → Buy → Track order).
2. Break into **user stories** under each step.
3. Prioritize the **simplest useful slice** across the journey.

**Result:** You build **one thin but complete workflow**, instead of many unfinished features.

---

#### **3. Kano Model**

Classify features based on how they affect customer satisfaction:

| Category          | Meaning                                    |
| ----------------- | ------------------------------------------ |
| Basic Needs       | Must exist or product fails                |
| Performance Needs | More = better satisfaction                 |
| Delighters        | Extra features users love but don’t expect |

**MVP = Basic + 1–2 Performance features**, no delighters.

---

#### **4. Riskiest Assumption Testing (Lean Startup)**

Identify the **most uncertain assumption** (e.g., “Users will pay monthly”),
and build the **smallest product needed to test that assumption**.

**Example:** Launch a landing page with a “Try Now” signup button to measure interest.

---

#### **5. Feature Value vs. Effort Matrix**

Plot features on a 2x2 grid:

```
            High Value     |      Low Value
High Effort     Avoid      |      Avoid
Low Effort      MVP        |    Maybe Later
```

MVP = **High Value + Low Effort** items.

---

### Key Characteristics of a Good MVP

A good MVP:

* Solves a **real problem**
* Provides **value immediately**
* Is **simple and small**
* Helps collect **real user feedback**
* Can be built **quickly**

A bad MVP:

* Tries to please everyone
* Requires complex architecture before launch

---

> A Minimum Viable Product is the **fastest, simplest version of a product** that allows real users to experience core value and provide feedback—helping the team learn before investing further.

---

## Template for experiments

Quick reference to the templates types to be discussed here:


| Template Type        | Best Use                             |
| -------------------- | ------------------------------------ |
| Hypothesis Statement | Testing product ideas                |
| Assumption Test      | Validating uncertain beliefs         |
| Experiment Card      | Recording structured learning        |
| Learning Objective   | Framing purpose of test              |
| Prototype Test       | Testing UX concepts                  |
| A/B Test             | Optimizing design or messaging       |
| MVP Test             | Validating core value before scaling |

### **1. Hypothesis Statement Template**

> **We believe** that *(target group)*
> **will** *(desired behavior/outcome)*
> **if we** *(change, feature, experiment)*.

**Success Criteria:** Measured by *(metric or observable behavior)*.

**Example:**

> We believe that new customers will complete checkout faster if we add a guest checkout option.
> **Success:** 20% increase in completed purchases within 2 weeks.

---

### **2. Assumption Experiment Template (Riskiest Assumption First)**

> Our assumption is that *(assumption to validate)*.
> To test this, we will *(experiment method)*.
> We will know we are right if *(success metric)*.

**Example:**

> Our assumption is that users want personalized workout recommendations.
> To test this, we will show a “Take Personal Fitness Quiz” prompt.
> Success = at least 35% of visitors complete the quiz.

---

### **3. Lean Startup Experiment Card Template**

| Field                 | Description                                   |
| --------------------- | --------------------------------------------- |
| **Assumption:**       | What needs to be true for the idea to succeed |
| **Experiment:**       | What we will do to test it                    |
| **Data to Collect:**  | What we will measure                          |
| **Expected Outcome:** | What success looks like                       |
| **Next Action:**      | What we’ll do depending on results            |

**Example:**

* **Assumption:** People want live chat support.
* **Experiment:** Add a “Live Chat” button linking to a survey sign-up.
* **Data:** Click-through and sign-ups.
* **Expected Outcome:** 10%+ click rate.
* **Next Action:** Build live chat if validated.

---

### **4. “We Will Learn” Learning Objective Template**

> By running this experiment, **we expect to learn** whether *(core question)*.

**Example:**

> By running this experiment, we expect to learn whether customers want self-service returns instead of phone support.

---

### **5. Prototype Test Statement (Design Thinking)**

> We are testing *(solution / concept)*
> with *(user group)*
> to learn *(behavior or preference)*
> to determine whether *(decision to proceed, pivot, or stop)*.

**Example:**

> We are testing a simplified subscription dashboard with frequent gym members to learn if visibility of workout streaks increases motivation.

---

### **6. A/B Test Experiment Template**

> If we change *(element)* from *(A)* to *(B)*,
> then *(specific user action)* will change,
> measured by *(metric)*.

**Example:**

> If we change the “Subscribe” button to “Start Free Trial,” sign-up rates will increase, measured by conversion %.

---

### **7. MVP / Feature Slice Test Template**

> We will release *(smallest feature version)* to *(specific user group)*
> to observe whether *(behavior / outcome)* occurs.

**Example:**

> We will release a single workout plan to 50 early-access users to observe whether they complete at least 3 sessions per week.

---
