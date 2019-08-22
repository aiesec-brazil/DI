
query_01 ="""{
  allOpportunityApplication 

  
  {
      paging {
      total_pages
    }
    data {
      id
      status
      created_at
      current_status
			date_approved
      
    }
    }
}
  """