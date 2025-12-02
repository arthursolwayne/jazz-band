
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7: F, A, C, E♭
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, short motif in F, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 start
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
