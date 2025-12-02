
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0), # Ab
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5), # C
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875), # C#
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0), # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875), # B
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875), # E
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375), # E
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875), # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Motif: Start with a short phrase, leave it hanging, then come back
sax_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25), # Bb
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5), # A
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0), # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
