package charitee.bananasockets.io.charitee.activities;

import android.app.Activity;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.androidannotations.annotations.Background;
import org.androidannotations.annotations.Click;
import org.androidannotations.annotations.EActivity;
import org.androidannotations.annotations.ViewById;

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

	@ViewById
	protected EditText requestFromUser;

	@ViewById
	protected EditText requestMessage;

	@ViewById
	Button btnSend;

	@Background protected void sendRequest() {
		Gson gson = new GsonBuilder().create();

		RestAdapter restAdapter = new RestAdapter.Builder()
				.setEndpoint("http://54.76.173.204:8000")
				.setLogLevel(RestAdapter.LogLevel.FULL)
				.setConverter(new GsonConverter(gson))
				.build();

		ApiClient cli = restAdapter.create(ApiClient.class);

		GeolocatedRequest r = new GeolocatedRequest();
		r.setFromUser("");

		cli.createRequest(r, new Callback<Response>(){

			@Override
			public void success(Response r, Response response) {
				Log.d("Request", String.format("Request success : %s", r.toString()));
			}

			@Override
			public void failure(RetrofitError error) {
				Log.d("Request", "Request error");
			}
		});

	}

	@Click public void btnSend() {
		sendRequest();
	}
}
