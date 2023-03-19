#
# https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started

# First install RTOOLS42 following instructions here:
# https://github.com/stan-dev/rstan/wiki/Configuring-C---Toolchain-for-Windows

Sys.getenv("BINPREF")
# If output looks like this: [1] ""
# no previous versions of RTools detected

remove.packages("rstan")
if (file.exists(".RData")) file.remove(".RData")

# install.packages("rstan", repos = "https://cloud.r-project.org/", dependencies = TRUE)

# unreleased version of RSTAN that is compatible with RTools4.2
install.packages("StanHeaders", repos = c("https://mc-stan.org/r-packages/", getOption("repos")))
install.packages("rstan", repos = c("https://mc-stan.org/r-packages/", getOption("repos")))

# Verify installation
example(stan_model, package = "rstan", run.dontrun = TRUE)
