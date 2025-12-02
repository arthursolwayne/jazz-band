
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
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, stay out of the way
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, D, rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    kick_start = start_time
    kick_end = kick_start + 0.375
    snare_start = kick_end
    snare_end = snare_start + 0.375
    hihat_start = start_time
    hihat_end = start_time + 1.5

    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("4_bar_intro.mid")
