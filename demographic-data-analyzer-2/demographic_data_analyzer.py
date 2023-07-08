import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    races=df['race']
    race_value=races.value_counts()
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = race_value

    age_men=df[['age','sex']]
    # print(age_men)
    age_men=age_men[age_men['sex']=='Male']
    
    # What is the average age of men?
    average_age_men = round(age_men['age'].mean(),1)

    bachelors=df['education']=='Bachelors'
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((bachelors.sum()/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    literate=df[['education','salary']]
    # print(literate)
    higher_education=literate[(literate['education']=='Bachelors')|(literate['education']=='Masters')|(literate['education']=='Doctorate')]
    lower_education = literate[(literate['education']!='Bachelors')&(literate['education']!='Masters')&(literate['education']!='Doctorate')]

  
    hihisal=higher_education['salary']=='>50K'
    lohisal=lower_education['salary']=='>50K'
    # print(hihisal.sum())
    # percentage with salary >50K
    higher_education_rich = round((hihisal.sum()/len(higher_education))*100,1)
    lower_education_rich = round((lohisal.sum()/len(lower_education))*100,1)
    # print("low",lower_education)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minworker=df[['hours-per-week','salary']]
    minworker=minworker[minworker['hours-per-week']==min_work_hours]

    smartpeople=minworker[minworker['salary']=='>50K']
    num_min_workers = len(minworker)
    rich_percentage = round((len(smartpeople)/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?

    cuntrysal=df[['native-country','salary']]
    country_salary_counts = cuntrysal.groupby(['native-country', 'salary']).size().unstack(fill_value=0)
  
    country_salary_counts['Percentage'] = (country_salary_counts['>50K'] / country_salary_counts.sum(axis=1)) * 100

    
       
    # print(country_salary_counts)     

    highest_earning_country =country_salary_counts['Percentage'].idxmax()
    highest_earning_country_percentage = round(country_salary_counts['Percentage'].max(),1)

    # Identify the most popular occupation for those who earn >50K in India.

    peopleoccu=df[['occupation','native-country','salary']]
    indiaocc=peopleoccu[(peopleoccu['native-country']=='India')&(peopleoccu['salary']=='>50K')]
    top_IN_occupation = indiaocc['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
