package charitee.bananasockets.io.charitee.models;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;

import java.lang.reflect.Type;
import java.util.Date;

/**
 * GeolocatedRequest
 * Model referring to a geolocated user request, either a question or a media sharing request
 */
public class GeolocatedRequest implements JsonSerializer {

	@Override
	public JsonElement serialize(Object src, Type typeOfSrc, JsonSerializationContext context) {
		final JsonObject obj = new JsonObject();

		obj.addProperty("from_user", this.fromUser);
		obj.addProperty("message", this.message);
		obj.addProperty("lat", 0.5);
		obj.addProperty("long", 0.5);
		obj.addProperty("expires", 1000911);

		return obj;
	}

	public enum RequestType { QUESTION, MEDIA_SHARING };

	private String message;

	private String fromUser;

	private Date expiresAt;

	private RequestType requestType;

	private LatLong location;

	public GeolocatedRequest(){

	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public String getFromUser() {
		return fromUser;
	}

	public void setFromUser(String fromUser) {
		this.fromUser = fromUser;
	}

	public Date getExpiresAt() {
		return expiresAt;
	}

	public void setExpiresAt(Date expiresAt) {
		this.expiresAt = expiresAt;
	}

	public RequestType getRequestType() {
		return requestType;
	}

	public void setRequestType(RequestType requestType) {
		this.requestType = requestType;
	}

	public LatLong getLocation() {
		return location;
	}

	public void setLocation(LatLong location) {
		this.location = location;
	}
}
