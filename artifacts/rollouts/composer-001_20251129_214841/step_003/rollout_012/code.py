
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=3.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # B
    # Bar 2: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # B
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # B
    # Bar 3: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # B
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # B
    # Bar 4: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # B
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): 1 short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: C - E - B - C (bar 2), then repeat with a descending chromatic (bar 4)

sax_notes = [
    # Bar 2: C - E - B - C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    # Bar 3: C - B - A - G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    # Bar 4: C - E - B - C again
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),
    # Bar 4: End with a descending chromatic line
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=59, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-3-4
# Kick on 1 and 3
for i in range(2, 4):
    kick_start = i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)

# Snare on 2 and 4
for i in range(2, 4):
    snare_start = i * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 1.875, end=snare_start + 2.0)

# Hi-hat on every eighth
for i in range(2, 4):
    snare_start = i * 1.5
    for j in range(0, 4):
        start = snare_start + j * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
