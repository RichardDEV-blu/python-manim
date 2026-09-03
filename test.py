from manim import *
import numpy as np

# ============================================================
# VERTICAL 9:16 — 1080p
# ============================================================

config.frame_height = 8.0
config.frame_width = 4.5

config.pixel_width = 1080
config.pixel_height = 1920

config.background_color = "#000000"
config.frame_rate = 60

# ============================================================
# COLORS
# ============================================================

COLOR_TEXT = "#F5F5F7"
COLOR_WALKING = "#FFFFFF"
COLOR_WALK = "#F06A6A"
COLOR_MINUS_WALK = "#FF8A8A"
COLOR_SWIM = "#58C4DD"
COLOR_RESULT = "#B57EF7"
COLOR_GRID = "#2B2F3A"
COLOR_OPERATOR = "#8E95A8"

# ============================================================
# TYPOGRAPHY
# ============================================================

FONT = "Montserrat"

# ============================================================
# GLOBAL TIMING
# ============================================================

# 1.35 = 35% slower
#
# Example:
# 2.0 sec -> 2.70 sec
# 1.5 sec -> 2.025 sec
#
# Change ONLY this value if you want another speed.

SPEED_FACTOR = 1.35

# Ambient camera rotation also becomes 35% slower.
AMBIENT_ROTATION_RATE = 0.08 / SPEED_FACTOR

# ============================================================
# SAFE DIMENSIONS
# ============================================================

SAFE_W = 4.0
GRID_W = 3.7
GRID_H = 4.8

# ============================================================
# UI POSITIONS
# ============================================================

CAPTION_Y = -1.80
EQUATION_Y = -2.80

# ============================================================
# 3D SCENE SHIFT
# ============================================================

SCENE_SHIFT = np.array([0.28, 0.0, 0.0])


# ============================================================
# SCENE
# ============================================================

class WalkingSwimmingVertical(ThreeDScene):

    def construct(self):

        self.camera.background_color = "#000000"

        # ====================================================
        # CAMERA
        # ====================================================

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            distance=10
        )

        # ====================================================
        # GRID
        # ====================================================

        grid = NumberPlane(
            x_range=[-2.2, 2.2, 1],
            y_range=[-2.8, 2.8, 1],
            x_length=GRID_W,
            y_length=GRID_H,

            background_line_style={
                "stroke_color": COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.45,
            },

            axis_config={
                "stroke_color": "#555B70",
                "stroke_opacity": 0.4,
            }
        )

        grid.shift(SCENE_SHIFT)

        self.play(
            Create(grid),
            run_time=1.9 * SPEED_FACTOR
        )

        self.begin_ambient_camera_rotation(
            rate=AMBIENT_ROTATION_RATE
        )

        # ====================================================
        # HEADER
        # ====================================================

        title = Text(
            "EMBEDDING ALGEBRA",
            font=FONT,
            font_size=28,
            color=COLOR_TEXT,
            weight=BOLD
        )

        # No artificial letter spacing.
        # Montserrat handles its own kerning.

        if title.width > SAFE_W:
            title.scale(
                SAFE_W / title.width
            )

        subtitle = Text(
            "LINGUISTIC RELATIONS AS VECTORS",
            font=FONT,
            font_size=14,
            color="#8E95A8",
            weight=BOLD
        )

        if subtitle.width > SAFE_W:
            subtitle.scale(
                SAFE_W / subtitle.width
            )

        header = VGroup(
            title,
            subtitle
        ).arrange(
            DOWN,
            buff=0.08
        )

        header.to_edge(
            UP,
            buff=0.25
        )

        self.add_fixed_in_frame_mobjects(
            header
        )

        self.play(
            FadeIn(header),
            run_time=1.1 * SPEED_FACTOR
        )

        # ====================================================
        # EQUATION
        # ====================================================

        eq_walking = Text(
            "WALKING",
            font=FONT,
            font_size=14,
            color=COLOR_WALKING,
            weight=BOLD
        )

        eq_minus = Text(
            "−",
            font=FONT,
            font_size=16,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_walk = Text(
            "WALK",
            font=FONT,
            font_size=14,
            color=COLOR_WALK,
            weight=BOLD
        )

        eq_plus = Text(
            "+",
            font=FONT,
            font_size=16,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_swim = Text(
            "SWIM",
            font=FONT,
            font_size=14,
            color=COLOR_SWIM,
            weight=BOLD
        )

        eq_approx = Text(
            "≈",
            font=FONT,
            font_size=16,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_swimming = Text(
            "SWIMMING",
            font=FONT,
            font_size=14,
            color=COLOR_RESULT,
            weight=BOLD
        )

        full_equation = VGroup(
            eq_walking,
            eq_minus,
            eq_walk,
            eq_plus,
            eq_swim,
            eq_approx,
            eq_swimming
        )

        full_equation.arrange(
            RIGHT,
            buff=0.12
        )

        full_equation.move_to(
            np.array([
                0,
                EQUATION_Y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            full_equation
        )

        # Initially invisible

        for item in full_equation:
            item.set_opacity(0)

        # ====================================================
        # SEMANTIC VECTORS
        # ====================================================

        origin = (
            np.array([
                0.0,
                0.0,
                0.0
            ])
            + SCENE_SHIFT
        )

        v_walking = (
            np.array([
                -1.35,
                -1.05,
                0.48
            ])
            + SCENE_SHIFT
        )

        v_walk = (
            np.array([
                -0.32,
                0.72,
                0.30
            ])
            + SCENE_SHIFT
        )

        v_swim = (
            np.array([
                1.05,
                0.38,
                0.30
            ])
            + SCENE_SHIFT
        )

        p_after_walking = v_walking

        p_after_subtraction = (
            v_walking
            - (v_walk - SCENE_SHIFT)
        )

        p_result = (
            v_walking
            - (v_walk - SCENE_SHIFT)
            + (v_swim - SCENE_SHIFT)
        )

        # ====================================================
        # VECTOR HELPER
        # ====================================================

        def make_vector(
            start,
            end,
            color,
            thickness=0.035
        ):

            return Arrow3D(
                start=start,
                end=end,
                color=color,
                thickness=thickness,
                height=0.22,
                base_radius=0.065
            )

        # ====================================================
        # BASE VECTORS
        # ====================================================

        walking_vector = make_vector(
            origin,
            v_walking,
            COLOR_WALKING,
            thickness=0.040
        )

        walk_vector_origin = make_vector(
            origin,
            v_walk,
            COLOR_WALK
        )

        swim_vector_origin = make_vector(
            origin,
            v_swim,
            COLOR_SWIM
        )

        # ====================================================
        # CAPTION HELPER
        # ====================================================

        def make_caption(
            text,
            color,
            font=FONT,
            font_size=16,
            max_width=SAFE_W
        ):

            if "Chain the vector to the tip of the previous one" in text:

                lines = [
                    "Chain the vector",
                    "to the tip of the previous one"
                ]

                fs = 15

            elif "Add SWIM using the tip-to-tail rule" in text:

                lines = [
                    "Add SWIM using",
                    "the tip-to-tail rule"
                ]

                fs = 15

            else:

                lines = [text]
                fs = font_size

            group = VGroup()

            for line in lines:

                t = Text(
                    line,
                    font=font,
                    font_size=fs,
                    color=color,
                    weight=BOLD
                )

                # Natural Montserrat kerning.
                # No set_letter_spacing().

                if t.width > max_width:
                    t.scale(
                        max_width / t.width
                    )

                group.add(t)

            group.arrange(
                DOWN,
                buff=0.05
            )

            group.move_to(
                np.array([
                    0,
                    CAPTION_Y,
                    0
                ])
            )

            return group

        # ====================================================
        # INITIAL CAPTION
        # ====================================================

        caption = make_caption(
            "Each word can be represented as a vector",
            "#AAB0BF",
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            caption
        )

        # ====================================================
        # STEP 1 — WALKING
        # ====================================================

        self.play(
            GrowFromPoint(
                walking_vector,
                origin
            ),

            FadeIn(
                eq_walking,
                shift=UP * 0.08
            ),

            FadeIn(caption),

            run_time=2.1 * SPEED_FACTOR
        )

        self.wait(
            1.6 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 2 — WALK
        # ====================================================

        walk_caption = make_caption(
            "The WALK vector represents the base verb",
            COLOR_WALK,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            walk_caption
        )

        self.play(
            FadeOut(caption),

            GrowFromPoint(
                walk_vector_origin,
                origin
            ),

            FadeIn(
                eq_minus,
                shift=UP * 0.05
            ),

            FadeIn(
                eq_walk,
                shift=UP * 0.05
            ),

            FadeIn(walk_caption),

            run_time=1.6 * SPEED_FACTOR
        )

        self.wait(
            1.3 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 3 — INVERT WALK
        # ====================================================

        v_minus_walk = (
            origin
            - (v_walk - SCENE_SHIFT)
        )

        minus_walk_origin = make_vector(
            origin,
            v_minus_walk,
            COLOR_MINUS_WALK
        )

        subtraction_caption = make_caption(
            "Subtracting WALK reverses its direction",
            COLOR_MINUS_WALK,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            subtraction_caption
        )

        self.play(
            FadeOut(walk_caption),

            Transform(
                walk_vector_origin,
                minus_walk_origin
            ),

            FadeIn(subtraction_caption),

            run_time=1.4 * SPEED_FACTOR
        )

        self.wait(
            1.1 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 4 — TRANSLATE -WALK
        # ====================================================

        minus_walk_chain = make_vector(
            p_after_walking,
            p_after_subtraction,
            COLOR_MINUS_WALK
        )

        chain_caption = make_caption(
            "Chain the vector to the tip of the previous one",
            "#AAB0BF",
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            chain_caption
        )

        self.play(
            FadeOut(walk_vector_origin),

            GrowFromPoint(
                minus_walk_chain,
                p_after_walking
            ),

            FadeOut(subtraction_caption),

            FadeIn(chain_caption),

            run_time=1.9 * SPEED_FACTOR
        )

        self.wait(
            1.6 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 5 — SWIM
        # ====================================================

        swim_caption = make_caption(
            "SWIM also has its own vector",
            COLOR_SWIM,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            swim_caption
        )

        self.play(
            FadeOut(chain_caption),

            GrowFromPoint(
                swim_vector_origin,
                origin
            ),

            FadeIn(
                eq_plus,
                shift=UP * 0.05
            ),

            FadeIn(
                eq_swim,
                shift=UP * 0.05
            ),

            FadeIn(swim_caption),

            run_time=1.6 * SPEED_FACTOR
        )

        self.wait(
            1.3 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 6 — TRANSLATE SWIM
        # ====================================================

        swim_vector_chain = make_vector(
            p_after_subtraction,
            p_result,
            COLOR_SWIM
        )

        addition_caption = make_caption(
            "Add SWIM using the tip-to-tail rule",
            COLOR_SWIM,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            addition_caption
        )

        self.play(
            FadeOut(swim_caption),

            FadeOut(swim_vector_origin),

            GrowFromPoint(
                swim_vector_chain,
                p_after_subtraction
            ),

            FadeIn(addition_caption),

            run_time=1.9 * SPEED_FACTOR
        )

        self.wait(
            1.9 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 7 — RESULT VECTOR
        # ====================================================

        result_vector = make_vector(
            origin,
            p_result,
            COLOR_RESULT,
            thickness=0.043
        )

        result_caption = make_caption(
            "The operation yields a new vector",
            COLOR_RESULT,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            result_caption
        )

        self.play(
            FadeOut(addition_caption),

            GrowFromPoint(
                result_vector,
                origin
            ),

            FadeIn(result_caption),

            run_time=1.9 * SPEED_FACTOR
        )

        self.wait(
            1.3 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 8 — SWIMMING
        # ====================================================

        self.play(
            FadeIn(
                eq_approx,
                shift=UP * 0.05
            ),

            FadeIn(
                eq_swimming,
                shift=UP * 0.05
            ),

            run_time=1.1 * SPEED_FACTOR
        )

        self.wait(
            0.8 * SPEED_FACTOR
        )

        # ====================================================
        # FINAL CAPTION
        # ====================================================

        line1 = Text(
            "The result lands close to",
            font=FONT,
            font_size=15,
            color="#AAB0BF",
            weight=BOLD
        )

        line2 = Text(
            "the embedding of SWIMMING",
            font=FONT,
            font_size=15,
            color="#AAB0BF",
            weight=BOLD
        )

        # Natural kerning.
        # No letter spacing.

        for line in (line1, line2):

            if line.width > SAFE_W:
                line.scale(
                    SAFE_W / line.width
                )

        nearest_caption = VGroup(
            line1,
            line2
        ).arrange(
            DOWN,
            buff=0.05
        )

        nearest_caption.move_to(
            np.array([
                0,
                CAPTION_Y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            nearest_caption
        )

        self.play(
            FadeOut(result_caption),

            FadeIn(nearest_caption),

            run_time=0.8 * SPEED_FACTOR
        )

        # ====================================================
        # FINAL RING
        # ====================================================

        ring = Circle(
            radius=0.30,
            color=COLOR_RESULT,
            stroke_width=4
        )

        ring.rotate(
            90 * DEGREES,
            axis=RIGHT
        )

        ring.move_to(
            p_result
        )

        self.play(
            Create(ring),
            run_time=0.8 * SPEED_FACTOR
        )

        self.play(
            ring.animate
                .scale(1.8)
                .set_opacity(0),
            run_time=1.6 * SPEED_FACTOR
        )

        # ====================================================
        # END
        # ====================================================

        self.stop_ambient_camera_rotation()

        self.wait(
            3.2 * SPEED_FACTOR
        )

        # self.interactive_embed()