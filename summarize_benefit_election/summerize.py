import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prod_review = """
1.9.1 Claimant’s reports - continuing claim
A claimant may request an exemption from completing claimant’s reports every two weeks when in receipt of the following types of benefits:
Claimants who opt out of completing claimant’s reports are still responsible for  reporting any situations that may affect entitlement to these benefits, to the  Commission, such as, receiving vacation pay (EI  Regulation 26.1(2)(c)).
Claimants wishing to be exempt from completing claimant’s reports must complete a declaration to cover all of the weeks payable. The single declaration includes an agreement that the claimant is not working, and that they will report any work they may perform, earnings they may receive, or any other condition that may affect entitlement to benefits. Claimants have until the end of their benefit period to report any such conditions.
At the end of the exemption period, a notice is sent to the claimant reminding them to report any earnings or other conditions that might affect benefits.
Commission policy provides an additional grace period of six weeks following the end of the benefit period or last payment, to provide this information. No penalty will be imposed on a claimant who is exempt from completing reports, if new information is submitted or discovered within six weeks of the last payment issued. In these cases, the Commission will only establish an overpayment.
1.9.1.1 Exception reporting
In very specific situations, a claimant’s report may be filed before the end of  the period it covers, and an advance payment may be made. This may happen at  Christmas time or where unemployment is the result of a disaster at the  claimant's place of work (EI Regulation 28).
1.9.1.2 Early reporting
Claimant’s reports should be filed as soon as they are due. Claimant’s reports not completed within three weeks of the date on which they were due could result in a disentitlement from benefits.
When a claimant stops submitting claimant’s reports for a period of four consecutive weeks or more, the claim becomes inactive, and no further benefits are paid unless an application to “renew” the claim is completed and submitted.
1.9.1.3 Timeframes for reporting
A renewal claim is an application for benefits received to renew (reactivate) a claim that has already been established, but has not yet terminated (still in effect). For example, where a claimant, for any number of reasons, stops claiming benefits for a period of time, and wishes to resume benefits, they must submit an application to renew or reactivate that claim.
An administrative policy has been adopted whereby, once an application for benefits is received, all claims with weeks of benefits still payable are automatically renewed. At the beginning of the online application process, claimants who have an existing benefit period with weeks of benefits still payable are presented with a message advising them their claim will be renewed.
This message also advises the claimant:
Claimants who proceed with the renewal of their claims and later decide they wanted a new claim, have the right to request a review of that decision.
A request to review the renewal of a previous benefit period will be allowed without question, if it is submitted within 30 days from the date the renewal was finalized.  Requests submitted after that period will be accepted if the claimant can show good cause existed for their delay in making the request.
"""

prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
