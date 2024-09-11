FROM golang:1.20-bookworm AS build
WORKDIR /build
COPY go.mod go.sum ./
RUN go mod download
COPY . .
ENV CGO_ENABLED=0
RUN go build -o ./dbq


log.Printf("shutting down")
ctx, cancel := context.WithTimeout(context.Background(), time.Second)
defer cancel()
if err := srv.Shutdown(ctx); err != nil {
    log.Printf("error: shutdown - %s", err)
}