# Use the official Elixir image from Docker Hub
FROM elixir:latest

# Set environment variables
ENV MIX_ENV=prod \
    LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

# Install Node.js (required for Phoenix asset building)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Hex and Rebar (Elixir build tools)
RUN mix local.hex --force && \
    mix local.rebar --force

# Install Phoenix globally
RUN mix archive.install hex phx_new --force

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies and compile the application
# RUN mix deps.get
# RUN mix deps.get && \
#     mix deps.compile && \
#     mix compile

# Expose the port the application will run on
EXPOSE 4000

# Start the application
# CMD ["mix", "phx.server"]