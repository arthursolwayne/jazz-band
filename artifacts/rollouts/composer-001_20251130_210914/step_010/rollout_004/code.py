
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# D minor key, D Dorian
bass_notes = [
    # Bar 2: D-Db-C-B (chromatic descent)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # Db
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),  # B
    # Bar 3: Bb-A-G-F# (chromatic descent)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.5),  # F#
    # Bar 4: F-E-D-C (chromatic descent)
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C) on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # C
    # Bar 3: Bm7 (B, D, F#, A) on 2 and 4
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # A
    # Bar 4: G7 (G, B, D, F) on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif (D, F#, B)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),   # B
    # Bar 3: Leave it hanging
    # No notes in bar 3
    # Bar 4: Come back and finish the motif (D, F#, B)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),   # B
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
