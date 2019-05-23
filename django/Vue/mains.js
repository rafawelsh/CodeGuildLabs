var vm = new Vue({
  el: '#app',
  data: {
    status: ''
  },
  created: function () {
    this.loadQuote();
  },
  methods: {
    loadQuote: function () {
      this.status = 'Loading...';
      var vm = this;
      axios.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
      .then(function (response) {
        vm.status = response.data[0]
      })
      .cath(function (error) {
        vm.status = 'An error occured'
      });
    }
  }
});

// var eventBus = new Vue()
//
// Vue.component('product', {
//   props: {
//     premium: {
//       type: Boolean,
//       required: true
//     }
//   },
//   template: `
//   <div class="product">
//     <div class="product-image">
//       <img :src="image">
//     </div>
//
//     <div class="product-info">
//       <h1>{{ title }}</h1>
//       <p v-if="inStock">In Stock</p>
//       <p v-else :class="{outOfStock: !inStock }">Out of Stock</p>
//       <p>Shipping: {{ shipping }}</p>
//
//       <ul>
//         <li v-for="detail in details">{{ detail }}</li>
//       </ul>
//
//       <div class="color-box"
//             v-for="(variant, index) in variants"
//             :key="variant.variantId"
//             :style="{ backgroundColor:variant.variantColor }"
//             @mouseover="updateProduct(index)"
//       >
//       </div>
//
//       <button v-on:click="addToCart"
//               :disabled="!inStock"
//               :class="{ disabledButton: !inStock }">Add to Cart</button>
//
//     </div>
//
//     <product-tabs :reviews="reviews"></product-tabs>
//
//   </div>
//   `,
//   data() {
//     return {
//       brand: 'Vue Mastery',
//       product: 'Socks',
//       selectedVariant: 0 ,
//       details: ["80% cotton", "20% polyester", "Gender-neutral"],
//       variants: [
//         {
//           variantId: 123,
//           variantColor: 'red',
//           variantImage: './pictures/sockos.jpg',
//           variantQuantity: 10
//         },
//         {
//           variantId: 456,
//           variantColor: 'blue',
//           variantImage: './pictures/sockus.jpg',
//           variantQuantity: 0
//         }
//       ],
//       reviews: []
//     }
//   },
//
//   methods: {
//     addToCart() {
//       this.$emit('add-to-cart', this.variants[this.selectedVariant].variantId)
//     },
//     updateProduct(index) {
//       this.selectedVariant = index
//       console.log(index)
//     }
//   },
//
//   computed: {
//     title() {
//       return this.brand + ' ' + this.product
//     },
//     image() {
//       return this.variants[this.selectedVariant].variantImage
//     },
//     inStock() {
//       return this.variants[this.selectedVariant].variantQuantity
//     },
//     shipping() {
//       if (this.premium){
//         return "Free"
//       }
//       return 2.00
//     }
//   },
//   mounted() {
//     eventBus.$on('review-submitted', productReview => {
//       this.reviews.push(productReview)
//     })
//   }
// })
//
// Vue.component('product-review', {
//   template: `
//   <form class="review-form" @submit.prevent="onSubmit">
//
//     <p v-if="errors.length">
//       <b>Please correct the following error(s):</b>
//       <ul>
//         <li v-for="error in errors">{{ error }}</li>
//       </ul>
//     </p>
//
//     <p>
//       <label for="name">Name:</label>
//       <input id="name" v-model="name" placeholder="name">
//     </p>
//
//     <p>
//       <label for="review">Review:</label>
//       <textarea id="review" v-model="review" required></textarea>
//     </p>
//
//     <p>
//       <label for="rating">Rating:</label>
//       <select id="rating" v-model.number="rating">
//         <option>5</option>
//         <option>4</option>
//         <option>3</option>
//         <option>2</option>
//         <option>1</option>
//       </select>
//     </p>
//
//     <p>
//       <input type="submit" value="Submit">
//     </p>
//
//   </form>
//   `,
//
//   data() {
//     return {
//       name: null,
//       review: null,
//       rating: null,
//       errors: []
//     }
//   },
//
//   methods: {
//     onSubmit() {
//       if (this.name && this.review && this.rating) {
//         let productReview = {
//           name: this.name,
//           review: this.review,
//           rating: this.rating
//         }
//         eventBus.$emit('review-submitted', productReview)
//         // this resets the review when the page refreshes.
//         this.name = null
//         this.review = null
//         this.rating = null
//       }
//       else {
//         if(!this.name) this.errors.push("Name required.")
//         if(!this.review) this.errors.push("Review required.")
//         if(!this.rating) this.errors.push("Rating required.")
//       }
//     }
//   }
// })
//
// Vue.component('product-tabs', {
//   props: {
//     reviews: {
//       type: Array,
//       required: true
//     }
//   },
//   template: `
//     <div>
//       <span class="tab"
//             :class="{ activeTab: selectedTab === tab}"
//             v-for="(tab, index) in tabs" :key="index"
//             @click="selectedTab = tab">
//             {{ tab }}</span>
//
//
//       <div v-show="selectedTab === 'Reviews'">
//
//         <p v-if="!reviews.length">There are no reviews yet.</p>
//
//         <ul v-else>
//           <li v-for="review in reviews">
//             <p>{{ review.name }}</p>
//             <p>Rating: {{ review.rating }}</p>
//             <p>{{ review.review }}</p>
//           </li>
//         </ul>
//
//       </div>
//
//       <product-review v-show="selectedTab === 'Make a Review'"></product-review>
//     </div>
//   `,
//   data() {
//     return {
//       tabs: ['Reviews', 'Make a Review'],
//       selectedTab: 'Reviews'
//     }
//   }
// })
//
// var app = new Vue({
//   el: '#app',
//   data: {
//     premium: false,
//     cart: []
//   },
//   methods: {
//     updateCart(id) {
//       this.cart.push(id)
//     }
//   }
// })
