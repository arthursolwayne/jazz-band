
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # D#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # B
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # B
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - motif in C
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    # Bar 3: Repeat motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    # Bar 4: End motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = 1.5 + (bar - 2) * 1.5
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 0.75, end=kick_start + 1.125)
    drums.notes.append(kick_1)
    drums.notes.append(kick_3)
# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = 1.5 + (bar - 2) * 1.5
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 1.875, end=snare_start + 2.0)
    drums.notes.append(snare_2)
    drums.notes.append(snare_4)
# Hi-hat on every eighth
for bar in range(2, 5):
    snare_start = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        start = snare_start + i * 0.375
        end = start + 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
        drums.notes.append(hihat)

# Set tempo
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=120)]

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
