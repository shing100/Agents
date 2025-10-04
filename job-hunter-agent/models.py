from typing import List, Union
from pydantic import BaseModel
from datetime import date


class Job(BaseModel):
    """채용 공고의 상세 정보를 담는 모델"""
    job_title: str
    company_name: str
    job_location: str
    is_remote_friendly: Union[bool, None] = None
    employment_type: Union[str, None] = None
    compensation: Union[str, None] = None
    job_posting_url: str
    job_summary: str

    key_qualifications: Union[List[str], None] = None
    job_responsibilities: Union[List[str], None] = None
    date_listed: Union[date, None] = None
    required_technologies: Union[List[str], None] = None
    core_keywords: Union[List[str], None] = None

    role_seniority_level: Union[str, None] = None
    years_of_experience_required: Union[str, None] = None
    minimum_education: Union[str, None] = None
    job_benefits: Union[List[str], None] = None
    includes_equity: Union[bool, None] = None
    offers_visa_sponsorship: Union[bool, None] = None
    hiring_company_size: Union[str, None] = None
    hiring_industry: Union[str, None] = None
    source_listing_url: Union[str, None] = None
    full_raw_job_description: Union[str, None] = None


class JobList(BaseModel):
    """Job 모델의 리스트를 담는 모델"""
    jobs: List[Job]


class RankedJob(BaseModel):
    """순위가 매겨진 채용 공고 정보를 담는 모델"""
    job: Job
    match_score: int
    reason: str


class RankedJobList(BaseModel):
    """순위가 매겨진 채용 공고의 리스트를 담는 모델"""
    ranked_jobs: List[RankedJob]


class ChosenJob(BaseModel):
    """최종 선택된 채용 공고 정보를 담는 모델"""
    job: Job
    selected: bool
    reason: str