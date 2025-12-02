
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
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.625, end=1.75), # F#
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0), # G#
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.125, end=2.25), # A#
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5), # C
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.625), # C#
    pretty_midi.Note(velocity=80, pitch=73, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=2.875), # D#
    pretty_midi.Note(velocity=80, pitch=75, start=2.875, end=3.0), # E
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0),
    # Bar 2, beat 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=2.75),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, motif (F, Bb, D, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.0625, end=2.25), # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.125), # C
    pretty_midi.Note(velocity=80, pitch=73, start=3.125, end=3.25), # C#
    pretty_midi.Note(velocity=80, pitch=74, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=75, start=3.375, end=3.5), # D#
    pretty_midi.Note(velocity=80, pitch=76, start=3.5, end=3.625), # E
    pretty_midi.Note(velocity=80, pitch=77, start=3.625, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=80, pitch=79, start=3.875, end=4.0), # G#
    pretty_midi.Note(velocity=80, pitch=80, start=4.0, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=81, start=4.125, end=4.25), # A#
    pretty_midi.Note(velocity=80, pitch=82, start=4.25, end=4.375), # B
    pretty_midi.Note(velocity=80, pitch=83, start=4.375, end=4.5), # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.5),
    # Bar 3, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.25),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=100, pitch=77, start=3.5625, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=3.9375), # G#
    pretty_midi.Note(velocity=100, pitch=81, start=3.9375, end=4.125), # A#
    pretty_midi.Note(velocity=100, pitch=83, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.3125, end=4.5), # C#
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=83, start=4.5, end=4.625), # C
    pretty_midi.Note(velocity=80, pitch=84, start=4.625, end=4.75), # C#
    pretty_midi.Note(velocity=80, pitch=85, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=86, start=4.875, end=5.0), # D#
    pretty_midi.Note(velocity=80, pitch=87, start=5.0, end=5.125), # E
    pretty_midi.Note(velocity=80, pitch=88, start=5.125, end=5.25), # F#
    pretty_midi.Note(velocity=80, pitch=89, start=5.25, end=5.375), # G
    pretty_midi.Note(velocity=80, pitch=90, start=5.375, end=5.5), # G#
    pretty_midi.Note(velocity=80, pitch=91, start=5.5, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=92, start=5.625, end=5.75), # A#
    pretty_midi.Note(velocity=80, pitch=93, start=5.75, end=5.875), # B
    pretty_midi.Note(velocity=80, pitch=94, start=5.875, end=6.0), # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=84, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=87, start=4.875, end=5.0),
    # Bar 4, beat 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=5.75),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.4375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.8125, end=6.0), # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and Bar 4
# Bar 3
for i in range(1.5, 3.0, 0.375):
    pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    pretty_midi.Note(velocity=110, pitch=38, start=i+0.75, end=i+0.875)
    pretty_midi.Note(velocity=80, pitch=42, start=i, end=i+0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.1875, end=i+0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.375, end=i+0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.5625, end=i+0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.75, end=i+0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.9375, end=i+1.125)

# Bar 4
for i in range(3.0, 4.5, 0.375):
    pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    pretty_midi.Note(velocity=110, pitch=38, start=i+0.75, end=i+0.875)
    pretty_midi.Note(velocity=80, pitch=42, start=i, end=i+0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.1875, end=i+0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.375, end=i+0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.5625, end=i+0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.75, end=i+0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=i+0.9375, end=i+1.125)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
