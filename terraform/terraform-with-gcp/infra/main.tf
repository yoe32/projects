# Bucket to store website

resource "google_storage_bucket" "website" {
    provider = google
    name = "example-website-by-yoe32"
    location = "US"
}

# Make the object publicy accesible
resource "google_storage_object_access_control" "public_rule" {
  object = google_storage_bucket_object.static_site_src.output_name
  bucket = google_storage_bucket.website.name
  role = "READER"
  entity = "allUsers"
}

# Upload the html file to the bucket
resource "google_storage_bucket_object" "static_site_src"{
    name = "index.html"
    source =  "../website/index.html"
    bucket = google_storage_bucket.website.name
}


