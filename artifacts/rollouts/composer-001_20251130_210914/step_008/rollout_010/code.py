
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

# Bar 2: Everyone in. Sax starts the melody
# F7 (F, A, C, E) - start on F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=90, start=2.625, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
# F - G - A - Bb over the first bar
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2, A7 on 4
piano_notes = [
    # F7 on beat 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0),  # E
    # A7 on beat 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=2.75),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues the motif
# F7 -> F6 -> Fmaj7 -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # F6
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # Fmaj7
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bass: Chromatic approach to F
# Bb - A - G - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2 (3.375 - 3.5)
# A7 on 4 (4.125 - 4.25)
piano_notes = [
    # F7 on beat 2 (3.375 - 3.5)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5),  # E
    # A7 on beat 4 (4.125 - 4.25)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.25),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Sax concludes the motif with a resolution
# F7 -> F -> Bb -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line again
# F - G - A - Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2 (4.875 - 5.0)
# A7 on 4 (5.625 - 5.75)
piano_notes = [
    # F7 on beat 2 (4.875 - 5.0)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.0),  # E
    # A7 on beat 4 (5.625 - 5.75)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=5.75),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    hihat_notes = []
    for i in range(8):
        hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))
    # Add all
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
