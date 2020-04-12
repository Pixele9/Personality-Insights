from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

apiKey = "TaRGRZEHYoWYm_D5Rc3dbUZ__wtf-BemTXCgoQrDNX-9"
url = "https://api.eu-gb.personality-insights.watson.cloud.ibm.com/instances/fb2ea819-bd93-48c7-858f-f75e32439355"

authenticator = IAMAuthenticator(apiKey)
service = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

service.set_service_url(url)


text = """To the Shareholders of Berkshire Hathaway Inc
Berkshire earned $81.4 billion in 2019 according to generally accepted accounting principles (commonly
called “GAAP”). The components of that figure are $24 billion of operating earnings, $3.7 billion of realized capital
gains and a $53.7 billion gain from an increase in the amount of net unrealized capital gains that exist in the stocks
we hold. Each of those components of earnings is stated on an after-tax basis.
That $53.7 billion gain requires comment. It resulted from a new GAAP rule, imposed in 2018, that requires
a company holding equity securities to include in earnings the net change in the unrealized gains and losses of those
securities. As we stated in last year’s letter, neither Charlie Munger, my partner in managing Berkshire, nor I agree
with that rule.
The adoption of the rule by the accounting profession, in fact, was a monumental shift in its own thinking.
Before 2018, GAAP insisted – with an exception for companies whose business was to trade securities – that
unrealized gains within a portfolio of stocks were never to be included in earnings and unrealized losses were to be
included only if they were deemed “other than temporary.” Now, Berkshire must enshrine in each quarter’s bottom
line – a key item of news for many investors, analysts and commentators – every up and down movement of the stocks
it owns, however capricious those fluctuations may be.
Berkshire’s 2018 and 2019 years glaringly illustrate the argument we have with the new rule. In 2018, a down
year for the stock market, our net unrealized gains decreased by $20.6 billion, and we therefore reported GAAP
earnings of only $4 billion. In 2019, rising stock prices increased net unrealized gains by the aforementioned $53.7
billion, pushing GAAP earnings to the $81.4 billion reported at the beginning of this letter. Those market gyrations
led to a crazy 1,900% increase in GAAP earnings!
Meanwhile, in what we might call the real world, as opposed to accounting-land, Berkshire’s equity holdings
averaged about $200 billion during the two years, and the intrinsic value of the stocks we own grew steadily and
substantially throughout the period.
Charlie and I urge you to focus on operating earnings – which were little changed in 2019 – and to ignore
both quarterly and annual gains or losses from investments, whether these are realized or unrealized.
Our advising that in no way diminishes the importance of these investments to Berkshire. Over time, Charlie
and I expect our equity holdings – as a group – to deliver major gains, albeit in an unpredictable and highly irregular
manner. To see why we are optimistic, move on to the next discussion.
The Power of Retained Earnings
In 1924, Edgar Lawrence Smith, an obscure economist and financial advisor, wrote Common Stocks as Long
Term Investments, a slim book that changed the investment world. Indeed, writing the book changed Smith himself,
forcing him to reassess his own investment beliefs.
Going in, he planned to argue that stocks would perform better than bonds during inflationary periods and
that bonds would deliver superior returns during deflationary times. That seemed sensible enough. But Smith was in
for a shock.
3
His book began, therefore, with a confession: “These studies are the record of a failure – the failure of facts
to sustain a preconceived theory.” Luckily for investors, that failure led Smith to think more deeply about how stocks
should be evaluated.
For the crux of Smith’s insight, I will quote an early reviewer of his book, none other than John Maynard
Keynes: “I have kept until last what is perhaps Mr. Smith’s most important, and is certainly his most novel, point.
Well-managed industrial companies do not, as a rule, distribute to the shareholders the whole of their earned profits.
In good years, if not in all years, they retain a part of their profits and put them back into the business. Thus there is
an element of compound interest (Keynes’ italics) operating in favour of a sound industrial investment. Over a period
of years, the real value of the property of a sound industrial is increasing at compound interest, quite apart from the
dividends paid out to the shareholders.”
And with that sprinkling of holy water, Smith was no longer obscure.
It’s difficult to understand why retained earnings were unappreciated by investors before Smith’s book was
published. After all, it was no secret that mind-boggling wealth had earlier been amassed by such titans as Carnegie,
Rockefeller and Ford, all of whom had retained a huge portion of their business earnings to fund growth and produce
ever-greater profits. Throughout America, also, there had long been small-time capitalists who became rich following
the same playbook.
Nevertheless, when business ownership was sliced into small pieces – “stocks” – buyers in the pre-Smith
years usually thought of their shares as a short-term gamble on market movements. Even at their best, stocks were
considered speculations. Gentlemen preferred bonds.
Though investors were slow to wise up, the math of retaining and reinvesting earnings is now well
understood. Today, school children learn what Keynes termed “novel”: combining savings with compound interest
works wonders.
************
At Berkshire, Charlie and I have long focused on using retained earnings advantageously. Sometimes this
job has been easy – at other times, more than difficult, particularly when we began working with huge and evergrowing sums of money.
In our deployment of the funds we retain, we first seek to invest in the many and diverse businesses we
already own. During the past decade, Berkshire’s depreciation charges have aggregated $65 billion whereas the
company’s internal investments in property, plant and equipment have totaled $121 billion. Reinvestment in
productive operational assets will forever remain our top priority.
In addition, we constantly seek to buy new businesses that meet three criteria. First, they must earn good
returns on the net tangible capital required in their operation. Second, they must be run by able and honest managers.
Finally, they must be available at a sensible price.
When we spot such businesses, our preference would be to buy 100% of them. But the opportunities to make
major acquisitions possessing our required attributes are rare. Far more often, a fickle stock market serves up
opportunities for us to buy large, but non-controlling, positions in publicly-traded companies that meet our standards.
Whichever way we go – controlled companies or only a major stake by way of the stock market – Berkshire’s
financial results from the commitment will in large part be determined by the future earnings of the business we have
purchased. Nonetheless, there is between the two investment approaches a hugely important accounting difference,
essential for you to understand.
4
In our controlled companies, (defined as those in which Berkshire owns more than 50% of the shares), the
earnings of each business flow directly into the operating earnings that we report to you. What you see is what you
get.
In the non-controlled companies, in which we own marketable stocks, only the dividends that Berkshire
receives are recorded in the operating earnings we report. The retained earnings? They’re working hard and creating
much added value, but not in a way that deposits those gains directly into Berkshire’s reported earnings.
At almost all major companies other than Berkshire, investors would not find what we’ll call this “nonrecognition of earnings” important. For us, however, it is a standout omission, of a magnitude that we lay out for you
below.
Here, we list our 10 largest stock-market holdings of businesses. The list distinguishes between their earnings
that are reported to you under GAAP accounting – these are the dividends Berkshire receives from those 10 investees
– and our share, so to speak, of the earnings the investees retain and put to work. Normally, those companies use
retained earnings to expand their business and increase its efficiency. Or sometimes they use those funds to repurchase
significant portions of their own stock, an act that enlarges Berkshire’s share of the company’s future earnings.
Yearend
Ownership
Berkshire’s Share (in millions)
Company Dividends(1) Retained Earnings(2)
American Express 18.7% $ 261 $ 998
Apple 5.7% 773 2,519
Bank of America 10.7% 682 2,167
Bank of New York Mellon 9.0% 101 288
Coca-Cola 9.3% 640 194
Delta Airlines 11.0% 114 416
J.P. Morgan Chase 1.9% 216 476
Moody’s 13.1% 55 137
U.S. Bancorp 9.7% 251 407
Wells Fargo 8.4% 705 730
Total $3,798 $8,332
(1) Based on current annual rate.
(2) Based on 2019 earnings minus common and preferred dividends paid.
Obviously, the realized gains we will eventually record from partially owning each of these companies will
not neatly correspond to “our” share of their retained earnings. Sometimes, alas, retentions produce nothing. But both
logic and our past experience indicate that from the group we will realize capital gains at least equal to – and probably
better than – the earnings of ours that they retained. (When we sell shares and realize gains, we will pay income tax on
the gain at whatever rate then prevails. Currently, the federal rate is 21%.)
It is certain that Berkshire’s rewards from these 10 companies, as well as those from our many other equity
holdings, will manifest themselves in a highly irregular manner. Periodically, there will be losses, sometimes
company-specific, sometimes linked to stock-market swoons. At other times – last year was one of those – our gain
will be outsized. Overall, the retained earnings of our investees are certain to be of major importance in the growth of
Berkshire’s value.
Mr. Smith got it right.
5
Non-Insurance Operations
Tom Murphy, a valued director of Berkshire and an all-time great among business managers, long ago gave
me some important advice about acquisitions: “To achieve a reputation as a good manager, just be sure you buy good
businesses.”
Over the years Berkshire has acquired many dozens of companies, all of which I initially regarded as “good
businesses.” Some, however, proved disappointing; more than a few were outright disasters. A reasonable number, on
the other hand, have exceeded my hopes.
In reviewing my uneven record, I’ve concluded that acquisitions are similar to marriage: They start, of course,
with a joyful wedding – but then reality tends to diverge from pre-nuptial expectations. Sometimes, wonderfully, the
new union delivers bliss beyond either party’s hopes. In other cases, disillusionment is swift. Applying those images
to corporate acquisitions, I’d have to say it is usually the buyer who encounters unpleasant surprises. It’s easy to get
dreamy-eyed during corporate courtships.
Pursuing that analogy, I would say that our marital record remains largely acceptable, with all parties happy
with the decisions they made long ago. Some of our tie-ups have been positively idyllic. A meaningful number,
however, have caused me all too quickly to wonder what I was thinking when I proposed.
Fortunately, the fallout from many of my errors has been reduced by a characteristic shared by most
businesses that disappoint: As the years pass, the “poor” business tends to stagnate, thereupon entering a state in which
its operations require an ever-smaller percentage of Berkshire’s capital. Meanwhile, our “good” businesses often tend
to grow and find opportunities for investing additional capital at attractive rates. Because of these contrasting
trajectories, the assets employed at Berkshire’s winners gradually become an expanding portion of our total capital.
As an extreme example of those financial movements, witness Berkshire’s original textile business. When
we acquired control of the company in early 1965, this beleaguered operation required nearly all of Berkshire’s capital.
For some time, therefore, Berkshire’s non-earning textile assets were a huge drag on our overall returns. Eventually,
though, we acquired a spread of “good” businesses, a shift that by the early 1980s caused the dwindling textile
operation to employ only a tiny portion of our capital.
Today, we have most of your money deployed in controlled businesses that achieve good-to-excellent returns
on the net tangible assets each requires for its operations. Our insurance business has been the superstar. That operation
has special characteristics that give it a unique metric for calibrating success, one unfamiliar to many investors. We
will save that discussion for the next section.
In the paragraphs that follow, we group our wide array of non-insurance businesses by size of earnings, after
interest, depreciation, taxes, non-cash compensation, restructuring charges – all of those pesky, but very real, costs
that CEOs and Wall Street sometimes urge investors to ignore. Additional information about these operations can be
found on pages K-6 – K-21 and pages K-40 – K-52.
Our BNSF railroad and Berkshire Hathaway Energy (“BHE”) – the two lead dogs of Berkshire’s noninsurance group – earned a combined $8.3 billion in 2019 (including only our 91% share of BHE), an increase of 6%
from 2018.
Our next five non-insurance subsidiaries, as ranked by earnings (but presented here alphabetically), Clayton
Homes, International Metalworking, Lubrizol, Marmon and Precision Castparts, had aggregate earnings in 2019 of
$4.8 billion, little changed from what these companies earned in 2018.
The next five, similarly ranked and listed (Berkshire Hathaway Automotive, Johns Manville, NetJets, Shaw
and TTI) earned $1.9 billion last year, up from the $1.7 billion earned by this tier in 2018.
6
The remaining non-insurance businesses that Berkshire owns – and there are many – had aggregate earnings
of $2.7 billion in 2019, down from $2.8 billion in 2018.
Our total net income in 2019 from the non-insurance businesses we control amounted to $17.7 billion, an
increase of 3% from the $17.2 billion this group earned in 2018. Acquisitions and dispositions had almost no net effect
on these results.
************
I must add one final item that underscores the wide scope of Berkshire’s operations. Since 2011, we have
owned Lubrizol, an Ohio-based company that produces and markets oil additives throughout the world. On September
26, 2019, a fire originating at a small next-door operation spread to a large French plant owned by Lubrizol.
The result was significant property damage and a major disruption in Lubrizol’s business. Even so, both the
company’s property loss and business-interruption loss will be mitigated by substantial insurance recoveries that
Lubrizol will receive.
But, as the late Paul Harvey was given to saying in his famed radio broadcasts, “Here’s the rest of the story.”
One of the largest insurers of Lubrizol was a company owned by . . . uh, Berkshire.
In Matthew 6:3, the Bible instructs us to “Let not the left hand know what the right hand doeth.” Your
chairman has clearly behaved as ordered.
Property/Casualty Insurance
Our property/casualty (“P/C”) insurance business has been the engine propelling Berkshire’s growth since
1967, the year we acquired National Indemnity and its sister company, National Fire & Marine, for $8.6 million.
Today, National Indemnity is the largest P/C company in the world as measured by net worth. Insurance is a business
of promises, and Berkshire’s ability to honor its commitments is unmatched.
One reason we were attracted to the P/C business was the industry’s business model: P/C insurers receive
premiums upfront and pay claims later. In extreme cases, such as claims arising from exposure to asbestos, or severe
workplace accidents, payments can stretch over many decades.
This collect-now, pay-later model leaves P/C companies holding large sums – money we call “float” – that
will eventually go to others. Meanwhile, insurers get to invest this float for their own benefit. Though individual
policies and claims come and go, the amount of float an insurer holds usually remains fairly stable in relation to
premium volume. Consequently, as our business grows, so does our float. And how it has grown, as the following
table shows:
Year Float (in millions)
1970 $ 39
1980 237
1990 1,632
2000 27,871
2010 65,832
2018 122,732
2019 129,423
We may in time experience a decline in float. If so, the decline will be very gradual – at the outside no more
than 3% in any year. The nature of our insurance contracts is such that we can never be subject to immediate or nearterm demands for sums that are of significance to our cash resources. That structure is by design and is a key
component in the unequaled financial strength of our insurance companies. That strength will never be compromised.
7
If our premiums exceed the total of our expenses and eventual losses, our insurance operation registers an
underwriting profit that adds to the investment income the float produces. When such a profit is earned, we enjoy the
use of free money – and, better yet, get paid for holding it.
For the P/C industry as a whole, the financial value of float is now far less than it was for many years. That’s
because the standard investment strategy for almost all P/C companies is heavily – and properly – skewed toward
high-grade bonds. Changes in interest rates therefore matter enormously to these companies, and during the last decade
the bond market has offered pathetically low rates.
Consequently, insurers suffered, as year by year they were forced – by maturities or issuer-call provisions –
to recycle their “old” investment portfolios into new holdings providing much lower yields. Where once these insurers
could safely earn 5 cents or 6 cents on each dollar of float, they now take in only 2 cents or 3 cents (or even less if
their operations are concentrated in countries mired in the never-never land of negative rates).
Some insurers may try to mitigate their loss of revenue by buying lower-quality bonds or non-liquid
“alternative” investments promising higher yields. But those are dangerous games and activities that most institutions
are ill-equipped to play.
Berkshire’s situation is more favorable than that of insurers in general. Most important, our unrivaled
mountain of capital, abundance of cash and a huge and diverse stream of non-insurance earnings allow us far more
investment flexibility than is generally available to other companies in the industry. The many choices open to us are
always advantageous – and sometimes have presented us with major opportunities.
Our P/C companies have meanwhile had an excellent underwriting record. Berkshire has now operated at an
underwriting profit for 16 of the last 17 years, the exception being 2017, when our pre-tax loss was a whopping $3.2
billion. For the entire 17-year span, our pre-tax gain totaled $27.5 billion, of which $400 million was recorded in 2019.
That record is no accident: Disciplined risk evaluation is the daily focus of our insurance managers, who
know that the rewards of float can be drowned by poor underwriting results. All insurers give that message lip service.
At Berkshire it is a religion, Old Testament style.
As I have repeatedly done in the past, I will emphasize now that happy outcomes in insurance are far from a
sure thing: We will most certainly not have an underwriting profit in 16 of the next 17 years. Danger always lurks.
Mistakes in assessing insurance risks can be huge and can take many years – even decades – to surface and
ripen. (Think asbestos.) A major catastrophe that will dwarf hurricanes Katrina and Michael will occur – perhaps
tomorrow, perhaps many decades from now. “The Big One” may come from a traditional source, such as wind or
earthquake, or it may be a total surprise involving, say, a cyber attack having disastrous consequences beyond anything
insurers now contemplate. When such a mega-catastrophe strikes, Berkshire will get its share of the losses and they
will be big – very big. Unlike many other insurers, however, handling the loss will not come close to straining our
resources, and we will be eager to add to our business the next day.
** **********
Close your eyes for a moment and try to envision a locale that might spawn a dynamic P/C insurer. New
York? London? Silicon Valley?
How about Wilkes-Barre?
8
Late in 2012, Ajit Jain, the invaluable manager of our insurance operations, called to tell me that he was
buying a tiny company – GUARD Insurance Group – in that small Pennsylvania city for $221 million (roughly its net
worth at the time). He added that Sy Foguel, GUARD’s CEO, was going to be a star at Berkshire. Both GUARD and
Sy were new names to me.
Bingo and bingo: In 2019, GUARD had premium volume of $1.9 billion, up 379% since 2012, and also
delivered a satisfactory underwriting profit. Since joining Berkshire, Sy has led the company into both new products
and new regions of the country and has increased GUARD’s float by 265%.
In 1967, Omaha seemed an unlikely launching pad for a P/C giant. Wilkes-Barre may well deliver a similar
surprise.
Berkshire Hathaway Energy
Berkshire Hathaway Energy is now celebrating its 20th year under our ownership. That anniversary suggests
that we should be catching up with the company’s accomplishments.
We’ll start with the topic of electricity rates. When Berkshire entered the utility business in 2000, purchasing
76% of BHE, the company’s residential customers in Iowa paid an average of 8.8 cents per kilowatt-hour (kWh).
Prices for residential customers have since risen less than 1% a year, and we have promised that there will be no base
rate price increases through 2028. In contrast, here’s what is happening at the other large investor-owned Iowa utility:
Last year, the rates it charged its residential customers were 61% higher than BHE’s. Recently, that utility received a
rate increase that will widen the gap to 70%.
The extraordinary differential between our rates and theirs is largely the result of our huge accomplishments
in converting wind into electricity. In 2021, we expect BHE’s operation to generate about 25.2 million megawatt-hours
of electricity (MWh) in Iowa from wind turbines that it both owns and operates. That output will totally cover the
annual needs of its Iowa customers, which run to about 24.6 million MWh. In other words, our utility will have attained
wind self-sufficiency in the state of Iowa.
In still another contrast, that other Iowa utility generates less than 10% of its power from wind. Furthermore,
we know of no other investor-owned utility, wherever located, that by 2021 will have achieved a position of wind
self-sufficiency. In 2000, BHE was serving an agricultural-based economy; today, three of its five largest customers
are high-tech giants. I believe their decisions to site plants in Iowa were in part based upon BHE’s ability to deliver
renewable, low-cost energy.
Of course, wind is intermittent, and our blades in Iowa turn only part of the time. In certain periods, when
the air is still, we look to our non-wind generating capacity to secure the electricity we need. At opposite times, we
sell the excess power that wind provides us to other utilities, serving them through what’s called “the grid.” The power
we sell them supplants their need for a carbon resource – coal, say, or natural gas.
Berkshire Hathaway now owns 91% of BHE in partnership with Walter Scott, Jr. and Greg Abel. BHE has
never paid Berkshire Hathaway a dividend since our purchase and has, as the years have passed, retained $28 billion
of earnings. That pattern is an outlier in the world of utilities, whose companies customarily pay big dividends –
sometimes reaching, or even exceeding, 80% of earnings. Our view: The more we can invest, the more we like it.
Today, BHE has the operating talent and experience to manage truly huge utility projects – requiring
investments of $100 billion or more – that could support infrastructure benefitting our country, our communities and
our shareholders. We stand ready, willing and able to take on such opportunities.
9
Investments
Below we list our fifteen common stock investments that at yearend had the largest market value. We exclude
our Kraft Heinz holding – 325,442,152 shares – because Berkshire is part of a control group and therefore must
account for this investment on the “equity” method. On its balance sheet, Berkshire carries the Kraft Heinz holding at
a GAAP figure of $13.8 billion, an amount that represents Berkshire’s share of the audited net worth of Kraft Heinz
at December 31, 2019. Please note, though, that the market value of our shares on that date was only $10.5 billion.
12/31/19
Shares* Company
Percentage of
Company
Owned Cost** Market
(in millions)
151,610,700 American Express Company .................. 18.7 $ 1,287 $ 18,874
250,866,566 Apple Inc. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.7 35,287 73,667
947,760,000 Bank of America Corp. ...................... 10.7 12,560 33,380
81,488,751 The Bank of New York Mellon Corp. . . . . . . . . . . . 9.0 3,696 4,101
5,426,609 Charter Communications, Inc. . . . . . . . . . . . . . . . . 2.6 944 2,632
400,000,000 The Coca-Cola Company . . . . . . . . . . . . . . . . . . . . 9.3 1,299 22,140
70,910,456 Delta Air Lines, Inc. ........................ 11.0 3,125 4,147
12,435,814 The Goldman Sachs Group, Inc. . . . . . . . . . . . . . . . 3.5 890 2,859
60,059,932 JPMorgan Chase & Co. . . . . . . . . . . . . . . . . . . . . . . 1.9 6,556 8,372
24,669,778 Moody’s Corporation ....................... 13.1 248 5,857
46,692,713 Southwest Airlines Co. . . . . . . . . . . . . . . . . . . . . . . 9.0 1,940 2,520
21,938,642 United Continental Holdings Inc. . . . . . . . . . . . . . . 8.7 1,195 1,933
149,497,786 U.S. Bancorp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.7 5,709 8,864
10,239,160 Visa Inc. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 0.6 349 1,924
345,688,918 Wells Fargo & Company . . . . . . . . . . . . . . . . . . . . . 8.4 7,040 18,598
Others*** ................................ 28,215 38,159
Total Equity Investments Carried at Market ...... $110,340 $248,027
* Excludes shares held by pension funds of Berkshire subsidiaries.
** This is our actual purchase price and also our tax basis.
*** Includes $10 billion investment in Occidental Petroleum Corporation consisting of preferred stock and
warrants to buy common stock.
Charlie and I do not view the $248 billion detailed above as a collection of stock market wagers – dalliances
to be terminated because of downgrades by “the Street,” an earnings “miss,” expected Federal Reserve actions,
possible political developments, forecasts by economists or whatever else might be the subject du jour.
What we see in our holdings, rather, is an assembly of companies that we partly own and that, on a weighted
basis, are earning more than 20% on the net tangible equity capital required to run their businesses. These companies,
also, earn their profits without employing excessive levels of debt.
Returns of that order by large, established and understandable businesses are remarkable under any
circumstances. They are truly mind-blowing when compared to the returns that many investors have accepted on
bonds over the last decade – 21⁄2% or even less on 30-year U.S. Treasury bonds, for example.
10
Forecasting interest rates has never been our game, and Charlie and I have no idea what rates will average
over the next year, or ten or thirty years. Our perhaps jaundiced view is that the pundits who opine on these subjects
reveal, by that very behavior, far more about themselves than they reveal about the future.
What we can say is that if something close to current rates should prevail over the coming decades and if
corporate tax rates also remain near the low level businesses now enjoy, it is almost certain that equities will over time
perform far better than long-term, fixed-rate debt instruments.
That rosy prediction comes with a warning: Anything can happen to stock prices tomorrow. Occasionally,
there will be major drops in the market, perhaps of 50% magnitude or even greater. But the combination of The
American Tailwind, about which I wrote last year, and the compounding wonders described by Mr. Smith, will make
equities the much better long-term choice for the individual who does not use borrowed money and who can control
his or her emotions. Others? Beware!"""


profile = service.profile(text, accept="application/json").get_result()

warnings = len(profile['warnings'])

print(f"Warnings: {warnings}")

# print(json.dumps(profile, indent=4))
print(json.dumps(profile["needs"], indent=4))
