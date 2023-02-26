
library(tidyverse)
library(GGally)

df = read_csv("data/vehicles.csv", show_col_types = FALSE)

df %>% glimpse()

# Get 6 most common classes
count_class <- df %>% count(VClass, sort = TRUE)
car_class <- count_class %>%  slice_head(n = 6) %>% pull(VClass)
car_class

car_class_df <- df %>%
    filter(VClass %in% car_class & (year >= 2015)) %>%
    mutate(transmission = case_when(
        str_detect(str_to_lower(trany), "manual") ~ "Manual",
        str_detect(str_to_lower(trany), "auto") ~ "Automatic",
        TRUE ~ "Other")) %>%
    select(transmission, cylinders, fuelCost08, co2, VClass, displ)

car_class_df %>% slice_head(n = 5)

ggpairs(data = car_class_df %>% select(-c(VClass, fuelCost08)),
        mapping = aes_string(color = "transmission"),
        # lower = "blank",
        legend = 1,
        diag = list(continuous = wrap("densityDiag", alpha = 0.3)),
        progress = FALSE,
        title = "US Vehicle CO2 Relationships (MFG YR 2015-22)") +
    theme(legend.position = "bottom") +
    theme_tq()

# Other examples:
ggpairs(data = car_class_df %>% select(-c(VClass, transmission)),
        # mapping = aes_string(color = "transmission"),
        # lower = "blank",
        # legend = 1,
        diag = list(continuous = wrap("densityDiag", alpha = 0.3)),
        progress = FALSE,
        title = "US Vehicle Fuel Economy Relationships (MFG YR 2015-22)") +
    # theme(legend.position = "bottom") +
    theme_tq()

ggpairs(data = car_class_df %>% select(-c(VClass)),
        mapping = aes_string(color = "transmission"),
        # lower = "blank",
        legend = 1,
        diag = list(continuous = wrap("densityDiag", alpha = 0.3)),
        progress = FALSE,
        title = "US Vehicle CO2 Relationships (MFG YR 2015-22)") +
    theme(legend.position = "bottom") +
    theme_tq()
