# Business Analysis

**Business Analysis** is the practice of **identifying business needs**, analyzing problems, and proposing solutions that **create value**.

It focuses on:

* Understanding business processes and goals
* Working with stakeholders to define **requirements**
* Ensuring the **solution delivered aligns with business objectives**

**Example:**
A retail company sees declining online sales → A Business Analyst studies customer behavior, compares competitor websites, and recommends improving the checkout process and adding mobile-friendly features.

---

## **Need Assessment**

A **Need Assessment** identifies gaps between the **current state** and the **desired future state**, and prioritizes which needs matter most.

**Steps:**

1. **Current State** – What is happening now?
2. **Desired State** – What should be happening?
3. **Gap Analysis** – What is missing or inefficient?
4. **Prioritize Needs** – Based on impact and urgency.

**Example:**
Call center wait times are 30 minutes (current) but target is under 5 minutes (desired).
Need = Hire more staff, improve call routing, or add self-service automation.

---

## **Situation Statement + Root Cause Techniques**

**Situation Statement Format:**
*“A problem of ___ is causing ___, which affects ___, because ___.”*

**Example:**
"A high number of product returns is increasing operational costs and damaging customer trust because product descriptions on the website are unclear."

### **Root Cause Analysis Tools**

| Tool                          | Description                                                          | Example Use                                                                                                                                                 |
| ----------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fishbone/Ishikawa Diagram** | Categorizes causes (People, Process, Tools, Materials, Environment). | Returns linked to unclear descriptions → Website team communication and product content guidelines lacking.                                                 |
| **5 Whys**                    | Ask “Why?” repeatedly to find the root cause.                        | Why returns? → Misunderstanding product features → Why? Poor product descriptions → Why? No standardized content process → Why? No assigned responsibility. |

**Example 5 Whys Walkthrough:**

1. Why returns are high? → Customers misunderstood product size.
2. Why misunderstanding? → Size chart unclear.
3. Why unclear? → Content team copied formats from suppliers.
4. Why copy? → No internal content guidelines.
5. Why no guidelines? → Lack of documentation ownership.

**Root Cause:** Lack of standardized product content guidelines.

**Example Fishbone walkthrough**

Below is a **text-based fishbone diagram**, structured for clarity.

```
                                  High Product Returns
                                             |
------------------------------------------------------------------------------------------------
|                 |                   |                   |                   |                |
People            Process             Tools/Tech          Materials           Policies         Customer
- Content team    - No review         - No content        - Supplier data     - No guidelines   - Misinterpreting
  untrained         workflow            formatting tools    varies in format     defined           product info
- No ownership    - No quality check  - Outdated CMS      - No standard       - No accountability- Expectations mismatch
                                        makes edits hard    size chart format    structure
```

Explanation of Branches:

| Category      | Key Cause Insight                                                    |
| ------------- | -------------------------------------------------------------------- |
| **People**    | No one responsible for maintaining product data quality              |
| **Process**   | No verification or approval workflow before publishing product pages |
| **Tools**     | CMS system not user-friendly and lacks content control features      |
| **Materials** | Supplier-provided information inconsistent and unformatted           |
| **Policies**  | No company standards or guidelines to control data consistency       |
| **Customer**  | Customers misinterpret features due to unclear descriptions          |


---

## **Solution Statement**

If the **Situation Statement** describes the *problem*, the **Solution Statement** describes the *proposed fix* and *intended improvement*.

### **Solution Statement Framework**

Use this template:

> **To address** *(root cause)*, **we will implement** *(solution / change)*, **which will result in** *(desired measurable outcome)*, **benefiting** *(affected stakeholders).*

### **Solution Statement Example (for the earlier product returns issue)**

**Situation (recap):** High return rates due to unclear product descriptions caused by lack of standardized content guidelines.

**Solution Statement:**

> To address the lack of standardized product content guidelines, we will implement a structured product information process with quality review steps, which will result in clearer product descriptions and a reduction in product returns, benefiting both customers and the fulfillment and support teams.

---

## **Stakeholder Classification & Power–Interest Map**

**Stakeholders** are individuals or groups affected by, or able to affect, the project.

### **Power–Interest Grid**

| Stakeholder Category           | Characteristics                   | Strategy           | Example                    |
| ------------------------------ | --------------------------------- | ------------------ | -------------------------- |
| **High Power / High Interest** | Strong influence and impacted     | **Manage Closely** | COO, Project Sponsor       |
| **High Power / Low Interest**  | Influence but limited involvement | **Keep Satisfied** | Legal or Finance           |
| **Low Power / High Interest**  | Impacted but lower authority      | **Keep Informed**  | Customer Service Agents    |
| **Low Power / Low Interest**   | Minimal interest and impact       | **Monitor**        | General staff not affected |

---

## **Business Case**

A **Business Case** justifies **why a project should be approved**, showing **benefits vs. costs and risks**.

### **Why It Is Used**

* To support decision-making
* To ensure investments produce value
* To align projects with strategy

### **Business Case Development Process**

1. Problem / Opportunity Definition
2. Options Analysis
3. Cost–Benefit and ROI Comparison
4. Risk and Impact Assessment
5. Recommendation

### **Framework Examples**

* **SWOT Analysis** (Strengths, Weaknesses, Opportunities, Threats)
* **Feasibility Study** (Technical, Operational, Economic Feasibility)

**Real Example:**
Investing $200k in automated customer support expected to reduce support staff costs by $500k annually → Business case supports automation.

### Issues that might arise

1. Portfolio Management process
2. Scope Creep
3. Cost overruns
4. Delays
5. Rework
6. Cancellations

### Business needs and Previous Analysis of the Situation

Previous Analysis Components:

1. Organizational strategies, goals and objectives supported
2. Analysis of the situations
3. Critical Success factors
4. Potential gaps
5. High level risk assessment, assumptions, constraints and regulations
6. Recommendations for alternatives
7. High level milestones, dependencies, roles, responsibilities and risks

---

## **Vision**

A **Vision Statement** describes the **future success** the project aims to achieve. It is an idealistic view of tasks, and defines the scope.

**Question it answers:**
*“What does success look like and why are we doing this?”*

### **Vision Statement Framework:**

*For [target user], who need [need], the [solution] will [benefit]*.

**Example:**
"For customers who need faster issue resolution, the self-service portal will provide answers without needing to contact support."

### **Elevator Pitch:**

“In the next six months, we will launch a 24/7 customer self-service portal that allows users to solve 70% of their issues on their own, reducing wait times and support workload.”

---

## **Project Roadmap**

A **project roadmap** is a high-level visual timeline that shows **major project milestones, phases, deliverables, and expected outcomes** over time.
It is *not* a detailed task plan — it communicates **direction and priority**, rather than step-by-step work.

**Key Purposes of a Roadmap:**

* Align stakeholders on **what will be delivered** and **when**
* Provide a timeline for **major release milestones**
* Communicate **priority and sequencing**

Think of it as the *“big picture delivery plan.”*

---

### **How the Roadmap Differs in Adaptive vs. Non-Adaptive Projects**

| Aspect                  | **Adaptive (Agile / Iterative)**                            | **Non-Adaptive (Predictive / Waterfall)**                                                    |
| ----------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Requirements            | Evolving and flexible                                       | Fixed early in the project                                                                   |
| Roadmap Level of Detail | High-level themes and features by *iterations or releases*  | Specific scope and detailed phase timelines                                                  |
| Timeline                | *Time is fixed*, scope adapts                               | *Scope is fixed*, time adapts                                                                |
| Updates                 | Updated frequently (every sprint/release)                   | Updated only when major changes occur                                                        |
| Example Roadmap View    | “Q1: User Login and Profile → Q2: Dashboard → Q3: Payments” | “Phase 1: Requirements → Phase 2: Design → Phase 3: Build → Phase 4: Test → Phase 5: Launch” |

#### Simple Visual Comparison:

**Predictive Roadmap (Waterfall):**

```
Requirements → Design → Development → Testing → Deployment
Jan        Feb       Mar           Apr        May
```

**Adaptive Roadmap (Agile):**

```
Release 1 (4 Weeks): Login + Profile
Release 2 (4 Weeks): Dashboard + Notifications
Release 3 (4 Weeks): Payments + Reports
```

---

### **Stakeholder Roles in the Roadmap**

#### **Product Manager**

* Owns the **product vision and strategy**
* Decides **feature priorities** based on customer value and business goals
* Ensures roadmap aligns with **market needs**
* Communicates roadmap to executives, marketing, and customers

**In Adaptive Projects:**
The Product Manager defines the **Feature / Epic level roadmap** and reprioritizes backlog items continuously.

**In Non-Adaptive Projects:**
The Product Manager helps define **scope and milestone objectives** at the start and monitors changes if needed.

---

#### **Business Analyst (BA)**

* Translates roadmap features into **clear requirements**
* Clarifies scope, acceptance criteria, and business rules
* Ensures **stakeholder needs are correctly understood**
* Works with technical teams so solutions match the roadmap goals

**In Adaptive Projects:**
The BA breaks roadmap items into **user stories**, supports sprint planning, and ensures continuous stakeholder feedback.

**In Non-Adaptive Projects:**
The BA gathers **complete requirements upfront**, documents them, and ensures alignment with the originally defined roadmap.

---

#### **How They Work Together**

| Activity                    | Product Manager            | Business Analyst                      |
| --------------------------- | -------------------------- | ------------------------------------- |
| Define Vision               | Leads                      | Supports with analysis                |
| Prioritize Roadmap Features | Leads                      | Advises based on feasibility and risk |
| Write Requirements          | Provides high-level intent | Writes detailed requirements          |
| Align Stakeholders          | Communicates decisions     | Clarifies impacts and dependencies    |
| Support Development Team    | Sets direction             | Provides detail and clarifications    |

**Example Collaboration (Real Scenario):**

A company wants to launch a new online subscription platform.

* **Product Manager:** Sets goal: “Launch subscription in Q3 to increase recurring revenue.”
* **BA:** Translates this into requirements such as subscription plans, renewal rules, user flows, etc.
* **Roadmap:**

  * Q1: Prototype and Research
  * Q2: Development
  * Q3: Launch

---

## **Requirements Elicitation (Based on Stakeholders)**

| Stakeholder     | Typical Concerns                 | Elicitation Techniques              |
| --------------- | -------------------------------- | ----------------------------------- |
| Executives      | ROI, strategic alignment         | Interviews, Business Case Review    |
| Managers        | Workflow efficiency              | Workshops, Process Mapping          |
| End Users       | Usability and daily tasks        | Observations, Surveys, User Stories |
| Technical Staff | System feasibility & constraints | Technical reviews, Prototyping      |

---

## **Traceability and Monitoring**

### **Traceability Matrix**

Links requirements from **origin → development → testing → deployment**.

| Req ID | Requirement                                      | Stakeholder | Implementation Reference | Test Case | Status      |
| ------ | ------------------------------------------------ | ----------- | ------------------------ | --------- | ----------- |
| R-001  | Website must allow self-service account recovery | Customers   | User Portal Module       | TC-008    | In Progress |

### **Task Board (Kanban)**

Visual board to track work progress:
**To Do → In Progress → Testing → Completed**

---

## **Change Control**

Change Control ensures **any change to requirements is reviewed, approved, and documented**.

### **Change Control Board (CCB)**

A decision group responsible for evaluating change requests.

**Responsibilities:**

* Review change impact (cost, timeline, scope)
* Approve or reject changes
* Ensure alignment with business goals

**Example Change Request:**
Adding a new payment gateway mid-project → CCB evaluates impact before approval.

---

## **Testing and Verification Methods**

| Testing Type                      | Purpose                                | Example                                    |
| --------------------------------- | -------------------------------------- | ------------------------------------------ |
| **Unit Testing**                  | Test individual components             | Login function works correctly             |
| **Integration Testing**           | Ensure system components work together | Login system works with user database      |
| **System Testing**                | Test the entire system end-to-end      | Complete checkout flow works               |
| **User Acceptance Testing (UAT)** | Validate solution meets user needs     | Employees test new HR portal before launch |

---

## **Release & Implementation Planning**

| Term                        | Meaning                                                        | Example                                                     |
| --------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| **Release Planning**        | Deciding which features are deployed and when                  | Portal v1 releases password reset & FAQ first               |
| **Implementation Planning** | Preparing for rollout, training, communication, and transition | Training staff, updating manuals, launching support hotline |

