export interface BillingDetails {
    country: string
    firstname: string
    lastname: string
    company_name?: string
    street_address: string
    apartment_or_suite?: string
    state_or_country: string
    posta_or_zip: string
    email: string
    phone: string
    order_notes: string
    total_price: number
}


export interface Country {
    value: number;
    text: string;
  }