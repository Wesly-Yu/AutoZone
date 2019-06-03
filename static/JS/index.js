var _createClass = function () {function defineProperties(target, props) {for (var i = 0; i < props.length; i++) {var descriptor = props[i];descriptor.enumerable = descriptor.enumerable || false;descriptor.configurable = true;if ("value" in descriptor) descriptor.writable = true;Object.defineProperty(target, descriptor.key, descriptor);}}return function (Constructor, protoProps, staticProps) {if (protoProps) defineProperties(Constructor.prototype, protoProps);if (staticProps) defineProperties(Constructor, staticProps);return Constructor;};}();function _classCallCheck(instance, Constructor) {if (!(instance instanceof Constructor)) {throw new TypeError("Cannot call a class as a function");}}var Line = function () {
  function Line(x, y, size, color, speed, seed, amplitude) {_classCallCheck(this, Line);
    this.x = x;
    this.y = y;
    this.size = size;
    this.color = color;
    this.speed = speed;
    this.seed = seed;
    this.amplitude = amplitude;
    this.i = this.seed;
  }_createClass(Line, [{ key: 'update', value: function update()

    {
      this.y -= this.speed;
      this.i += this.seed;
    } }, { key: 'draw', value: function draw(

    canvas) {
      var x = this.x + Math.sin(this.i) * this.amplitude;

      canvas.ctx.beginPath();
      canvas.ctx.fillStyle = this.color;
      canvas.ctx.shadowColor = this.color;
      canvas.ctx.shadowBlur = 5;
      canvas.ctx.arc(x, this.y, this.size, 0, 2 * Math.PI);
      canvas.ctx.fill();
      canvas.ctx.closePath();
    } }]);return Line;}();var


Canvas = function () {
  function Canvas(ctx, w, h) {_classCallCheck(this, Canvas);
    this.ctx = ctx;
    this.width = w;
    this.height = h;
    this.scale = 1.0;
    this.lines = [];
  }_createClass(Canvas, [{ key: 'pushParticle', value: function pushParticle()

    {
      var x = Math.random() * this.width;
      var y = this.height + Math.random() * 250;
      var size = 1 + Math.random();

      var g = Math.floor(150 + Math.random() * 50);
      var b = Math.floor(150 + Math.random() * 50);
      var color = 'rgba(120,' + g + ',' + b + ',0.7)';

      var speed = 2 + Math.random() * 1.5;
      var seed = Math.random() / 20;
      var amp = Math.random() * 15;

      this.lines.push(new Line(x, y, size, color, speed, seed, amp));
    } }, { key: 'start', value: function start()

    {
      for (var i = 0; i < 100; i++) {
        this.pushParticle();
      }
    } }, { key: 'update', value: function update()

    {
      for (var i = 0; i < this.lines.length; i++) {
        var line = this.lines[i];

        line.update();
      }

      this.lines = this.lines.filter(function (line) {
        return line.y > -2;
      });

      var toAdd = 100 - this.lines.length;

      if (toAdd === 0) {return;}

      for (var _i = 0; _i < toAdd; _i++) {
        this.pushParticle();
      }
    } }, { key: 'draw', value: function draw()

    {
      this.ctx.shadowColor = '#000';
      this.ctx.shadowBlur = 0;
      this.ctx.globalCompositeOperation = 'source-over';
      this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
      this.ctx.fillRect(0, 0, this.width, this.height);
      this.ctx.globalCompositeOperation = 'lighter';

      for (var i = 0; i < this.lines.length; i++) {
        var line = this.lines[i];

        line.draw(this);
      }
    } }]);return Canvas;}();


(function (_) {
  var canvasElement = document.getElementById('canvas'),
  ctx = canvasElement.getContext('2d'),
  canvas = new Canvas(ctx);

  var w = canvasElement.width = window.innerWidth,
  h = canvasElement.height = window.innerHeight,
  density = 1;

  function setup() {
    window.addEventListener('resize', resize);

    density = window.devicePixelRatio != undefined ? window.devicePixelRatio : 1.0;

    canvasElement.width = w * density;
    canvasElement.height = h * density;

    canvas.width = w;
    canvas.height = h;
    canvas.scale = density;

    ctx.scale(density, density);

    canvas.start();

    draw();
  }

  function draw() {
    canvas.update();
    canvas.draw();

    window.requestAnimationFrame(draw);
  }

  function resize() {
    w = canvasElement.width = window.innerWidth;
    h = canvasElement.height = window.innerHeight;

    canvasElement.width = w * density;
    canvasElement.height = h * density;

    canvas.width = w;
    canvas.height = h;

    ctx.scale(density, density);
  }

  setup();
})();