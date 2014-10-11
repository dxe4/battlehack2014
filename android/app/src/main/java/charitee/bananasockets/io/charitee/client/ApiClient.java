package charitee.bananasockets.io.charitee.client;

import charitee.bananasockets.io.charitee.models.GeolocatedRequest;
import retrofit.Callback;
import retrofit.client.Response;
import retrofit.http.Body;
import retrofit.http.POST;

/**
 * Created by codi on 11/10/2014.
 */
public interface ApiClient {

	@POST("/create_request")
	void createRequest(@Body GeolocatedRequest r, Callback<Response> cb);

}
