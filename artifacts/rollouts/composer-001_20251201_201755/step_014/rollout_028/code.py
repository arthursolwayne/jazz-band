
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on beat 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F (41) on beat 2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    # G2 (43) on beat 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    # D2 (38) on beat 4
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D (62)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F (65)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A (69)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # C (71)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (Dm)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),
    # Bar 4: Finish it
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    # F (41) on beat 1
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),
    # A (45) on beat 2
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),
    # Bb (46) on beat 3
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),
    # D2 (38) on beat 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb-D-F-A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    # Bb (46) on beat 1
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),
    # D (49) on beat 2
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),
    # F (52) on beat 3
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),
    # Bb (46) on beat 4
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.3125),

    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]

# Bar 4: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.8125),

    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
