from models.responses import AddComicToLayawayResponse, ErrorResponse

add_to_layaway_response = {
    200: {"model": AddComicToLayawayResponse},
    409: {"model": ErrorResponse}
}