
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
    # Bar 3: A2 (45) -> Bb2 (46) -> D3 (50) -> Eb3 (51)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),
    # Bar 4: Eb3 (51) -> F3 (53) -> A3 (57) -> Bb3 (58)
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),
])
# Bar 4: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0),
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Bb (67), D (69), leave it hanging on Bb (67), then return with F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
