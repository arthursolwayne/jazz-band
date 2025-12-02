
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # D - C - Eb - F (chromatic approach to Dm)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
    # D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    # D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=63, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),
    # D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
    # D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=63, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=65, start=6.25, end=6.5),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on 1 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    # Rest on 1
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    # Dm7 on 3 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),
    # Rest on 3
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),
    # Dm7 on 5 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),
    # Rest on 5
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),
    # Dm7 on 7 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    # Rest on 7
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    # Dm7 on 9 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, short motif, make it sing
sax_notes = [
    # First bar: 3 notes, leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # A (Dm7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.625, end=1.75),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # B (chromatic)
    # Second bar: repeat the first two notes and resolve
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),
    # Third bar: variation with a half-step down
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),  # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0),    # A#
    # Fourth bar: resolve back to Dm
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),   # B
    # Repeat the motif
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),
    # Final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
]
sax.notes.extend(sax_notes)

# Drums: Continue with same pattern through bars 2-4
for bar in range(2, 5):  # bars 2, 3, 4
    start_time = 1.5 + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hi-hats on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1875)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.1875, end=start_time + 0.375)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.5625)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.5625, end=start_time + 0.75)
    hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 0.9375)
    hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.9375, end=start_time + 1.125)
    hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.3125)
    hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.3125, end=start_time + 1.5)
    # Add all notes to drums
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_sax_intro.mid")
