package charitee.bananasockets.io.charitee.activities;

import android.app.Activity;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.androidannotations.annotations.EActivity;

import charitee.bananasockets.io.charitee.R;
import charitee.bananasockets.io.charitee.client.ApiClient;
import charitee.bananasockets.io.charitee.models.GeolocatedRequest;
import retrofit.Callback;
import retrofit.RestAdapter;
import retrofit.RetrofitError;
import retrofit.client.Response;
import retrofit.converter.GsonConverter;

/**
 * Created by codi on 11/10/2014.
 */
@EActivity(R.layout.activity_request) public class Request extends Activity {

	private void sendRequest() {
		Gson gson = new GsonBuilder().create();

		RestAdapter restAdapter = new RestAdapter.Builder()
				.setEndpoint("http://54.76.173.204:8000")
				.setLogLevel(RestAdapter.LogLevel.FULL)
				.setConverter(new GsonConverter(gson))
				.build();

		ApiClient cli = restAdapter.create(ApiClient.class);

		GeolocatedRequest r = new GeolocatedRequest();
		r.setUserId("");

		cli.createRequest(r, new Callback(){

			@Override
			public void success(Object o, Response response) {
				Toast.makeText(Request.this, "Successfully created request", Toast.LENGTH_SHORT);
			}

			@Override
			public void failure(RetrofitError error) {

			}
		});
	}
}
