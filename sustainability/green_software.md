# Green Software

## Principles

Base :

1. Energy Efficient : Consume the least amount of electricity possible
2. Hardware Efficiency : Use the least amount of embodied carbon as possible
3. Carbon Awareness : Do more when the electricity is clean and less when it's dirty

Others:

1. Carbon Efficiency : Emit the least amount of carbon possible
2. Measurement : What you can't measure, you can't improve
3. Climate Commitments : Understand the exact mechansim of carbon reduction

## History

In 2019 the original eight principles of green software engineering were released. This 2022 update of the principles took on feedback received over the years, merging some principles and adding a new one regarding understanding climate commitments.

## Acronyms

Acronyms
ACRONYM	TERM	DEFINITION
CFE

Carbon-free energy

This term is usually used to talk about the percentage of renewable energy used as a proportion of the total energy used.
CH4

Methane

A common gaseous hydrocarbon that has a warming effect 25 times that of CO2.
CO2

Carbon dioxide

One of the most common greenhouse gases.
CO2eq / CO2-eq / CO2e

Carbon dioxide equivalent

Carbon is used as a common form of measurement for all greenhouse gases. This unit of measurement indicates the potential impact of non-CO2 gases on global warming in carbon terms.
COP

Conference of the Parties

An annual event involving all parties in the United Nations Framework Convention on Climate Change.
gCO2eq/kWh

grams of carbon per kilowatt hour

The standard unit of carbon intensity is gCO2eq/kWh, or grams of carbon per kilowatt hour.
GHGs

Greenhouse gases

Greenhouse gases are a group of gases that trap heat from solar radiation in the Earth's atmosphere. These gases act as a blanket, increasing the temperature on the surface of the Earth.
GWP

Global warming potential

The potential impact of greenhouse gases on global warming. Measured in terms of CO2e.
IPCC

Intergovernmental Panel on Climate Change

The objective of the IPCC is to provide governments at all levels with scientific information that they can use to develop climate policies.
J

joules

Energy is measured in joules (J).
kWh

kilowatt hours

Energy consumption is measured in kilowatt hours (kWh).
MMTCDE

Million metric tonnes of carbon dioxide equivalent

Measurement term for CO2eq.
NDC

Nationally Determined Contribution

The means by which members of the Paris Climate Agreement are expected to update their progress.
PCA

Paris Climate Agreement

An international treaty agreed in 2015 by 196 parties and the UN to reduce the Earth's temperature increase.
PPA

Power Purchase Agreement

A contract you sign with a power plant to purchase RECs.
PUE

Power usage effectiveness

The metric used to measure data center energy efficiency.
REC

Renewable Energy Credit

Renewable energy credits (also known as renewable energy certificates) represent the energy generated by renewable energy sources.
SBTi

Science Based Targets initiative

A body that defines and promotes best practice in science-based target setting. For example, creating the standards for net zero.
SCI

Software Carbon Intensity

A standard which gives an actionable approach to software designers, developers and operations to measure the carbon impacts of their systems.
SF6

Sulfur hexafluoride

A man-made gas used as an electrical insulator that has a warming effect 23,500 times that of CO2.
UNFCCC

United Nations Framework Convention on Climate Change

A group created to achieve the stabilization of greenhouse gas concentrations in the atmosphere at a level that would prevent dangerous interference with the climate system.
VCM

Voluntary Carbon Market

A decentralized market where private actors voluntarily buy and sell carbon credits that represent certified removals or reductions of greenhouse gases (GHGs) in the atmosphere.
VCS

Verified Carbon Standard

A standard for certifying carbon emissions reductions.
WMO

World Meteorological Organization

A specialized agency of the United Nations whose mandate covers weather, climate and water resources.

## Useful Terms

Carbon Intensity - Measures the amount of greenhouse gases emitted per unit of electricity produced.  
Demand Shaping - The strategy of moving workloads to regions or times when the carbon intensity is less  
Greenhouse Gas protocol - The most widely used and internationally recognized greenhouse gas accounting standard.  
Value chain emissions - These are scope 3 emissions according to the GHG protocol, and the most significant source of emissions. They encompass the full range of activities needed to create a product or service, from conception to distribution.   
Energy proportionality - Measures the relationship between power consumed by a computer and the rate at which useful work is done (its utilization).  
Static power draw - This refers to how much electricity is drawn when a device is in an idle state.  
Embodied carbon (also known as "embedded carbon") - The amount of carbon pollution emitted during the creation and disposal of a device.  

## Carbon Efficiency Main Points

The **Paris Climate Agreement** is an international treaty agreed in 2015 by 196 parties and the UN to reduce the Earth's temperature increase. The agreement is to keep the rise in global mean temperature to 2°C compared to pre-industrial levels, with a preferable lower limit of 1.5°C. The agreement is reviewed every five years and mobilizes finance to developing nations to mitigate the impacts of climate change and prepare for and adapt to the environmental effects caused by climate change. In addition, each party is expected to update its progress through a Nationally Determined Contribution (NDC). The agreement is currently signed by 193 parties.

The **United Nations Framework Convention on Climate (UNFCCC)** is a group created to achieve the stabilization of greenhouse gas concentrations in the atmosphere at a level that would prevent dangerous interference with the climate system.

The **COP (Conference of the Parties)** is an annual event involving all parties in the United Nations Framework Convention on Climate Change. At the conference, each party member's progress on tackling global warming, as agreed as part of the Paris Climate Agreement, is reviewed and assessed. The COP is also a chance for parties to come together and make decisions that will reduce the effects of global warming. Common topics include strategies to reduce carbon, financing low carbon strategies and preservation of natural habitats.

The **IPCC (Intergovernmental Panel on Climate Change)**, created by the UN in 1988, aims to provide governments at all levels with scientific information that they can use to develop climate policies. IPCC reports are also a key input into international climate change negotiations. The IPCC is an organization of governments that are members of the United Nations or the World Meteorological Organization (WMO). The IPCC currently has 195 members.

GHGs is Greenhouse Gases. Carbon emmissions are quantified in **Carbon Equivalent(CO2eq/CO2-eq/CO2E/Carbon)**.

## Energy Efficiency Main Points

Energy measurement​:
- Energy is measured in joules (J). Joules measure the SI unit of energy.
- Power is measured in watts, where 1 watt (W) is a rate corresponding to one joule per second.
- A kilowatt (kW) is, therefore, also a rate corresponding to 1000 joules per second.
- A kilowatt-hour (kWh) is a measure of energy (J) corresponding to one kilowatt of power sustained for one hour.

The data center industry uses the **power usage effectiveness (PUE)** metric, developed by Green Grid in 2006, to measure data center energy efficiency. Specifically, this relates to how much energy the computing equipment uses as compared to cooling and other overheads supporting the equipment. When a data center's PUE is close to 1.0, computing is using nearly all energy. When the PUE is 2.0, this means an additional watt of IT power is required to cool and distribute power to the IT equipment for every watt of IT power it uses.

**Energy proportionality**, first proposed in 2007 by engineers at Google, measures the relationship between power consumed by a computer and the rate at which useful work is done (its utilization).

## Carbon Awareness Main Points

Carbon intensity measures how much carbon (CO2e) is emitted per kilowatt-hour (KWh) of electricity consumed. The standard unit of carbon intensity is gCO2eq/kWh, or grams of carbon per kilowatt hour.

### Dispatchability and Curtailment
Electricity demand varies during the day, and supply always needs to be able to meet that demand. A brownout (a dip in the voltage level of the power line) occurs if a utility doesn't produce enough electricity to meet demand. Conversely, if a utility produces more electricity than is required, then to stop infrastructure burning out, breakers trip and we have blackouts.

There needs to be a balance between the demand and supply of electricity at all times and the responsibility for this usually falls to the utility provider.

In the case of fossil fuels such as coal, it is easier to control the power produced for this supply; this is called dispatchability. However, in the case of renewable power sources such as wind farms, the power produced cannot easily be controlled (we can't control how much the wind blows). If the power source produces more electricity than is needed, that electricity is thrown away; this is called curtailment.

### Marginal Carbon Intensity

If you suddenly need to access more power - for example, you need to turn on a light - that energy comes from the marginal power plant. The marginal power plant is dispatchable, which means marginal power plants are often powered by fossil fuels.

Marginal carbon intensity is the carbon intensity of the power plant that would have to be employed to meet any new demand.

Fossil-fueled power plants rarely scale down to 0. They have a minimum functioning threshold, and some don't scale; they are considered a consistent, always-on baseload. Because of this, we sometimes have the scenario where we curtail (throw away) renewable energy while still consuming energy from fossil fuel power plants.

Always buy less energy from both fossil fuel plants as well as renewable plants.

Being carbon aware means responding to shifts in carbon intensity by increasing or decreasing your demand. If your work allows you to be flexible with when and where you run workloads, you can shift accordingly - consuming electricity when the carbon intensity is lower and pausing production when it is higher. For example, training a Machine Learning model at a different time or region with much lower carbon intensity.

Studies show these actions can result in 45% to 99% carbon reductions depending on the number of renewables powering the grid.

Demand shifting can be further broken down into spatial and temporal shifting.

Spatial shifting means moving your computation to another physical location where the current carbon intensity is lower. It might be a region that naturally has lower carbon sources of energy. For example, moving to different hemispheres depending on the season for more sunlight hours.

If you can't shift your computation spatially to another region, another option you have is to shift to another time. Perhaps later in the day or night when it's sunnier or windier and, therefore, the carbon intensity is lower. This is called temporal demand shifting. We can predict future carbon intensity reasonably well through advances in weather forecasting.

Demand shifting is the strategy of moving computation to regions or times when the carbon intensity is lowest. Demand shaping is a similar strategy. However, instead of moving demand to a different region or time, we shape our computation to match the existing supply.

## Hardware Efficiency Important Points

Embodied carbon​

The device you are using to read this on produced carbon when it was manufactured and, once it reaches the end of life, disposing of it may release more. Embodied carbon (also referred to as "embedded carbon") is the amount of carbon pollution emitted during the creation and disposal of a device.

When calculating the total carbon pollution for computers running software, both the carbon pollution associated with running the computer as well as the embodied carbon of the computer must be accounted for.

Amortization

A way to account for embodied carbon is to amortize the carbon over the expected life span of a device. For example, suppose it took 4000kg CO2eq to build a server, and we expect it to last four years. Amortization means that we can say the server emits 1000kg CO2eq/year.

Improving Hardware Efficiency :

1. Extending lifespan of hardware(End-User) : Hardware is retired when it breaks down or struggles to handle modern workloads. Of course, hardware will always break down eventually but, as developers, we can use software to build applications that run on older hardware and extend their lifetime.
2. Increasing device Utilization(Cloud) :  It’s better to use one server at 100% utilization than 5 servers at 20% utilization because of the cost of embodied carbon.

## Measurement Important Points

The GHG protocol divides emissions into three scopes:

- Scope 1: Direct emissions from operations owned or controlled by the reporting organization, such as on-site fuel combustion or fleet vehicles.
- Scope 2: Indirect emissions related to emission generation of purchased energy, such as heat and electricity.
- Scope 3: Other indirect emissions from all the other activities you are engaged in. Including all emissions from an organization's supply chain; business travel for employees, and the electricity customers may consume when using your product. Also referred to as value chain emissions

| GHG Scope | Scope 2 | Scope 3 |
| :---: | :---: | :---:|
| Private Cloud | Energy | Embodied |
| Public Cloud | | Energy + Embodied |
| Hybrid Cloud | Some Energy | Some Energy + Embodied |
| Frontend | | Energy + Embodied |

To calculate a total for software carbon emissions, you need access to detailed data regarding the energy consumption, carbon intensity, and hardware that your software is running on. This is challenging data to gather, even in the case of an organization's own closed-source software products where they can track its usage with telemetry or logs.

A total is only one metric that describes the state of something. To make the right decisions, you need to look at many different metrics.

The **Software Carbon Intensity (SCI)** specification is a methodology developed by the Standards Working Group in the Green Software Foundation, designed to score a software application along a dimension of sustainability and to encourage action towards eliminating emissions.

While the GHG protocol calculates the total emissions, the SCI is about calculating the rate of emissions.

Instead of bucketing the carbon emissions of software into scopes 1-3, it buckets them into operational emissions (carbon emissions from the running of software) and embodied emissions (carbon emissions from the physical resources required to run the software). It's also an intensity rather than a total, which is more inclusive of open-source software.

Offsets are an essential component of any climate strategy; however, offsets are not eliminations and therefore are not included in the SCI metric.

If you make your application more energy efficient, hardware efficient, or carbon aware, your SCI score will decrease. The only way to reduce your SCI score is to invest time or resources into one of those three principles. As such, adopting the SCI as a metric for your software application along with the GHG protocol, will drive investment into one of the three pillars of green software.

Equation to calculate SCI :

$$SCI = ((E * I) + M) per R$$

E = Energy consumed by a software system I = Location-based marginal carbon emissions M = Embodied emissions of a software system. R = Functional unit (e.g. carbon per additional user, API-call, ML job, etc)

This summarizes to:

SCI = C per R (Carbon per R)

R is the core characteristic of the SCI and turns it into an intensity rather than a total. This is what we call a functional unit.

Steps to follow to calculate SCI : 

1. Decide what to include
2. Choose your functional units
3. Decide how to measure your emissions : It can be a measurement or a calculation
4. Quantify

## Climate Commitments important points

Carbon reduction methodologies :

- Abatement/Eliminations : eliminating sources of CO2 emissions associated with a company's operations and value chain so that they do not enter the atmosphere.
- Offsets : direct investments in emission-reduction projects through the purchase of carbon credits on the voluntary carbon market (VCM). The VCM is a decentralized market where private actors voluntarily buy and sell carbon credits that represent certified removals or reductions of GHGs from the atmosphere.
    - Compensation/Avoidance : actions that companies take to help society avoid or reduce emissions outside of their value chain. This is essentially investing in other organizations' abatement projects. Includes
        - Conservation - Credits are created based on carbon not released through protecting old trees.
        - Community Projects - These projects help communities worldwide, mainly undeveloped ones, by introducing sustainable living methods.
        - Waste to energy - These projects capture methane/landfill gas in smaller villages, human or agriculture waste, and convert it into electricity.
    - Neutralization/Removal : actions that companies take to remove carbon from the atmosphere within or beyond their value chain. Neutralizations refer to the removal and permanent storage of atmospheric carbon to counterbalance the effect of releasing CO2 into the atmosphere. This includes actions such as:
        - Enhancing natural carbon sinks that remove CO2 from the atmosphere. For example, forest restoration, since photosynthesis removes CO2 naturally. Forest expansion comes with challenges as it's essential not to impact the dynamics of farmland and food supply elsewhere. Modern farming methods can also prolong the time carbon remains stored in soil.
        - Direct air capture is the process of capturing CO2 from the air and storing it permanently, either underground or in long-lived products like concrete.

Carbon neutrality is defined by an internationally recognized standard: PAS 2060. Although this does recommend an organization sets abatement targets, it doesn't demand they reduce their emissions. So to be considered carbon neutral, an organization can just measure and offset without investing resources in eliminating their carbon emissions.

The standard for net zero is being developed by the Science Based Targets initiative (SBTi). They calculate that there is a 66% probability of limiting global warming to 1.5°C if we reach a level of abatement of about 90% of all GHG emissions by mid-century. So, to meet a net-zero target, an organization needs to eliminate 90% of its emissions by 2050. The remaining emissions can only be offset using neutralizations and permanent carbon removals.

When organizations set a target of 100% renewable power, they might distinguish between being matched by vs. powered by renewables.

To solve the problem of distinguishing between amount of power used from renewables and non-renewables coming from a power grid, a renewable plant sells two things. The first is its electricity, which it sells into a grid. The second is a REC, a Renewable Energy Certificate. 1 REC equals 1kWh of energy.

You might also hear the term PPA used alongside RECs. A PPA is a Power Purchase Agreement, which is another way to purchase RECs. If you estimate you need 500MWh of electricity per year for a particular data center, you might sign a PPA to purchase 500MWh per year from a renewable plant. You would then get all the RECs associated with this power plant.

PPAs are typically very long-term contracts. A renewable plant can find financing with one of these agreements since it already has had a buyer for its electricity for many years.

PPAs encourage something called additionality. Purchasing a PPA drives the creation of new renewable plants. PPAs are a solution that gets us towards a future where everyone has access to 100% renewable energy.

When it comes to 100% renewable claims, the critical question is, what is the granularity of matching? Do you sum up and net off yearly, monthly, weekly, daily, or hourly? That question is essential because to truly transition to renewable energy, we need 100% of the power to come from low-carbon energy sources like renewables 100% of the time. This fine granular matching is often called 24/7 hourly matching.

Carbon-free energy is defined as the average percentage of carbon-free energy consumed in a particular location on an hourly basis.

Carbon aware computing involves responding to electrical carbon intensity signals and changing the behavior of software, so it emits less carbon. Carbon awareness also helps an organization meet their 24/7 hourly matching target and increase its CFE percentage.
