# Dictionaries and lookups with R?
countries = c('spain', 'france', 'germany', 'norway')
capitals = c('madrid', 'paris', 'berlin', 'oslo')

# Index Germany
?match()

# ?distinct() for dataframes
# Get the index of the first matching element
match("germany", countries)

# Get all indices of all matching elements
which(countries %in% c("germany"))

ind_ger <- match("germany", countries)

capitals[ind_ger]

madrid <- list(
    madrid = c("Salamanca", "Malasana", "Chamberi", "Retiro")
)

europe['france']

europe <- list(
    spain = madrid,
    france = "paris"
)

europe['spain']$spain$madrid

europe['france']


# Lookup tables ----

x <- c("WA", "WA", "NSW", "VIC", "TAS", "NT", "SA", "QLD")

lookup <- c(WA = "Western Australia",
            NSW = "New South Wales",
            VIC = "Victoria",
            TAS = "Tasmania",
            NT = "Northern Territory",
            SA = "South Australia",
            QLD = "Queensland")

unname(lookup[x])

get_value <- function(keys) {

    lookup <- c(WA = "Western Australia",
                NSW = "New South Wales",
                VIC = "Victoria",
                TAS = "Tasmania",
                NT = "Northern Territory",
                SA = "South Australia",
                QLD = "Queensland")

    values <- unname(lookup[keys])

}

print(get_value(keys = x))

tibble(Abbreviation = x) %>%
    mutate(State = get_value(Abbreviation))


cities <- tribble(
    ~Abbreviation, ~City,
    "WA", "Perth",
    "NSW", "Sydney",
    "QLD", "Brisbane",
    "NT", "Darwin",
    "SA", "Adelaide",
    "TAS", "Tasmania",
    "VIC", "Melbourne",
    "NSW", "Newcastle",
    "QLD", "Townsville",
    "WA", "Bunbury",
    "WA", "Manjimup",
    "NT", "Alice Springs",
    "TAS", "Tasmania",
    "VIC", "Melbourne",
    "NSW", "Newcastle",
    "QLD", "Townsville",
    "WA", "Bunbury",
    "SA", "Adelaide")

cities

if (require("tibble")) {
    as_tibble(vec_group_loc(cities[c("Abbreviation", "City")]))
} %>% tidyr::unnest(loc)

vec_group_rle(cities$Abbreviation)
vec_group_loc(cities$Abbreviation)
vec_group_id(cities$Abbreviation)

?interaction()

# See also adv-r.had.co.nz Matching and Merging

interaction(cities$Abbreviation, cities$City)

cities %>%
    mutate(blend = paste(Abbreviation, City, sep = "_"),
           id = vctrs::vec_group_id(Abbreviation, City))
?vctrs::vec_group_id()

library(vctrs)
purrr <- c("p", "u", "r", "r", "r")
vec_group_id(purrr)
vec_group_rle(purrr)

groups <- mtcars[c("vs", "am")]
vec_group_id(groups)

group_rle <- vec_group_rle(groups)
group_rle

# Access fields with `field()`
field(group_rle, "group")
field(group_rle, "length")

# `vec_group_id()` is equivalent to
vec_match(groups, vec_unique(groups))

vec_group_loc(mtcars$vs)
vec_group_loc(mtcars[c("vs", "am")])

?unnest()

# Find locations of matching groups in tibble
if (require("tibble")) {
    as_tibble(vec_group_loc(mtcars[c("vs", "am")]))
} %>% tidyr::unnest(loc)

mtcars
